#!/usr/bin/env python3
"""frames.py reelN out.jpg seg:t seg:t ... -> 2x2 (or 2xN) full-res frames with a labeled 50-px grid."""
import sys, cv2
from PIL import Image, ImageDraw, ImageFont
reel, outp, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
tiles = []
for sp in specs:
    seg, t = sp.split(":"); t = float(t)
    cap = cv2.VideoCapture(f"/home/claude/mt/reels/{reel}/{seg}.mp4"); fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * fps)); ok, fr = cap.read()
    im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)); d = ImageDraw.Draw(im)
    for x in range(50, 1000, 50):
        d.line([(x, 0), (x, 750)], fill=(255, 255, 0) if x % 100 == 0 else (120, 120, 0), width=1)
        if x % 100 == 0: d.text((x + 2, 2), str(x), fill=(255, 255, 0), font=f)
    for y in range(50, 750, 50):
        d.line([(0, y), (1000, y)], fill=(0, 255, 255) if y % 100 == 0 else (0, 120, 120), width=1)
        if y % 100 == 0: d.text((2, y + 2), str(y), fill=(0, 255, 255), font=f)
    d.rectangle((820, 710, 1000, 750), fill="black"); d.text((828, 716), f"{seg} {t:.1f}s", fill="white", font=f)
    tiles.append(im)
import os
cols = int(os.environ.get('COLS', '2'))
S = Image.new("RGB", (cols * 1004, ((len(tiles) + cols - 1) // cols) * 754), "white")
for i, im in enumerate(tiles): S.paste(im, ((i % cols) * 1004, (i // cols) * 754))
S.save(outp, quality=82)
