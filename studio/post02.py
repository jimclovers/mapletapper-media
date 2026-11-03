"""Post 02 - Myth or Fact: "Tapping a maple hurts the tree." (4 slides, real MapleTapper photo)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, arrow_svg, leaf_mark, kicker_row, footer_row, swipe, headline, body,
                   root, column, dc_html, preview_html)  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"cover": "post02-cover.jpg", "detail": "post02-detail.jpg", "pull": "book/p2_pull_spile.jpg"}


def pill(text, bg, fg, size=24):
    return (
        f'<span style="display: inline-flex; align-items: center; background: {bg}; color: {fg}; border-radius: 999px; '
        f'padding: 10px 20px 8px; font-family: {TYPE}; font-size: {size}px; letter-spacing: 0.06em; text-transform: uppercase">{text}</span>'
    )


def slide1():
    photo = (
        f'<img src="@@IMG_cover@@" alt="A MapleTapper spile and blue drop line in a maple trunk, snow behind" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: 780px; object-fit: cover; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Sugarmaker’s Almanac · No. 02", C["cream"], C["maroon"])}{pill("17 weeks to sap season", C["gold"], C["maroon"])}</div>'
    )
    stamp = (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: 712px; z-index: 3; transform: rotate(-3deg); background: {C["gold"]}; '
        f'border: 6px solid {C["cream"]}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 18px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 76px; letter-spacing: -0.02em; line-height: 1; color: {C["maroon"]}">'
        f'MYTH<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">or</span>FACT?</div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: 780px; width: {W}px; height: {H - 780}px; box-sizing: border-box; '
        f'padding: 108px 72px 60px; display: flex; flex-direction: column; gap: 22px; background: {C["maroon"]}">'
        + headline("“Tapping a maple<br>hurts the tree.”", 94, C["cream"], chk="statement")
        + body("What do you think? Swipe for the answer.", 36, C["gold"], "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
        + "</div>"
    )
    inner = photo + top + stamp + bottom
    return root(C["maroon"], inner, C["cream"]), "Myth or fact: tapping hurts the tree"


def slide2():
    stamp = (
        f'<div aria-hidden="true" style="position: absolute; right: 74px; top: 150px; width: 230px; height: 230px; border-radius: 50%; '
        f'border: 8px solid {C["red"]}; display: flex; align-items: center; justify-content: center; transform: rotate(12deg); '
        f'font-family: {TYPE}; font-size: 42px; letter-spacing: 0.08em; color: {C["red"]}">BUSTED</div>'
    )
    photo = (
        f'<div data-chk="photo" style="display: flex; align-items: center; gap: 36px; margin-top: 18px">'
        f'<img src="@@IMG_pull@@" alt="Prying a spile out of a maple trunk with a claw hammer" '
        f'style="width: 420px; height: 420px; border-radius: 50%; object-fit: cover; border: 12px solid {C["cream"]}; flex: none; display: block">'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 40px; line-height: 1.18; color: {C["maroon"]}">'
        f'Pull the spile at season’s end, and new wood grows over the hole. <span style="color: {C["red"]}">A healthy tree closes it in 1 to 3 years.</span></div></div>'
    )
    inner = (
        kicker_row("The answer", "2 / 4", C["maroon"])
        + f'<div data-chk="myth" style="font-family: {DISPLAY}; font-weight: 800; font-size: 250px; line-height: 0.84; letter-spacing: -0.04em; color: {C["maroon"]}; margin-top: 30px">Myth.</div>'
        + body("Done right, tapping takes about 10% or less of a tree’s stored sugar, and only for a few weeks.", 50, C["maroon"], "answer", "; font-weight: 700; max-width: 930px; margin-top: 22px")
        + photo
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], stamp + column(inner, gap=30), C["maroon"]), "The answer: myth"


def rule(n, main, note=""):
    extra = f'<div style="font-weight: 500; font-size: 33px; margin-top: 6px">{note}</div>' if note else ""
    return (
        f'<div style="display: flex; gap: 24px; align-items: center">'
        f'<div style="width: 92px; height: 92px; border-radius: 50%; background: {C["maroon"]}; color: {C["cream"]}; flex: none; display: flex; '
        f'align-items: center; justify-content: center; font-family: {DISPLAY}; font-weight: 800; font-size: 48px">{n}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 46px; line-height: 1.1; color: {C["maroon"]}">{main}{extra}</div></div>'
    )


def slide3():
    card = (
        f'<div data-chk="rules" style="background: {C["cream"]}; border-radius: 36px; padding: 60px 52px; display: flex; flex-direction: column; gap: 60px">'
        + rule(1, "Only tap trees 12 in.+ across", "Measured 4½ ft above the ground")
        + rule(2, "Never more than 2 taps on a tree", "12–18 in.: 1 tap · Over 18 in. and healthy: up to 2")
        + rule(3, "Drill just 1½ in. deep", "Sapwood only, never the heartwood")
        + rule(4, "Move to a new spot each year", "A few inches to the side and about 12 in. above or below an old taphole")
        + "</div>"
    )
    inner = (
        kicker_row("The tree-friendly way", "3 / 4", C["maroon"])
        + headline("4 rules that keep<br>your tree healthy", 112, C["maroon"])
        + card
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["sky"], column(inner, gap=34), C["maroon"]), "4 rules that keep your tree healthy"


def rings_svg(size=380):
    import math, random
    random.seed(21)
    c = size / 2
    p = []
    R = size / 2 - 6
    # bark edge
    pts = []
    for i in range(72):
        a = 2 * math.pi * i / 72
        r = R * (1 + 0.025 * math.sin(5 * a) + random.uniform(-0.012, 0.012))
        pts.append(f"{c + r * math.cos(a):.1f} {c + r * math.sin(a):.1f}")
    p.append(f'<path d="M{" L".join(pts)} Z" fill="{C["bark"]}"></path>')
    rings = 14
    cols = ["#F3CF91", "#E9B872", "#F6DAA6", "#DFA65E"]
    for k in range(rings):
        rr = (R - 22) * (1 - k / rings)
        pts = []
        for i in range(60):
            a = 2 * math.pi * i / 60
            r = rr * (1 + 0.018 * math.sin(3 * a + k) + 0.01 * math.sin(7 * a))
            pts.append(f"{c + 6 + r * math.cos(a):.1f} {c - 4 + r * math.sin(a):.1f}")
        p.append(f'<path d="M{" L".join(pts)} Z" fill="{cols[k % 4]}" stroke="#C98E4B" style="stroke-width:1.6"></path>')
    p.append(f'<circle cx="{c + 6:.1f}" cy="{c - 4:.1f}" r="7" fill="#B9773A"></circle>')
    p.append(f'<path d="M{c + 6:.1f} {c - 4:.1f} L{c + R * 0.62:.1f} {c + R * 0.38:.1f}" fill="none" stroke="#B9773A" style="stroke-width:3;stroke-linecap:round"></path>')
    return (f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="display: block; flex: none">'
            + "".join(p) + "</svg>")


def slide4():
    teaser = (
        f'<div data-chk="teaser" style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 32px; padding: 30px 36px; display: flex; '
        f'flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Next up</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.04; letter-spacing: -0.01em">Tree ID: the red maple</div></div>'
    )
    inner = (
        kicker_row("The proof", "4 / 4", C["cream"])
        + f'<div data-chk="big" style="display: flex; align-items: baseline; gap: 22px; margin-top: 10px">'
        f'<span style="font-family: {DISPLAY}; font-weight: 800; font-size: 320px; line-height: 0.85; letter-spacing: -0.04em; color: {C["gold"]}">100+</span>'
        f'<span style="font-family: {DISPLAY}; font-weight: 800; font-size: 84px; line-height: 1; color: {C["cream"]}">years</span></div>'
        + f'<div data-chk="proofrow" style="display: flex; align-items: center; gap: 34px; margin-top: 8px">'
        + f'<div style="flex: 1 1 0; display: flex; flex-direction: column; gap: 24px">'
        + body("Some maple farms have tapped the same trees for over 100 years.", 54, C["cream"], "proof", "; font-weight: 700; line-height: 1.16")
        + body("Heard a maple myth? Drop it in the comments and we’ll bust it.", 36, C["gold"], "cta", "; font-weight: 600")
        + "</div>" + rings_svg(410) + "</div>"
        + '<div style="flex-grow: 1"></div>'
        + teaser
        + footer_row(C["cream"], f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; letter-spacing: 0; color: {C["cream"]}">mapletapper.com</span>')
    )
    return root(C["maroon"], column(inner, gap=30), C["cream"]), "The proof: 100+ years"


SLIDES = [("Post02-1-Cover", slide1), ("Post02-2-Answer", slide2), ("Post02-3-Rules", slide3), ("Post02-4-Proof", slide4)]


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
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
