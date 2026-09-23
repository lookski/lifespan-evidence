# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-23 13:05:20
脚本功能: 给 topics/*.md (除 README.md 与 00-total.md 外的维度页) 的
          "## 一句话结论" 节末尾追加 "## TL;DR (EN)" 英文速览节.
          英文速览内容从 TLDR 映射表注入 (人工翻译, 数字照抄中文页,
          数字由 audit_bilingual.py 与中文页回读比对).
参数: argv[1] = "--apply" 实际写回, 缺省只预览
输入格式: topics/*.md (含 "## 一句话结论" 节)
输出格式: stdout 预览/写回报告
依赖: 仅 Python 3 标准库 (pathlib)
注意事项:
  - 英文速览是翻译层, 统计数字必须与中文页完全一致 (审计脚本强制)
  - 已有 "## TL;DR (EN)" 节的页面跳过 (幂等)
  - 数字手填禁令: TLDR 表里的数字是翻译时从中文页复制的, 审计脚本比对两侧
    数字集合, 不一致即报错
"""
from pathlib import Path

# 文件名 (不含 .md) -> 英文速览 (不含标题行, 数字与中文页逐字一致)
TLDR = {
    "01-diet-patterns":
        "You don't need to invent a diet: the Mediterranean pattern (PREDIMED RCT, "
        "major CV events HR 0.69-0.72) and healthy-eating scores (incremental at "
        "every point) are the two best-supported \"pattern-level\" choices.",
    "02-foods":
        "Vegetables/fruit, nuts, whole grains, fish and plant protein each show "
        "dose-response benefits; unsweetened tea and coffee are the right hot "
        "drinks; eggs need no fear at moderate intake.",
    "03-avoid":
        "Sugar-sweetened beverages and processed meat are the two clearest "
        "negatives: each extra daily serving, mortality +8% / +15%; artificially "
        "sweetened drinks are no safer (J-curve rise from 2.5 servings/day).",
    "04-energy":
        "The benefit comes from calories themselves (CALERIE: 11.9% restriction "
        "improved aging biomarkers); an 8-h eating window adds nothing over plain "
        "dieting; \"intermittent fasting extends life\" has no RCT support.",
    "05-activity":
        "The single biggest behavioral lever: device-measured, highest vs lowest "
        "activity HR 0.27; moving from \"inactive\" to \"active\" (Q1 to Q2) "
        "already captures about half the benefit; resistance plus aerobic "
        "training (HR 0.60) beats either alone.",
    "05b-sedentary":
        "Sitting time is an independent risk factor: longest vs shortest, "
        "all-cause mortality HR 1.24, incident diabetes HR 1.91; but 30-40 "
        "min/day of moderate-vigorous activity nearly erases the association — "
        "\"sitting + inactive\" is the real risk combo.",
    "06-sleep":
        "All three sleep dimensions have independent, stacking effects: "
        "regularity (20%-48% lower mortality) \u2265 timing (late bedtime HR "
        "1.27-1.53) > duration (short sleep RR 1.12); mutual adjustment shows "
        "neither is a shadow of the others.",
    "07-tobacco-alcohol-bmi":
        "Smokers' cardiovascular deaths arrive 5.5 years early (quitting at any "
        "age claws it back); the alcohol J-curve is a methodological artifact; "
        "BMI 20-25 is the mortality minimum — \"healthy obesity\" has no "
        "epidemiological footing.",
    "08-social-mind":
        "Strong social ties = 50% higher survival odds; objective isolation is "
        "more dangerous than subjective loneliness; optimism, purpose and "
        "hobbies are each measurable, trainable psychological assets "
        "(HR 0.65-0.83).",
    "09-vitamin-c":
        "\"High plasma vitamin C \u2192 lower mortality\" is real observationally, "
        "but the causal chain fails at all three test layers: MR shows no "
        "causation \u2192 oral RCTs show no effect \u2192 high-dose IV in sepsis "
        "shows no effect; high-dose supplements add kidney-stone risk in men. "
        "The benefit is in foods, not pills.",
    "10-sex":
        "The data run opposite to \"excess shortens life\": the low-orgasm group "
        "had ~90% higher mortality, higher ejaculation frequency does not raise "
        "prostate cancer risk (slightly lower); frequency and mortality are "
        "U-shaped (minimum at roughly weekly), with a suspected-confounding rise "
        "at the extreme high end.",
    "11-frontier":
        "The metformin / rapamycin / senolytics tracks are mechanistically hot "
        "but lack hard human endpoints: TAME has no results, TRIAD and UNITY "
        "are small surrogate-endpoint trials — do not self-medicate.",
    "12-frameworks":
        "Official checklists converge with this handbook: each +10 AHA Life's "
        "Essential 8 points, all-cause mortality aHR 0.79; 45% of dementia is "
        "attributable to 14 modifiable factors; 47.1% of global deaths are "
        "attributable to controllable risks (GBD 2021).",
    "13-work":
        "High-pressure work does cost health, in limited measure: job strain "
        "raises coronary heart disease risk +23%, male mortality +21%, and "
        "clinical depression risk clearly; long hours (\u226555 h/week) raise "
        "stroke +33% and atrial fibrillation +42%; the diabetes risk lands only "
        "in low-socioeconomic-status jobs.",
}

MARK = "## TL;DR (EN)"

def main():
    apply = "--apply" in __import__("sys").argv
    root = Path("topics")
    for f in sorted(root.glob("*.md")):
        if f.name == "README.md" or f.stem == "00-total":
            continue  # 00-total 无一句话结论节, 跳过
        t = f.read_text(encoding="utf-8")
        if MARK in t:
            print(f"[跳过] {f} 已有 TL;DR")
            continue
        key = f.stem
        if key not in TLDR:
            print(f"[缺表] {f} 无 TLDR 条目, 跳过")
            continue
        # 插入位置: "## 一句话结论" 节的末尾 (下一个 "## " 之前)
        idx = t.find("## 一句话结论")
        assert idx >= 0, f
        nxt = t.find("\n## ", idx + 1)
        if nxt < 0:
            nxt = len(t)
        block = f"\n{MARK}\n\n{TLDR[key]}\n"
        new = t[:nxt] + block + t[nxt:]
        if apply:
            f.write_text(new, encoding="utf-8")
            print(f"[修改] {f}  +{block.count(chr(10))} 行")
        else:
            print(f"[预览] {f}")

if __name__ == "__main__":
    main()
