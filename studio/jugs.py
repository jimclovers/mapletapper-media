"""Sap-to-syrup jug pictogram shared by the Tree ID posts."""
from build import C, DISPLAY, TYPE

SAP = "#BBDCF3"      # pale sap-blue
SAP_EDGE = "#5F8FB0"
SYRUP = "#E0902A"    # amber syrup
INK = C["maroon"]

# one jug drawn in a 40 x 50 box
JUG_BODY = "M9 15 Q9 11 13 11 H21 Q23 11 25 13 L31 19 Q33 21 33 24 V44 Q33 48 29 48 H13 Q9 48 9 44 Z"
JUG_CAP = (11, 5, 9, 6)          # x, y, w, h
JUG_HOLE = "M23 18 H28 V24 H23 Z"


def jug(x, y, s, fill, edge, hole_bg, stroke_w=1.6):
    """A jug at (x, y) scaled by s (1 = 40 x 50)."""
    cx, cy, cw, ch = JUG_CAP
    return (
        f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.3f})">'
        f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="1.6" fill="{edge}"></rect>'
        f'<path d="{JUG_BODY}" fill="{fill}" stroke="{edge}" style="stroke-width:{stroke_w}"></path>'
        f'<path d="{JUG_HOLE}" fill="{hole_bg}" stroke="{edge}" style="stroke-width:{stroke_w * 0.8}"></path></g>'
    )


def jug_grid_svg(n, cols=10, size=46, gap=8, bg="#FFF5DE"):
    rows = (n + cols - 1) // cols
    w = cols * size + (cols - 1) * gap
    h = rows * size * 1.25 + (rows - 1) * gap
    s = size / 40
    parts = []
    for i in range(n):
        r, c = divmod(i, cols)
        parts.append(jug(c * (size + gap), r * (size * 1.25 + gap), s, SAP, SAP_EDGE, bg))
    return (f'<svg aria-hidden="true" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" style="display: block; flex: none">'
            + "".join(parts) + "</svg>")


def syrup_jug_svg(size=112, bg="#FFF5DE"):
    s = size / 40
    w, h = size, size * 1.25
    return (f'<svg aria-hidden="true" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" style="display: block; flex: none">'
            + jug(0, 0, s, SYRUP, INK, bg, stroke_w=1.4) + "</svg>")


def arrow(size=46, col=INK):
    return (f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{col}" '
            f'style="stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round;flex: none"><path d="M3 12 H20"></path><path d="M14 6 L20 12 L14 18"></path></svg>')


def sap_card(name, pct, gallons, highlight=True, size=36, chk="sapcard"):
    """A cream card: tree name + sugar %, a grid of `gallons` sap jugs -> one jug of syrup."""
    bg = C["cream"] if highlight else "#FBEFD3"
    border = f"border: 5px solid {INK}" if highlight else "border: 5px solid transparent"
    name_col = INK
    return (
        f'<div data-chk="{chk}" style="background: {bg}; {border}; border-radius: 28px; padding: 18px 28px 16px; display: flex; flex-direction: column; gap: 10px">'
        f'<div style="display: flex; justify-content: space-between; align-items: center">'
        f'<span style="font-family: {DISPLAY}; font-weight: 800; font-size: 34px; color: {name_col}">{name}</span>'
        f'<span style="background: {C["gold"]}; color: {INK}; border-radius: 999px; padding: 8px 18px 7px; font-family: {DISPLAY}; '
        f'font-weight: 800; font-size: 26px">{pct} sugar</span></div>'
        f'<div style="display: flex; align-items: center; gap: 26px">'
        + jug_grid_svg(gallons, size=size, bg=bg)
        + arrow(58)
        + f'<div style="flex: 1 1 0; display: flex; justify-content: center">' + syrup_jug_svg(150, bg=bg) + '</div>'
        + "</div>"
        f'<div style="display: flex; justify-content: space-between; align-items: baseline; font-family: {DISPLAY}; color: {INK}">'
        f'<span style="font-weight: 700; font-size: 28px">About {gallons} gallons of sap</span>'
        f'<span style="font-weight: 800; font-size: 28px; color: {C["red_dk"]}">= 1 gallon of syrup</span></div></div>'
    )


def rule86_note(color=INK):
    return (
        f'<div data-chk="rule86" style="font-family: {TYPE}; font-size: 24px; line-height: 1.35; letter-spacing: 0.02em; color: {color}">'
        f'Sugarmaker’s Rule of 86: divide 86 by the sap’s sugar % to get the gallons of sap per gallon of syrup.</div>'
    )


def small_fact(kind, html):
    from build import icon_badge
    return (
        f'<div data-chk="sfact" style="display: flex; gap: 22px; align-items: center">{icon_badge(kind, 72)}'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 34px; line-height: 1.18; color: {INK}">{html}</div></div>'
    )
