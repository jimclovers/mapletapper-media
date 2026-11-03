#!/usr/bin/env python3
"""clipsheet.py out.jpg cols tile_w CLIP:start:end:step [...] -> labeled contact sheet of source-clip frames."""
import sys, subprocess, io
from PIL import Image, ImageDraw, ImageFont
out, cols, tw = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
tiles = []
for spec in sys.argv[4:]:
    path, a, b, st = spec.rsplit(":", 3); a, b, st = float(a), float(b), float(st)
    name = path.split("/")[-1].split("-")[-1].replace(".mov", "")
    t = a
    while t <= b + 1e-6:
        png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                             capture_output=True).stdout
        im = Image.open(io.BytesIO(png)).convert("RGB"); im = im.resize((tw, int(tw * im.height / im.width)))
        d = ImageDraw.Draw(im); lab = f"{name[-4:]} {t:.2f}"
        d.rectangle((0, 0, 10 * len(lab) + 10, 22), fill="black"); d.text((4, 1), lab, fill="yellow", font=f)
        tiles.append(im); t += st
th = tiles[0].height
S = Image.new("RGB", (cols * (tw + 4), ((len(tiles) + cols - 1) // cols) * (th + 4)), "white")
for i, im in enumerate(tiles): S.paste(im, ((i % cols) * (tw + 4), (i // cols) * (th + 4)))
S.save(out, quality=82); print(out, S.size, len(tiles))
