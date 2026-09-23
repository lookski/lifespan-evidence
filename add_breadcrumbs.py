# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-23 13:10:45
脚本功能: 给 evidence/E*.md 顶部加面包屑导航行 (README -> topics/xx -> 本页),
          给 topics/*.md 顶部加层级行; 幂等 (已有则跳过).
参数: argv[1] = "--apply" 实际写回, 缺省只预览
输入格式: evidence/E*.md, topics/*.md
输出格式: stdout 预览/写回报告
依赖: 仅 Python 3 标准库 (pathlib, re)
注意事项:
  - E 条目到 topics 维度的映射硬编码在 E2TOPIC (手工维护, 加新条目时同步)
  - 面包屑行插在 H1 标题之后, 不改任何内容文字
"""
import re
from pathlib import Path
import sys

# E 编号 -> topics 页 (相对链接)
E2TOPIC = {}
for e in range(1, 4):          # E01-E03
    E2TOPIC[f"E{e:02d}"] = ("00-total.md", "00-total")
E2TOPIC.update({"E04": ("01-diet-patterns.md", "01-diet-patterns"),
                "E05": ("01-diet-patterns.md", "01-diet-patterns")})
for e in range(6, 13):         # E06-E12
    E2TOPIC[f"E{e:02d}"] = ("02-foods.md", "02-foods")
E2TOPIC["E15"] = ("02-foods.md", "02-foods")
E2TOPIC.update({"E13": ("03-avoid.md", "03-avoid"),
                "E14": ("03-avoid.md", "03-avoid")})
for e in range(16, 20):        # E16-E19
    E2TOPIC[f"E{e:02d}"] = ("04-energy.md", "04-energy")
for e in range(20, 24):        # E20-E23
    E2TOPIC[f"E{e:02d}"] = ("05-activity.md", "05-activity")
E2TOPIC.update({"E24": ("06-sleep.md", "06-sleep"),
                "E25": ("06-sleep.md", "06-sleep"),
                "E53": ("06-sleep.md", "06-sleep")})
for e in range(26, 31):        # E26-E30
    E2TOPIC[f"E{e:02d}"] = ("07-tobacco-alcohol-bmi.md", "07-tobacco-alcohol-bmi")
for e in range(31, 36):        # E31-E35
    E2TOPIC[f"E{e:02d}"] = ("08-social-mind.md", "08-social-mind")
for e in range(36, 44):        # E36-E43
    E2TOPIC[f"E{e:02d}"] = ("09-vitamin-c.md", "09-vitamin-c")
for e in range(44, 47):        # E44-E46
    E2TOPIC[f"E{e:02d}"] = ("11-frontier.md", "11-frontier")
for e in range(47, 50):        # E47-E49
    E2TOPIC[f"E{e:02d}"] = ("12-frameworks.md", "12-frameworks")
for e in range(50, 53):        # E50-E52
    E2TOPIC[f"E{e:02d}"] = ("10-sex.md", "10-sex")
E2TOPIC["E54"] = ("13-work.md", "13-work")

def main():
    apply = "--apply" in sys.argv
    # evidence: 面包屑插在 H1 后
    for f in sorted(Path("evidence").glob("E*.md")):
        t = f.read_text(encoding="utf-8")
        if t.startswith("> 层级:") or "> 层级:" in t[:200]:
            continue
        key = f.stem
        m = re.match(r"E(\d+)", key)
        topic = E2TOPIC.get(key)
        if not topic:
            print(f"[缺映射] {f}")
            continue
        crumbs = (f"> 层级: [← 总结 README](../README.md) · "
                  f"[维度速览 {topic[1]}](../topics/{topic[0]}) · 本页 `{key}`\n\n")
        # H1 行末插入
        lines = t.split("\n")
        assert lines[0].startswith("# "), f
        lines.insert(1, "\n" + crumbs.rstrip("\n"))
        new = "\n".join(lines)
        if apply:
            f.write_text(new, encoding="utf-8")
            print(f"[修改] {f}")
        else:
            print(f"[预览] {f}")

if __name__ == "__main__":
    main()
