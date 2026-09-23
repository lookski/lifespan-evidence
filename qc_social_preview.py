# -*- coding: utf-8 -*-
"""
编写时间: 2026-09-24 00:58:30 (系统时间实取)
脚本功能: 程序化 QC social-preview.png: 检查四个区域是否有非背景墨迹 (文字/框线已画上).
参数: 无
输入格式: social-preview.png
输出格式: 控制台各区域墨迹像素计数
依赖: Pillow
注意事项: 只读; 本会话模型无视觉通道, 用像素计数代替目检
"""
from PIL import Image

BG = (16, 24, 32)


def region_has_ink(px, x0, y0, x1, y1):
    cnt = 0
    for x in range(x0, x1, 4):
        for y in range(y0, y1, 4):
            p = px[x, y]
            if abs(p[0] - BG[0]) + abs(p[1] - BG[1]) + abs(p[2] - BG[2]) > 60:
                cnt += 1
    return cnt


def main():
    im = Image.open("social-preview.png")
    px = im.load()
    checks = [
        ("title", 60, 110, 900, 175),
        ("hook numbers", 60, 268, 1100, 380),
        ("three layers", 60, 440, 700, 590),
        ("footer", 60, 590, 800, 625),
    ]
    ok = True
    for name, a, b, c, dd in checks:
        n = region_has_ink(px, a, b, c, dd)
        status = "OK" if n > 10 else "EMPTY"
        if n <= 10:
            ok = False
        print(name, "ink:", n, status)
    print("QC:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
