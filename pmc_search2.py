# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-23 12:05:30
脚本功能: 批量调用 Europe PMC REST API 检索文献 (v2: 支持对象格式含独立 sort), 按引用数排序, 输出标题/年份/期刊/DOI/PMID
参数: argv[1] = JSON 查询文件, 两种格式兼容:
      - 数组的数组: [["标签", "查询串"], ...] (旧格式, sort 固定 CITED desc)
      - 对象: {"queries": [{"name": "...", "q": "...", "sort": "CITED desc", "pageSize": 5}, ...]}
      argv[2] 可选默认 pageSize
输入格式: UTF-8 JSON
输出格式: stdout 纯文本, 每个 label 下逐条列文献
依赖: 仅 Python 3 标准库 (urllib, json)
注意事项: 网络需可访问 www.ebi.ac.uk; 查询语法为 Europe PMC search syntax;
          本文件为新增格式兼容, 不改动 pmc_search.py 原有行为
"""
import json, urllib.request, urllib.parse, sys

BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

def search(query, n=6, sort="CITED desc"):
    url = BASE + "?" + urllib.parse.urlencode(
        {"query": query, "format": "json", "pageSize": n, "sort": sort})
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
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    if isinstance(data, dict):  # v2 对象格式
        queries = [(x["name"], x["q"], x.get("sort", "CITED desc"),
                    x.get("pageSize", n)) for x in data["queries"]]
    else:  # 旧格式 [标签, 查询串]
        queries = [(label, q, "CITED desc", n) for label, q in data]
    for label, q, sort_key, size in queries:
        print("=" * 25, label, "=" * 25)
        try:
            for it in search(q, size, sort_key):
                print(f"[{it['year']}] {it['journal']}")
                print(f"  {it['title']}")
                print(f"  PMID:{it['pmid']}  DOI:{it['doi']}  被引:{it['cited']}  OA:{it['oa']}")
        except Exception as e:
            print("  检索失败:", e)
