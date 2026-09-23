# The Science of Living Longer: An Evidence Handbook

> **[中文版](README.md) | English** — a translation of the Chinese README.
> Read online: **https://lookski.github.io/lifespan-evidence/** (full-text search)

![License](https://img.shields.io/badge/content-CC--BY_4.0-blue) ![Method](https://img.shields.io/badge/figures-Europe_PMC_verified-56c49b) ![Version](https://img.shields.io/badge/version-v0.1-green)

> Compiled: 2026-09-20 23:12:47 (system time at creation).
> Search method: Europe PMC REST API (`https://www.ebi.ac.uk/europepmc/webservices/rest/search`), sorted by citations.
> Every key figure was checked line-by-line against the original paper abstract
> (Europe PMC `resultType=core`), not typed from memory.
> Scripts: `pmc_search.py` / `verify_abstracts.py`; search terms and verified PMID
> lists in `q*.json` / `pmids*.txt`.
>
> **General caveat**: except for PREDIMED and CALERIE (randomized controlled trials),
> most evidence comes from prospective cohorts and meta-analyses — it shows
> *association*, not causation. All HR/RR/OR are relative risks and must be read
> with their 95% CI. Individual variation is large; consult a doctor before major changes.

---

## How to read this handbook: three layers

```
README.md / README.en.md   Summary layer: conclusions + navigation
topics/*.md                Dimension briefs: one page per dimension, quick tables
evidence/E*.md             Per-item analyses: one file per study, 7-section template
```

**Two most surprising findings first**:

- **Weak social ties = survival OR 1.50 (1.42-1.59)**, on par with quitting smoking
  and obesity — "loneliness harms" is not a platitude but a cohort figure from
  148 studies, 308,849 people ([E31](evidence/E31.md))
- **Sleep regularity predicts mortality better than duration**: the most regular
  group had 20%-48% lower risk; adding duration does not improve the model
  ([E25](evidence/E25.md), UK Biobank accelerometry)

**Dimension briefs** ([topics/](topics/)):

| Page | Dimension | One-liner |
|---|---|---|
| [00-total](topics/00-total.md) | The big picture | Lifestyle package: 8-10 years (China) to 12-14 years (US, Circulation 2018) |
| [01-diet-patterns](topics/01-diet-patterns.md) | Dietary patterns | Mediterranean HR 0.69-0.72; every score point counts |
| [02-foods](topics/02-foods.md) | Foods to eat more | Vegetables/fruit, nuts, whole grains, fish, plant protein |
| [03-avoid](topics/03-avoid.md) | Foods to cut back | SSB +8%/serving, processed meat +15%/serving |
| [04-energy](topics/04-energy.md) | Calories & eating window | Benefit comes from calories; time-restricted eating adds nothing |
| [05-activity](topics/05-activity.md) | Physical activity | Biggest single lever: Q4 vs Q1 HR 0.27 |
| [05b-sedentary](topics/05b-sedentary.md) | Sedentary time | Independent harm HR 1.24; 30-40 min/day offsets it |
| [06-sleep](topics/06-sleep.md) | Sleep (3 dimensions) | Regularity ≥ timing > duration; effects stack |
| [07-tobacco-alcohol-bmi](topics/07-tobacco-alcohol-bmi.md) | Tobacco, alcohol, weight | Smoking costs 5.5 years; the alcohol J-curve is an artifact; BMI 20-25 |
| [08-social-mind](topics/08-social-mind.md) | Mind & social ties | Strong ties: survival OR 1.50; isolation worse than loneliness |
| [09-vitamin-c](topics/09-vitamin-c.md) | Vitamin C full chain | The benefit is in foods, not pills |
| [10-sex](topics/10-sex.md) | Sexual activity | Opposite of folk wisdom: regular activity tracks lower risk |
| [11-frontier](topics/11-frontier.md) | Anti-aging frontier | Metformin/rapamycin/senolytics: no hard-endpoint evidence yet |
| [12-frameworks](topics/12-frameworks.md) | Official frameworks | LE8 / dementia commission / GBD converge on the same list |
| [13-work](topics/13-work.md) | Work stress & long hours | Job strain: CHD +23%; ≥55 h/week: stroke +33% |

Per-study analyses: [evidence/00-index.md](evidence/00-index.md) (E01-E54).

---

## 0. The bottom line: how many years is a healthy lifestyle worth

The most important group of studies — lifestyle packaged, answering "how many years" directly.

| Population | Study | Key numbers (machine-verified) | Source |
|---|---|---|---|
| US adults | Nurses' Health Study + Health Professionals Follow-up Study, n≈112,000, ~34 y follow-up | Women aged 50 with all 5 low-risk factors (non-smoking, BMI 18.5-24.9, ≥30 min/day moderate-vigorous activity, moderate alcohol, diet in top 40%): chronic-disease-free life expectancy **34.4 y (95% CI 33.1-35.5)** vs **23.7 y (22.6-24.7)** with 0 factors; men **31.1 y (29.5-32.5)** vs **23.5 y (22.3-24.7)**; total life expectancy from the same cohorts: women +14.0 y (11.8-16.2), men +12.2 y (10.1-14.2) | Li Y, et al. **BMJ 2020;368:l6669.** doi:10.1136/bmj.l6669 (PMID 31915124); Li Y, et al. **Circulation 2018;138(4):345-355.** doi:10.1161/CIRCULATIONAHA.117.032047 (PMID 29712712) |
| Chinese adults | China Kadoorie Biobank (CKB), n≈487,000, median 11.1 y | At age 30, men with all 5 low-risk factors: life expectancy **50.5 y (48.5-52.4)**, women **55.4 y (53.5-57.4)**; 0-1 factors: men 41.7 y (41.5-42.0), women 47.3 y (46.6-48.0); gap **men +8.8 y (6.8-10.7), women +8.1 y (6.5-9.9)** | **Lancet Public Health 2022;7(12):e1029-e1039.** doi:10.1016/S2468-2667(22)00110-4 (PMID 35926549) |
| US adults | NHANES 2005-2018 linked to mortality records, n=19,951, median 7.6 y | AHA "Life's Essential 8" high score (≥75): all-cause mortality **HR 0.42 (95% CI 0.32-0.56)**; moderate (50-74): **HR 0.60 (0.51-0.71)** vs low scorers | Sun J, et al. **BMC Med 2023;21:96.** doi:10.1186/s12916-023-02824-8 (PMID 36978123) |

**Reading**: in Chinese adults the 5-factor package tracks a +8.8 y / +8.1 y life-expectancy
gap, driven mostly by cardiovascular disease (+2.4/+3.7 y), cancer (+2.6/+0.9 y) and
chronic respiratory disease (+0.6/+1.2 y). Behavior change is the cheapest longevity drug.

---

## 1. Diet

### 1.1 Whole dietary patterns

| Exposure | Key numbers (machine-verified) | Source |
|---|---|---|
| **Mediterranean diet (RCT)** | 7,447 people at cardiovascular risk randomized, median 4.8 y: major CV events (MI/stroke/CV death) 3.8% (olive-oil arm) vs 4.4% control, **HR 0.69 (95% CI 0.53-0.91)**; nuts arm 3.4%, **HR 0.72 (0.54-0.95)**. The 2013 paper was retracted and republished in 2018 after randomization irregularities — these are the corrected figures | Estruch R, et al. **N Engl J Med 2018;378:e34.** doi:10.1056/NEJMoa1800389 (PMID 29897866) |
| **Mediterranean adherence ↑, mortality ↓** | 29 prospective cohorts, 1,676,901 people, 221,603 deaths: each +2 adherence points, all-cause mortality **HR 0.90 (95% CI 0.89-0.91)**, linear dose-response | Soltani S, et al. **Adv Nutr 2019;10(6):1029-1045.** doi:10.1093/advances/nmz041 (PMID 31111871) |

**Takeaway**: the Mediterranean pattern has the strongest dietary evidence — vegetables
and fruit, whole grains, legumes, nuts, olive oil, fish often, red/processed meat rarely.
Copy the structure, not the recipes.

### 1.2 Foods to eat more of (doses from meta-analyses)

| Food | Key numbers (machine-verified) | Source |
|---|---|---|
| **Vegetables & fruit** | Each +200 g/day: all-cause mortality RR **0.90 (95% CI 0.87-0.93)**; benefit keeps accruing to **800 g/day (~10 servings)**, except cancer (plateau at 600 g/day); marginal gains flatten past ~400 g/day (Circulation 2021 cohort+meta) | Aune D, et al. **Int J Epidemiol 2017;46(3):1029-1056.** doi:10.1093/ije/dyw319 (PMID 28338764); Miller V, et al. **Circulation 2021;143(23):2302-2313.** doi:10.1161/CIRCULATIONAHA.120.048996 (PMID 33641343) |
| **Nuts** | Each +28 g/day: all-cause mortality RR **0.78 (95% CI 0.72-0.84)**, CHD 0.71 (0.63-0.80), CVD 0.79 (0.70-0.88), cancer 0.85 (0.76-0.94) | Aune D, et al. **BMC Med 2016;14:207.** doi:10.1186/s12916-016-0730-3 (PMID 27916000) |
| **Whole grains** | Each +90 g/day (3 servings): all-cause mortality RR **0.83 (95% CI 0.77-0.90)**, CHD 0.81 (0.75-0.87), cancer 0.85 (0.80-0.91); benefit continues to 210-225 g/day; no association for refined grains/white rice | Aune D, et al. **BMJ 2016;353:i2716.** doi:10.1136/bmj.i2716 (PMID 27301975) |
| **Fish** | Cohort meta: fish intake inversely associated with all-cause mortality (Eur J Clin Nutr 2016); for pooled HRs at the 100 g/week level see the original tables | Jayedi A, et al. **Eur J Clin Nutr 2016.** doi:10.1038/ejcn.2015.72 (PMID 25969396); update: Zhong VW, et al. J Intern Med 2018 |
| **Plant replacing animal protein** | 131,342 people (NHS+HPFS), ~30 y: each +3% energy from plant protein, all-cause mortality **HR 0.90 (95% CI 0.86-0.95)**; animal protein not significantly associated with all-cause mortality (HR 1.02, 0.98-1.05) but positively with CV mortality (HR 1.08, 1.01-1.16); substitution for processed red meat tracks lower mortality | Song M, et al. **JAMA Intern Med 2016;176(10):1453-1463.** doi:10.1001/jamainternmed.2016.4182 (PMID 27479196) |
| **Coffee** | Umbrella review (BMJ 2017, 201 meta-analyses): coffee inversely associated with all-cause mortality and many outcomes; benefit most consistent at 3-4 cups/day; caffeine limits in pregnancy and high-risk groups | Poole R, et al. **BMJ 2017;359:j5024.** doi:10.1136/bmj.j5024 (PMID 29167102); Grosso G, et al. **Eur J Epidemiol 2019.** doi:10.1007/s10654-019-00524-3 (PMID 31055709) |
| **Tea** | 38 prospective cohorts meta: nonlinear inverse association with all-cause mortality, minimum risk at **~2 cups/day (ES 0.91, 95% CI 0.88-0.94)**; cancer mortality minimum ~1.5 cups (0.92); CVD mortality keeps falling past a 1.5-3 cup plateau | Xu R, et al. **Epidemiol Health 2024;46:e2024056.** doi:10.4178/epih.e2024056 (PMID 38938012) |

### 1.3 Foods to cut back

| Food | Key numbers (machine-verified) | Source |
|---|---|---|
| **Sugar-sweetened beverages** | Each +1 serving/day (355 mL): all-cause mortality **HR 1.08 (95% CI 1.04-1.12)**, CV mortality HR 1.08 (1.04-1.12); artificially sweetened drinks show a J-curve, HR 1.13 (1.09-1.18) at 2.5 servings/day — "zero sugar" is not free either | Zhang YB, et al. **Adv Nutr 2021;12(2):374-403.** doi:10.1093/advances/nmaa110 (PMID 33786594) |
| **Processed meat** | Each +1 serving/day: all-cause mortality RR **1.15 (95% CI 1.11-1.19)**, nonlinear (steeper rise at low intakes) | Qian F, et al. **Public Health Nutr 2016;19(15):2703-2718.** doi:10.1017/s1368980015002062 (PMID 26143683); consistent meta in Ann Intern Med 2019 (PMID 31569213) |
| **Eggs (mixed evidence)** | Adv Nutr 2022 (33 cohorts, 2,216,720 people): highest vs lowest intake, all-cause mortality RR **1.02 (95% CI 0.94-1.11)** (not significant), cancer mortality 1.20 (1.04-1.39) up, stroke mortality 0.81 (0.64-1.02) down; +1 egg/week: all-cause +2%, cancer +4%. Circulation 2022 (ATBC smoking men + meta): +50 g eggs/day, all-cause HR 1.06 / CV mortality 1.09 — the risk signal concentrates in US/European cohorts, **no significant association in Asian cohorts** | Tahvildari S, et al. **Adv Nutr 2022.** doi:10.1093/advances/nmac040 (PMID 35396834); Zhuang P, et al. **Circulation 2022;145(20):1506-1520.** doi:10.1161/CIRCULATIONAHA.121.057642 (PMID 35360933) |

### 1.4 Calorie restriction & eating windows (how much vs when)

| Intervention | Key numbers (machine-verified) | Source |
|---|---|---|
| **Calorie restriction (CR) RCT** | CALERIE 2: 218 healthy non-obese adults, 2 y, sustained **11.9% CR**; aging biomarkers improved, no psychological/behavioral adverse effects | Redman LM, et al. (CALERIE) **Nutr Rev 2021;79(9):983-1001.** doi:10.1093/nutrit/nuaa085 (PMID 32940695); telomere analysis: **Aging Cell 2024;23(4):e14149.** doi:10.1111/acel.14149 (PMID 38504468) |
| **Primate evidence** | Monkeys: ~30% CR from youth, improved age-related and all-cause survival (Wisconsin 2014); NIA 2012 found no survival difference, but post-hoc the control arm was also near CR | Colman RJ, et al. **Science 2009;325(5937):201-204** (PMID 19590001); **Nat Commun 2014;5:3557.** doi:10.1038/ncomms4557 (PMID 24691430) |
| **Time-restricted eating (8 h) RCT** | 139 adults with obesity, 12 months, 8:00-16:00 eating + CR vs CR alone: weight -8.0 vs -6.3 kg, between-arm difference **-1.8 kg (95% CI -4.0 to 0.4), P=0.11** — TRE not superior to CR alone | Liu D, et al. **N Engl J Med 2022;386(26):2467-2477.** doi:10.1056/NEJMoa2114833 (PMID 35443107) |
| **⚠ Long-term safety of 8-h eating windows unclear** | AHA EPI/Lifestyle 2024 conference abstract (NHANES 2003-2018 linked mortality, ~15 y): self-reported 8-h eating window, CV death ~**91%** higher vs 12-16 h. **Caution: conference abstract, not peer-reviewed full text, observational, methodological disputes** | AHA Scientific Sessions press release: https://newsroom.heart.org/news/8-hour-time-restricted-eating-linked-to-91-higher-risk-of-cardiovascular-death |

**Reading**: the evidence for "eat a bit less" is far stronger than for "eat at X o'clock".
Moderate CR has a complete chain from worms and mice through primates to CALERIE, but
sustaining 20-30% restriction is hard for most people; the realistic version is avoiding
excess (fewer sugary drinks and processed snacks). Time-restricted eating works as a
weight-loss tool about as well as ordinary dieting; long-term safety (especially very
narrow windows) is unsettled.

---

## 2. Daily habits

### 2.1 Physical activity: the single biggest win

| Metric | Key numbers (machine-verified) | Source |
|---|---|---|
| **Total activity (device-measured)** | 8 accelerometer studies, n=36,383, median 5.8 y, 2,149 deaths: top vs bottom quartile of total activity, all-cause mortality **HR 0.27 (95% CI 0.23-0.32)**; second quartile already HR 0.48 (0.43-0.54) — the biggest marginal gain is getting from "inactive" to "active" | Ekelund U, et al. **BMJ 2019;366:l4570.** doi:10.1136/bmj.l4570 (PMID 31434697) |
| **Daily steps** | 15 international cohorts, 47,471 people, 3,013 deaths, median 7.1 y: vs lowest quartile (~3,553 steps), highest (~10,901) all-cause mortality **HR 0.47 (95% CI 0.39-0.57)**; risk plateau: ≥60 y at **6,000-8,000 steps/day**, <60 y at **8,000-10,000** | Paluch AE, et al. **Lancet Public Health 2022;7(3):e219-e228.** doi:10.1016/S2468-2667(21)00302-9 (PMID 35247352) |
| **Resistance training** | 11 studies, 370,256 people, mean 8.85 y: resistance training vs none, all-cause mortality **HR 0.79 (95% CI 0.69-0.91)**; resistance+aerobic combined **HR 0.60 (0.49-0.72)** | Momma H, et al. **Eur J Prev Cardiol 2022;29(12):1647-1662.** (online 2019) doi:10.1177/2047487319850718 (PMID 31104484) |
| **Sedentary time (independent risk)** | 13-study meta: longest vs shortest sitting time, all-cause mortality **HR 1.24 (95% CI 1.09-1.41)**, incident type 2 diabetes HR 1.91 (1.64-2.22); risk most pronounced in low-activity people | Biswas A, et al. **Ann Intern Med 2015;162(2):123-132.** doi:10.7326/M14-1651 (PMID 25599350) |

**Takeaway**: any movement beats none, sooner beats later. A practical target is
7,000-8,000 steps/day + resistance training twice a week; break up sitting every hour.

### 2.2 Sleep

| Metric | Key numbers (machine-verified) | Source |
|---|---|---|
| **Sleep duration (J/U-shaped)** | 16 studies, 27 cohorts, 1,382,999 people, 112,566 deaths: short sleep (<7 h) all-cause mortality **RR 1.12 (95% CI 1.06-1.18)**; long sleep (>8-9 h) also elevated (both directions significant in the source) | Cappuccio FP, et al. **Sleep 2010;33(5):585-594.** doi:10.1093/sleep/33.5.585 (PMID 20469800) |
| **Sleep regularity (newer evidence)** | UK Biobank, 60,977 people, >10 million accelerometer-hours: highest vs lowest sleep regularity index, all-cause mortality **20%-48% lower**, and regularity outpredicts duration | Windred DP, et al. **Sleep 2024;47(1):zsad253.** doi:10.1093/sleep/zsad253 (PMID 37738616); eLife 2023;12:e88359 (PMID 37995126) |

**Takeaway**: aim for 7-9 h (individualized), but **going to bed and getting up at the
same time every day** may matter more than "getting 8 hours".

### 2.3 Tobacco & alcohol

| Exposure | Key numbers (machine-verified) | Source |
|---|---|---|
| **Smoking** | 25 cohorts, 503,905 people 60+: current smokers CV mortality **HR 2.07 (95% CI 1.82-2.36)**, CV deaths occurring **5.50 y (4.25-6.75) earlier** | Gellert C, et al. **BMJ 2015;350:h1551.** doi:10.1136/bmj.h1551 (PMID 25896935); consistent with GBMI/Lancet studies |
| **Quitting (works at any age)** | Same CHANCES analysis: former smokers CV mortality HR falls to 1.37 (1.25-1.49), advance period shrinks to **2.16 y (1.38-2.39)**; risk keeps declining with years since quitting | Same source (PMID 25896935) |
| **Combined obesity + smoking** | Modeling: if all US adults became non-smokers of normal weight by 2020, life expectancy at 18 would rise **3.76 y (5.16 quality-adjusted)** | Stewart ST, et al. **N Engl J Med 2009;361(20):1985-1995.** doi:10.1056/NEJMsa0900459 (PMID 19955525) |
| **Alcohol (the J-curve is an artifact)** | 87 studies, 3,998,626 people, 367,103 deaths: without quality correction, light drinkers RR 0.86 (0.83-0.90) — the classic J-curve; **after correcting for study-design bias, light drinking shows no net benefit vs lifetime abstainers** | Stockwell T, et al. **J Stud Alcohol Drugs 2016;77(2):185-198.** doi:10.15288/jsad.2016.77.185 (PMID 26997174) |
| **BMI and mortality** | 239 studies, 4 continents, 3.95 million never-smokers, IPD meta: all-cause mortality minimum at **BMI 20.0-25.0 kg/m²**; overweight and every obesity grade consistently higher | Global BMI Mortality Collaboration. **Lancet 2016;388(10046):776-786.** doi:10.1016/S0140-6736(16)30175-1 (PMID 27423262) |

**Takeaway**: don't smoke (vaping included) and don't drink are the two hardest-hitting
lines. Target BMI 18.5-25.

### 2.4 Mind & social connection (long underrated)

| Exposure | Key numbers (machine-verified) | Source |
|---|---|---|
| **Social relationships** | 148 studies, 308,849 people: stronger social ties, survival **OR 1.50 (95% CI 1.42-1.59)**; effect size comparable to quitting smoking or obesity | Holt-Lunstad J, et al. **PLoS Med 2010;7(7):e1000316.** doi:10.1371/journal.pmed.1000316 (PMID 20668659) |
| **Social isolation / loneliness** | 90 cohorts, 2,205,199 people: social isolation all-cause mortality **ES 1.32 (95% CI 1.26-1.39)**, loneliness **1.14 (1.08-1.20)**; isolated people CV mortality 1.34 (1.25-1.44) | Wang F, et al. **Nat Hum Behav 2023;7(7):1079-1096.** doi:10.1038/s41562-023-01617-6 (PMID 37337095) |
| **Optimism** | 15 studies, 229,391 people, mean 13.8 y: optimists CV events **RR 0.65 (95% CI 0.51-0.78)**; all-cause mortality also lower (9-study pooled estimate significant) | Rozanski A, et al. **JAMA Netw Open 2019;2(9):e1912200.** doi:10.1001/jamanetworkopen.2019.12200 (PMID 31560385) |
| **Purpose in life** | Meta: higher purpose associated with lower all-cause mortality and CV events (effect sizes in the original tables) | Cohen R, et al. **Psychosom Med 2016;78(2):122-135.** doi:10.1097/PSY.0000000000000274 (PMID 26630073) |
| **Hobbies** | Japanese Ohsaki elderly cohort: having hobbies associated with lower mortality and maintained ADL/IADL (see original tables) | Tomida K, et al. **J Epidemiol 2016.** doi:10.2188/jea.je20150153 (PMID 26947954) |

**Takeaway**: maintaining close relationships is not a "soft" recommendation — the
effect size rivals smoking cessation. Regular social activities + hobbies + purpose.

---

## 3. Supplement case study: vitamin C ("does vitamin C lengthen life?")

**One-line conclusion: vitamin C as a supplement does not extend life and does not
lower mortality; the vitamin C in fruit and vegetables is part of a beneficial dietary
pattern.** Supplement if deficient (scurvy risk); if not deficient, supplementing adds nothing.

| Evidence type | Key numbers (machine-verified) | Source |
|---|---|---|
| **Observational: high dietary/plasma vitamin C, lower mortality** | 15+3 prospective studies, 320,548 people: highest vs lowest dietary vitamin C, CV mortality RR **0.79 (95% CI 0.68-0.89)**; highest plasma concentration RR **0.60 (0.42-0.78)** — but this reflects "people who eat more produce are healthier overall" | Jayedi A, et al. **Public Health Nutr 2019;22(12):1872-1887.** doi:10.1017/S1368980018003725 (PMID 30630552) |
| **Observational: 16-year Chinese cohort** | 948 people, 551 deaths: adequate plasma vitamin C (>28 µmol/L) vs inadequate, all-cause mortality **HR 0.77 (0.63-0.95)**, heart-disease mortality 0.62 (0.42-0.89) | Wang SM, et al. **J Epidemiol Community Health 2018;72(12):1076-1082.** doi:10.1136/jech-2018-210809 (PMID 30100578) |
| **Causal test: Mendelian randomization (MR)** | 97,203 genotyped: genetically higher plasma vitamin C vs all-cause mortality, CI crosses 1.0 (not significant) — "cannot rule out that part of the produce benefit comes from vitamin C, but no causal evidence either" | Kobylecki CJ, et al. **Am J Clin Nutr 2015;101(6):1213-1222.** doi:10.3945/ajcn.114.104497 (PMID 25948669) |
| **RCT: large antioxidant-supplement meta (incl. vitamin C)** | Bjelakovic 2007 (68 RCTs, 232,606 people): β-carotene/vitamin A/E **increase** mortality, **vitamin C no significant effect on mortality**; Cochrane 2012 (78 RCTs, 296,707 people): in low-bias-risk trials antioxidant supplements overall increase mortality (RR 1.04, 1.01-1.07); vitamin C alone RR 1.02 (CI crosses 1, no effect) | Bjelakovic G, et al. **JAMA 2007;297(8):842-857.** doi:10.1001/jama.297.8.842 (PMID 17327526); Cochrane: **Cochrane Database Syst Rev 2012;3:CD007176.** doi:10.1002/14651858.CD007176.pub2 (PMID 22419320) |
| **RCT: vitamin C directly (PHS II)** | 14,641 US male physicians randomized double-blind to 500 mg/d vitamin C, mean 8 y: major CV events **HR 0.99 (95% CI 0.89-1.11)**, CV mortality 1.02 (0.85-1.21), all-cause 1.07 (0.97-1.18) — no significant benefit anywhere | Sesso HD, et al. **JAMA 2008;300(18):2123-2133.** doi:10.1001/jama.2008.600 (PMID 18997197) |
| **RCT: high-dose IV vitamin C in sepsis** | CITRIS-ALI (167 people) and VICTAS (501): high-dose IV vitamin C (± thiamine/hydrocortisone) did not significantly improve organ-failure scores, ventilator days, or 30-day mortality | Fowler AA, et al. **JAMA 2019;322(8):751-760.** doi:10.1001/jama.2019.11825 (PMID 31573637); VICTAS: **JAMA 2021;325(8):742-750.** doi:10.1001/jama.2020.24505 (PMID 33620405) |
| **⚠ Safety: high-dose vitamin C supplements and kidney stones** | Swedish male cohort (COSM): ≥1,000 mg/d ascorbic-acid supplements associated with significantly higher kidney-stone risk vs non-users (short report; HR in the original); subsequent meta (4 studies): significant positive association in men at 250-499 mg/d (OR 1.14, 95% CI 1.00-1.28) and other dose bands, no significant association in women | Thomas LDK, et al. **JAMA Intern Med 2013;173(5):386-388.** doi:10.1001/jamainternmed.2013.2296 (PMID 23381591); meta: **Urol J 2019.** doi:10.22037/uj.v0i0.4275 (PMID 30178451) |

**Reading**: "high plasma vitamin C → lower mortality" holds observationally, but vitamin
C is a marker of produce intake; when vitamin C is given directly in RCTs the benefit
vanishes and very high doses may add kidney-stone risk. This is a textbook instance of
the handbook's methodological warning: **nutrient supplements ≠ whole foods**. If daily
produce intake falls short, small-dose supplements (100-200 mg/d, about one RDI) have no
evidence of harm, but don't expect life extension; mega-dosing effervescent vitamin C at
cold onset has weak evidence (Cochrane: routine supplementation does not prevent colds
in the general population; it shortens duration by 8% [3%-12%] in adults, 14% [7%-21%]
in children; people under acute physical stress — e.g. marathon runners — are the one
exception) — see Hemilä H, et al. **Cochrane Database Syst Rev 2013;1:CD000980.**
doi:10.1002/14651858.CD000980.pub4.

---

## 4. Research frontier: anti-aging interventions (temper expectations)

> Background: aging is organized into "hallmarks"; see López-Otín C, et al.
> **Cell 2013;153(6):1194-1217.** doi:10.1016/j.cell.2013.05.039 (PMID 23746838, cited
> 12,000+); 2023 expansion **Cell 2023;186(2):243-278.** doi:10.1016/j.cell.2022.11.001 (PMID 36599349).

| Direction | Status | Source |
|---|---|---|
| **Metformin (TAME trial)** | RCT with "aging" as clinical endpoint planned, not completed; current evidence mostly animal and observational | Barzilai N, et al. **Cell Metab 2016;24(3):407-414.** doi:10.1016/j.cmet.2016.05.011 (PMID 27304507) |
| **Rapamycin/mTOR** | Strong lifespan evidence in animals (dog TRIAD trial ongoing); low-dose human immunology/skin exploratory trials show biomarker changes, **no lifespan endpoints** | Dog Aging Project TRIAD: **Geroscience 2025.** doi:10.1007/s11357-024-01484-7 (PMID 39951177); skin RCT: **Geroscience 2019.** doi:10.1007/s11357-019-00113-y (PMID 31761958) |
| **Senolytics (clearing senescent cells)** | Dasatinib+quercetin early human trials (diabetic kidney disease, idiopathic pulmonary fibrosis, cognition/physical function) show feasibility and partial improvements; small samples, no lifespan endpoints | Hickson LJ, et al. **EBioMedicine 2019;48:471-482.** doi:10.1016/j.ebiom.2019.08.069 (PMID 31542391); Schafer MJ, et al. **EBioMedicine 2025.** doi:10.1016/j.ebiom.2025.105612 (PMID 40010154) |
| **CR mimetics, stem cells, young plasma, etc.** | Mostly animal-stage; insufficient human evidence | — |

**Conclusion**: **no drug has been proven to extend human lifespan**. Any supplement
claiming "ten extra years" has no reliable human evidence. If you can wait, wait for
large RCTs; if you can't, go back to sections 0-2.

---

## 5. What the authoritative bodies say (directly actionable)

| Body / framework | Key points | Source |
|---|---|---|
| **AHA Life's Essential 8** | Scores diet, activity, nicotine exposure, sleep health, BMI, lipids, glucose, blood pressure — a quantifiable "longevity dashboard" | Lloyd-Jones DM, et al. **Circulation 2022;146(5):e18-e43.** doi:10.1161/CIR.0000000000001078 (PMID 35766027) |
| **Lancet dementia commission 2024** | Modifiable risk factors expanded to 14: education, hearing, vision loss, depression, diabetes, high LDL, hypertension, obesity, smoking, excess alcohol, physical inactivity, social isolation, brain injury, PM2.5 (PAF values in the original) | Livingston G, et al. **Lancet 2024;404(10452):572-628.** doi:10.1016/S0140-6736(24)01296-0 (PMID 39096926) |
| **GBD 2021 risk attribution** | Systematic analysis of disease burden for 88 risk factors, 2021; metabolic (hypertension etc.), behavioral (smoking etc.) and environmental classes dominate preventable death | GBD 2021 Risk Factors Collaborators. **Lancet 2024;403(10440):2162-2196.** doi:10.1016/S0140-6736(24)00933-4 (PMID 38762324) |
| **Validation in Chinese adults** | The 5-factor model validated in the CKB cohort (section 0); "Healthy China 2030" targets the same factors | Lancet Public Health 2022 (PMID 35926549) |

---

## 6. One-page summary (ordered by evidence strength)

**Hardest evidence (RCTs / mega-metas — just do these)**:
1. Don't smoke, don't drink
2. ~7,000-8,000 steps/day + resistance training twice a week, sit less
3. BMI 18.5-25
4. Diet: plenty of vegetables and fruit (target 400-800 g/day), 28 g/day nuts, 90 g+/day whole grains, fish regularly, replace some red/processed meat with plant protein; few sugar-sweetened beverages and processed meats; eggs in moderation (~3-7/week) — neither feared nor overdone
5. Sleep 7-9 h, and **keep it regular**
6. Maintain social ties, keep hobbies and purpose

**Moderate evidence (follow along, no need for extremes)**:
- Mediterranean-style pattern; moderate calorie control (avoid chronic excess); coffee 3-4 cups (unsweetened) and tea in moderation

**Low/uncertain evidence (don't spend big money)**:
- Vitamin C and other antioxidant supplements as life-extension tools (no RCT benefit; high doses carry kidney-stone risk — section 3)
- Long-term safety of very narrow eating windows (>14 h fasting); various "anti-aging supplements"; metformin/rapamycin for healthy people (experimental)

**The single most important number**: in Chinese adults, keeping 5 healthy lifestyle
factors from age 30 tracks a life-expectancy gap of +8.8 years in men and +8.1 years in
women (Lancet Public Health 2022, PMID 35926549).

---

## Appendix: evidence grades used in this handbook

- **RCT**: PREDIMED (Mediterranean diet), CALERIE 2 (calorie restriction), Liu 2022 (time-restricted eating) — interventional evidence
- **Prospective cohort meta-analyses**: the source of every other number — observational, residual confounding cannot be excluded
- **Conference abstract**: AHA 2024 8-hour eating window data — lowest grade, reference only
- All key figures verified on 2026-09-20 by read-back against Europe PMC abstracts

## Appendix: reproducing this handbook

```bash
# Search
python lifespan-evidence/pmc_search.py lifespan-evidence/q1.json 5   # q1-q9 in turn
# Supplementary searches: spermidine candidates (q_guess) and vitamin C (q_vc, q_vc2)
python lifespan-evidence/pmc_search.py lifespan-evidence/q_guess.json 3
python lifespan-evidence/pmc_search.py lifespan-evidence/q_vc.json 5
python lifespan-evidence/pmc_search.py lifespan-evidence/q_vc2.json 5
# Number verification
python lifespan-evidence/verify_abstracts.py lifespan-evidence/pmids.txt     # pmids1-4 in turn
python lifespan-evidence/verify_abstracts.py lifespan-evidence/pmids_vc.txt  # vitamin C set
python lifespan-evidence/verify_abstracts.py lifespan-evidence/pmids_vc2.txt
python lifespan-evidence/verify_abstracts.py lifespan-evidence/pmids_vc3.txt
```

Files: `pmc_search.py` (search), `verify_abstracts.py` (verify), `q*.json` (search
terms), `pmids*.txt` (verification lists), `README.md` (Chinese summary), `README.en.md`
(this file), `topics/` (dimension briefs), `evidence/` (per-study analyses).

## Cite & license

- Citation: `lookski. The Science of Living Longer: An Evidence Handbook. GitHub, 2026.`
- Content (README/topics/evidence): **CC BY 4.0** — attribution plus a link to
  this repository when redistributing
- Utility scripts (the search/verify/audit pipeline): MIT — reuse them to
  verify your own topic
- This handbook is a structured summary of published epidemiological research,
  not medical advice; consult a doctor for personal decisions
