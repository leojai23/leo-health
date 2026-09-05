# -*- coding: utf-8 -*-
"""Generate icon-192.png / icon-512.png for Leo-Health (clean leaf mark)."""
import os
import sys
import math
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "dist")

BG = (79, 123, 176)      # --accent blue
LEAF = (247, 245, 240)   # cream
VEIN = (79, 123, 176)


def leaf_polygon(cx, cy, length, width, angle_deg):
    """Parametric leaf: pointed at both ends, widest in the middle."""
    pts_top, pts_bot = [], []
    n = 120
    a = math.radians(angle_deg)
    ca, sa = math.cos(a), math.sin(a)
    for i in range(n + 1):
        t = i / n                       # 0..1 along the leaf
        x = (t - 0.5) * length
        # width profile: 0 at ends, fat middle, slight skew towards the base
        w = width * (math.sin(math.pi * t) ** 0.85) * (0.72 + 0.28 * (1 - t))
        for sign, bucket in ((1, pts_top), (-1, pts_bot)):
            px, py = x, sign * w / 2
            pts_top_x = cx + px * ca - py * sa
            pts_top_y = cy + px * sa + py * ca
            bucket.append((pts_top_x, pts_top_y))
    return pts_top + list(reversed(pts_bot))


def make(size):
    ss = 4  # supersample
    S = size * ss
    img = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(img)
    cx = cy = S / 2
    ang = -32

    d.polygon(leaf_polygon(cx, cy, S * 0.82, S * 0.40, ang), fill=LEAF)

    # midrib
    a = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)
    half = S * 0.36

    def rot(px, py):
        return (cx + px * ca - py * sa, cy + px * sa + py * ca)

    d.line([rot(-half, 0), rot(half, 0)], fill=VEIN, width=max(2, S // 110))
    # side veins
    for t in (0.32, 0.5, 0.68):
        x = (t - 0.5) * S * 0.82
        w = S * 0.40 * (math.sin(math.pi * t) ** 0.85) * (0.72 + 0.28 * (1 - t)) * 0.5
        lw = max(1, S // 200)
        d.line([rot(x, 0), rot(x + S * 0.06, w)], fill=VEIN, width=lw)
        d.line([rot(x, 0), rot(x + S * 0.06, -w)], fill=VEIN, width=lw)

    return img.resize((size, size), Image.LANCZOS)


for s in (192, 512):
    make(s).save(os.path.join(OUT, "icon-%d.png" % s))
    print("wrote icon-%d.png" % s)
