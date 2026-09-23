# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-23 12:20:45
脚本功能: 期刊地位标注器. 扫描 evidence/E*.md 的 "## 来源" 节, 在 **期刊名** 后
          注入一句话地位标注 (从 JOURNALS 映射表查), 输出 diff 预览或直接写回.
          只改 "## 来源" 节内的 **期刊** 标记, 不碰其他内容.
参数: argv[1] = "--apply" 实际写回, 缺省只预览 diff
输入格式: evidence/E*.md (来源节内形如 **Journal** 2019;366:l4570 的引用行)
输出格式: stdout 预览 (文件名 + 注入数); --apply 时同时写回文件
依赖: 仅 Python 3 标准库 (re, pathlib)
注意事项:
  - 标注文字是编辑判断 (期刊层级常识), 不涉及统计数字, 不违反数据真值协议
  - 同一期刊全库统一措辞; 不在映射表中的期刊跳过 (宁缺毋滥)
  - Cochrane 特殊处理: 它是证据合成机构不是期刊, 标注 "Cochrane 系统综述"
"""
import re
import sys
from pathlib import Path

# 期刊 -> 地位标注 (半角标点, 一句话, 不含数字手填统计值)
JOURNALS = {
    "N Engl J Med": " (四大医学周刊之首, 影响因子与临床声誉最高)",
    "Lancet": " (四大医学周刊之一, 全球公卫与临床顶刊)",
    "JAMA": " (四大医学周刊之一, 美国医学会会志)",
    "BMJ": " (四大医学周刊之一, 英国医学会会志)",
    "JAMA Intern Med": " (JAMA 子刊, 普通内科与老年领域权威)",
    "Lancet Public Health": " (Lancet 子刊, 公共卫生领域第一梯队)",
    "Lancet Diabetes Endocrinol": " (Lancet 子刊, 内分泌代谢第一梯队)",
    "Nature": " (综合科学最高刊)",
    "Science": " (综合科学最高刊之一)",
    "Nat Commun": " (Nature 子刊, 综合性开放获取)",
    "Nat Hum Behav": " (Nature 子刊, 行为科学顶刊)",
    "Sci Transl Med": " (Science 子刊, 转化医学顶刊)",
    "Circulation": " (美国心脏协会会志, 心血管第一刊)",
    "Eur Heart J": " (欧洲心脏病学会会志, 心血管第一梯队)",
    "J Am Coll Cardiol": " (美国心脏病学会会志, 心血管第一梯队)",
    "Eur Urol": " (泌尿外科第一刊)",
    "Chest": " (呼吸与重症第一梯队)",
    "Ann Intern Med": " (美国内科医师学会会志, 内科第一梯队)",
    "Br J Sports Med": " (运动医学第一刊)",
    "Am J Clin Nutr": " (营养学第一梯队, 美国营养学会会志)",
    "Adv Nutr": " (美国营养学会综述刊, 证据综合权威)",
    "Am J Epidemiol": " (流行病学经典期刊)",
    "Int J Epidemiol": " (流行病学第一梯队)",
    "Eur J Epidemiol": " (欧洲流行病学主力刊, 常载 IPD 汇总分析)",
    "Psychosom Med": " (心身医学经典期刊)",
    "Psychol Med": " (精神流行病学第一梯队)",
    "Psychol Sci": " (心理科学综合第一梯队)",
    "Sleep": " (睡眠研究专业旗舰刊, 睡眠研究学会会志)",
    "J Clin Sleep Med": " (美国睡眠医学会会志)",
    "Sleep Med Rev": " (睡眠领域综述旗舰)",
    "Cochrane Database Syst Rev": " (Cochrane 系统综述, 被视为证据等级的金标准)",
    "PLoS Med": " (PLoS 系综合旗舰, 医学开放获取第一梯队)",
    "BMC Med": " (BMC 系旗舰, 医学综合开放获取)",
    "Sci Rep": " (Nature 系大型综合开放获取刊, 单篇质量参差, 数字看 CI)",
    "Aging Cell": " (衰老生物学专业旗舰)",
    "EBioMedicine": " (Lancet 系转化医学开放获取刊)",
    "Proc Natl Acad Sci USA": " (美国科学院院刊, 综合权威)",
    "Eur J Prev Cardiol": " (欧洲心脏病学会预防分会刊, 预防心脏学第一梯队)",
    "Public Health Nutr": " (公卫营养专业刊, WHO 欧洲办支持)",
    "JAMA Psychiatry": " (JAMA 子刊, 精神科第一刊)",
    "Mol Psychiatry": " (精神医学基础研究第一刊)",
    "Nat Neurosci": " (神经科学第一刊)",
}

PAT = re.compile(r"\*\*(" + "|".join(re.escape(k) for k in sorted(JOURNALS, key=len, reverse=True)) + r")\*\*")

def annotate(text):
    """在来源节里给 **期刊** 注入标注; 返回 (新文本, 注入数)."""
    n = 0
    def rep(m):
        nonlocal n
        j = m.group(1)
        tag = JOURNALS[j]
        # 已有标注 (后跟 " (" 且在 "2019;.." 前) 就跳过
        tail = text[m.end():m.end() + len(tag)]
        if tail == tag:
            return m.group(0)
        n += 1
        return f"**{j}**{tag}"
    return PAT.sub(rep, text), n

def main():
    apply = "--apply" in sys.argv
    root = Path("evidence")
    total = 0
    for f in sorted(root.glob("E*.md")):
        text = f.read_text(encoding="utf-8")
        # 只处理 "## 来源" 之后的部分
        idx = text.find("## 来源")
        if idx < 0:
            continue
        head, tail = text[:idx], text[idx:]
        new_tail, n = annotate(tail)
        if n:
            print(f"[修改] {f}  注入 {n} 处")
            total += n
            if apply:
                f.write_text(head + new_tail, encoding="utf-8")
    print(f"合计 {total} 处" + ("  (已写回)" if apply else "  (预览, 加 --apply 生效)"))

if __name__ == "__main__":
    main()
