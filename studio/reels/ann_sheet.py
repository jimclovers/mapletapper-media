#!/usr/bin/env python3
"""ann_sheet.py reelN out.jpg seg:t seg:t ... -> frames with every box anchored at that time, numbered by its index."""
import json, sys, cv2
from PIL import Image, ImageDraw, ImageFont
reel, out, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
ann = json.load(open(f"blur/{reel}_all.json"))
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
tiles = []
for sp in specs:
    seg, t = sp.split(":"); t = float(t)
    cap = cv2.VideoCapture(f"{reel}/{seg}.mp4"); fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps))); ok, fr = cap.read()
    im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)); d = ImageDraw.Draw(im)
    for i, a in enumerate(ann.get(seg, [])):
        if a.get("t") == t and "box" in a:
            b = a["box"]; d.rectangle(b, outline=(255, 0, 255), width=5)
            d.text((b[0] + 6, b[1] + 2), str(i), fill=(255, 255, 0), font=f, stroke_width=3, stroke_fill="black")
    d.rectangle((760, 700, 1000, 750), fill="black"); d.text((770, 708), f"{seg} {t:g}s", fill="white", font=f)
    tiles.append(im.resize((500, 375)))
cols = 4
S = Image.new("RGB", (cols * 504, ((len(tiles) + cols - 1) // cols) * 379), "white")
for i, im in enumerate(tiles): S.paste(im, ((i % cols) * 504, (i // cols) * 379))
S.save(out, quality=85); print(out, S.size)
