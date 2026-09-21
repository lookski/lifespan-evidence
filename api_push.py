#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-21 20:13:38
脚本功能: 当 github.com:443 直连不通但 api.github.com 可达时, 用 GitHub REST Contents API
         把本地 git 提交逐个文件推送到远端仓库 (Blobs -> Tree -> Commit -> Update Ref).
参数: 无命令行参数, 常量在脚本头部 (REPO, TOKEN_ENV, LOCAL_DIR, 远端分支).
输入格式: 本地 lifespan-evidence 目录 (git 仓库, origin/main 指向上次已同步 commit).
输出格式: 每文件一行推送结果; 最终 commit SHA 与远端核验 JSON (github_log.txt).
依赖: requests 库; gh CLI 的 token 放在环境变量 GH_TOKEN 或 ~/.pi/github_token.
注意事项: 只新增/更新文件, 不删除; 大文件 (>50MB) 不支持; 推送完成后回读远端树校验.
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
===== [2026-09-21 20:47:55] =====
修复校验 bug: 递归遍历远端树时未把父目录前缀累加到子树条目路径上,
导致 evidence/ 下 50 个文件被误报为根目录文件 (missing/extra 假阳性, sha_diff 为空).
改为栈内携带 (子树sha, 前缀) 二元组.
"""

import base64
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import requests

REPO = "lookski/lifespan-evidence"
LOCAL_DIR = Path(__file__).resolve().parent  # lifespan-evidence/
API = "https://api.github.com"
LOG = LOCAL_DIR / "github_log.txt"

# ---- token: 优先环境变量 GH_TOKEN, 其次 gh CLI ----
token = os.environ.get("GH_TOKEN", "").strip()
if not token:
    try:
        token = subprocess.check_output(
            ["gh", "auth", "token"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        token = ""
if not token:
    print("没有可用 token (GH_TOKEN / gh auth token)")
    sys.exit(2)

S = requests.Session()
S.headers.update({
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "lifespan-evidence-sync",
})


def api(method, path, **kw):
    """用 curl 子进程调 GitHub API (python OpenSSL 被干扰, curl/schannel 稳定).
    kw 只支持 json (请求体 dict) 或 data (原始 bytes). 返回解析后的 JSON."""
    body = kw.get("json")
    data = kw.get("data")
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
    elif data is not None:
        cmd += ["--data-binary@-"]
    cmd.append(f"{API}{path}")
    last = None
    for attempt in range(8):
        p = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", input=(data.decode() if data else None))
        if p.returncode == 0:
            return json.loads(p.stdout)
        last = f"curl rc={p.returncode} err={p.stderr[:200]} out={p.stdout[:200]}"
        # 22 = --fail-with-body 的 HTTP >= 400; 429/500 系才重试, 其他直接抛
        if p.returncode == 22:
            try:
                rj = json.loads(p.stdout)
                code = p.stdout  # 原样报错即可
            except Exception:
                pass
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


def main():
    # 1. 本地待推送提交: origin/main..main
    base_sha = git("rev-parse", "origin/main")
    head_sha = git("rev-parse", "main")
    if base_sha == head_sha:
        print("本地与远端一致, 无需推送")
        return
    # 每个提交引入的文件 (A/M 状态), D 不处理 (本仓库无删除)
    commits = git(
        "log", "--reverse", "--format=%H %s", f"{base_sha}..{head_sha}"
    ).splitlines()
    print(f"待同步提交 {len(commits)} 个: {base_sha[:7]}..{head_sha[:7]}")

    # 2. 远端当前 commit
    remote = api("GET", f"/repos/{REPO}/git/ref/heads/main")
    cur_sha = remote["object"]["sha"]
    print(f"远端 main = {cur_sha[:7]}")

    # 3. 逐提交应用
    for line in commits:
        csha, _, cmsg = line.partition(" ")
        # 该提交改动的路径
        diff = subprocess.check_output(
            ["git", "-C", str(LOCAL_DIR), "diff-tree", "--no-commit-id",
             "--name-status", "-r", csha],
            text=True, encoding="utf-8",
        ).splitlines()
        entries = []  # [(path, mode, blob_sha)]
        for row in diff:
            st, _, path = row.partition("\t")
            if st == "D":
                raise RuntimeError(f"遇到删除 {path}, 本脚本未实现, 请人工处理")
            full = LOCAL_DIR / path
            data = full.read_bytes()
            blob = api("POST", f"/repos/{REPO}/git/blobs",
                       json={"content": base64.b64encode(data).decode(),
                             "encoding": "base64"})
            entries.append({"path": path, "mode": "100644",
                            "type": "blob", "sha": blob["sha"]})
        # tree: 以远端当前 commit 的 tree 为 base
        cur_commit = api("GET", f"/repos/{REPO}/git/commits/{cur_sha}")
        tree = api("POST", f"/repos/{REPO}/git/trees",
                   json={"base_tree": cur_commit["tree"]["sha"], "tree": entries})
        new_commit = api("POST", f"/repos/{REPO}/git/commits", json={
            "message": cmsg,
            "tree": tree["sha"],
            "parents": [cur_sha],
        })
        cur_sha = new_commit["sha"]
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"OK commit {cur_sha[:7]} {cmsg} ({len(entries)} files)\n")
        print(f"OK commit {cur_sha[:7]} {cmsg} ({len(entries)} files)")

    # 4. 更新远端 ref (带 expect: 202 需要无 fast-forward 校验, 直接 update)
    api("PATCH", f"/repos/{REPO}/git/refs/heads/main",
        json={"sha": cur_sha, "force": False})
    print(f"远端 main -> {cur_sha[:7]}")

    # 5. 回读校验: 远端树文件数 vs 本地 git ls-files
    tree_sha = api("GET", f"/repos/{REPO}/git/commits/{cur_sha}")["tree"]["sha"]
    files_remote = {}
    stack = [(tree_sha, "")]  # (子树sha, 路径前缀)
    while stack:
        t, prefix = stack.pop()
        for e in api("GET", f"/repos/{REPO}/git/trees/{t}")["tree"]:
            if e["type"] == "blob":
                files_remote[prefix + e["path"]] = e["sha"]
            elif e["type"] == "tree":
                stack.append((e["sha"], prefix + e["path"] + "/"))
    local_files = {}
    for p in git("ls-files").splitlines():
        local_files[p] = git("rev-parse", f"HEAD:{p}")
    missing = set(local_files) - set(files_remote)
    extra = set(files_remote) - set(local_files)
    diff_sha = [p for p in set(local_files) & set(files_remote)
                if local_files[p] != files_remote[p]]
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"VERIFY remote_files={len(files_remote)} "
                f"local_files={len(local_files)} missing={sorted(missing)} "
                f"extra={sorted(extra)} sha_diff={sorted(diff_sha)}\n")
    print(f"校验: 远端 {len(files_remote)} 文件, 本地 {len(local_files)} 文件")
    if missing or extra or diff_sha:
        print(f"不一致! missing={sorted(missing)} extra={sorted(extra)} "
              f"sha_diff={sorted(diff_sha)}")
        sys.exit(1)
    print("完全一致, 同步完成")


if __name__ == "__main__":
    main()
