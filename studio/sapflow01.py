"""Explainer - "Why does sap run?" (1 slide infographic + pin). Our own design and wording (inspired by a Boston Globe
graphic Jim liked, but nothing copied: different layout, art and text).
Facts checked against 2+ sources, Nov 7 2026:
  - Sap flow depends on temperature: freezing nights + days above freezing (best in the 40s): Massachusetts Maple Producers
    Assn (massmaple.org "How sugar maple trees work"); Northern Woodlands "Why does sap run?"; MapleTapper product copy.
  - As the wood freezes, gas-filled fiber cells draw sap in, it freezes on their walls and compresses the gas; this suction
    pulls water up from the roots (recharge): Milburn & O'Malley 1984 via UVM Proctor/Graf et al. (arXiv 2106.02802);
    MMPA; Northern Woodlands (Tyree, UVM Proctor).
  - On thaw, ice melts and compressed gas expands, pushing sap back into the vessels; with gravity, sap flows down and out
    the taphole: Saint John's Univ. biology lab (Tyree 2001); Northern Woodlands; MMPA.
  - Not root pressure / sap comes down from the stem (stump test): Northern Woodlands; D. Brynn (Addison Cty Forester);
    Saint John's Univ.
  - Flow stops when freeze-thaw cycles stop: MMPA; arXiv 2106.02802 (needs temps oscillating around freezing).
"""
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, W, H, ROOT, kicker_row, headline, body, root, preview_html  # noqa: E402

NAVY, ICE, SKY = "#1E3557", "#CFE6F5", "#9CC9E8"
M, CR, GOLD, RED = C["maroon"], C["cream"], C["gold"], C["red"]
BARK, BARK2 = "#6B4A33", "#4E3424"
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()


def tree_svg(mode, w=330, h=380):
    """Trunk + roots. mode 'night': arrows up from roots, ice specks. mode 'day': arrows down to a spout and bucket."""
    t = []
    # roots + trunk
    t.append(f'<path d="M135 40 L195 40 L200 300 Q230 330 290 345 L250 350 Q215 342 200 330 L205 355 L175 355 L165 330 Q140 345 95 352 '
             f'L60 348 Q120 330 130 300 Z" fill="{BARK}"></path>')
    t.append(f'<path d="M150 60 L152 290 M178 70 L180 300" stroke="{BARK2}" style="stroke-width:4;opacity:.5"></path>')
    if mode == "night":
        for y in (290, 225, 160, 95):
            t.append(f'<path d="M165 {y} L165 {y - 40} M152 {y - 26} L165 {y - 42} L178 {y - 26}" fill="none" stroke="{ICE}" '
                     f'style="stroke-width:7;stroke-linecap:round;stroke-linejoin:round"></path>')
        for x, y in ((140, 120), (188, 180), (142, 240), (190, 110), (186, 270), (145, 180)):
            t.append(f'<g transform="translate({x} {y})" stroke="#FFFFFF" style="stroke-width:2.5;stroke-linecap:round">'
                     f'<path d="M-7 0 L7 0 M0 -7 L0 7 M-5 -5 L5 5 M-5 5 L5 -5"></path></g>')
        for x, y in ((60, 368), (250, 370), (165, 372)):
            t.append(f'<path d="M{x} {y + 6} L{x} {y - 6} M{x - 6} {y} L{x} {y - 7} L{x + 6} {y}" fill="none" stroke="{SKY}" '
                     f'style="stroke-width:4;stroke-linecap:round"></path>')
    else:
        for y in (70, 135, 200):
            t.append(f'<path d="M165 {y} L165 {y + 40} M152 {y + 26} L165 {y + 42} L178 {y + 26}" fill="none" stroke="{CR}" '
                     f'style="stroke-width:7;stroke-linecap:round;stroke-linejoin:round"></path>')
        # spout + drop line into a bucket
        t.append(f'<rect x="196" y="236" width="34" height="12" rx="4" fill="#222"></rect>')
        t.append(f'<path d="M230 242 Q262 246 268 290" fill="none" stroke="#2F5FB3" style="stroke-width:8;stroke-linecap:round"></path>')
        t.append(f'<path d="M240 285 L300 285 L294 345 L246 345 Z" fill="#FFFFFF" stroke="{BARK2}" style="stroke-width:3"></path>')
        t.append(f'<path d="M268 296 q5 9 0 14 q-5 -5 0 -14" fill="{SKY}"></path>')
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 330 380">{"".join(t)}</svg>'


