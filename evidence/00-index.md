# 证据条目索引 (Evidence Index)

> 本目录是 README.md 主报告的逐项分析层。README 只保留结论, 每条证据的详细分析
> (研究设计, 人群, 剂量反应, 机制, 局限性, 与其他证据的一致性) 放在这里, 一个条目一个文件。
> 所有数字均从论文摘要原文机器核验 (Europe PMC `resultType=core`), 核验清单见根目录 `pmids*.txt`。
> 未核验数字一律标注"见原文", 不手工填写。

## 编号规则

- `E01`-`E03`: 总纲 (健康生活方式打包研究)
- `E04`-`E19`: 饮食 (模式/多吃的/少吃的/热量与进食窗口)
- `E20`-`E25`: 运动 + 睡眠
- `E26`-`E30`: 烟酒 + BMI
- `E31`-`E35`: 心理与社会连接
- `E36`-`E43`: 维生素 C 专项
- `E44`-`E46`: 前沿干预 (TAME / 雷帕霉素 / Senolytics)
- `E47`-`E49`: 权威框架 (Life's Essential 8 / Lancet 痴呆委员会 / GBD)
- `E50`-`E52`: 性活动 (性高潮与死亡 / 射精与前列腺癌 / NHANES U 型与心梗触发)
- `E53`: 睡眠三维度比较 (时长 vs 规律性 vs 时间段, 含光照机制)
- `E54`: 工作压力与长工时 (job strain/ERI/IPD-Work 联盟)
- `E55`-`E60`: 维生素 D (观察性剂量反应 + 大型 RCT + RCT meta)
- `E61`-`E63`: Omega-3 海洋脂肪酸 (VITAL 分支 + 两项大型 RCT meta)
- `E64`-`E65`: 复合维生素 (PHS II / COSMOS)
- `E66`-`E68`: 钙补剂与补剂总体 (钙心梗信号 + Iowa 队列的健康使用者偏倚)
- `E69`-`E70`: 蛋白质来源 (植物替代动物, 两条大队列)
- `E71`-`E72`: 桑拿/热暴露 (芬兰队列, 男女兼有)
- `E73`-`E74`: 空气污染 PM2.5 (短期时间序列 meta + 长期队列)
- `E75`-`E77`: 听力损失与痴呆 (队列 + meta + ACHIEVE 干预 RCT)

## 条目清单

| 编号 | 条目 | 类型 | 证据等级 | 文件 |
|---|---|---|---|---|
| E01 | 健康生活方式与无慢病预期寿命 (美国, BMJ 2020) | 前瞻队列×2 | 队列 | [evidence/E01.md](E01.md) |
| E02 | 健康生活方式与中国人群预期寿命 (CKB, Lancet Public Health 2022) | 前瞻队列 | 队列 | [evidence/E02.md](E02.md) |
| E03 | AHA Life's Essential 8 评分与死亡 (NHANES) | 前瞻队列 | 队列 | [evidence/E03.md](E03.md) |
| E04 | 地中海饮食 RCT (PREDIMED 2013/2018 撤回重发) | RCT | RCT | [evidence/E04.md](E04.md) |
| E05 | 地中海饮食依从性与全因死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E05.md](E05.md) |
| E06 | 蔬果摄入与死亡 (剂量反应 meta) | 前瞻队列 meta | 队列 | [evidence/E06.md](E06.md) |
| E07 | 坚果摄入与死亡 (剂量反应 meta) | 前瞻队列 meta | 队列 | [evidence/E07.md](E07.md) |
| E08 | 全谷物与死亡 (剂量反应 meta) | 前瞻队列 meta | 队列 | [evidence/E08.md](E08.md) |
| E09 | 鱼类摄入与全因死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E09.md](E09.md) |
| E10 | 植物蛋白替代动物蛋白与死亡 | 前瞻队列×2 | 队列 | [evidence/E10.md](E10.md) |
| E11 | 咖啡与死亡 (剂量反应 meta) | 前瞻队列 meta | 队列 | [evidence/E11.md](E11.md) |
| E12 | 茶与死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E12.md](E12.md) |
| E13 | 含糖饮料与死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E13.md](E13.md) |
| E14 | 红肉/加工肉与死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E14.md](E14.md) |
| E15 | 鸡蛋与死亡 (meta, 证据分歧) | 前瞻队列 meta | 队列 | [evidence/E15.md](E15.md) |
| E16 | 热量限制 RCT (CALERIE 2) | RCT | RCT | [evidence/E16.md](E16.md) |
| E17 | 热量限制灵长类实验 (恒河猴) | 动物实验 | 动物 | [evidence/E17.md](E17.md) |
| E18 | 限时进食 RCT (8h 窗口 vs 普通节食) | RCT | RCT | [evidence/E18.md](E18.md) |
| E19 | 8 小时进食窗口与心血管死亡 (AHA 会议摘要) | 观察性会议摘要 | 低 | [evidence/E19.md](E19.md) |
| E20 | 总体力活动与死亡 (加速计 meta) | 前瞻队列 meta | 队列 | [evidence/E20.md](E20.md) |
| E21 | 每天步数与死亡 (15 队列 meta) | 前瞻队列 meta | 队列 | [evidence/E21.md](E21.md) |
| E22 | 力量训练与死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E22.md](E22.md) |
| E23 | 久坐与死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E23.md](E23.md) |
| E24 | 睡眠时长与死亡 (J/U 型, meta) | 前瞻队列 meta | 队列 | [evidence/E24.md](E24.md) |
| E25 | 睡眠规律性与死亡 (UK Biobank) | 前瞻队列 | 队列 | [evidence/E25.md](E25.md) |
| E26 | 吸烟与心血管死亡 (CHANCES 个体数据 meta) | 前瞻队列 meta | 队列 | [evidence/E26.md](E26.md) |
| E27 | 戒烟的寿命获益 (CHANCES) | 前瞻队列 meta | 队列 | [evidence/E27.md](E27.md) |
| E28 | 肥胖+吸烟对美国预期寿命的联合预测 | 建模研究 | 建模 | [evidence/E28.md](E28.md) |
| E29 | 饮酒与全因死亡 (J 型曲线的再分析) | 队列 meta+meta 回归 | 队列 | [evidence/E29.md](E29.md) |
| E30 | BMI 与全因死亡 (GBMI 个体数据 meta) | 个体数据 meta | 队列 | [evidence/E30.md](E30.md) |
| E31 | 社会关系与死亡 (经典 meta) | 前瞻队列 meta | 队列 | [evidence/E31.md](E31.md) |
| E32 | 社会隔离/孤独与死亡 (90 队列 meta) | 前瞻队列 meta | 队列 | [evidence/E32.md](E32.md) |
| E33 | 乐观与心血管事件/死亡 (meta + NHS 队列) | meta + 队列 | 队列 | [evidence/E33.md](E33.md) |
| E34 | 人生目标感与死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E34.md](E34.md) |
| E35 | 爱好与目标感 (ikigai) 与老年死亡 | 前瞻队列 | 队列 | [evidence/E35.md](E35.md) |
| E36 | 膳食/血浆维 C 与心血管死亡 (meta) | 前瞻队列 meta | 队列 | [evidence/E36.md](E36.md) |
| E37 | 血浆维 C 与全因死亡 (中国 16 年队列) | 前瞻队列 | 队列 | [evidence/E37.md](E37.md) |
| E38 | 基因高维 C 与死亡 (孟德尔随机化) | 孟德尔随机化 | MR | [evidence/E38.md](E38.md) |
| E39 | 抗氧化补剂与死亡 (Bjelakovic JAMA + Cochrane) | RCT meta | RCT meta | [evidence/E39.md](E39.md) |
| E40 | 维 C 直接 RCT (PHS II, 心血管 + 癌症) | RCT | RCT | [evidence/E40.md](E40.md) |
| E41 | 大剂量静脉维 C 与脓毒症 (CITRIS-ALI + VICTAS) | RCT×2 | RCT | [evidence/E41.md](E41.md) |
| E42 | 大剂量维 C 补剂与肾结石 | 前瞻队列 + meta | 队列 | [evidence/E42.md](E42.md) |
| E43 | 维 C 与感冒 (Cochrane) | RCT meta | RCT meta | [evidence/E43.md](E43.md) |
| E44 | 二甲双胍抗衰 (TAME 试验框架) | 试验设计综述 | 前瞻 | [evidence/E44.md](E44.md) |
| E45 | 雷帕霉素与衰老 (犬 TRIAD + 人体探索) | 进行中试验 | 动物/早期 | [evidence/E45.md](E45.md) |
| E46 | Senolytics 人体初步试验 | 早期 RCT/试点 | 早期 | [evidence/E46.md](E46.md) |
| E47 | AHA Life's Essential 8 框架本身 | 学会声明 | 指南 | [evidence/E47.md](E47.md) |
| E48 | Lancet 痴呆预防委员会 2024 | 委员会报告 | 指南 | [evidence/E48.md](E48.md) |
| E49 | GBD 2021 危险因素归因 | 系统分析 | 负担估计 | [evidence/E49.md](E49.md) |
| E50 | 性高潮频率与死亡 (Caerphilly) | 前瞻队列 | 队列 | [evidence/E50.md](E50.md) |
| E51 | 射精频率与前列腺癌 (HPFS) | 前瞻队列 | 队列 | [evidence/E51.md](E51.md) |
| E52 | 性频率与 CVD/死亡 U 型 + 心梗触发 | NHANES + case-crossover | 队列 | [evidence/E52.md](E52.md) |
| E53 | 睡眠时间段与死亡 (时长/规律/时间点三维比较) | 队列 + 光照测量 | 队列 | [evidence/E53.md](E53.md) |
| E54 | 工作压力与长工时 (job strain → 冠心病/死亡/抑郁; ≥55h/周 → 卒中/房颤) | IPD 联盟 + 队列 meta | 队列 | [evidence/E54.md](E54.md) |
| E55 | 血清 25(OH)D 最低四分位与全因死亡 (NHANES III) | 前瞻队列 | 队列 | [evidence/E55.md](E55.md) |
| E56 | 标准化 25(OH)D 与死亡 (欧洲 8 队列 IPD meta) | 个体数据 meta | 队列 | [evidence/E56.md](E56.md) |
| E57 | 补充维生素 D 与死亡 (52 RCT, 75 454 人) | RCT meta | RCT meta | [evidence/E57.md](E57.md) |
| E58 | VITAL: 2000 IU/日 维生素 D 与癌症/心血管 | RCT | RCT | [evidence/E58.md](E58.md) |
| E59 | D-Health: 60 000 IU/月 与死亡 | RCT | RCT | [evidence/E59.md](E59.md) |
| E60 | 维生素 D 与心血管 (21 RCT, 83 291 人) | RCT meta | RCT meta | [evidence/E60.md](E60.md) |
| E61 | VITAL Omega-3: 1 g/日 与心血管/癌症 | RCT | RCT | [evidence/E61.md](E61.md) |
| E62 | 海洋 omega-3 与心血管 (13 RCT, 127 477 人) | RCT meta | RCT meta | [evidence/E62.md](E62.md) |
| E63 | Omega-3 与心血管结局 (38 RCT, 149 051 人, 含房颤/出血风险) | RCT meta | RCT meta | [evidence/E63.md](E63.md) |
| E64 | PHS II: 复合维生素与癌症 (14 641 男, 11.2 年) | RCT | RCT | [evidence/E64.md](E64.md) |
| E65 | COSMOS: 复合维生素与癌症/心血管 (21 442 人) | RCT | RCT | [evidence/E65.md](E65.md) |
| E66 | 钙补剂与心肌梗死 (15 RCT) | RCT meta | RCT meta | [evidence/E66.md](E66.md) |
| E67 | WHI 再分析: 钙±维 D 与心血管事件 | RCT 再分析 | RCT | [evidence/E67.md](E67.md) |
| E68 | Iowa 女性队列: 补剂与死亡 (健康使用者偏倚) | 前瞻队列 | 队列 | [evidence/E68.md](E68.md) |
| E69 | 动植物蛋白与死亡 (NHS/HPFS, 131 342 人) | 前瞻队列 | 队列 | [evidence/E69.md](E69.md) |
| E70 | 动植物蛋白与死亡 (NIH-AARP, 416 104 人) | 前瞻队列 | 队列 | [evidence/E70.md](E70.md) |
| E71 | 桑拿与致死性心血管/全因死亡 (KIHD, 2315 男) | 前瞻队列 | 队列 | [evidence/E71.md](E71.md) |
| E72 | 桑拿与心血管死亡 (1688 男女, 风险预测) | 前瞻队列 | 队列 | [evidence/E72.md](E72.md) |
| E73 | PM2.5 短期暴露与每日死亡 (110 项时间序列) | 时间序列 meta | 队列 | [evidence/E73.md](E73.md) |
| E74 | PM2.5 长期暴露与心血管死亡 (565 477 人) | 前瞻队列 | 队列 | [evidence/E74.md](E74.md) |
| E75 | 听力损失与痴呆 (639 人, 每 10 dB HR 1.27) | 前瞻队列 | 队列 | [evidence/E75.md](E75.md) |
| E76 | 年龄相关听力损失与认知/痴呆 (40 项研究 meta) | 系统综述+meta | 队列 | [evidence/E76.md](E76.md) |
| E77 | ACHIEVE: 听力干预 RCT 与认知下降 (977 人) | RCT | RCT | [evidence/E77.md](E77.md) |

