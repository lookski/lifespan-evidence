# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-20 23:12:47
脚本功能: 批量调用 Europe PMC REST API 检索文献, 按引用数排序, 输出标题/年份/期刊/DOI/PMID
参数: argv[1] = JSON 查询文件 (数组的数组: [标签, 查询串]), argv[2] 可选 pageSize 默认 5
输入格式: UTF-8 JSON, 如 [["标签", "TITLE:\"...\""], ...]
输出格式: stdout 纯文本, 每个 label 下逐条列文献
依赖: 仅 Python 3 标准库 (urllib, json)
注意事项: 网络需可访问 www.ebi.ac.uk; 查询语法为 Europe PMC search syntax
"""
import json, urllib.request, urllib.parse, sys

BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

def search(query, n=6):
    url = BASE + "?" + urllib.parse.urlencode(
        {"query": query, "format": "json", "pageSize": n, "sort": "CITED desc"})
    req = urllib.request.Request(url, headers={"User-Agent": "lit-scan/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        d = json.loads(r.read().decode("utf-8"))
    out = []
    for x in d.get("resultList", {}).get("result", []):
        out.append({
            "year": x.get("pubYear", ""),
            "journal": (x.get("journalTitle", "") or x.get("bookOrReportDetails", {}).get("publisher", ""))[:60],
            "title": x.get("title", "").strip(),
            "pmid": x.get("pmid", ""),
            "doi": x.get("doi", ""),
            "cited": x.get("citedByCount", "0"),
            "oa": x.get("isOpenAccess", "N"),
        })
    return out

if __name__ == "__main__":
    queries = json.load(open(sys.argv[1], encoding="utf-8"))
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for label, q in queries:
        print("=" * 25, label, "=" * 25)
        try:
            for it in search(q, n):
                print(f"[{it['year']}] {it['journal']} | cited={it['cited']} | OA={it['oa']}")
                print(f"    {it['title']}")
                print(f"    DOI: {it['doi']}  PMID: {it['pmid']}")
        except Exception as e:
            print("ERROR:", type(e).__name__, e)
        print()
