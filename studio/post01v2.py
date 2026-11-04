"""Post 01 v2 - Find your syrup trees this fall, rebuilt with real photos from the MapleTapper books."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, arrow_svg, leaf_mark, kicker_row, footer_row, swipe, headline, body,
                   root, column, dc_html, preview_html, check_badge, icon_badge)  # noqa: E402
from post02 import pill  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos", "book")
ASSETS = {
    "jar": "p1_cover_jar.jpg", "leafhard": "p1_leaf_hard.jpg", "leafsoft": "p1_leaf_soft.jpg",
    "barkhard": "p1_bark_hard.jpg", "barksoft": "p1_bark_soft.jpg", "seed": "p1_seed.jpg",
    "trunk": "p1_trunk_ruler.jpg", "pancakes": "p1_pancakes.jpg",
}


def img(key, alt, style):
    return f'<img src="@@IMG_{key}@@" alt="{alt}" style="display: block; {style}">'


def slide1():
    photo = img("jar", "A jar of golden maple syrup resting in the fork of a maple tree",
                f"position: absolute; left: 0; top: 0; width: {W}px; height: 720px; object-fit: cover; object-position: 50% 45%")
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Sugarmaker’s Almanac · No. 01", C["cream"], C["maroon"])}{pill("17 weeks to sap season", C["gold"], C["maroon"])}</div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: 720px; width: {W}px; height: {H - 720}px; box-sizing: border-box; '
        f'padding: 54px 72px 56px; display: flex; flex-direction: column; gap: 22px; background: {C["sky"]}">'
        + headline(f'Find your <span style="color: {C["red"]}">syrup<br>trees</span> this fall.', 124, C["maroon"], chk="headline")
        + body("While the leaves are still on, maples are easy to spot. Here’s how to find (and mark) yours.", 38, C["maroon"], "sub", "; font-weight: 600")
        + '<div style="flex-grow: 1"></div>'
        + f'<div data-chk="pill" style="align-self: flex-start; display: flex; align-items: center; gap: 14px; background: {C["maroon"]}; '
        f'color: {C["cream"]}; border-radius: 999px; padding: 18px 30px 18px 34px; font-family: {DISPLAY}; font-weight: 700; font-size: 32px">'
        f'Swipe for 3 easy clues{arrow_svg(C["cream"], 32)}</div>'
        + "</div>"
    )
    return root(C["sky"], photo + top + bottom, C["maroon"]), "Find your syrup trees this fall"


def leaf_card(key, tag, alt, points):
    items = "".join(
        f'<div style="display: flex; gap: 12px; align-items: baseline"><span style="flex: none; width: 12px; height: 12px; border-radius: 50%; '
        f'background: {C["red"]}; transform: translateY(-3px)"></span><span>{p}</span></div>' for p in points
    )
    return (
        f'<div data-chk="card-{key}" style="flex: 1 1 0; min-width: 0; background: {C["sky"]}; border-radius: 36px; padding: 18px 18px 26px; '
        f'display: flex; flex-direction: column; gap: 16px">'
        + img(key, alt, "width: 100%; height: 470px; object-fit: cover; object-position: 50% 0%; border-radius: 24px")
        + f'<div style="align-self: flex-start; margin-left: 8px; font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase; '
        f'color: {C["cream"]}; background: {C["maroon"]}; border-radius: 10px; padding: 7px 14px 5px">{tag}</div>'
        + f'<div style="margin: 0 10px; display: flex; flex-direction: column; gap: 8px; font-family: {DISPLAY}; font-weight: 700; font-size: 30px; '
        f'line-height: 1.15; color: {C["maroon"]}">{items}</div></div>'
    )


def slide2():
    inner = (
        kicker_row("Clue 1 · The leaf", "2 / 5", C["maroon"])
        + headline("Check the leaf", 120, C["maroon"])
        + body("Sugar maples usually have 5 lobes, with rounded, U-shaped valleys between them.", 38, C["maroon"], "sub", "; font-weight: 600; max-width: 920px")
        + f'<div data-chk="cards" style="display: flex; gap: 24px">'
        + leaf_card("leafhard", "Hard maple", "A hard maple leaf", ["Smooth edges", "Dark green on top", "Red, orange or yellow in fall"])
        + leaf_card("leafsoft", "Soft maple", "A soft or silver maple leaf", ["Toothed edges", "Pointier lobes", "Whitish underneath"])
        + "</div>"
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["cream"], column(inner, gap=24), C["maroon"]), "Clue 1: check the leaf"


def bark_card(key, tag, alt, note):
    return (
        f'<div data-chk="bark-{key}" style="flex: 1 1 0; display: flex; flex-direction: column; gap: 14px">'
        + img(key, alt, f"width: 100%; height: 330px; object-fit: cover; border-radius: 28px; border: 8px solid {C['cream']}; box-sizing: border-box")
        + f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["gold"]}">{tag}</div>'
        + f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 33px; line-height: 1.16; color: {C["cream"]}">{note}</div></div>'
    )


def slide3():
    sub = f'font-family: {DISPLAY}; font-weight: 800; font-size: 46px; letter-spacing: -0.02em; line-height: 1; color: {C["gold"]}; margin: 0'
    seed = (
        f'<div data-chk="seed-row" style="display: flex; align-items: center; gap: 30px">'
        f'<div style="flex: none; width: 210px; height: 250px; border-radius: 28px; background: #FFFFFF; display: flex; align-items: center; justify-content: center; overflow: hidden">'
        + img("seed", "Drawing of a sugar maple seed with two wings", "width: 190px; height: 240px; object-fit: contain")
        + "</div>"
        + body("Every maple grows “helicopter” seeds in pairs, with wings that spin as they fall.", 36, C["cream"], "seed-text", "; font-weight: 600; flex: 1 1 0")
        + "</div>"
    )
    inner = (
        kicker_row("Clues 2 &amp; 3 · Bark + seeds", "3 / 5", C["cream"])
        + headline("Bark &amp; helicopters", 112, C["cream"])
        + f'<h2 data-chk="h-bark" style="{sub}; margin-top: 6px">Read the bark</h2>'
        + f'<div data-chk="bark-row" style="display: flex; gap: 30px">'
        + bark_card("barkhard", "Hard maple", "Sugar maple bark", "Gray, with deep furrows on older trees")
        + bark_card("barksoft", "Soft maple", "Silver maple bark", "More layered and flaky")
        + "</div>"
        + f'<h2 data-chk="h-seeds" style="{sub}; margin-top: 8px">Look for helicopters</h2>'
        + seed
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
    )
    return root(C["maroon"], column(inner, gap=22), C["maroon"]), "Clues 2 and 3: bark and helicopters"


def check_item(main, note=""):
    extra = f'<div style="font-weight: 500; font-size: 26px; margin-top: 4px">{note}</div>' if note else ""
    return (
        f'<div style="display: flex; gap: 16px; align-items: flex-start">{check_badge()}'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 31px; line-height: 1.14; color: {C["maroon"]}">{main}{extra}</div></div>'
    )


def slide4():
    photo = (
        f'<div data-chk="trunk" style="position: relative; width: 390px; flex: none">'
        + img("trunk", "A maple trunk with a ruler across it to measure the width",
              f"width: 390px; height: 560px; object-fit: cover; border-radius: 32px; border: 8px solid {C['cream']}; box-sizing: border-box")
        + f'<div style="position: absolute; left: 24px; bottom: 26px; background: {C["maroon"]}; color: {C["cream"]}; border-radius: 12px; '
        f'padding: 8px 14px 6px; font-family: {TYPE}; font-size: 26px; letter-spacing: 0.04em">Measure 4½ ft up</div></div>'
    )
    card = (
        f'<div data-chk="checklist" style="flex: 1 1 0; min-width: 0; background: {C["cream"]}; border-radius: 32px; padding: 34px 30px; '
        f'display: flex; flex-direction: column; justify-content: center; gap: 24px">'
        + check_item("At least 12 in. across", "About 38 in. around the trunk")
        + check_item("A full canopy of leaves", "More leaves, sweeter sap")
        + check_item("No big broken limbs or rot", "A missing twig or two is fine")
        + check_item("Never sprayed with pesticides or herbicides")
        + "</div>"
    )
    mark = (
        f'<div data-chk="mark" style="background: {C["maroon"]}; color: {C["cream"]}; border-radius: 28px; padding: 24px 30px; display: flex; '
        f'flex-direction: column; gap: 6px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.05">Then mark it today.</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 30px; line-height: 1.25">Tie on a bright ribbon, plant a flag, or drop a GPS pin. In March, bare maples all look alike.</div></div>'
    )
    inner = (
        kicker_row("Found one?", "4 / 5", C["maroon"])
        + headline("Is it tap-ready?", 120, C["maroon"])
        + f'<div data-chk="row" style="display: flex; gap: 24px; align-items: stretch">{photo}{card}</div>'
        + mark
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], column(inner, gap=24), C["maroon"]), "Is it tap-ready?"


def step(kind, label, main, here=False):
    badge = (
        f'<span style="display: inline-block; vertical-align: middle; margin-left: 12px; background: {C["gold"]}; color: {C["maroon"]}; '
        f'border-radius: 999px; padding: 5px 14px 3px; font-family: {TYPE}; font-size: 21px; letter-spacing: 0.04em">You are here</span>'
        if here else ""
    )
    return (
        f'<div style="display: flex; gap: 22px; align-items: center; position: relative; z-index: 1">{icon_badge(kind, 76)}'
        f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0">'
        f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["cream"]}">{label}{badge}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 35px; line-height: 1.12; color: {C["cream"]}">{main}</div></div></div>'
    )


def slide5():
    photo = img("pancakes", "Maple syrup pouring onto a stack of pancakes with butter",
                f"width: 440px; height: 440px; object-fit: cover; object-position: 50% 50%; border-radius: 36px; border: 8px solid {C['cream']}; box-sizing: border-box; flex: none")
    timeline = (
        f'<div data-chk="timeline" style="position: relative; display: flex; flex-direction: column; gap: 20px">'
        f'<div style="position: absolute; left: 36px; top: 38px; bottom: 38px; border-left: 5px dashed {C["cream"]}; opacity: 0.55"></div>'
        + step("leaf", "Now · Fall", "Find &amp; mark your maples", here=True)
        + step("snow", "Christmas", "Find a tapping kit under the tree")
        + step("tap", "Late winter", "Tap when nights hit the 20s and days the 40s °F")
        + step("jar", "Early spring", "Collect, boil &amp; bottle with the whole family")
        + "</div>"
    )
    top = (
        f'<div data-chk="toprow" style="display: flex; gap: 28px; align-items: center">'
        + headline("From tree to pancakes", 110, C["cream"], extra="; flex: 1 1 0")
        + photo + "</div>"
    )
    inner = (
        kicker_row("Your sweet-season roadmap", "5 / 5", C["cream"])
        + top
        + timeline
        + f'<div data-chk="stat" style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 28px; padding: 22px 28px; font-family: {DISPLAY}; '
        f'font-weight: 800; font-size: 40px; line-height: 1.1">4 taps make about 1 gallon of syrup a season.</div>'
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; letter-spacing: 0; color: {C["cream"]}">mapletapper.com</span>')
    )
    return root(C["red"], column(inner, gap=28), C["cream"]), "From tree to pancakes"


SLIDES = [("Main", slide1), ("Post01-2-Notches", slide2), ("Post01-3-Bark", slide3), ("Post01-4-Ribbon", slide4), ("Post01-5-Roadmap", slide5)]


def with_images(markup, mapping):
    for key, url in mapping.items():
        markup = markup.replace(f"@@IMG_{key}@@", url)
    return markup


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", "v2_" + name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_p1.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