## 分析模板结构

每个条目文件固定包含以下小节:

1. **一句话结论** — 该证据对"延寿"问题的直接回答
2. **研究设计与人群** — 设计类型, 样本量, 人群特征, 随访时长
3. **关键数字** — 全部为机器核验值, 含 95% CI; 未经核验的标注"见原文"
4. **剂量反应与可执行解读** — 多少剂量起效, 普通人怎么执行
5. **证据强度与局限性** — 因果性, 混杂, 外推性
6. **与其他证据的一致性** — 跨研究互证或矛盾
7. **来源** — 完整引文 (作者, 期刊, 年;卷(期):页, DOI, PMID)

## 证据等级图例

- **RCT**: 随机对照试验, 因果性最强
- **RCT meta**: 多项 RCT 的合并分析
- **队列**: 前瞻性队列研究/其 meta, 反映相关而非因果
- **个体数据 meta**: 用原始个体数据做的 meta, 混杂控制最好 (E26/E30)
- **MR**: 孟德尔随机化, 用基因变异做工具变量近似因果推断 (E38)
- **动物**: 动物实验, 不能直接外推人
- **建模**: 统计建模/情景预测
- **低**: 会议摘要等未经同行评议全文的证据

## 与主报告的关系

- 主报告 `README.md` 第 0-6 节的每张表都对应本目录的条目; 结论以本目录逐项分析为准
- 若逐项分析发现与 README 结论冲突, 修改 README 并在本目录记一行 changelog
- 本索引随条目增加同步更新
