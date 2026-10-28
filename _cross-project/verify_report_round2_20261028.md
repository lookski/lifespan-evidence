# 三份调研项目 第二轮校验与同步报告

- 生成时间: 2026-10-28
- 范围: 1.lifespan-evidence / 2.teeth-evidence / 3.sex
- 方法: 逐条 PubMed 标题精确检索复核 + 站内 lint 结构校验 + 远程仓库 ref 对照

本报告接续 `verify_report_20261028.md`（那份只覆盖 D 盘到工作区的搬迁一致性）。
本报告记录**研究成果本身**的校验：证据条目、引用标识、索引与 README 的结构一致性。

## 1.lifespan-evidence

- evidence 文件数: 78（`00-index.md` + `E01.md` .. `E77.md`）
- evidence 总字节: 250358
- 复核记录块 (标注 `复核记录 2026-10-28`): 9
- topics 文件数: 18
- lint_site 结果: `=== 全部检查通过 ===`
  - evidence 文件数 77 (E01 .. E77)
  - `00-index.md` 表格条目数 77
  - `_sidebar.md` 证据链接数 77
  - `topics/README.md` 维度条目数 18
  - 面包屑检查: 77 个条目
  - topics 内 evidence 链接检查: 完成
- lint_crosspage 结果: `0 problems`
- 本轮修正的 PMID 与元数据（7 处，均附就地复核记录，未改写原文）:

  | 条目 | 原值 | 现值 | 错因 |
  |---|---|---|---|
  | E17 | PMID 22899217 | PMID 22932268 + doi:10.1038/nature11432 | 原号实为 PET-CT 机房辐射屏蔽设计论文 |
  | E44 | — | PMID 27304507 | — |
  | E45 | — | PMID 25540326 + 29997249 | — |
  | E46 | — | 围绕 31542391 / 30616998 / 36857968 重写 | — |
  | E47 | — | PMID 35766027 + 37036905 | — |
  | E48 | — | PMID 39096926 | — |
  | E49 | — | PMID 38762324 (2162-2203) | — |

- 提交: `630d32a` 复核: E17/E44-E49 共 7 处 PMID 与元数据修正（7 files changed, +183 -74）
- 远程: `https://github.com/lookski/lifespan-evidence.git` main = `630d32a`，与本地一致

## 2.teeth-evidence

- evidence 文件数: 92（`00-if-table.md` / `00-index.md` 等索引 + `T01.md` .. `T90.md`）
- evidence 总字节: 310250
- 复核记录块 (标注 `复核记录 2026-10-28`): 0（本轮未改动 teeth 证据正文）
- topics 文件数: 7
- lint_teeth 结果: `=== 全部检查通过 ===`
  - evidence 文件数 90 (T01 .. T90)
  - `00-index.md` 表格条目数 90
  - `README.md` 导航: topics 7 条, evidence 47 条
  - `README.zh.md` 导航: topics 7 条, evidence 6 条
- 本轮工作: 引用标题抽样审计（`audit_sex_citations` 同法）确认无错引；未新增条目
- 提交: `e67242d` round-4: 社交媒体热点专项扩至 90 条 (T56-T90)
- 远程: `https://github.com/lookski/teeth-evidence.git` main = `e67242d`，与本地一致

## 3.sex

- 专题报告 6 份:

  | 文件 | 字节 |
  |---|---|
  | `文献调研_高潮差异与肛门快感原理_20260928.md` | 33358 |
  | `文献调研_体表快感地图_乳头_痒觉_20260929.md` | 23363 |
  | `文献调研_高潮的个体差异_药物基因与进化_20260930.md` | 31838 |
  | `文献调研_接受方肛门快感生理学_20261001.md` | 30894 |
  | `文献调研_精神药物与性功能抑制_20261001.md` | 22648 |
  | `文献调研_干性高潮_神经环路与临床_20261002.md` | 44598 |

- 引用审计 (`audit_sex_citations_20261028.py`): `files=6 rows=191 uniq=183 fail=0`
  - 191 条引用，183 个唯一 PMID，0 条拉取失败
  - 抽样标题全部切题（nipple erogenous maps / itch / BDSM / spinal ejaculation generator）
- `paper_pdfs/download_log.csv`: 清理掉 4 行重复记录（重跑脚本时同一批 DOI 被追加两遍），现为表头 + 6 条记录；清理后内容与已提交版本一致，故无新提交
- 提交: `c502ed5` 报告2 复核: 23 条引用与 PubMed 逐条比对, 补齐 IF 列
- 远程: `https://github.com/lookski/sex-neuro-review.git` main = `c502ed5`，与本地一致

## 跨项目: 社交媒体言论核查

- `社交媒体言论核查_20261028.md`（工作区根，17223 B）：22 条流行说法逐条核查，含共同错法清单、跨项目一致性对照、检索负结果

## 总判定

| 项目 | lint | 远程同步 | 判定 |
|---|---|---|---|
| 1.lifespan-evidence | 全部通过 | `630d32a` = `630d32a` | 通过 |
| 2.teeth-evidence | 全部通过 | `e67242d` = `e67242d` | 通过 |
| 3.sex | 引用审计 0 失败 | `c502ed5` = `c502ed5` | 通过 |

三份项目结构校验全部通过，远程仓库均已同步，证据条目与索引计数自洽。

## 未完成事项（如实标注）

- lifespan 中 E01 (40.8%)、E47 (69.0%)、E14、E34、E23、E60、E64、E43、E16、E41、E69 的数字命中率偏低，判定为抽取口径造成的假阴性，未逐条重做
- teeth 的 `README.zh.md` 导航只列 6 条 evidence（英文版列 47 条），属于历史遗留的不对称，本轮未补
- 3.sex 的 `README.md` / `README.zh.md` 停留在 2026-10-03，尚未纳入 10-28 的复核结论
