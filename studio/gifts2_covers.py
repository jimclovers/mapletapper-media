"""Holiday Gift Guide week 2 (evening posts Nov 16-22 2026): slide-1 covers following the Grid variety rule.
Usage: python3 gifts2_covers.py -> preview/G2-NN-cover.html ; render with render.js.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, headline, preview_html  # noqa: E402
from covers_v2 import logo_badge, tag, handle, rootdiv, data_uri, PINE, SKY, NAVY, SNOW  # noqa: E402

M, CR, G = C["maroon"], C["cream"], C["gold"]
PR = lambda n: os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos", "products", n)
JIM = lambda n: os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos", "jim", n)
GUIDE = "Holiday gift guide"


def photo(path, pos="50% 50%", extra=""):
    return (f'<img src="{data_uri(path)}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; '
            f'object-fit: cover; object-position: {pos}{extra}">')


def fade(h=760):
    return (f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: {h}px; '
            f'background: linear-gradient(to top, rgba(20,10,5,.85), rgba(20,10,5,0))"></div>')


def top_tag(text, bg, fg):
    return f'<div style="position: absolute; left: 56px; top: 60px; z-index: 3">{tag(text, bg, fg, 30)}</div>'


# 1 Mon Nov 16 - Deluxe Kit + Book: product flat-lay on snow
def g1():
    inner = (
        top_tag(GUIDE, M, CR)
        + f'<div style="position: absolute; left: 56px; top: 140px; width: 960px">' + headline("Room for 20 trees", 120, M, chk="title") + "</div>"
        + f'<div data-chk="pic" style="position: absolute; left: 90px; right: 90px; top: 300px; height: 820px; border-radius: 30px; overflow: hidden; background: #fff; '
          f'box-shadow: 0 14px 40px rgba(0,0,0,.12)">{photo(PR("deluxe_flatlay.jpg"), "50% 50%", "; object-fit: contain")}</div>'
        + handle(M) + logo_badge(bg=CR)
    )
    return rootdiv(SNOW, inner)


# 2 Tue Nov 17 - Teacher / classroom gift: full-bleed real photo, small label only
def g2():
    inner = (
        photo(PR("kids_kit_snow_jugs.jpg"), "50% 50%") + fade(420)
        + f'<div data-chk="title" style="position: absolute; left: 56px; bottom: 150px; z-index: 3">{tag("A gift for the class", CR, M, 40, "; font-weight: 700")}</div>'
        + handle("#FFFFFF") + logo_badge(bottom=40, size=130)
    )
    return rootdiv("#2a1a10", inner)


# 3 Wed Nov 18 - Gifts at every budget: sunny gold block
def g3():
    chips = [("$12.99", "Guide book"), ("$14.99", "Kid’s Guide"), ("$19.97", "10 spiles"), ("$39.97", "Kid’s Kit"),
             ("$69.96", "Deluxe Kit"), ("$179.99", "Ultimate Kit")]
    grid = "".join(
        f'<div style="background: {CR}; border-radius: 26px; padding: 26px 28px; box-shadow: 0 8px 20px rgba(0,0,0,.08)">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 64px; line-height: 1; color: {M}">{p}</div>'
        f'<div style="font-family: {TYPE}; font-size: 28px; color: {NAVY}; margin-top: 8px">{n}</div></div>' for p, n in chips)
    inner = (
        top_tag(GUIDE, NAVY, G)
        + f'<div style="position: absolute; left: 56px; top: 140px; width: 960px">' + headline("A maple gift<br>for every budget", 120, NAVY, chk="title") + "</div>"
        + f'<div data-chk="grid" style="position: absolute; left: 56px; right: 56px; top: 450px; display: grid; grid-template-columns: 1fr 1fr; gap: 26px">{grid}</div>'
        + handle(NAVY) + logo_badge(bg=CR)
    )
    return rootdiv(G, inner)


# 4 Thu Nov 19 - Filters + glass leaf bottles: close-up photo, big white words
def g4():
    inner = (
        photo(PR("leaf_bottle_fall.jpg"), "50% 100%", "; transform: scale(1.6); transform-origin: 50% 100%") + fade(700)
        + top_tag(GUIDE, "rgba(255,255,255,.92)", M)
        + f'<div style="position: absolute; left: 56px; right: 56px; bottom: 210px">'
        + headline("Bottle their<br>first batch", 140, "#FFFFFF", chk="title", extra="; text-shadow: 0 3px 16px rgba(0,0,0,.4)") + "</div>"
        + handle("#FFFFFF") + logo_badge(bottom=40, size=130)
    )
    return rootdiv("#2a1a10", inner)


# 5 Fri Nov 20 - Grandparents: sky blue block + BIG Kid's Guide cover cut-out
def g5():
    inner = (
        top_tag("For grandparents", G, NAVY)
        + f'<div style="position: absolute; left: 56px; top: 130px; width: 960px">' + headline("Start a family tradition", 84, NAVY, chk="title", extra="; white-space: nowrap") + "</div>"
        + f'<div data-chk="pic" style="position: absolute; left: 170px; top: 290px; width: 740px; height: 780px; transform: rotate(-2deg); '
          f'border: 16px solid #fff; box-shadow: 0 16px 44px rgba(0,0,0,.28); overflow: hidden">{photo(PR("kids_guide_cover_hi.jpg"))}</div>'
        + handle(NAVY) + logo_badge(bg="#FFFFFF")
    )
    return rootdiv(SKY, inner)


# 6 Sat Nov 21 - Pink spiles: pine block + product cut-out (flag badge cropped off)
def g6():
    inner = (
        top_tag("Stocking stuffer", "#F4A6C4", PINE)
        + f'<div style="position: absolute; left: 56px; top: 140px; width: 960px">' + headline("Pink taps?<br>Yes, really.", 140, SNOW, chk="title") + "</div>"
        + f'<div data-chk="pic" style="position: absolute; left: 140px; right: 140px; top: 470px; height: 640px; border-radius: 40px; overflow: hidden; background: #fff">'
          f'<img src="{data_uri(PR("pink_spiles.jpg"))}" alt="" style="position: absolute; left: 0; top: -210px; width: 1100px"></div>'
        + handle(SNOW) + logo_badge(bg=CR)
    )
    return rootdiv(PINE, inner)


# 7 Sun Nov 22 - Thanksgiving host gift: navy block + Guide book cut-out (yellow text band cropped off)
def g7():
    inner = (
        top_tag("Thanksgiving host gift", G, NAVY)
        + f'<div style="position: absolute; left: 56px; top: 140px; width: 960px">' + headline("Bring this,<br>not another pie", 120, SNOW, chk="title") + "</div>"
        + f'<div data-chk="pic" style="position: absolute; left: 290px; top: 470px; width: 500px; height: 590px; transform: rotate(-3deg); '
          f'border: 14px solid #fff; box-shadow: 0 14px 40px rgba(0,0,0,.35); overflow: hidden">'
          f'<img src="{data_uri(PR("guide_book.jpg"))}" alt="" style="position: absolute; left: -110px; top: -8px; width: 720px"></div>'
        + handle(SNOW) + logo_badge(bg=CR)
    )
    return rootdiv(NAVY, inner)


COVERS = [g1, g2, g3, g4, g5, g6, g7]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview")
    os.makedirs(out, exist_ok=True)
    for i, fn in enumerate(COVERS, 1):
        open(os.path.join(out, f"G2-{i:02d}-cover.html"), "w").write(preview_html(f"Gift {i}", fn()))
    print("built", len(COVERS))
