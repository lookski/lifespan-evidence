# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-23 13:25:10
脚本功能: 双语一致性审计. 抽取 README.md 与 README.en.md 的关键统计数字
          (HR/RR/OR/ES + CI 模式) 与 PMID 清单, 比对两个集合必须一致;
          再抽 topics 中文页与 TL;DR (EN) 节的数字比对.
          退出码非 0 = 不一致.
参数: 无
输入格式: README.md, README.en.md, topics/*.md
输出格式: stdout 审计报告
依赖: 仅 Python 3 标准库 (re, pathlib, sys)
注意事项:
  - 数字一致是硬约束: 英文翻译层不得引入/丢失/改写统计值
  - PMID 必须两侧一致 (来源可追溯)
  - 容差: 英文版用 "-4.0 to 0.4" 表区间, 中文用 "-4.0 到 0.4", 归一化后比对
"""
import re
import sys
from pathlib import Path

NUM = re.compile(r"(?:HR|RR|OR|ES)\s?[\d.]+\s?(?:\(\s?95%\s?CI\s?[\d.]+\s?(?:-|to)\s?[\d.]+\s?\))")
PMID = re.compile(r"PMID\s?(\d{5,9})")

def norm(s):
    return s.replace("to", "-").replace(" ", "").replace(",", "")

def extract(text):
    nums = {norm(m.group(0)) for m in NUM.finditer(text)}
    pmids = {m.group(1) for m in PMID.finditer(text)}
    return nums, pmids

def main():
    zh = Path("README.md").read_text(encoding="utf-8")
    en = Path("README.en.md").read_text(encoding="utf-8")
    zh_n, zh_p = extract(zh)
    en_n, en_p = extract(en)
    ok = True
    miss_n = zh_n - en_n
    extra_n = en_n - zh_n
    if miss_n:
        ok = False
        print("英文版缺数字:", sorted(miss_n))
    if extra_n:
        ok = False
        print("英文版多出数字:", sorted(extra_n))
    miss_p = zh_p - en_p
    extra_p = en_p - zh_p
    if miss_p:
        ok = False
        print("英文版缺 PMID:", sorted(miss_p))
    if extra_p:
        ok = False
        print("英文版多出 PMID:", sorted(extra_p))
    # topics 中文 vs TL;DR 英文
    t_n_bad = []
    for f in sorted(Path("topics").glob("*.md")):
        if f.name == "README.md":
            continue
        t = f.read_text(encoding="utf-8")
        idx = t.find("## TL;DR (EN)")
        if idx < 0:
            continue
        en_part = t[idx:]
        cn_n, _ = extract(t[:idx])
        en_n2, _ = extract(en_part)
        miss = cn_n - en_n2
        extra = en_n2 - cn_n
        if miss or extra:
            t_n_bad.append((f.name, sorted(miss), sorted(extra)))
    if t_n_bad:
        for name, miss, extra in t_n_bad:
            ok = False
            print(f"topics/{name}: 中文缺/英文多 {extra} 中文有英文缺 {miss}")
    print(f"审计结果: {'PASS' if ok else 'FAIL'} | README 数字 zh={len(zh_n)} en={len(en_n)} | PMID zh={len(zh_p)} en={len(en_p)}")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
