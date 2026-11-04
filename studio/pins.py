"""Tall Pinterest pins (1000x1500) for the MapleTapper series.

Usage: python3 pins.py   -> writes pins/preview/<name>.html, then render with render_pin.js
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from art import C  # noqa: E402
from build import DISPLAY, TYPE, ROOT, font_faces_local, leaf_mark  # noqa: E402

PW, PH, PHOTO_H = 1000, 1500, 960
OUT = os.path.join(ROOT, "pins", "preview")

# name, photo, object-position, kicker, title, sub
PINS = [
    ("pin01-find-maples", "p6/p6_03_995da72e.jpg", "50% 40%", "Backyard maple syrup",
     "How to Find Maple Trees to Tap", "Mark them now, while the leaves are still on"),
    ("pin02-silver-maple", "gemini/silver_tree.jpg", "50% 30%", "Maple tree ID",
     "How to Identify a Silver Maple", "Leaf clues, and can you tap it for syrup?"),
    ("pin03-tapping-myth", "post02-cover.jpg", "40% 50%", "Myth or fact",
     "Does Tapping Hurt a Maple Tree?", "4 tree-friendly tapping rules"),
    ("pin04-red-maple", "gemini/red_tree.jpg", "50% 30%", "Maple tree ID",
     "How to Identify a Red Maple", "Leaf clues, and can you tap it for syrup?"),
    ("pin05-family-project", "book/p3_sap_drip.jpg", "50% 50%", "Family fun",
     "Maple Tapping with Kids", "Why it's the perfect family project"),
    ("pin06-sugar-maple", "jim/sugar_tree_real.jpg", "55% 50%", "Maple tree ID",
     "How to Identify a Sugar Maple", "The sweetest tree for maple syrup"),
    ("pin07-taphole-size", "book/p4_drill.jpg", "30% 50%", "Kids corner",
     "How Big Is a Taphole?", "Kitchen-table maple science for kids"),
]


def pin(photo, pos, kicker, title, sub):
    src = "file://" + os.path.join(ROOT, "photos", photo)
    return (
        f'<div data-root style="position: relative; width: {PW}px; height: {PH}px; overflow: hidden; background: {C["maroon"]}; '
        f'font-family: {DISPLAY}; color: {C["cream"]}">'
        f'<img src="{src}" alt="" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PHOTO_H}px; '
        f'object-fit: cover; object-position: {pos}; display: block">'
        f'<span data-chk="kicker" style="position: absolute; left: 48px; top: 48px; background: {C["cream"]}; color: {C["maroon"]}; '
        f'border-radius: 999px; padding: 12px 26px 10px; font-family: {TYPE}; font-size: 30px; letter-spacing: 0.06em; '
        f'text-transform: uppercase">{kicker}</span>'
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {PW}px; height: {PH - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 58px 64px 50px; display: flex; flex-direction: column; gap: 22px">'
        f'<h1 data-chk="title" style="margin: 0; font-weight: 800; font-size: 96px; line-height: 0.95; letter-spacing: -0.025em; text-wrap: balance">{title}</h1>'
        f'<p data-chk="sub" style="margin: 0; font-weight: 700; font-size: 42px; line-height: 1.2; text-wrap: balance; color: {C["gold"]}">{sub}</p>'
        f'<div style="flex-grow: 1"></div>'
        f'<div data-chk="footer" style="display: flex; align-items: center; gap: 14px; font-family: {TYPE}; font-size: 34px; '
        f'letter-spacing: 0.04em">{leaf_mark(C["gold"], 40)}mapletapper.com</div>'
        f'</div></div>'
    )


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, photo, pos, kicker, title, sub in PINS:
        html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
                f'<style>{font_faces_local()} body{{margin:0}}</style></head><body>{pin(photo, pos, kicker, title, sub)}</body></html>')
        open(os.path.join(OUT, name + ".html"), "w").write(html)
    print("built", len(PINS))
