"""Tree ID 02 - Red maple (5 slides). Photos: Jim's red maple tree and leaf images."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   dc_html, preview_html)
from post02 import pill, with_images  # noqa: E402
from tree01 import leaf_badge, clue, bar, fact  # noqa: E402
from funfacts import red_fun  # noqa: E402
from jugs import small_fact, sap_card  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"tree": "gemini/red_tree.jpg", "leaves": "gemini/red_leaves.jpg", "leaf": "gemini/red_leaf_crop.jpg"}
PHOTO_H = 860


def slide1():
    photo = (
        f'<img src="@@IMG_tree@@" alt="A red maple in scarlet fall color in a park" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-fit: cover; object-position: 50% 18%; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Tree ID · 2 of 9", C["cream"], C["maroon"])}{pill("17 weeks to sap season", C["gold"], C["maroon"])}</div>'
    )
    stamp = (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: {PHOTO_H - 64}px; z-index: 3; transform: rotate(-3deg); background: {C["gold"]}; '
        f'border: 6px solid {C["cream"]}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 16px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 72px; letter-spacing: -0.02em; line-height: 1; color: {C["maroon"]}">'
        f'TREE ID<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">no. 2</span></div>'
    )
    ai_tag = (
        f'<span data-chk="aitag" style="position: absolute; right: 56px; top: {PHOTO_H - 62}px; z-index: 3; background: rgba(255,245,222,0.88); '
        f'color: {C["maroon"]}; border-radius: 999px; padding: 7px 16px 5px; font-family: {TYPE}; font-size: 19px; letter-spacing: 0.05em; '
        f'text-transform: uppercase">AI illustration</span>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 104px 72px 60px; display: flex; flex-direction: column; gap: 18px; background: {C["maroon"]}">'
        + headline("Red maple", 132, C["cream"], chk="title")
        + body("Can you tap it? Swipe to find out.", 38, C["gold"], "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
        + "</div>"
    )
    return root(C["maroon"], photo + top + stamp + ai_tag + bottom, C["cream"]), "Tree ID: red maple"


def slide2():
    photo = (
        f'<div data-chk="photo" style="position: relative; border-radius: 30px; overflow: hidden; height: 430px; flex: none">'
        f'<img src="@@IMG_leaves@@" alt="Three red maple leaves on slate, turning from green to scarlet" '
        f'style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; display: block">'
        f'<span style="position: absolute; left: 22px; bottom: 20px; background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; '
        f'padding: 9px 18px 7px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.05em; text-transform: uppercase">Green to scarlet in fall · AI illustration</span></div>'
    )
    clues = (
        f'<div data-chk="clues" style="display: flex; flex-direction: column; gap: 30px; margin-top: 8px">'
        + clue(leaf_badge("#4E7A3A"), "Usually 3 lobes", "Sometimes 5, with toothed edges")
        + clue(leaf_badge("#7A1E1A"), "Dark red twigs", "Check the tips of the branches")
        + clue(leaf_badge("#D8352A"), "Scarlet in fall", "Sometimes orange or yellow")
        + "</div>"
    )
    inner = (
        kicker_row("How to spot it", "2 / 5", C["maroon"])
        + headline("Toothed leaves,<br>scarlet in fall", 92, C["maroon"])
        + photo
        + clues
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["cream"], column(inner, gap=30), C["maroon"]), "How to spot a red maple"


def slide3():
    cards = (
        f'<div data-chk="cards" style="display: flex; flex-direction: column; gap: 22px">'
        + sap_card("Red maple", "1.5–2%", 50, highlight=True, chk="card1")
        + sap_card("Sugar maple", "2–2.5%", 40, highlight=False, chk="card2")
        + "</div>"
    )
    inner = (
        kicker_row("Can you tap it?", "3 / 5", C["maroon"])
        + headline("Yes, with a few<br>trade-offs.", 88, C["maroon"])
        + cards
        + small_fact("leaf", "It buds out earlier than sugar maple, which can end its season sooner.")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], column(inner, gap=26), C["maroon"]), "Can you tap a red maple?"


def slide4():
    state = (
        f'<div data-chk="state" style="display: flex; align-items: center; gap: 36px">'
        f'<div style="position: relative; flex: none">'
        f'<img src="@@IMG_leaf@@" alt="A scarlet red maple leaf (AI illustration)" style="width: 330px; height: 330px; border-radius: 50%; object-fit: cover; '
        f'border: 10px solid {C["cream"]}; flex: none; display: block">'
        f'<span data-chk="aitag" style="position: absolute; left: 50%; bottom: -12px; transform: translateX(-50%); white-space: nowrap; '
        f'background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; padding: 7px 16px 5px; font-family: {TYPE}; font-size: 19px; '
        f'letter-spacing: 0.05em; text-transform: uppercase">AI illustration</span></div>'
        f'<div style="display: flex; flex-direction: column; gap: 14px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 60px; line-height: 1.02; color: {C["cream"]}">Rhode Island’s state tree</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 35px; line-height: 1.25; color: {C["gold"]}">Chosen in 1964. Red maple grows across most of the eastern U.S.</div></div></div>'
    )
    ground = (
        f'<div data-chk="ground" style="display: flex; flex-direction: column; gap: 10px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 62px; line-height: 1.04; color: {C["cream"]}">Wet ground or dry</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 38px; line-height: 1.25; color: {C["gold"]}">It grows from low, wet spots to higher ground. Got one? Tell us in the comments.</div></div>'
    )
    chip = lambda t: (f'<span style="border: 3px solid {C["gold"]}; color: {C["cream"]}; border-radius: 999px; padding: 10px 22px 9px; '
                      f'font-family: {DISPLAY}; font-weight: 700; font-size: 30px; line-height: 1">{t}</span>')
    glance = (
        f'<div data-chk="glance" style="display: flex; flex-direction: column; gap: 16px">'
        f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["gold"]}">Red maple at a glance</div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 14px">'
        + "".join(chip(t) for t in ["Usually 3 lobes", "Toothed edges", "Dark red twigs", "Scarlet in fall", "1.5–2% sugar"])
        + "</div></div>"
    )
    teaser = (
        f'<div data-chk="teaser" style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 32px; padding: 30px 36px; display: flex; '
        f'flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Next up</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.04; letter-spacing: -0.01em">Why tapping is the perfect family project</div></div>'
    )
    inner = (
        kicker_row("Good to know", "4 / 5", C["cream"])
        + state
        + '<div style="flex-grow: 1"></div>'
        + ground
        + '<div style="flex-grow: 1"></div>'
        + glance
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
    )
    return root(C["maroon"], column(inner, gap=50), C["cream"]), "Good to know: red maple"


def slide5():
    return red_fun()


SLIDES = [("Tree02-1-Cover", slide1), ("Tree02-2-Spot", slide2), ("Tree02-3-Tap", slide3), ("Tree02-4-Know", slide4), ("Tree02-5-Fun", slide5)]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_t2.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
