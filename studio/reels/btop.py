#!/usr/bin/env python3
"""btop.py reelN out.jpg H seg:t ... -> top strips (0..H px) of the BLURRED segment files, 2 per row, x labels."""
import sys, os, cv2
from PIL import Image, ImageDraw, ImageFont
reel, out, H, specs = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4:]
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
rows = []
for sp in specs:
    seg, t = sp.split(":"); t = float(t)
    cap = cv2.VideoCapture(f"{reel}/{seg}b.mp4"); fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps))); ok, fr = cap.read()
    im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)).crop((0, 0, 1000, H)); d = ImageDraw.Draw(im)
    for x in range(100, 1000, 100):
        d.text((x + 2, H - 24), str(x), fill=(255, 255, 0), font=f, stroke_width=2, stroke_fill="black")
    d.rectangle((840, 0, 1000, 26), fill="black"); d.text((846, 2), f"{seg} {t:g}s", fill="white", font=f)
    rows.append(im)
S = Image.new("RGB", (2004, ((len(rows) + 1) // 2) * (H + 4)), "white")
for i, im in enumerate(rows): S.paste(im, ((i % 2) * 1004, (i // 2) * (H + 4)))
S.save(out, quality=88); print(out, S.size)
