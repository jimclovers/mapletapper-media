"""Tree ID 03 - Sugar maple, the syrup tree (5 slides). Photos: Jim's sugar maple tree and leaf images."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   dc_html, preview_html)
from post02 import pill, with_images  # noqa: E402
from tree01 import clue, bar, fact  # noqa: E402
from funfacts import sugar_fun  # noqa: E402
from jugs import sap_card, rule86_note  # noqa: E402
from art import SUGAR, leaf_path  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"tree": "jim/sugar_tree_real.jpg", "leaves": "jim/sugar_leaves_real.jpg", "leaf": "jim/sugar_leaf_real.jpg", "bark": "jim/sugar_bark_real.jpg"}
PHOTO_H = 860


def sugar_badge(fill, size=84):
    """Cream circle with a sugar maple leaf in the given color."""
    return (
        f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {C["cream"]}; display: flex; '
        f'align-items: center; justify-content: center; flex: none; box-shadow: inset 0 0 0 3px #EAD9B5">'
        f'<svg aria-hidden="true" width="{size - 12}" height="{size - 12}" viewBox="0 0 80 80">'
        f'<path d="{leaf_path(SUGAR, 25, 40, 48)}" fill="{fill}"></path>'
        f'<path d="M40 48 L40 66" fill="none" stroke="{fill}" style="stroke-width:3.5;stroke-linecap:round"></path></svg></div>'
    )


def slide1():
    photo = (
        f'<img src="@@IMG_tree@@" alt="A sugar maple in a park, red and orange on its sunny side and gold on its shaded side" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-fit: cover; object-position: 50% 50%; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Tree ID · 3 of 9", C["cream"], C["maroon"])}{pill("17 weeks to sap season", C["gold"], C["maroon"])}</div>'
    )
    stamp = (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: {PHOTO_H - 64}px; z-index: 3; transform: rotate(-3deg); background: {C["gold"]}; '
        f'border: 6px solid {C["cream"]}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 16px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 72px; letter-spacing: -0.02em; line-height: 1; color: {C["maroon"]}">'
        f'TREE ID<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">no. 3</span></div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 104px 72px 60px; display: flex; flex-direction: column; gap: 18px; background: {C["maroon"]}">'
        + headline("Sugar maple", 132, C["cream"], chk="title")
        + body("The syrup tree. Swipe to see why.", 38, C["gold"], "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
        + "</div>"
    )
    return root(C["maroon"], photo + top + stamp + bottom, C["cream"]), "Tree ID: sugar maple"


def slide2():
    photo = (
        f'<div data-chk="photo" style="position: relative; border-radius: 30px; overflow: hidden; height: 430px; flex: none">'
        f'<img src="@@IMG_leaves@@" alt="Red and orange sugar maple leaves, each with 5 lobes and rounded valleys between them" '
        f'style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; display: block">'
        f'<span style="position: absolute; left: 22px; bottom: 20px; background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; '
        f'padding: 9px 18px 7px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.05em; text-transform: uppercase">Real sugar maple leaves</span></div>'
    )
    clues = (
        f'<div data-chk="clues" style="display: flex; flex-direction: column; gap: 30px; margin-top: 8px">'
        + clue(sugar_badge("#4E7A3A"), "Smooth edges", "Red and silver maple leaves have toothed edges")
        + clue(sugar_badge("#2F5A2A"), "Dark green on top", "Lighter green underneath")
        + clue(sugar_badge("#E8622C"), "Vivid fall color", "Red, orange or yellow")
        + "</div>"
    )
    inner = (
        kicker_row("How to spot it", "2 / 5", C["maroon"])
        + headline("5 lobes with<br>U-shaped valleys", 92, C["maroon"])
        + photo
        + clues
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["cream"], column(inner, gap=30), C["maroon"]), "How to spot a sugar maple"


def slide3():
    cards = (
        f'<div data-chk="cards" style="display: flex; flex-direction: column; gap: 22px">'
        + sap_card("Sugar maple", "2–2.5%", 40, highlight=True, size=32, chk="card1")
        + sap_card("Silver maple", "About 1.5%", 57, highlight=False, size=32, chk="card2")
        + "</div>"
    )
    between = (
        f'<div data-chk="between" style="font-family: {DISPLAY}; font-weight: 700; font-size: 32px; line-height: 1.2; color: {C["maroon"]}">'
        f'Red maple lands in between: 1.5–2% sugar, about 50 gallons. These are typical averages; every tree is different.</div>'
    )
    inner = (
        kicker_row("Why it’s the best to tap", "3 / 5", C["maroon"])
        + headline("The sweetest sap<br>of any native maple.", 88, C["maroon"])
        + cards
        + between
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], column(inner, gap=26), C["maroon"]), "Why sugar maple is the best to tap"


def slide4():
    state = (
        f'<div data-chk="state" style="display: flex; align-items: center; gap: 36px">'
        f'<img src="@@IMG_leaf@@" alt="A red sugar maple leaf" style="width: 300px; height: 300px; border-radius: 50%; object-fit: cover; '
        f'border: 10px solid {C["cream"]}; flex: none; display: block">'
        f'<div style="display: flex; flex-direction: column; gap: 14px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 60px; line-height: 1.02; color: {C["cream"]}">State tree of 4 states</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 35px; line-height: 1.25; color: {C["gold"]}">New York, Vermont, West Virginia and Wisconsin.</div></div></div>'
    )
    bark = (
        f'<div data-chk="bark" style="display: flex; align-items: center; gap: 36px">'
        f'<div style="display: flex; flex-direction: column; gap: 14px; flex: 1 1 0">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 60px; line-height: 1.02; color: {C["cream"]}">Gray, furrowed bark</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 35px; line-height: 1.25; color: {C["gold"]}">On older trees, look for rough, deep furrows. Got one? Tell us in the comments.</div></div>'
        f'<img src="@@IMG_bark@@" alt="Close-up of a sugar maple trunk with rough, deeply furrowed gray bark" style="width: 300px; height: 300px; border-radius: 50%; object-fit: cover; '
        f'border: 10px solid {C["cream"]}; flex: none; display: block"></div>'
    )
    chip = lambda t: (f'<span style="border: 3px solid {C["gold"]}; color: {C["cream"]}; border-radius: 999px; padding: 10px 22px 9px; '
                      f'font-family: {DISPLAY}; font-weight: 700; font-size: 30px; line-height: 1">{t}</span>')
    glance = (
        f'<div data-chk="glance" style="display: flex; flex-direction: column; gap: 16px">'
        f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["gold"]}">Sugar maple at a glance</div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 14px">'
        + "".join(chip(t) for t in ["5 lobes", "U-shaped valleys", "Vivid fall color", "Furrowed gray bark", "2–2.5% sugar"])
        + "</div></div>"
    )
    teaser = (
        f'<div data-chk="teaser" style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 32px; padding: 30px 36px; display: flex; '
        f'flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Next up</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.04; letter-spacing: -0.01em">Kids Corner: how big is a taphole?</div></div>'
    )
    inner = (
        kicker_row("Good to know", "4 / 5", C["cream"])
        + state
        + '<div style="flex-grow: 1"></div>'
        + bark
        + '<div style="flex-grow: 1"></div>'
        + glance
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
    )
    return root(C["maroon"], column(inner, gap=50), C["cream"]), "Good to know: sugar maple"


def slide5():
    return sugar_fun()


SLIDES = [("Tree03-1-Cover", slide1), ("Tree03-2-Spot", slide2), ("Tree03-3-Best", slide3), ("Tree03-4-Know", slide4), ("Tree03-5-Fun", slide5)]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_t3.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
