#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本名称: lint_site_20261028.py
编写时间: 2026-10-28 11:20:00
作    者: deepseek-harness agent
适用项目: 1.lifespan-evidence (docsify 站点一致性检查)

===== 脚本功能 =====
本地静态检查, 确认新增条目与导航完全一致:
1. evidence/E*.md 实际文件清单 vs 00-index.md 表格行 vs _sidebar.md 链接.
2. topics/*.md 实际文件清单 vs topics/README.md 表格行 vs _sidebar.md.
3. 每个 evidence/E*.md 的 "维度速览" 面包屑指向的文件是否存在.
4. 每个 md 文件里的相对链接 (../evidence/E*.md, ../topics/*.md) 是否指向存在的文件.

===== 参数 =====
--root PATH   仓库根目录, 默认脚本所在目录
--out PATH    可选, 报告写入文件 (UTF-8); 省略则输出到 stdout

===== 输入格式 =====
目录: 含 evidence/, topics/, _sidebar.md, README.md 的项目根

===== 输出格式 =====
文本报告: 每个检查项一行, 失败项前缀 [FAIL]
退出码: 0 全部通过; 1 存在失败项

===== 依赖 =====
python3.12 + stdlib (os, re, sys, argparse)

===== 注意事项 =====
1. 只读, 不修改任何文件.
2. 检查是静态的, 不解析 markdown 全部语法, 只覆盖本项目的固定引用形式.
"""

import argparse
import os
import re
import sys


def read(p):
    with open(p, encoding='utf-8-sig') as f:
        return f.read()


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument('--out')
    args = ap.parse_args()

    root = args.root
    ev_dir = os.path.join(root, 'evidence')
    tp_dir = os.path.join(root, 'topics')

    fails = []
    lines = []

    ev_files = sorted(f for f in os.listdir(ev_dir) if re.match(r'^E\d+\.md$', f))
    ev_ids = [f[:-3] for f in ev_files]
    lines.append('evidence 文件数: {} ({} .. {})'.format(len(ev_files), ev_ids[0], ev_ids[-1]))

    index = read(os.path.join(ev_dir, '00-index.md'))
    index_ids = set(re.findall(r'\|\s*(E\d+)\s*\|', index))
    missing_in_index = [e for e in ev_ids if e not in index_ids]
    extra_in_index = sorted(i for i in index_ids if i not in ev_ids)
    if missing_in_index:
        fails.append('00-index.md 缺少条目: {}'.format(', '.join(missing_in_index)))
    if extra_in_index:
        fails.append('00-index.md 有索引但无文件: {}'.format(', '.join(extra_in_index)))
    lines.append('00-index.md 表格条目数: {}'.format(len(index_ids)))

    sidebar = read(os.path.join(root, '_sidebar.md'))
    sb_ev = set(re.findall(r'evidence/(E\d+)\.md', sidebar))
    missing_in_sb = [e for e in ev_ids if e not in sb_ev]
    if missing_in_sb:
        fails.append('_sidebar.md 缺少证据链接: {}'.format(', '.join(missing_in_sb)))
    lines.append('_sidebar.md 证据链接数: {}'.format(len(sb_ev)))

    tp_files = sorted(f for f in os.listdir(tp_dir) if f.endswith('.md') and f != 'README.md')
    lines.append('topics 文件数: {}'.format(len(tp_files)))
    tp_readme = read(os.path.join(tp_dir, 'README.md'))
    tp_listed = set(re.findall(r'\((\d+[a-z]?-[a-z-]+\.md)\)', tp_readme))
    missing_tp = [t for t in tp_files if t not in tp_listed]
    extra_tp = sorted(t for t in tp_listed if t not in tp_files)
    if missing_tp:
        fails.append('topics/README.md 缺少维度: {}'.format(', '.join(missing_tp)))
    if extra_tp:
        fails.append('topics/README.md 列了但无文件: {}'.format(', '.join(extra_tp)))
    lines.append('topics/README.md 维度条目数: {}'.format(len(tp_listed)))

    sb_tp = set(re.findall(r'topics/(\d+[a-z]?-[a-z-]+\.md)', sidebar))
    missing_sb_tp = [t for t in tp_files if t not in sb_tp]
    if missing_sb_tp:
        fails.append('_sidebar.md 缺少维度链接: {}'.format(', '.join(missing_sb_tp)))

    # 面包屑与相对链接
    broken = []
    for fn in ev_files:
        body = read(os.path.join(ev_dir, fn))
        m = re.search(r'\[维度速览\s+(\S+?)\]\(\.\./topics/([a-z0-9-]+\.md)\)', body)
        if m:
            target = os.path.join(tp_dir, m.group(2))
            if not os.path.exists(target):
                broken.append('{} -> topics/{}'.format(fn, m.group(2)))
        else:
            broken.append('{} 缺少维度速览面包屑'.format(fn))
    if broken:
        fails.append('面包屑问题 {} 项: {}'.format(len(broken), '; '.join(broken[:12])))
    lines.append('面包屑检查: {} 个条目'.format(len(ev_files)))

    # topics 页内的 ../evidence/E*.md 链接
    bad_links = []
    for fn in tp_files:
        body = read(os.path.join(tp_dir, fn))
        for ref in re.findall(r'\.\./evidence/(E\d+)\.md', body):
            if not os.path.exists(os.path.join(ev_dir, ref + '.md')):
                bad_links.append('topics/{} -> E{}'.format(fn, ref))
    if bad_links:
        fails.append('topics 内坏链接: {}'.format('; '.join(bad_links)))
    lines.append('topics 内 evidence 链接检查: 完成')

    lines.append('')
    if fails:
        lines.append('=== FAIL {} 项 ==='.format(len(fails)))
        for f in fails:
            lines.append('[FAIL] ' + f)
    else:
        lines.append('=== 全部检查通过 ===')

    report = '\n'.join(lines)
    if args.out:
        with open(args.out, 'w', encoding='utf-8', newline='\n') as f:
            f.write(report + '\n')
        print('报告写入 {}'.format(args.out))
    else:
        print(report)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
