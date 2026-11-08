"""Tree ID bonus - Norway maple: can you tap it? (5 slides). Photos: Jim's Norway maple tree, leaf and bark (Nov 2026).

Facts (2+ sources each, rewritten):
- Milky sap in snapped leaf stem; native maples clear: Purdue Extension, Illinois Wildflowers, USDA Forest Service, UConn.
  Milky sap can fade by late summer: Utah State Extension.
- Fall color usually yellow; sugar maple more orange/red: Illinois Wildflowers, UConn/Wikibooks.
- Bark regular criss-cross grooves vs sugar maple irregular/shaggy plates: invasive.org (USFS), Columbia Univ. summary.
- Seed wings spread nearly flat (~180 deg) vs sugar maple V: invasive.org, Illinois Wildflowers, Purdue.
- Leaves broader than sugar maple, more points with hair-like tips: UConn Plant Database, Ontario Trees, Wikibooks.
- Native to Europe, brought to U.S. mid-1700s (1756): USFS/invasive.org, Columbia.
- Invasive: dense shade + heavy seeding crowd out natives incl. sugar maple: Purdue, UConn, USDA Forest Service.
- Tapping: Ohio State F-36 (many report sap about as sweet as sugar maple); Utah State/HortTechnology 2024
  (2.2-2.8% sugar, 7.5-9.3 L sap per tree per season; USU thesis: ~35 gal sap per gal syrup, matches Rule of 86); UNH thesis (tapping guidelines similar to sugar maple).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   dc_html, preview_html)
from post02 import pill, with_images  # noqa: E402
from tree01 import clue  # noqa: E402
from jugs import sap_card  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"tree": "jim/norway_tree_real.jpg", "leaf": "jim/norway_leaf_real.jpg", "bark": "jim/norway_bark_real.jpg",
          "yellow": "jim/norway_yellow_real.jpg", "logo": "../assets/logo.png"}
PHOTO_H = 860


def num_badge(n, bg, fg, size=84):
    return (
        f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; color: {fg}; display: flex; '
        f'align-items: center; justify-content: center; flex: none; font-family: {DISPLAY}; font-weight: 800; font-size: 44px">{n}</div>'
    )


def slide1():
    photo = (
        f'<img src="@@IMG_tree@@" alt="Looking up the trunk of a Norway maple into a canopy of yellow and green leaves" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-fit: cover; object-position: 50% 60%; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Tree ID · Bonus", C["cream"], C["maroon"])}{pill("16 weeks to sap season", C["gold"], C["maroon"])}</div>'
    )
    stamp = (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: {PHOTO_H - 64}px; z-index: 3; transform: rotate(-3deg); background: {C["gold"]}; '
        f'border: 6px solid {C["cream"]}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 16px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 72px; letter-spacing: -0.02em; line-height: 1; color: {C["maroon"]}">'
        f'TREE ID<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">bonus</span></div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 104px 72px 60px; display: flex; flex-direction: column; gap: 18px; background: {C["maroon"]}">'
        + headline("Norway maple", 132, C["cream"], chk="title")
        + body("The street maple. Can you tap it? Swipe.", 38, C["gold"], "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
        + "</div>"
    )
    return root(C["maroon"], photo + top + stamp + bottom, C["cream"]), "Tree ID bonus: Norway maple"


def slide2():
    photo = (
        f'<div data-chk="photo" style="position: relative; border-radius: 30px; overflow: hidden; height: 430px; flex: none">'
        f'<img src="@@IMG_leaf@@" alt="Wide green Norway maple leaves with sharp, pointed lobes hanging beside a big trunk" '
        f'style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 62%; display: block">'
        f'<span style="position: absolute; left: 22px; bottom: 20px; background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; '
        f'padding: 9px 18px 7px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.05em; text-transform: uppercase">Real Norway maple leaves</span></div>'
    )
    clues = (
        f'<div data-chk="clues" style="display: flex; flex-direction: column; gap: 30px; margin-top: 8px">'
        + clue(num_badge(1, C["maroon"], C["cream"]), "Milky white sap", "Native maples run clear. Easiest to see before late summer.")
        + clue(num_badge(2, "#4E7A3A", C["cream"]), "Wide leaves, sharp points", "Each point ends in a fine, hair-like tip")
        + clue(num_badge(3, C["gold"], C["maroon"]), "Fall color is usually yellow", "Sugar maples lean orange to red")
        + "</div>"
    )
    inner = (
        kicker_row("How to spot it", "2 / 5", C["maroon"])
        + headline("Snap a leaf stem.<br>Milky? It’s Norway.", 88, C["maroon"])
        + photo
        + clues
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["cream"], column(inner, gap=30), C["maroon"]), "How to spot a Norway maple"


def seeds_svg(flat, size=300):
    """Simple drawing of a pair of maple seeds: flat (Norway) or V-shaped (sugar)."""
    import math
    ang = 90 if flat else 38  # degrees each wing tilts away from straight down
    wings, nuts = "", ""
    for sign in (1, -1):
        a = math.radians(ang) * sign
        dx, dy = math.sin(a), math.cos(a)
        nx, ny = 150 + 22 * dx, 60 + 22 * dy
        cx, cy = 150 + 78 * dx, 60 + 78 * dy
        rot = -math.degrees(a)
        wings += (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="24" ry="58" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})" '
                  f'fill="#D9B470" stroke="{C["maroon"]}" style="stroke-width:3.5"></ellipse>')
        nuts += f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="17" fill="{C["maroon"]}"></circle>'
    return (f'<svg aria-hidden="true" width="{size}" height="{size * 0.6:.0f}" viewBox="0 0 300 180">{wings}{nuts}</svg>')


def slide3():
    bark = (
        f'<div data-chk="bark" style="display: flex; align-items: center; gap: 36px">'
        f'<img src="@@IMG_bark@@" alt="Close-up of Norway maple bark with tight, criss-crossing grooves" style="width: 380px; height: 380px; '
        f'border-radius: 50%; object-fit: cover; border: 10px solid {C["cream"]}; flex: none; display: block">'
        f'<div style="display: flex; flex-direction: column; gap: 12px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 54px; line-height: 1.02; color: {C["maroon"]}">Tight, criss-cross grooves</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 33px; line-height: 1.25; color: {C["maroon"]}">Older sugar maple bark breaks into shaggy plates.</div></div></div>'
    )
    lab = lambda t: f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["maroon"]}">{t}</div>'
    seeds = (
        f'<div data-chk="seeds" style="display: flex; flex-direction: column; gap: 18px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 54px; line-height: 1.02; color: {C["maroon"]}">Seeds spread out flat</div>'
        f'<div style="display: flex; gap: 28px">'
        f'<div style="flex: 1 1 0; background: {C["cream"]}; border-radius: 28px; padding: 30px 22px; display: flex; flex-direction: column; align-items: center; gap: 14px">'
        f'{seeds_svg(True)}{lab("Norway: almost a straight line")}</div>'
        f'<div style="flex: 1 1 0; background: #F7D98A; border-radius: 28px; padding: 30px 22px; display: flex; flex-direction: column; align-items: center; gap: 14px">'
        f'{seeds_svg(False)}{lab("Sugar maple: a V shape")}</div></div></div>'
    )
    inner = (
        kicker_row("Two more clues", "3 / 5", C["maroon"])
        + bark
        + '<div style="flex-grow: 1"></div>'
        + seeds
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], column(inner, gap=40), C["maroon"]), "Two more Norway maple clues"


def point(icon, main, note):
    return (
        f'<div style="display: flex; gap: 26px; align-items: flex-start">'
        f'<div style="font-size: 52px; line-height: 1; flex: none; width: 64px; text-align: center">{icon}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.08; color: {C["cream"]}">{main}'
        f'<div style="font-weight: 600; font-size: 29px; line-height: 1.25; margin-top: 6px; color: {C["gold"]}">{note}</div></div></div>'
    )


def slide4():
    cards = (
        f'<div data-chk="cards" style="display: flex; flex-direction: column; gap: 20px">'
        + sap_card("Norway maple", "2.2–2.8%", 35, highlight=True, size=26, chk="card1")
        + sap_card("Sugar maple", "2–2.5%", 40, highlight=False, size=26, chk="card2")
        + "</div>"
    )
    src = (f'<div data-chk="src" style="font-family: {TYPE}; font-size: 23px; line-height: 1.35; letter-spacing: 0.02em; color: {C["gold"]}">'
           f'Norway numbers from a Utah State University study. Every tree is different.</div>')
    pts = (
        f'<div data-chk="points" style="display: flex; flex-direction: column; gap: 18px">'
        + point("💧", "The catch: a slow drip", "About 2 to 2½ gallons of sap per tree all season in that study.")
        + point("📏", "Same rules", "12+ inches across, a 5/16″ spout. Street tree? Ask your town first.")
        + "</div>"
    )
    inner = (
        kicker_row("Can you tap it?", "4 / 5", C["cream"])
        + headline("Yes! Almost as<br>sweet as sugar maple.", 66, C["cream"])
        + cards
        + src
        + '<div style="flex-grow: 1"></div>'
        + pts
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
    )
    return root(C["maroon"], column(inner, pad="60px 72px 48px", gap=18), C["cream"]), "Can you tap a Norway maple?"


def slide5():
    photo = (
        f'<div data-chk="photo" style="position: relative; border-radius: 30px; overflow: hidden; height: 470px; flex: none">'
        f'<img src="@@IMG_yellow@@" alt="Bright yellow Norway maple leaves against a blue sky" '
        f'style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; display: block"></div>'
    )
    facts = (
        f'<div data-chk="facts" style="display: flex; flex-direction: column; gap: 22px">'
        + body("<b>From Europe.</b> It came to America in the mid-1700s and became a favorite street tree.", 36, C["maroon"], "f1")
        + body("<b>Invasive in many states.</b> Its deep shade and loads of seeds crowd out native trees, even sugar maple.", 36, C["maroon"], "f2")
        + body("<b>Have one? Tap it and enjoy it.</b> Planting a new tree? Pick a native maple.", 36, C["maroon"], "f3")
        + "</div>"
    )
    teaser = (
        f'<div data-chk="teaser" style="background: {C["maroon"]}; color: {C["cream"]}; border-radius: 32px; padding: 26px 34px; display: flex; '
        f'flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["gold"]}">Your turn · comment below</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 42px; line-height: 1.04">Got a Norway maple on your street?</div></div>'
    )
    inner = (
        kicker_row("Good to know", "5 / 5", C["maroon"])
        + photo
        + facts
        + '<div style="flex-grow: 1"></div>'
        + f'<div style="display: flex; align-items: center; gap: 28px">' + teaser.replace('display: flex; \'\n        f\'flex-direction', 'flex: 1 1 0; display: flex; \'\n        f\'flex-direction') + f'<img data-chk="logo" src="@@IMG_logo@@" alt="MapleTapper logo, www.mapletapper.com" style="width: 210px; flex: none; display: block"></div>'
        + footer_row(C["maroon"], '<span></span>')
    )
    return root(C["cream"], column(inner, gap=28), C["maroon"]), "Good to know: Norway maple"


SLIDES = [("Norway01-1-Cover", slide1), ("Norway01-2-Spot", slide2), ("Norway01-3-Clues", slide3),
          ("Norway01-4-Tap", slide4), ("Norway01-5-Know", slide5)]

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
    for name, fn in SLIDES:
        markup, title = fn()
        open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
    print("preview built")
