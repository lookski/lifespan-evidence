# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-20 23:12:47
脚本功能: 按 PMID 列表从 Europe PMC 拉取标题+摘要, 用于核实报告引用的具体数字
参数: argv[1] = 文本文件, 每行一个 PMID (允许 # 注释)
输入格式: UTF-8 纯文本, 每行一个 PMID
输出格式: stdout, 每篇输出标题与摘要原文
依赖: 仅 Python 3 标准库
注意事项: resultType=core 才返回 abstractText
===== [2026-09-22 00:58:30] =====
修复: PMIDS 解析改为每行先按 '#' 截断再 strip, 允许行尾注释
(之前 '9448525 # 注释' 整行当 PMID 导致 NOT FOUND).
"""
import urllib.request, urllib.parse, json, re, sys

PMIDS = [l.split("#")[0].strip() for l in open(sys.argv[1], encoding="utf-8")
         if l.split("#")[0].strip()]

for pmid in PMIDS:
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
           + urllib.parse.urlencode({"query": f"EXT_ID:{pmid} AND SRC:MED",
                                     "format": "json", "resultType": "core"}))
    req = urllib.request.Request(url, headers={"User-Agent": "lit-verify/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        d = json.loads(r.read().decode("utf-8"))
    rs = d.get("resultList", {}).get("result", [])
    print("=" * 30, "PMID", pmid, "=" * 30)
    if not rs:
        print("NOT FOUND")
        continue
    x = rs[0]
    print(x.get("title", ""))
    print(x.get("journalTitle", ""), x.get("pubYear", ""), "DOI:", x.get("doi", ""))
    ab = x.get("abstractText", "(no abstract)")
    ab = re.sub(r"<[^>]+>", " ", ab)
    print(ab.strip()[:3600])
    print()
