"""Grid-variety covers (Jim, Nov 11 2026): new slide-1 covers for posts scheduled Nov 12-15.
Rule: rotate cover styles so the Instagram grid isn't a wall of maroon bands.
Usage: python3 covers_v2.py -> preview/cv2-*.html ; render with render.js -> posts/<post>/<post>-1-cover-v2.jpg
"""
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, W, H, ROOT, headline, preview_html, leaf_mark  # noqa: E402

M, CR, G, R = C["maroon"], C["cream"], C["gold"], C["red"]
PINE, SKY, NAVY, SNOW = "#1F4A36", "#9FD3F0", "#16233F", "#F7F4EE"


def data_uri(path, mime="image/jpeg"):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


LOGO = data_uri(os.path.join(ROOT, "assets", "logo.png"), "image/png")
P = lambda *a: os.path.join(ROOT, "photos", *a)
JIM = "/home/claude/mt/jimphotos"
BOOK = "/home/claude/mt/photos"


def logo_badge(right=48, bottom=48, size=150, bg=CR, top=None):
    pos = f"top: {top}px" if top is not None else f"bottom: {bottom}px"
    return (f'<div data-chk="logo" style="position: absolute; right: {right}px; {pos}; width: {size}px; height: {size}px; '
            f'border-radius: 50%; background: {bg}; display: flex; align-items: center; justify-content: center; z-index: 5; '
            f'box-shadow: 0 6px 18px rgba(0,0,0,.25)"><img src="{LOGO}" alt="MapleTapper logo" style="width: {int(size * .78)}px"></div>')


def tag(text, bg, fg, size=30, extra=""):
    return (f'<span data-chk="tag" style="display: inline-block; background: {bg}; color: {fg}; font-family: {TYPE}; font-size: {size}px; '
            f'letter-spacing: .06em; text-transform: uppercase; padding: 10px 22px; border-radius: 999px{extra}">{text}</span>')


def handle(color, left=56, bottom=64):
    return (f'<div data-chk="handle" style="position: absolute; left: {left}px; bottom: {bottom}px; display: flex; align-items: center; gap: 10px; '
            f'font-family: {TYPE}; font-size: 28px; color: {color}; z-index: 4">{leaf_mark(color, 32)}@mapletapper</div>')


def rootdiv(bg, inner):
    return (f'<div data-root style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: {bg}; '
            f'font-family: {DISPLAY}">{inner}</div>')


# 1 - Kids Corner, sky-blue block + round photo cut-out (post07)
def kids07():
    ruler = "".join(
        f'<rect x="{i * 40}" y="0" width="4" height="{40 if i % 3 == 0 else 22}" fill="{NAVY}"></rect>' for i in range(24))
    inner = (
        f'<div style="position: absolute; left: 56px; top: 64px">{tag("Kids corner", G, NAVY, 34, "; font-weight: 700")}</div>'
        f'<div style="position: absolute; left: 56px; top: 150px; width: 640px">'
        + headline("Is your tree big enough to tap?", 112, NAVY, chk="title") + '</div>'
        f'<div style="position: absolute; right: -90px; bottom: 210px; width: 720px; height: 720px; border-radius: 50%; overflow: hidden; '
        f'border: 16px solid #FFFFFF; box-shadow: 0 14px 40px rgba(0,0,0,.25)">'
        f'<img src="{data_uri(os.path.join(JIM, "trunk.jpg"))}" alt="A big maple trunk in a park" '
        f'style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%"></div>'
        f'<svg aria-hidden="true" style="position: absolute; left: 56px; top: 700px" width="300" height="40" viewBox="0 0 960 40">{ruler}</svg>'
        f'<div data-chk="sub" style="position: absolute; left: 56px; top: 770px; width: 360px; font-family: {DISPLAY}; font-weight: 700; '
        f'font-size: 40px; line-height: 1.15; color: {NAVY}">Grab a string and a ruler.</div>'
        + handle(NAVY) + logo_badge(bg="#FFFFFF")
    )
    return rootdiv(SKY, inner)


# 2 - Label check, full-bleed close-up photo with big white words (post08)
def pancake08():
    inner = (
        f'<img src="{data_uri(os.path.join(BOOK, "book", "p1_pancakes.jpg"))}" alt="Maple syrup pouring onto pancakes with butter" '
        f'style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 50%">'
        f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 760px; background: linear-gradient(to top, rgba(20,10,5,.88), rgba(20,10,5,0))"></div>'
        f'<div style="position: absolute; left: 56px; top: 60px">{tag("Label check", "rgba(255,255,255,.92)", M, 30)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; bottom: 210px">'
        + headline("Is that <i>really</i><br>maple syrup?", 132, "#FFFFFF", chk="title", extra="; text-shadow: 0 3px 16px rgba(0,0,0,.4)")
        + '</div>' + handle("#FFFFFF") + logo_badge(bottom=40, size=130)
    )
    return rootdiv("#2a1a10", inner)


# 3 - Scavenger hunt, full real photo, small label only (post09)
def scav09():
    inner = (
        f'<img src="{data_uri(os.path.join(BOOK, "p6", "p6_12_2e190651.jpg"))}" alt="A big maple in orange and gold fall color" '
        f'style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%">'
        f'<div data-chk="title" style="position: absolute; left: 56px; top: 64px; background: {CR}; border-radius: 24px; padding: 26px 34px 30px; '
        f'box-shadow: 0 8px 24px rgba(0,0,0,.25); transform: rotate(-2deg)">'
        f'<div style="font-family: {TYPE}; font-size: 28px; letter-spacing: .06em; text-transform: uppercase; color: {R}">Family game</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 74px; line-height: .95; letter-spacing: -.02em; color: {M}">Maple<br>scavenger hunt</div></div>'
        f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 220px; background: linear-gradient(to top, rgba(0,0,0,.45), rgba(0,0,0,0))"></div>'
        + handle("#FFFFFF") + logo_badge(bottom=40, size=130)
    )
    return rootdiv("#333", inner)


