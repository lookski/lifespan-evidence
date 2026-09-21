#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-21 20:13:38
脚本功能: 当 github.com:443 直连不通但 api.github.com 可达时, 用 GitHub REST Git Data API
         把本地仓库内容同步到远端 (Blobs -> Tree -> Commit -> Update Ref).
参数: 无命令行参数, 常量在脚本头部 (REPO, LOCAL_DIR, 远端分支).
输入格式: 本地 lifespan-evidence 目录 (git 仓库).
输出格式: 控制台每步结果; 详细记录追加到 github_log.txt; 结束时回读远端树校验.
依赖: curl (传输层), gh CLI (token 来源 GH_TOKEN 或 gh auth token).
注意事项: 只新增/更新文件, 不删除; 大文件 (>50MB) 不支持.
===== [2026-09-21 20:20:11] =====
修复: subprocess.check_output 增加 encoding="utf-8", 否则中文提交信息触发 GBK 解码错误
(UnicodeDecodeError: 'gbk' codec can't decode byte 0xac).
===== [2026-09-21 20:29:39] =====
修复: api() 重试逻辑覆盖网络层异常 (requests.exceptions.RequestException),
之前只重试 429/5xx 状态码, SSLError EOF 直接炸出. 网络间歇抖动 (curl 测试 5/5 成功
但 python 首连失败) 需要同层退避重试.
===== [2026-09-21 20:32:48] =====
改用 curl 子进程替代 requests 做 HTTP 传输: python OpenSSL 指纹对 api.github.com
持续被重置 (SSLEOFError 8/8 次重试全部失败), 而 curl/schannel 5/5 成功;
传输层换 curl 后重试逻辑保留.
===== [2026-09-21 21:12:33] =====
重构为内容驱动同步 (v2): 不再按本地提交逐个重放 (远端游离提交被 GitHub GC 后
base_tree 404 导致 422 Invalid tree info), 改为:
  1. 比较远端 HEAD 树 (recursive) 与本地 HEAD 树 (ls-tree -r);
  2. 只对内容不同的文件 POST blobs;
  3. 以远端 HEAD 为 base_tree 建新树 -> 建单个 squash commit -> PATCH ref;
  4. 回读远端树与本地逐 blob 比对.
历史链差异不影响内容; 未来同步均走此幂等逻辑.
===== [2026-09-21 21:26:40] =====
修复校验 bug: 递归遍历远端树时未把父目录前缀累加到子树条目路径上,
导致 evidence/ 下 50 个文件被误报为根目录文件 (missing/extra 假阳性, sha_diff 为空).
改为栈内携带 (子树sha, 前缀) 二元组.
===== [2026-09-21 21:18:24] =====
修复行尾不一致: core.autocrlf=input 使 HEAD blob 为 LF, 而脚本上传的是工作区
原始字节 (日志文件含 CRLF), 回读校验 sha_diff 假阳性. 上传前按 git 存储口径
规范化 (text=auto: 二进制检测, 含 \0 视为二进制不处理, 否则 CRLF -> LF).
"""

import base64
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = "lookski/lifespan-evidence"
LOCAL_DIR = Path(__file__).resolve().parent  # lifespan-evidence/
API = "https://api.github.com"
LOG = LOCAL_DIR / "github_log.txt"

# ---- token: 优先环境变量 GH_TOKEN, 其次 gh CLI ----
token = os.environ.get("GH_TOKEN", "").strip()
if not token:
    try:
        token = subprocess.check_output(
            ["gh", "auth", "token"], text=True, encoding="utf-8",
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        token = ""
if not token:
    print("没有可用 token (GH_TOKEN / gh auth token)")
    sys.exit(2)


def api(method, path, **kw):
    """用 curl 子进程调 GitHub API (python OpenSSL 被干扰, curl/schannel 稳定).
    kw 只支持 json (请求体 dict). 返回解析后的 JSON."""
    body = kw.get("json")
    cmd = [
        "curl", "-sS", "--fail-with-body", "--max-time", "60",
        "-X", method,
        "-H", f"Authorization: Bearer {token}",
        "-H", "Accept: application/vnd.github+json",
        "-H", "X-GitHub-Api-Version: 2022-11-28",
        "-H", "User-Agent: lifespan-evidence-sync",
    ]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json",
                "--data-binary", json.dumps(body)]
    cmd.append(f"{API}{path}")
    last = None
    for attempt in range(8):
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if p.returncode == 0:
            return json.loads(p.stdout)
        last = f"curl rc={p.returncode} err={p.stderr[:200]} out={p.stdout[:200]}"
        if p.returncode == 22:  # --fail-with-body: HTTP >= 400
            if "rate limit" in p.stdout.lower():
                time.sleep(60)
                continue
            raise RuntimeError(f"API {method} {path} HTTP错误: {p.stdout[:300]}")
        time.sleep(2 ** attempt)
    raise RuntimeError(f"API {method} {path} 失败: {last}")


def git(*args):
    """本地 git 查询 (只读)."""
    return subprocess.check_output(
        ["git", "-C", str(LOCAL_DIR)] + list(args),
        text=True, encoding="utf-8",
    ).strip()


def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)


def main():
    # 1. 本地 HEAD 树 (recursive, 含 blob sha)
    local = {}
    for row in git("ls-tree", "-r", "HEAD").splitlines():
        meta, _, path = row.partition("\t")
        _mode, _typ, sha = meta.split()
        local[path] = sha
    # 2. 远端 HEAD commit 与树 (recursive)
    remote_head = api("GET", f"/repos/{REPO}/git/ref/heads/main")["object"]["sha"]
    remote_commit = api("GET", f"/repos/{REPO}/git/commits/{remote_head}")
    remote_tree_sha = remote_commit["tree"]["sha"]
    remote = {}
    stack = [(remote_tree_sha, "")]
    while stack:
        t_sha, prefix = stack.pop()
        for e in api("GET", f"/repos/{REPO}/git/trees/{t_sha}")["tree"]:
            if e["type"] == "blob":
                remote[prefix + e["path"]] = e["sha"]
            elif e["type"] == "tree":
                stack.append((e["sha"], prefix + e["path"] + "/"))
    print(f"本地 HEAD 树 {len(local)} blob, 远端 {remote_head[:7]} 树 {len(remote)} blob")
    if local == remote:
        print("内容已一致, 无需同步")
        return
    changed = [p for p in set(local) | set(remote)
               if local.get(p) != remote.get(p)]
    removed = [p for p in changed if p not in local]
    if removed:
        print(f"警告: 远端多出 {len(removed)} 个本地没有的文件, 本脚本不删除: {removed}")
    added = [p for p in changed if p in local]
    print(f"需上传 {len(added)} 个文件")

    # 3. 逐文件 POST blobs (按 git 存储口径规范化行尾, 与 HEAD blob 一致)
    entries = []
    for p in added:
        data = (LOCAL_DIR / p).read_bytes()
        if b"\0" not in data:  # 文本文件: CRLF -> LF (与 autocrlf=input 一致)
            data = data.replace(b"\r\n", b"\n")
        blob = api("POST", f"/repos/{REPO}/git/blobs",
                   json={"content": base64.b64encode(data).decode(),
                         "encoding": "base64"})
        entries.append({"path": p, "mode": "100644", "type": "blob",
                        "sha": blob["sha"]})
        print(f"  blob {p}")

    # 4. 建树 (base=远端当前树) -> squash commit -> 更新 ref
    n = time.strftime("%Y-%m-%d %H:%M:%S")
    msg = f"sync: {len(added)} files via api_push v2 ({n})"
    tree = api("POST", f"/repos/{REPO}/git/trees",
               json={"base_tree": remote_tree_sha, "tree": entries})
    new_commit = api("POST", f"/repos/{REPO}/git/commits", json={
        "message": msg, "tree": tree["sha"], "parents": [remote_head]})
    api("PATCH", f"/repos/{REPO}/git/refs/heads/main",
        json={"sha": new_commit["sha"], "force": False})
    log(f"OK sync {new_commit['sha'][:7]} {msg}")
    print(f"远端 main -> {new_commit['sha'][:7]}")

    # 5. 回读校验: 远端树 vs 本地 (带路径前缀)
    tree_sha = api("GET", f"/repos/{REPO}/git/commits/{new_commit['sha']}")["tree"]["sha"]
    files_remote = {}
    stack = [(tree_sha, "")]
    while stack:
        t_sha, prefix = stack.pop()
        for e in api("GET", f"/repos/{REPO}/git/trees/{t_sha}")["tree"]:
            if e["type"] == "blob":
                files_remote[prefix + e["path"]] = e["sha"]
            elif e["type"] == "tree":
                stack.append((e["sha"], prefix + e["path"] + "/"))
    missing = set(local) - set(files_remote)
    extra = set(files_remote) - set(local)
    diff_sha = [p for p in set(local) & set(files_remote)
                if local[p] != files_remote[p]]
    log(f"VERIFY remote={len(files_remote)} local={len(local)} "
        f"missing={sorted(missing)} extra={sorted(extra)} sha_diff={sorted(diff_sha)}")
    if missing or extra or diff_sha:
        print(f"不一致! missing={sorted(missing)} extra={sorted(extra)} "
              f"sha_diff={sorted(diff_sha)}")
        sys.exit(1)
    print("回读校验: 完全一致, 同步完成")


if __name__ == "__main__":
    main()
