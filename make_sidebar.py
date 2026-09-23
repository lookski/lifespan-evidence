# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-24 01:32:00 (系统时间实取)
脚本功能: 程序化生成 docs/_sidebar.md (docsify 侧边栏).
          从 README.md 与 topics/*.md 的 H1 提取标题, 从 README 维度表提取一句话;
          evidence 全列表折叠在末尾 (从 evidence/*.md H1 提取).
参数: 无
输入格式: 仓库根 README.md, topics/*.md, evidence/*.md
输出格式: docs/_sidebar.md
依赖: Python 3 标准库
注意事项: 幂等, 重跑覆盖; 相对链接以 docs/ 为基准指向上级
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"


def h1_of(p):
    for ln in p.read_text(encoding="utf-8", errors="replace").split("\n"):
        if ln.startswith("# "):
            return ln[2:].strip()
    return p.stem


def main():
    lines = []
    lines.append("- [总结 (zh/en)](README.md)")
    # topics 页: 保持编号排序
    tdir = ROOT / "topics"
    tpages = sorted(tdir.glob("*.md"), key=lambda p: p.name)
    for p in tpages:
        if p.name == "README.md":
            continue
        title = h1_of(p)
        lines.append(f"- [{title}](topics/{p.name})")
    # evidence 折叠
    lines.append("- [逐项证据 (54 条)](evidence/00-index.md)")
    edir = ROOT / "evidence"
    epages = sorted(edir.glob("E*.md"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    for p in epages:
        title = h1_of(p)
        lines.append(f"  - [{title}](evidence/{p.name})")
    out = ROOT / "_sidebar.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("sidebar written:", len(lines), "entries")


if __name__ == "__main__":
    main()
