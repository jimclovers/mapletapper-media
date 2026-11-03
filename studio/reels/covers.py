#!/usr/bin/env python3
"""Reel cover images (1080x1920). Everything that matters sits inside the 3:4 grid crop (y 240-1680).
Houses in the photos are softened with the same blur the Reels use; saved files carry no metadata."""
import base64
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
from build_reel import page, chip, C, DISPLAY, TYPE, GOLD, W, H  # noqa: E402
from blur import apply as blur_apply  # noqa: E402

OUT = Path("/home/claude/mt/deliver")
TMP = Path("/home/claude/mt/reels/covers")
U = "/mnt/user-data/uploads/"


def frame(src, t, out):
    import subprocess
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", str(out)], check=True)
    return out


R = Path("/home/claude/mt/reels")


def seg_frame(path, t, out):
    """A frame from a pre-rendered (already blurred) Reel segment, so the cover matches the video."""
    import subprocess
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(path), "-frames:v", "1", str(out)], check=True)
    return out


def prep(src, out, crop=None, blur=()):
    """Crop to 4:3, size to 1000x750, soften the given boxes (window coordinates), save without EXIF."""
    im = Image.open(src).convert("RGB")
    if crop:
        im = im.crop(crop)
    im = im.resize((1000, 750), Image.LANCZOS)
    if blur:
        bgr = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
        im = Image.fromarray(cv2.cvtColor(blur_apply(bgr, list(blur)), cv2.COLOR_BGR2RGB))
    im.save(out, quality=92)
    return out


COVERS = [
    dict(name="MapleTapper-Reel-PerfectTappingSpot-cover.png", kicker="Reel · Scouting trees",
         title=f"The perfect<br>tapping {GOLD('spot.')}",
         img=prep(seg_frame(R / "reel1/seg2b.mp4", 7.7, TMP / "c1_seg.png"), TMP / "img1.jpg"),
         foot="Jim's field video"),
    dict(name="MapleTapper-Reel-SugarMapleOrNot-cover.png", kicker="Reel · Tree ID",
         title=f"Sugar maple<br>or {GOLD('not?')}",
         img=prep(U + "378100a0-image.jpg", TMP / "img2.jpg", blur=[(785, 400, 1000, 600)]),
         foot="Jim's field video"),
    dict(name="MapleTapper-Reel-LeafDetective-cover.png", kicker="Reel · Family fun",
         title=f"Before you bag<br>the {GOLD('leaves…')}",
         img=prep(seg_frame(R / "reel3/seg1b.mp4", 2.9, TMP / "c3_seg.png"), TMP / "img3.jpg"),
         foot="Play leaf detective 🔍"),
    dict(name="MapleTapper-Reel-WhyHalfRed-cover.png", kicker="Reel · Tree ID",
         title=f"Why is half<br>this maple {GOLD('red?')}",
         img=prep(frame(U + "IMG_2264.mov", 2.5, TMP / "c_2264_2.5.png"), TMP / "img4.jpg", (240, 0, 1680, 1080)),
         foot="Watch where the sun hits"),
]


def cover_html(c):
    img = "data:image/jpeg;base64," + base64.b64encode(open(c["img"], "rb").read()).decode()
    body = (
        f'<div style="position: absolute; inset: 0; background: {C["maroon"]}"></div>'
        f'<div style="position: absolute; left: 72px; right: 72px; top: 268px; display: flex; justify-content: space-between; '
        f'align-items: center">{chip(c["kicker"])}<span style="font-family: {TYPE}; font-size: 28px; color: {C["cream"]}">'
        f'@mapletapper</span></div>'
        f'<div data-chk="1" style="position: absolute; left: 72px; top: 340px; font-family: {DISPLAY}; font-weight: 800; '
        f'font-size: 132px; line-height: 0.93; letter-spacing: -0.03em; color: {C["cream"]}">{c["title"]}</div>'
        f'<img src="{img}" style="position: absolute; left: 40px; top: 640px; width: 1000px; height: 750px; '
        f'border-radius: 36px; object-fit: cover">'
        f'<div style="position: absolute; left: 72px; top: 1430px; display: flex; align-items: center; gap: 18px">'
        f'<div style="width: 76px; height: 76px; border-radius: 999px; background: {C["gold"]}; display: flex; align-items: center; '
        f'justify-content: center"><div style="width: 0; height: 0; border-left: 28px solid {C["maroon"]}; border-top: 17px solid '
        f'transparent; border-bottom: 17px solid transparent; margin-left: 8px"></div></div>'
        f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 40px; color: {C["cream"]}">{c["foot"]}</span></div>'
    )
    return page(body, W, H)


with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport=dict(width=W, height=H))
    for c in COVERS:
        pg.set_content(cover_html(c))
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(200)
        pg.screenshot(path=str(OUT / c["name"]))
        print("wrote", c["name"])
    br.close()

# grid preview (3:4 center crop) for checking
prev = Image.new("RGB", (len(COVERS) * 540 + (len(COVERS) - 1) * 20, 720), "white")
for i, c in enumerate(COVERS):
    im = Image.open(OUT / c["name"]).crop((0, 240, 1080, 1680)).resize((540, 720))
    prev.paste(im, (i * 560, 0))
prev.save(TMP / "grid_preview.jpg", quality=85)
