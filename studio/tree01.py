"""Tree ID 01 - Silver maple (5 slides). Photos: Jim's tree and leaf images + the book's silver maple seed scan."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   icon_badge, dc_html, preview_html)
from post02 import pill, with_images  # noqa: E402
from art import SOFT, leaf_path  # noqa: E402
from funfacts import silver_fun  # noqa: E402
from jugs import small_fact, sap_card, rule86_note  # noqa: E402


def leaf_badge(fill, size=84, stroke=None):
    """Cream circle with a pointy (silver maple) leaf in the given color."""
    edge = f' stroke="{stroke}" style="stroke-width:2.5"' if stroke else ""
    return (
        f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {C["cream"]}; display: flex; '
        f'align-items: center; justify-content: center; flex: none; box-shadow: inset 0 0 0 3px #EAD9B5">'
        f'<svg aria-hidden="true" width="{size - 12}" height="{size - 12}" viewBox="0 0 80 80">'
        f'<path d="{leaf_path(SOFT, 24, 40, 48, serrate=1)}" fill="{fill}"{edge}></path>'
        f'<path d="M40 48 L40 66" fill="none" stroke="{stroke or fill}" style="stroke-width:3.5;stroke-linecap:round"></path></svg></div>'
    )

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"tree": "gemini/silver_tree.jpg", "leaves": "gemini/silver_leaves.jpg", "seed": "book/t1_silver_seed.jpg"}
PHOTO_H = 860


def slide1():
    photo = (
        f'<img src="@@IMG_tree@@" alt="A silver maple in golden fall color in a park" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-fit: cover; object-position: 50% 38%; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Tree ID · 1 of 9", C["cream"], C["maroon"])}{pill("17 weeks to sap season", C["gold"], C["maroon"])}</div>'
    )
    stamp = (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: {PHOTO_H - 64}px; z-index: 3; transform: rotate(-3deg); background: {C["gold"]}; '
        f'border: 6px solid {C["cream"]}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 16px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 72px; letter-spacing: -0.02em; line-height: 1; color: {C["maroon"]}">'
        f'TREE ID<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">no. 1</span></div>'
    )
    ai_tag = (
        f'<span data-chk="aitag" style="position: absolute; right: 56px; top: {PHOTO_H - 62}px; z-index: 3; background: rgba(255,245,222,0.88); '
        f'color: {C["maroon"]}; border-radius: 999px; padding: 7px 16px 5px; font-family: {TYPE}; font-size: 19px; letter-spacing: 0.05em; '
        f'text-transform: uppercase">AI illustration</span>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 104px 72px 60px; display: flex; flex-direction: column; gap: 18px; background: {C["maroon"]}">'
        + headline("Silver maple", 132, C["cream"], chk="title")
        + body("Can you tap it? Swipe to find out.", 38, C["gold"], "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
        + "</div>"
    )
    return root(C["maroon"], photo + top + stamp + ai_tag + bottom, C["cream"]), "Tree ID: silver maple"


def clue(badge, main, note):
    return (
        f'<div style="display: flex; gap: 26px; align-items: center">{badge}'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 40px; line-height: 1.12; color: {C["maroon"]}">{main}'
        f'<div style="font-weight: 500; font-size: 31px; line-height: 1.25; margin-top: 4px">{note}</div></div></div>'
    )


def slide2():
    photo = (
        f'<div data-chk="photo" style="position: relative; border-radius: 30px; overflow: hidden; height: 400px; flex: none">'
        f'<img src="@@IMG_leaves@@" alt="Three silver maple leaves on a wooden bench, turning from green to yellow" '
        f'style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 52%; display: block">'
        f'<span style="position: absolute; left: 22px; bottom: 20px; background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; '
        f'padding: 9px 18px 7px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.05em; text-transform: uppercase">Green to gold in fall · AI illustration</span></div>'
    )
    clues = (
        f'<div data-chk="clues" style="display: flex; flex-direction: column; gap: 30px; margin-top: 8px">'
        + clue(leaf_badge("#4E7A3A"), "Much pointier leaves", "5 deep-cut lobes with toothed edges")
        + clue(leaf_badge("#D7DCDD", stroke="#8F9A9C"), "Silvery-white underneath", "Flip a leaf over to check")
        + clue(leaf_badge("#F2B92B"), "Fall color tends to yellow", "Sugar maples go red, orange or yellow")
        + "</div>"
    )
    inner = (
        kicker_row("How to spot it", "2 / 5", C["maroon"])
        + headline("Pointy leaves,<br>silver underneath", 92, C["maroon"])
        + photo
        + clues
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["cream"], column(inner, gap=30), C["maroon"]), "How to spot a silver maple"


def bar(label, solid_pct, top_pct, text, col):
    full = 3.0
    track = 560
    solid = track * solid_pct / full
    span = track * (top_pct - solid_pct) / full
    return (
        f'<div style="display: flex; flex-direction: column; gap: 12px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 38px; color: {C["maroon"]}">{label}</div>'
        f'<div style="display: flex; align-items: center; gap: 22px">'
        f'<div style="display: flex; width: {track}px; height: 46px; border-radius: 12px; background: #F3E3BF; overflow: hidden; flex: none">'
        f'<div style="width: {solid:.0f}px; background: {col}"></div>'
        f'<div style="width: {span:.0f}px; background: {col}; opacity: 0.45"></div></div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 42px; color: {col}; white-space: nowrap">{text}</div></div></div>'
    )


def fact(kind, html):
    return (
        f'<div style="display: flex; gap: 26px; align-items: center">{icon_badge(kind, 92)}'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 42px; line-height: 1.16; color: {C["maroon"]}">{html}</div></div>'
    )


def slide3():
    cards = (
        f'<div data-chk="cards" style="display: flex; flex-direction: column; gap: 22px">'
        + sap_card("Silver maple", "About 1.5%", 57, highlight=True, size=34, chk="card1")
        + sap_card("Sugar maple", "2–2.5%", 40, highlight=False, size=34, chk="card2")
        + "</div>"
    )
    inner = (
        kicker_row("Can you tap it?", "3 / 5", C["maroon"])
        + headline("Yes, but it takes<br>more sap.", 88, C["maroon"])
        + cards
        + small_fact("leaf", "It’s also one of the first trees to bud out in spring, which can cut its season short.")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], column(inner, gap=26), C["maroon"]), "Can you tap a silver maple?"


def slide4():
    seed = (
        f'<div data-chk="seed" style="display: flex; align-items: center; gap: 34px">'
        f'<div style="width: 480px; height: 428px; border-radius: 30px; background: #FFFFFF; flex: none; overflow: hidden; display: flex; align-items: center; justify-content: center">'
        f'<img src="@@IMG_seed@@" alt="A silver maple seed with two big, papery wings" style="width: 456px; height: 406px; object-fit: contain; display: block"></div>'
        f'<div style="display: flex; flex-direction: column; gap: 14px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 60px; line-height: 1.02; color: {C["cream"]}">The biggest “helicopters”</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 35px; line-height: 1.25; color: {C["gold"]}">No native maple grows bigger seeds, and they can sprout right away, with no winter wait.</div></div></div>'
    )
    wet = (
        f'<div data-chk="wet" style="display: flex; flex-direction: column; gap: 10px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 62px; line-height: 1.04; color: {C["cream"]}">Look in low, wet spots</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 38px; line-height: 1.25; color: {C["gold"]}">Silver maple likes wet ground. Got one? Tell us in the comments.</div></div>'
    )
    chip = lambda t: (f'<span style="border: 3px solid {C["gold"]}; color: {C["cream"]}; border-radius: 999px; padding: 10px 22px 9px; '
                      f'font-family: {DISPLAY}; font-weight: 700; font-size: 30px; line-height: 1">{t}</span>')
    glance = (
        f'<div data-chk="glance" style="display: flex; flex-direction: column; gap: 16px">'
        f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["gold"]}">Silver maple at a glance</div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 14px">'
        + "".join(chip(t) for t in ["Pointy, toothed leaves", "Silvery underside", "Yellow in fall", "Biggest helicopters", "About 1.5% sugar"])
        + "</div></div>"
    )
    teaser = (
        f'<div data-chk="teaser" style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 32px; padding: 30px 36px; display: flex; '
        f'flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Next up</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.04; letter-spacing: -0.01em">Myth or fact: does tapping hurt the tree?</div></div>'
    )
    inner = (
        kicker_row("Two more clues", "4 / 5", C["cream"])
        + seed
        + '<div style="flex-grow: 1"></div>'
        + wet
        + '<div style="flex-grow: 1"></div>'
        + glance
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
    )
    return root(C["maroon"], column(inner, gap=50), C["cream"]), "Two more clues"


def slide5():
    return silver_fun()


SLIDES = [("Tree01-1-Cover", slide1), ("Tree01-2-Spot", slide2), ("Tree01-3-Tap", slide3), ("Tree01-4-Clues", slide4), ("Tree01-5-Fun", slide5)]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_t1.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
