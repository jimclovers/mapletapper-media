"""Tall pins for Nov 11-17 (pin08-pin13). Same style as pins.py; pin12 uses the post 10 illustration."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from art import C  # noqa: E402
from build import DISPLAY, TYPE, ROOT, font_faces_local, leaf_mark  # noqa: E402
from pins import PW, PH, PHOTO_H, OUT  # noqa: E402
import post10  # noqa: E402

PINS = [
    ("pin08-too-warm", "p6/p6_05_25960ccb.jpg", "50% 45%", "Myth or fact",
     "Is It Getting Too Warm for Sugar Maples?", "What the research says about maple syrup and climate"),
    ("pin09-measure-tree", "/home/claude/mt/jimphotos/trunk.jpg", "50% 60%", "Kids corner",
     "Is Your Tree Big Enough to Tap?", "Measure it with a string, a ruler and a little math"),
    ("pin10-real-syrup", "book/p1_pancakes.jpg", "50% 40%", "Label check",
     "Real Maple Syrup vs. Pancake Syrup", "Read the label: what to look for"),
    ("pin11-scavenger-hunt", "p6/p6_12_2e190651.jpg", "50% 40%", "Family fun",
     "Maple Tree Scavenger Hunt for Kids", "An easy outdoor game for fall weekends"),
    ("pin12-baking-swap", None, "", "Baking swap",
     "How to Bake with Maple Syrup Instead of Sugar", "Use ¾ cup syrup for every 1 cup of sugar"),
    ("pin13-which-trees", "/home/claude/mt/jim2/p07_d43e50b6.jpg", "50% 45%", "Tree check",
     "Which Maple Trees Should You Not Tap?", "Storm damage, rot and the red flags to check"),
]


def top_area(photo, pos):
    if photo is None:
        return (f'<div style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PHOTO_H}px; background: {C["gold"]}; display: flex; '
                f'align-items: center; justify-content: center"><div style="transform: scale(0.95); margin-top: 40px">{post10.cover_art()}</div></div>')
    src = "file://" + (photo if photo.startswith("/") else os.path.join(ROOT, "photos", photo))
    return (f'<img src="{src}" alt="" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PHOTO_H}px; '
            f'object-fit: cover; object-position: {pos}; display: block">')


def pin(photo, pos, kicker, title, sub):
    return (
        f'<div data-root style="position: relative; width: {PW}px; height: {PH}px; overflow: hidden; background: {C["maroon"]}; '
        f'font-family: {DISPLAY}; color: {C["cream"]}">'
        + top_area(photo, pos)
        + f'<span data-chk="kicker" style="position: absolute; left: 48px; top: 48px; background: {C["cream"]}; color: {C["maroon"]}; '
        f'border-radius: 999px; padding: 12px 26px 10px; font-family: {TYPE}; font-size: 30px; letter-spacing: 0.06em; '
        f'text-transform: uppercase">{kicker}</span>'
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {PW}px; height: {PH - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 58px 64px 50px; display: flex; flex-direction: column; gap: 22px">'
        f'<h1 data-chk="title" style="margin: 0; font-weight: 800; font-size: 92px; line-height: 0.95; letter-spacing: -0.025em; text-wrap: balance">{title}</h1>'
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