def thermo(label, warm):
    col = RED if warm else "#5AA7DE"
    fill = 70 if warm else 22
    svg = (f'<svg aria-hidden="true" width="34" height="86" viewBox="0 0 34 86"><rect x="11" y="4" width="12" height="62" rx="6" fill="#FFFFFF"></rect>'
           f'<rect x="14" y="{66 - fill * 0.8:.0f}" width="6" height="{fill * 0.8:.0f}" fill="{col}"></rect><circle cx="17" cy="70" r="12" fill="{col}"></circle></svg>')
    return (f'<div style="display: flex; align-items: center; gap: 10px">{svg}<span style="font-family: {TYPE}; font-size: 26px; '
            f'letter-spacing: 0.05em; text-transform: uppercase">{label}</span></div>')


def panel(mode):
    night = mode == "night"
    bg, fg, accent = (NAVY, CR, SKY) if night else (GOLD, M, M)
    num, title = ("1", "Cold night: it soaks up sap") if night else ("2", "Warm day: the sap runs out")
    text = ("As the wood freezes, tiny air-filled cells pull in sap and freeze it to their walls, squeezing the air inside. "
            "That suction draws water up from the roots, like a sponge soaking up a spill."
            if night else
            "The ice melts and the squeezed air springs back. With a push from that air and from gravity, "
            "sap runs down the trunk and out the taphole.")
    badge = (f'<div style="width: 64px; height: 64px; border-radius: 50%; background: {accent}; color: {bg}; display: flex; '
             f'align-items: center; justify-content: center; font-family: {DISPLAY}; font-weight: 800; font-size: 38px; flex: none">{num}</div>')
    art = tree_svg(mode, 260, 299)
    copy = (f'<div style="display: flex; flex-direction: column; gap: 14px; flex: 1 1 0">'
            f'{thermo("Below 32°F" if night else "Above 32°F · best in the 40s", not night)}'
            f'<div style="display: flex; gap: 16px; align-items: center">{badge}<div style="font-family: {DISPLAY}; font-weight: 800; '
            f'font-size: 40px; line-height: 1.02; letter-spacing: -0.01em">{title}</div></div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 29px; line-height: 1.26">{text}</div></div>')
    sky = ""
    if night:
        sky = (f'<svg aria-hidden="true" width="70" height="70" viewBox="0 0 70 70" style="position: absolute; right: 36px; top: 24px">'
               f'<path d="M48 8 A28 28 0 1 0 62 52 A22 22 0 1 1 48 8 Z" fill="{CR}"></path></svg>')
    else:
        rays = "".join(f'<path d="M35 35 L{35 + 30 * __import__("math").cos(a * 0.7854):.1f} {35 + 30 * __import__("math").sin(a * 0.7854):.1f}" '
                       f'stroke="{RED}" style="stroke-width:5;stroke-linecap:round"></path>' for a in range(8))
        sky = (f'<svg aria-hidden="true" width="70" height="70" viewBox="0 0 70 70" style="position: absolute; right: 36px; top: 24px">'
               f'{rays}<circle cx="35" cy="35" r="15" fill="{RED}"></circle></svg>')
    return (f'<div data-chk="panel-{mode}" style="position: relative; background: {bg}; color: {fg}; border-radius: 34px; padding: 20px 28px 18px 14px; '
            f'display: flex; align-items: center; gap: 18px">{sky}<div style="flex: none">{art}</div>{copy}</div>')


def slide():
    head = (kicker_row("Sugarmaker’s Almanac · How it works", "16 weeks to sap season", M)
            + headline(f'Why does <span style="color: {RED}">sap run?</span>', 92, M)
            + body("It all comes down to freezing nights and thawing days.", 34, M, "sub", "; font-weight: 700"))
    repeat = (f'<div data-chk="repeat" style="display: flex; align-items: center; gap: 24px">'
              f'<div style="flex: 1 1 0; background: {M}; color: {CR}; border-radius: 30px; padding: 22px 30px; display: flex; flex-direction: column; gap: 6px">'
              f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase; color: {GOLD}">3 · Repeat</div>'
              f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 29px; line-height: 1.2">Every freeze refills the tree and every thaw '
              f'lets it run. When the nights stop freezing, sap season is over.</div></div>'
              f'<img src="{LOGO}" alt="MapleTapper logo, www.mapletapper.com" style="width: 175px; flex: none; display: block"></div>')
    src = (f'<div data-chk="src" style="font-family: {TYPE}; font-size: 19px; line-height: 1.3; color: {M}; opacity: 0.85">Sources: Massachusetts Maple '
           f'Producers Assn.; UVM Proctor Maple Research Center; Northern Woodlands.</div>')
    inner = head + panel("night") + panel("day") + repeat + src
    col = (f'<div style="position: relative; z-index: 1; box-sizing: border-box; width: {W}px; height: {H}px; padding: 44px 48px 30px; '
           f'display: flex; flex-direction: column; gap: 26px">{inner}</div>')
    return root(CR, col, M), "Why does sap run?"


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    markup, title = slide()
    open(os.path.join(ROOT, "preview", "SapFlow01.html"), "w").write(preview_html(title, markup))
    print("built")
