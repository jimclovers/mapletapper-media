#!/usr/bin/env python3
"""bsheet.py reelN out.jpg seg:t ... -> frames from the blurred segment files (segXb.mp4, else segX.mp4), 4 per row."""
import sys, os, cv2
from PIL import Image, ImageDraw, ImageFont
reel, out, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
tiles = []
for sp in specs:
    seg, t = sp.split(":"); t = float(t)
    p = f"{reel}/{seg}b.mp4" if os.path.exists(f"{reel}/{seg}b.mp4") else f"{reel}/{seg}.mp4"
    cap = cv2.VideoCapture(p); fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps))); ok, fr = cap.read()
    im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)).resize((500, 375)); d = ImageDraw.Draw(im)
    d.rectangle((370, 345, 500, 375), fill="black"); d.text((376, 349), f"{seg} {t:g}s", fill="white", font=f)
    tiles.append(im)
cols = 4
S = Image.new("RGB", (cols * 504, ((len(tiles) + cols - 1) // cols) * 379), "white")
for i, im in enumerate(tiles): S.paste(im, ((i % cols) * 504, (i // cols) * 379))
S.save(out, quality=85); print(out, S.size)