# 4 - Baking swap, all-gold illustration, no maroon band (post10)
def bake10():
    sys.argv = [sys.argv[0]]
    import post10
    art = post10.cover_art()
    inner = (
        f'<div style="position: absolute; left: 56px; top: 64px">{tag("Swap guide", M, CR, 30)}</div>'
        f'<div style="position: absolute; left: 56px; right: 200px; top: 150px">'
        + headline("Bake with maple instead of sugar", 116, M, chk="title") + '</div>'
        f'<div style="position: absolute; left: 40px; top: 560px">{art}</div>'
        + handle(M) + logo_badge(bg=CR, top=40, size=130)
    )
    return rootdiv(G, inner)


# 5 - Ultimate kit, pine-green product layout (gift04)
def gift04():
    inner = (
        f'<div style="position: absolute; left: 56px; top: 64px">{tag("Holiday gift guide", G, PINE, 28)}</div>'
        f'<div style="position: absolute; right: 56px; top: 64px">{tag("Order by Dec 21", CR, PINE, 28)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 160px; height: 560px; border-radius: 32px; overflow: hidden; background: #000">'
        f'<img src="{data_uri(P("crops", "g04.jpg"))}" alt="The Ultimate Maple Tapping Kit laid out: taps, tubing, filters, bottle and Guide book" '
        f'style="width: 100%; height: 100%; object-fit: contain"></div>'
        f'<div style="position: absolute; left: 56px; right: 220px; top: 790px">'
        + headline("The gift for the DIYer who has everything", 92, CR, chk="title") + '</div>'
        f'<div data-chk="price" style="position: absolute; left: 56px; top: 1130px; font-family: {DISPLAY}; font-weight: 800; font-size: 46px; color: {G}">'
        f'Ultimate Kit · $179.99</div>'
        + logo_badge()
    )
    return rootdiv(PINE, inner)


# 6 - Stocking stuffers, snowy white with red (gift05)
def gift05():
    inner = (
        f'<div style="position: absolute; left: 56px; top: 64px">{tag("Holiday gift guide", R, "#FFFFFF", 28)}</div>'
        f'<div style="position: absolute; right: 56px; top: 64px">{tag("Order by Dec 21", PINE, "#FFFFFF", 28)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 150px; height: 590px">'
        f'<img src="{data_uri(P("crops", "g05.jpg"))}" alt="Glass maple leaf bottles, filters and recipe cards" '
        f'style="width: 100%; height: 100%; object-fit: contain; mix-blend-mode: multiply"></div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 790px">'
        + headline("Stocking stuffers for syrup lovers", 104, R, chk="title") + '</div>'
        f'<div style="position: absolute; left: 56px; top: 1060px">{tag("All under $35", G, PINE, 34, "; font-weight: 700")}</div>'
        + handle(PINE) + logo_badge(bg="#FFFFFF")
    )
    return rootdiv(SNOW, inner)


# 7 - Gift timeline, night-navy with snowflakes + tilted photo print (gift06)
def gift06():
    import random
    rnd = random.Random(7)
    flakes = "".join(f'<circle cx="{rnd.randint(0, 1080)}" cy="{rnd.randint(0, 1350)}" r="{rnd.choice([3, 4, 5, 7])}" fill="#FFFFFF" '
                     f'fill-opacity="{rnd.choice([.35, .5, .7])}"></circle>' for _ in range(90))
    inner = (
        f'<svg aria-hidden="true" style="position: absolute; inset: 0" width="1080" height="1350">{flakes}</svg>'
        f'<div style="position: absolute; left: 56px; top: 64px">{tag("Holiday gift guide", CR, NAVY, 28)}</div>'
        f'<div style="position: absolute; right: 56px; top: 64px">{tag("Order by Dec 21", G, NAVY, 28)}</div>'
        f'<div style="position: absolute; left: 150px; top: 170px; width: 780px; background: #FFFFFF; padding: 22px 22px 70px; '
        f'transform: rotate(3deg); box-shadow: 0 16px 40px rgba(0,0,0,.45)">'
        f'<img src="{data_uri(P("crops", "g06.jpg"))}" alt="A hand fitting blue tubing through a white bucket lid at a maple" '
        f'style="width: 100%; height: 470px; object-fit: cover; display: block"></div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 830px">'
        + headline('Give it in December.<br><span style="color: ' + G + '">Boil syrup by March.</span>', 100, "#FFFFFF", chk="title") + '</div>'
        + handle(CR) + logo_badge()
    )
    return rootdiv(NAVY, inner)


SLIDES = [("cv2-post07", kids07), ("cv2-post08", pancake08), ("cv2-post09", scav09), ("cv2-post10", bake10),
          ("cv2-gift04", gift04), ("cv2-gift05", gift05), ("cv2-gift06", gift06)]

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    out = []
    for name, fn in SLIDES:
        p = os.path.join(ROOT, "preview", name + ".html")
        open(p, "w").write(preview_html(name, fn()))
        out.append(p)
    print(" ".join(out))
