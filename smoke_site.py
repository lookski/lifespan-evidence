# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-24 01:45:00 (系统时间实取)
脚本功能: 冒烟测试 GitHub Pages 站点关键资源可访问且内容非空.
参数: 无
输入格式: https://lookski.github.io/lifespan-evidence/
输出格式: 控制台打印各资源字节数
依赖: curl, Python 3 标准库
注意事项: 只读
"""
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = "https://lookski.github.io/lifespan-evidence/"
PATHS = ["", "_sidebar.md", "README.md", "topics/00-total.md",
         "evidence/E54.md", "docsify.js"]
MIN_BYTES = 500


def main():
    ok = True
    for path in PATHS:
        p = subprocess.run(["curl", "-sS", "-m", "15", BASE + path],
                           capture_output=True)
        n = len(p.stdout)
        status = "OK" if n > MIN_BYTES else ("CHECK" if path == "" else "FAIL")
        if status == "FAIL":
            ok = False
        print((path or "root") + ":", n, "bytes", status)
        time.sleep(1)
    print("smoke:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
