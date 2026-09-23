# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-24 00:55:00 (系统时间实取)
脚本功能: 生成 GitHub social preview 图 (1280x640).
          深色底, 大标题 + 钩子数字 (+14.0 年 / OR 1.50) + 三层结构示意.
          只用 PIL 自带字体栈 (Arial/Segoe UI), 不引外部字体文件.
参数: 无 (写死输出 social-preview.png)
输入格式: 无
输出格式: social-preview.png (PNG, 1280x640)
依赖: Pillow
注意事项: 数字来自 README 已核验值, 不新造统计量
"""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("PILLOW-MISSING")
    sys.exit(2)

W, H = 1280, 640
BG = (16, 24, 32)
FG = (240, 244, 248)
ACCENT = (86, 196, 155)
DIM = (150, 162, 175)

FONT_STACK = [
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "C:/Windows/Fonts/segoeuib.ttf",
    "C:/Windows/Fonts/segoeui.ttf",
    "C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/msyh.ttc",
]


def load_font(size, bold=True):
    for p in FONT_STACK:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # 左上: 仓库名
    f_repo = load_font(30)
    d.text((60, 48), "lookski / lifespan-evidence", font=f_repo, fill=DIM)

    # 主标题 (中英)
    f_title = load_font(58)
    d.text((60, 110), "延长寿命的科学证据手册", font=f_title, fill=FG)
    f_sub = load_font(30)
    d.text((62, 182), "The Science of Living Longer - an Evidence Handbook",
           font=f_sub, fill=ACCENT)

    # 钩子数字块
    f_big = load_font(72)
    f_small = load_font(24)
    d.text((60, 268), "+14.0", font=f_big, fill=ACCENT)
    d.text((60, 350),
           "years (US women, 5 low-risk factors vs 0)",
           font=f_small, fill=DIM)
    d.text((420, 268), "OR 1.50", font=f_big, fill=ACCENT)
    d.text((420, 350),
           "survival, strong social ties (148 studies)",
           font=f_small, fill=DIM)
    d.text((860, 268), "54", font=f_big, fill=ACCENT)
    d.text((860, 350),
           "evidence items, every figure verified",
           font=f_small, fill=DIM)

    # 三层结构示意
    f_layer = load_font(26)
    y = 440
    d.rectangle([60, y, 700, y + 44], outline=(60, 76, 92), width=2)
    d.text((80, y + 8), "README.md  summary", font=f_layer, fill=FG)
    d.rectangle([60, y + 54, 700, y + 98], outline=(60, 76, 92), width=2)
    d.text((80, y + 62), "topics/  one page per dimension",
           font=f_layer, fill=FG)
    d.rectangle([60, y + 108, 700, y + 152], outline=(60, 76, 92), width=2)
    d.text((80, y + 116), "evidence/  per-item, 7-section template",
           font=f_layer, fill=FG)

    # 底部一行
    f_foot = load_font(22)
    d.text((60, 596),
           "Europe PMC API verified  |  bilingual (EN/CN)  |  CC BY 4.0",
           font=f_foot, fill=DIM)

    img.save("social-preview.png")
    print("saved social-preview.png")


if __name__ == "__main__":
    main()
