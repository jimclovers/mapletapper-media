"""Bonus 01 - Tree Talk: "Maples light up the horizon" (5 slides), built from Jim's own fall photos.
Photos: cropped so no house, car or plate is in frame; saved without metadata (photos/p5/).
Facts checked against 2+ sources:
  - in fall, maples show bright red, orange and gold, the time to find and mark them (UNH Extension; UW-Madison Ext.; MDC)
  - other trees and shrubs also turn red: red oak, staghorn sumac, burning bush (Iowa State Ext.; Nebraska Ext.)
  - farm families planted sugar maples near the house and along roads for syrup and shade (UNH Extension; Boston Globe)
  - silver maple: fast-growing, widely planted in towns, brittle wood (Arbor Day Foundation; SIU Arboretum; Missouri Ext.)
  - Dutch elm disease arrived in 1930, killed millions of elms; maples replaced many street elms (USDA Forest Service;
    Casey Trees; Central Park Conservancy; EBSCO)
  - Freeman's maple (red x silver) is very common as a Chicago-area parkway tree, red-orange in fall (Morton Arboretum; UMN)
  - "wedding trees": newlyweds planted a pair of sugar maples by the front walk (UNH Extension; Fedco Trees)
  - red needs sunlight; shaded leaves show gold (Brooklyn Botanic Garden; NJ Forest Service)
  - parkway trees belong to the village in many towns (Clarendon Hills; Lincolnwood)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   dc_html, preview_html)
from post02 import pill, with_images  # noqa: E402
from post03 import stamp, check_svg, PHOTO_H  # noqa: E402
from funfacts import site_footer  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"cover": "p5/bonus_cover.jpg", "spot": "p5/bonus_spot.jpg", "history": "p5/bonus_history.jpg",
          "wedding": "p5/bonus_wedding.jpg", "halfred": "p5/bonus_halfred.jpg"}
M, CR, RED, GOLD, SKY = C["maroon"], C["cream"], C["red"], C["gold"], C["sky"]


def img(key, alt, style):
    return f'<img src="@@IMG_{key}@@" alt="{alt}" style="display: block; object-fit: cover; {style}">'


def slide1():
    photo = img("cover", "Roadside maples glowing red and orange above a green thicket under a blue sky",
                f"position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-position: 50% 40%")
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Sugarmaker’s Almanac · Tree Talk", CR, M)}{pill("17 weeks to sap season", GOLD, M)}</div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 100px 72px 60px; display: flex; flex-direction: column; gap: 20px; background: {M}">'
        + headline("Maples light up<br>the horizon.", 96, CR, chk="title")
        + body("Fall color makes them easy to spot from the road. Swipe for scouting tips!", 36, GOLD, "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(CR, swipe(CR))
        + "</div>"
    )
    return root(M, photo + top + stamp("SCOUTING", "season") + bottom, CR), "Maples light up the horizon"


def slide2():
    photo = img("spot", "A wooded hillside in fall with one bright red-orange maple standing out among brown and gold trees",
                "width: 936px; height: 560px; border-radius: 30px; object-position: 50% 45%")
    tag = lambda t: (f'<span style="background: {CR}; color: {M}; border: 3px solid {M}; border-radius: 999px; padding: 8px 18px 7px; '
                     f'font-family: {DISPLAY}; font-weight: 700; font-size: 28px; line-height: 1">{t}</span>')
    card = (
        f'<div data-chk="check" style="background: {M}; color: {CR}; border-radius: 30px; padding: 28px 34px; display: flex; flex-direction: column; gap: 14px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.05">Then walk up and check the leaf.</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 30px; line-height: 1.25">Not every red tree is a maple. These turn red too:</div>'
        f'<div style="display: flex; gap: 12px; flex-wrap: wrap">'
        + "".join(f'<span style="background: {GOLD}; color: {M}; border-radius: 999px; padding: 9px 20px 8px; font-family: {DISPLAY}; '
                  f'font-weight: 700; font-size: 28px; line-height: 1">{t}</span>' for t in ("Red oak", "Sumac", "Burning bush"))
        + '</div></div>'
    )
    inner = (
        kicker_row("Scouting tip · From the road", "2 / 5", M)
        + headline(f'Look for the<br><span style="color: {RED}">brightest crowns.</span>', 84, M)
        + f'<div data-chk="photo" style="position: relative">{photo}'
          f'<div style="position: absolute; left: 22px; bottom: 22px; display: flex; gap: 10px">{tag("Hillsides")}{tag("Fencerows")}{tag("Yards")}</div></div>'
        + '<div style="flex-grow: 1"></div>'
        + card
        + '<div style="flex-grow: 1"></div>'
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=26), M), "Look for the brightest crowns"


def slide3():
    photo = img("history", "A big neighborhood maple covered in red-orange leaves",
                f"width: 300px; height: 300px; border-radius: 50%; border: 10px solid {GOLD}; flex: none")
    rows = [
        ("1800s", "Farm families planted sugar maples by the house and along country roads, for shade and syrup."),
        ("Fast shade", "Towns planted lots of quick-growing silver maples along their streets."),
        ("1930s on", "Dutch elm disease killed millions of elm street trees. Many towns replanted with maples."),
        ("Today", "Freeman maples, a red and silver maple cross, line many Chicago-area parkways for their red-orange fall color."),
    ]
    items = "".join(
        f'<div style="display: flex; gap: 22px; align-items: flex-start">'
        f'<div style="flex: none; width: 205px; padding-top: 4px; font-family: {DISPLAY}; font-weight: 800; font-size: 38px; '
        f'line-height: 1.05; color: {GOLD}">{y}</div>'
        f'<div style="flex: 1 1 0; font-family: {DISPLAY}; font-weight: 500; font-size: 34px; line-height: 1.24; color: {CR}">{t}</div></div>'
        for y, t in rows
    )
    inner = (
        kicker_row("History", "3 / 5", CR)
        + f'<div data-chk="top" style="display: flex; align-items: center; justify-content: space-between; gap: 24px">'
          + headline(f'Why so<br>many<br><span style="color: {GOLD}">maples?</span>', 100, CR)
          + photo + "</div>"
        + '<div style="flex-grow: 1"></div>'
        + f'<div data-chk="rows" style="display: flex; flex-direction: column; gap: 30px">{items}</div>'
        + '<div style="flex-grow: 1"></div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=26), CR), "Why so many maples?"


def slide4():
    photo = img("wedding", "A big maple with orange-red fall leaves standing alone on a green lawn",
                "width: 936px; height: 600px; border-radius: 30px; object-position: 45% 50%")
    inner = (
        kicker_row("Fun fact", "4 / 5", M)
        + headline(f'Wedding<br><span style="color: {RED}">trees.</span>', 110, M)
        + f'<div data-chk="photo">{photo}</div>'
        + body("An old New England custom: newlyweds planted two sugar maples by the front walk of their new home, one on each side.",
               34, M, "story", "; font-weight: 600")
        + body("Some of those “wedding trees” still shade old farmhouses today.", 30, M, "today")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(M, swipe(M))
    )
    return root(SKY, column(inner, gap=26), M), "Wedding trees"


def slide5():
    photo = img("halfred", "A maple turning red on top and on its sunny side, still green and gold below",
                f"width: 380px; height: 552px; border-radius: 30px; flex: none")
    tip = (
        f'<div data-chk="tip" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 26px 32px; display: flex; flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase">Found a big one?</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 31px; line-height: 1.25">'
        f'<b style="font-weight: 800">Mark it now</b> with a ribbon or a GPS pin. And ask before tapping a tree that isn’t yours: '
        f'in many towns, parkway trees belong to the village.</div></div>'
    )
    text = (
        f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 22px">'
        + body("Red color needs sunlight to form.", 38, M, "why1", "; font-weight: 800; line-height: 1.12")
        + body("The sunniest leaves turn red. Shaded leaves show gold instead.", 32, M, "why2")
        + body("That’s why many maples turn reddest on top and on their sunny side.", 30, RED, "why3", "; font-weight: 700")
        + "</div>"
    )
    inner = (
        kicker_row("Why half red?", "5 / 5", M)
        + headline(f'Why is half<br>this tree <span style="color: {RED}">red?</span>', 88, M)
        + f'<div data-chk="mid" style="display: flex; gap: 32px; align-items: center">{photo}{text}</div>'
        + '<div style="flex-grow: 1"></div>'
        + tip
        + '<div style="flex-grow: 1"></div>'
        + site_footer(M)
    )
    return root(CR, column(inner, gap=26), M), "Why is half this tree red?"


SLIDES = [("Bonus01-1-Cover", slide1), ("Bonus01-2-Spot", slide2), ("Bonus01-3-History", slide3),
          ("Bonus01-4-Wedding", slide4), ("Bonus01-5-HalfRed", slide5)]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_b1.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
