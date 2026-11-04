"""Post 06 - Myth or fact: "Too warm now for Midwest sugar maples?" (6 slides). Jim's question, Nov 4 2026.
Photo: Jim's real sugar maple (photos/jim/sugar_tree_real.jpg). Facts checked against 2+ sources, Nov 4 2026:
  - season shifting earlier at the southern edge: Cincinnati Parks naturalist Olivia Canada ("Changing the Flow"): was
    February into mid-March, now late December/January to mid-February; ~20 years teaching sugaring. Ohio State
    alumni magazine: Ohio on the southern edge, will see the first impacts (Ohio Maple Syrup Producers Assn treasurer)
  - Rapp et al. 2019, Forest Ecology and Management 448 (USGS pubs page), RCP 8.5, by 2100: season midpoint ~1 month
    earlier; sap sugar -0.7 Brix; max sap-flow region ~400 km (~250 mi) north, from near 43 N to near 48 N; US yields
    down, Canada flat to up (also Dartmouth release; NECASC abstract)
  - Houle & Duchesne (Quebec MFFP; Forest Ecology and Management 458): yields stable across a broad latitude and
    temperature gradient; say the 2019 projection is flawed
  - USDA Forest Service Climate Change Tree Atlas v4, sugar maple: widely distributed and dense across much of the
    northern 2/3 of the eastern US; modeled to decline only modestly (earlier models showed more); very good capacity
    to cope; drought or other stress could still cause decline
  - Ohio State tested red x silver maple hybrids ("rilvers") alongside sugar maples (Ohio State alumni magazine)
  - city latitudes: Madison 43.07 N, Milwaukee 43.04 N, Thunder Bay 48.38 N, International Falls 48.60 N
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from art import SUGAR, leaf_path  # noqa: E402
from build import DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column  # noqa: E402
from funfacts import teaser, site_footer  # noqa: E402
from wk2 import (M, CR, RED, GOLD, GREEN, SPACER, stamp, cover, circle_badge, check_mark, x_mark, row,  # noqa: E402
                 build_preview)

ASSETS = {"cover": "jim/sugar_tree_real.jpg"}


def src_line(text, color):
    return (f'<div data-chk="src" style="font-family: {TYPE}; font-size: 22px; line-height: 1.35; color: {color}">{text}</div>')


def season_svg():
    """Dec 1 - Mar 31 axis; then: Feb 1 - Mar 15; now: late Dec/Jan - Feb 15 (soft start)."""
    w, h = 936, 380
    x0, x1, days = 20, 916, 121
    X = lambda d: x0 + (x1 - x0) * d / days
    p = [
        f'<defs><linearGradient id="fadein" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{GOLD}" stop-opacity="0.12"></stop>'
        f'<stop offset="1" stop-color="{GOLD}" stop-opacity="1"></stop></linearGradient></defs>',
    ]
    lab = lambda x, y, t, size=24, col=CR, anchor="start", font=TYPE, weight=400: (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-family: {font}; font-size: {size}px; font-weight: {weight}; '
        f'letter-spacing: 0.03em; fill: {col}">{t}</text>')
    for d in (0, 31, 62, 90):
        p.append(f'<path d="M{X(d):.1f} 20 V320" stroke="{CR}" style="stroke-width:2;stroke-opacity:0.25;stroke-dasharray:4 6"></path>')
    for d0, d1, name in [(0, 31, "DEC"), (31, 62, "JAN"), (62, 90, "FEB"), (90, 121, "MAR")]:
        p.append(lab((X(d0) + X(d1)) / 2, 366, name, 30, CR, "middle"))
    p.append(f'<path d="M{x0} 330 H{x1}" stroke="{CR}" style="stroke-width:3"></path>')
    p.append(lab(X(62), 48, "WHEN SHE STARTED", 26, GOLD))
    p.append(f'<rect x="{X(62):.1f}" y="62" width="{X(104) - X(62):.1f}" height="78" rx="39" fill="{CR}"></rect>')
    p.append(lab((X(62) + X(104)) / 2, 113, "Feb to mid-Mar", 34, M, "middle", DISPLAY, 800))
    p.append(lab(X(24), 196, "NOW", 26, GOLD))
    p.append(f'<rect x="{X(22):.1f}" y="210" width="{X(41) - X(22):.1f}" height="78" fill="url(#fadein)"></rect>')
    p.append(f'<rect x="{X(40):.1f}" y="210" width="{X(76) - X(40):.1f}" height="78" rx="39" fill="{GOLD}"></rect>')
    p.append(f'<rect x="{X(40):.1f}" y="210" width="44" height="78" fill="{GOLD}"></rect>')
    p.append(lab((X(22) + X(76)) / 2 + 8, 260, "Dec or Jan to mid-Feb", 30, M, "middle", DISPLAY, 800))
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block">{"".join(p)}</svg>'


def latitude_svg():
    w, h = 936, 330
    p = []
    lab = lambda x, y, t, size, col, font=DISPLAY, weight=800, anchor="start": (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-family: {font}; font-size: {size}px; font-weight: {weight}; fill: {col}">{t}</text>')
    for y, col in [(70, RED), (260, GREEN)]:
        p.append(f'<path d="M0 {y} H{w}" stroke="{col}" style="stroke-width:6;stroke-linecap:round"></path>')
    p.append(f'<rect x="0" y="40" width="132" height="60" rx="30" fill="{RED}"></rect>' + lab(66, 82, "48°N", 32, CR, anchor="middle"))
    p.append(f'<rect x="0" y="230" width="132" height="60" rx="30" fill="{GREEN}"></rect>' + lab(66, 272, "43°N", 32, CR, anchor="middle"))
    p.append(lab(156, 52, "By 2100 (projected)", 32, M))
    p.append(lab(156, 128, "Near Thunder Bay and International Falls", 27, M, DISPLAY, 500))
    p.append(lab(156, 242, "Best sap flow today", 32, M))
    p.append(lab(156, 318, "Near Madison and Milwaukee", 27, M, DISPLAY, 500))
    ax = 870
    p.append(f'<path d="M{ax} 238 V100 M{ax - 22} 122 L{ax} 98 L{ax + 22} 122" fill="none" stroke="{M}" '
             f'style="stroke-width:6;stroke-linecap:round;stroke-linejoin:round"></path>')
    p.append(lab(ax - 22, 180, "about 250 miles", 28, M, TYPE, 400, "end"))
    return f'<svg aria-hidden="true" width="876" height="{h * 876 / w:.0f}" viewBox="0 0 {w} {h}" style="display: block">{"".join(p)}</svg>'


def small_icon(kind, color):
    s = f'fill="none" stroke="{color}" style="stroke-width:5;stroke-linecap:round;stroke-linejoin:round"'
    if kind == "cal":
        return (f'<rect x="14" y="18" width="52" height="48" rx="8" {s}></rect><path d="M14 32 H66 M28 12 V24 M52 12 V24" {s}></path>'
                f'<path d="M30 46 L37 53 L51 40" {s}></path>')
    if kind == "drop":
        return f'<path d="M40 12 C40 12 20 38 20 50 A20 20 0 0 0 60 50 C60 38 40 12 40 12 Z" {s}></path><path d="M30 52 L50 52" {s}></path>'
    if kind == "up":
        return f'<path d="M40 66 V16 M22 34 L40 16 L58 34" {s}></path>'
    if kind == "leaf":
        return (f'<svg x="8" y="6" width="64" height="68" viewBox="0 0 24 24"><path d="{leaf_path(SUGAR, 10.5, 12, 15.5)}" '
                f'fill="{color}"></path></svg>')
    if kind == "heart":
        return (f'<path d="M40 64 C18 48 14 38 14 30 A13 13 0 0 1 40 24 A13 13 0 0 1 66 30 C66 38 62 48 40 64 Z" {s}></path>')
    return ""


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover(
        "cover", "A sugar maple in bright orange and red fall color in a Midwest park", "Sugarmaker’s Almanac · No. 06",
        stamp("MYTH", "or fact?"),
        "Too warm now for<br>Midwest sugar maples?",
        "We checked the research. Swipe!",
        title_size=86, obj_pos="50% 45%",
    )
    return root(M, inner, CR), "Too warm now for Midwest sugar maples?"


def slide2():
    yes = circle_badge(check_mark(CR), GREEN, size=104, ring="#4E7A40")
    no = circle_badge(x_mark(CR), RED, size=104, ring="#A82A1A")
    block = lambda badge, tag, title, note, chk: (
        f'<div data-chk="{chk}" style="display: flex; gap: 26px; align-items: flex-start">{badge}<div style="display: flex; flex-direction: column; gap: 6px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase; color: {M}">{tag}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.03; color: {M}">{title}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 31px; line-height: 1.24; color: {M}">{note}</div></div></div>'
    )
    inner = (
        kicker_row("Myth or fact · The answer", "2 / 6", M)
        + headline(f'Partly<br><span style="color: {RED}">true.</span>', 150, M)
        + SPACER
        + block(yes, "True", "The sap season is starting earlier.",
                "At the southern edge of maple country, sap now runs weeks earlier than it used to.", "true")
        + block(no, "Not true (yet)", "Sugar maples aren’t leaving the Midwest.",
                "They’re still common across most of the eastern US, and newer Forest Service models project only a modest decline.", "nottrue")
        + SPACER
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=34), M), "Partly true"


def slide3():
    inner = (
        kicker_row("Myth or fact · Happening now", "3 / 6", CR)
        + headline(f'Earlier sap,<br><span style="color: {GOLD}">already.</span>', 110, CR)
        + body("A Cincinnati Parks naturalist who has taught maple sugaring for almost 20 years has watched her season move:", 33, CR, "lead")
        + SPACER
        + f'<div data-chk="season">{season_svg()}</div>'
        + SPACER
        + f'<div data-chk="tip" style="align-self: flex-start; background: {GOLD}; color: {M}; border-radius: 999px; padding: 14px 30px 12px; '
          f'font-family: {DISPLAY}; font-weight: 800; font-size: 31px">Tip: tap by the forecast, not the calendar</div>'
        + src_line("Source: Cincinnati Parks, “Changing the Flow”", GOLD)
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=28), CR), "Earlier sap, already"


def slide4():
    pts = [
        ("cal", "The season comes about a month earlier"),
        ("drop", "Sap gets a little less sweet"),
    ]
    rows = "".join(
        f'<div style="display: flex; gap: 20px; align-items: center"><svg aria-hidden="true" width="58" height="58" viewBox="0 0 80 80" '
        f'style="flex: none">{small_icon(k, RED)}</svg><span style="font-family: {DISPLAY}; font-weight: 700; font-size: 36px; '
        f'line-height: 1.12; color: {M}">{t}</span></div>' for k, t in pts
    )
    inner = (
        kicker_row("Myth or fact · By 2100?", "4 / 6", M)
        + headline(f'What one study<br><span style="color: {RED}">projects.</span>', 100, M)
        + body("If emissions stay high, a 2019 study projects that by 2100:", 33, M, "lead")
        + f'<div data-chk="pts" style="display: flex; flex-direction: column; gap: 16px">{rows}</div>'
        + SPACER
        + f'<div data-chk="lat" style="background: #FFFFFF; border-radius: 30px; padding: 26px 30px 18px; display: flex; flex-direction: column; gap: 10px">'
          f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 36px; line-height: 1.1; color: {M}">The best sap-flow zone moves north</div>'
          f'{latitude_svg()}</div>'
        + SPACER
        + src_line("Source: Rapp et al. 2019, Forest Ecology and Management", RED)
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=24), M), "What one study projects"


def slide5():
    card = lambda who, text, chk: (
        f'<div data-chk="{chk}" style="background: {CR}; border-radius: 30px; padding: 30px 34px; display: flex; flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase; color: {RED}">{who}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 37px; line-height: 1.16; color: {M}">{text}</div></div>'
    )
    inner = (
        kicker_row("Myth or fact · Second opinions", "5 / 6", CR)
        + headline(f'Not everyone<br><span style="color: {GOLD}">agrees.</span>', 120, CR)
        + SPACER
        + card("Quebec government scientists", "Syrup yields hold steady across a wide range of climates, they found. "
               "They say the 2019 projection is flawed.", "c1")
        + card("US Forest Service", "Its tree atlas projects only a modest decline in sugar maple habitat, "
               "and rates the tree’s ability to cope as very good.", "c2")
        + SPACER
        + body(f'<b style="color: {GOLD}">Bottom line:</b> seasons are shifting now, and the trees are expected to cope better than older forecasts said.',
               34, CR, "bottom")
        + src_line("Sources: Houle &amp; Duchesne, Quebec MFFP; USDA Forest Service Climate Change Tree Atlas", GOLD)
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=28), CR), "Not everyone agrees"


def slide6():
    tips = [
        ("cal", "Tap by the forecast", "Start when thawing days follow freezing nights, not on a set date."),
        ("leaf", "Red and silver maples count too", "Ohio State is testing red-silver hybrids as a backup."),
        ("heart", "Keep your trees healthy", "Drought and other stress hit trees hardest."),
    ]
    rows = "".join(row(circle_badge(small_icon(k, CR), RED, size=100, ring="#A82A1A"), t, n, M, 42, 30) for k, t, n in tips)
    inner = (
        kicker_row("Myth or fact · Your backyard", "6 / 6", M)
        + headline(f'What it means<br><span style="color: {RED}">for you.</span>', 108, M)
        + SPACER
        + f'<div data-chk="rows" style="display: flex; flex-direction: column; gap: 28px">{rows}</div>'
        + SPACER
        + teaser("Thursday", "Kids Corner: measure your tree!", GOLD, M)
        + site_footer(M)
    )
    return root(CR, column(inner, gap=28), M), "What it means for you"


SLIDES = [("Post06-1-Cover", slide1), ("Post06-2-Answer", slide2), ("Post06-3-Now", slide3), ("Post06-4-2100", slide4),
          ("Post06-5-Disagree", slide5), ("Post06-6-You", slide6)]

if __name__ == "__main__":
    for p in build_preview(SLIDES, ASSETS):
        print(p)
