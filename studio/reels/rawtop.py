#!/usr/bin/env python3
"""rawtop.py reelN out.jpg H seg:t ... -> unblurred top strips (0..H px) with a 50-px grid, 2 per row."""
import sys, cv2
from PIL import Image, ImageDraw, ImageFont
reel, out, H, specs = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4:]
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
rows = []
for sp in specs:
    seg, t = sp.split(":"); t = float(t)
    cap = cv2.VideoCapture(f"{reel}/{seg}.mp4"); fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps))); ok, fr = cap.read()
    im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)).crop((0, 0, 1000, H)); d = ImageDraw.Draw(im)
    for x in range(50, 1000, 50):
        d.line([(x, 0), (x, H)], fill=(255, 255, 0) if x % 100 == 0 else (150, 150, 0), width=1)
        if x % 100 == 0: d.text((x + 2, H - 24), str(x), fill=(255, 255, 0), font=f)
    for y in range(50, H, 50):
        d.line([(0, y), (1000, y)], fill=(0, 255, 255), width=1); d.text((2, y + 2), str(y), fill=(0, 255, 255), font=f)
    d.rectangle((840, 0, 1000, 26), fill="black"); d.text((846, 2), f"{seg} {t:g}s", fill="white", font=f)
    rows.append(im)
S = Image.new("RGB", (2004, ((len(rows) + 1) // 2) * (H + 4)), "white")
for i, im in enumerate(rows): S.paste(im, ((i % 2) * 1004, (i // 2) * (H + 4)))
S.save(out, quality=88); print(out, S.size)
