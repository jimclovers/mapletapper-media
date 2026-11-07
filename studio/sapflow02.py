"""Explainer v2 - "What makes sap run?" Full-tree diagram split night | day, with a person checking the sap bucket.
Our own drawing and wording (Jim liked the layout idea of a Boston Globe graphic; nothing copied).
Facts checked against 2+ sources, Nov 7 2026:
  - Best runs: nights in the 20s F, days in the 40s: UMaine Extension (K. Hopkins: days 40-45, nights mid-20s);
    SDSU Extension P-00326 (nights 25-30, days above 40); UW-Madison SSEC (nights in the 20s, days in the 40s).
  - Freeze: gas-filled wood cells take in sap that freezes on their walls, compressing the gas; suction pulls water up
    from the roots: MMPA (massmaple.org); Northern Woodlands (Tyree, UVM Proctor); arXiv 2106.02802 (UVM Proctor).
  - Thaw: ice melts, compressed gas expands, pressure + gravity push sap down and out the taphole: Saint John's Univ.
    biology lab (Tyree 2001); Northern Woodlands; MMPA.
  - Runs stop when freeze-thaw cycles stop (nights and days both above freezing): SDSU Extension; MMPA.
"""
import base64
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, W, H, ROOT, root, preview_html  # noqa: E402

M, CR, GOLD, RED = C["maroon"], C["cream"], C["gold"], C["red"]
NAVY, NIGHT2, DAY, DAY2 = "#1B2F50", "#24406A", "#BFE0F4", "#E3F2FB"
BARK, BARK_D, BARK_N = "#7A5236", "#5A3B26", "#3C3550"
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()
SY, SH = 230, 960          # scene top and height


def arrow(x, y, up, color, size=46):
    d = -1 if up else 1
    return (f'<path d="M{x} {y - d * size / 2} L{x} {y + d * size / 2} M{x - 13} {y + d * (size / 2 - 15)} L{x} {y + d * size / 2} '
            f'L{x + 13} {y + d * (size / 2 - 15)}" fill="none" stroke="{color}" style="stroke-width:8;stroke-linecap:round;stroke-linejoin:round"></path>')


def scene_svg():
    s = []
    s.append(f'<rect x="0" y="0" width="540" height="{SH}" fill="{NAVY}"></rect>')
    s.append(f'<rect x="540" y="0" width="540" height="{SH}" fill="{DAY}"></rect>')
    # stars + moon / sun
    for x, y, r in ((70, 60, 3), (160, 30, 2), (250, 90, 2.5), (330, 40, 2), (420, 110, 3), (110, 150, 2), (470, 30, 2)):
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF"></circle>')
    # ground (snow) with the split
    s.append(f'<path d="M0 760 Q270 730 540 745 L540 {SH} L0 {SH} Z" fill="#DDE6F2"></path>')
    s.append(f'<path d="M540 745 Q810 735 1080 760 L1080 {SH} L540 {SH} Z" fill="#FFFFFF"></path>')
    # crown: bare branches (drawn once, night half tinted later via clip)
    br = []
    def limb(x1, y1, x2, y2, w):
        br.append(f'<path d="M{x1} {y1} Q{(x1 + x2) / 2 + (x2 - x1) * 0.1} {(y1 + y2) / 2 - 20} {x2} {y2}" fill="none" '
                  f'style="stroke-width:{w};stroke-linecap:round"></path>')
    limb(540, 300, 380, 120, 26); limb(540, 300, 700, 110, 26); limb(540, 260, 540, 20, 24)
    limb(450, 200, 330, 190, 12); limb(410, 150, 400, 40, 10); limb(630, 190, 770, 200, 12); limb(670, 140, 690, 30, 10)
    limb(540, 120, 470, 50, 9); limb(540, 120, 610, 40, 9); limb(380, 120, 300, 90, 8); limb(700, 110, 790, 80, 8)
    limb(540, 340, 300, 290, 14); limb(540, 340, 790, 280, 14)
    branches = "".join(br)
    trunk = (f'<path d="M512 230 Q540 210 568 230 L585 330 L600 700 Q640 760 720 780 L660 786 Q615 778 598 760 L606 800 L474 800 L482 760 '
             f'Q465 778 420 786 L360 780 Q440 760 480 700 L495 330 Z"></path>')
    s.append('<defs><clipPath id="L"><rect x="0" y="0" width="540" height="960"></rect></clipPath>'
             '<clipPath id="R"><rect x="540" y="0" width="540" height="960"></rect></clipPath></defs>')
    s.append(f'<g clip-path="url(#R)" stroke="{BARK}" fill="{BARK}">{branches}{trunk}</g>')
    s.append(f'<g clip-path="url(#L)" stroke="{BARK_N}" fill="{BARK_N}">{branches}{trunk}</g>')
    # bark texture lines
    for x in (505, 525, 560, 578):
        s.append(f'<path d="M{x} 320 L{x + 2} 760" stroke="#000" style="stroke-width:3;opacity:.12"></path>')
    # roots underground + water dots
    for d in ("M500 800 Q440 840 360 870", "M540 800 Q545 860 530 920", "M580 800 Q640 840 720 870"):
        s.append(f'<path d="{d}" fill="none" stroke="#8C6A52" style="stroke-width:12;stroke-linecap:round;opacity:.8"></path>')
    for x, y in ((380, 900), (420, 880), (470, 905), (350, 860), (440, 925), (500, 935)):
        s.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#6FB3E6"></circle>')
    # arrows: up on the night half, down on the day half
    for y in (700, 600, 500, 400):
        s.append(arrow(515, y, True, "#CFE8FA"))
    for y in (380, 470, 560):
        s.append(arrow(565, y, False, "#FFF5DE"))
    # spout + hanging bucket on the day side
    s.append(f'<rect x="596" y="612" width="34" height="11" rx="3" fill="#2A2A2A"></rect>')
    s.append(f'<path d="M612 626 L606 696 L668 696 L662 626 Z" fill="#B9C3CC" stroke="#7D8A96" style="stroke-width:3"></path>')
    s.append(f'<path d="M608 626 L666 626" stroke="#7D8A96" style="stroke-width:5"></path>')
    s.append(f'<path d="M624 616 q4 8 0 12 q-4 -4 0 -12" fill="#7FC0EC"></path>')
    # person (flat drawing) checking the bucket: winter coat, knit hat, boots
    p = 715
    s.append(f'<ellipse cx="{p + 45}" cy="868" rx="85" ry="10" fill="#000" opacity=".08"></ellipse>')
    s.append(f'<rect x="{p + 20}" y="760" width="26" height="100" rx="10" fill="#2E3A4E"></rect>')
    s.append(f'<rect x="{p + 52}" y="760" width="26" height="100" rx="10" fill="#26303F"></rect>')
    s.append(f'<path d="M{p + 12} 860 h40 v14 h-46 z M{p + 48} 860 h40 v14 h-44 z" fill="#3B2A1E"></path>')
    s.append(f'<path d="M{p + 8} 640 Q{p + 48} 618 {p + 90} 640 L{p + 96} 775 L{p + 2} 775 Z" fill="{RED}"></path>')
    s.append(f'<path d="M{p + 48} 640 L{p + 48} 775" stroke="#9E2617" style="stroke-width:3"></path>')
    s.append(f'<path d="M{p + 14} 660 Q{p - 30} 668 {p - 50} 690" fill="none" stroke="{RED}" style="stroke-width:24;stroke-linecap:round"></path>')
    s.append(f'<circle cx="{p - 52}" cy="692" r="12" fill="#3B2A1E"></circle>')
    s.append(f'<circle cx="{p + 48}" cy="602" r="32" fill="#E8B58F"></circle>')
    s.append(f'<path d="M{p + 15} 598 Q{p + 48} 545 {p + 81} 598 Z" fill="{GOLD}"></path>')
    s.append(f'<rect x="{p + 13}" y="590" width="70" height="14" rx="6" fill="{M}"></rect>')
    s.append(f'<circle cx="{p + 48}" cy="560" r="9" fill="{M}"></circle>')
    s.append(f'<path d="M{p + 18} 618 q30 18 60 0" fill="none" stroke="{GOLD}" style="stroke-width:12"></path>')
    # center split line
    s.append(f'<path d="M540 0 L540 {SH}" stroke="#FFFFFF" style="stroke-width:3;opacity:.55" stroke-dasharray="10 10"></path>')
    return f'<svg aria-hidden="true" width="{W}" height="{SH}" viewBox="0 0 {W} {SH}" style="position: absolute; left: 0; top: {SY}px">{"".join(s)}</svg>'


def thermo(warm):
    col = RED if warm else "#6FB3E6"
    h = 44 if warm else 18
    return (f'<svg aria-hidden="true" width="30" height="78" viewBox="0 0 30 78"><rect x="9" y="3" width="12" height="58" rx="6" fill="#FFFFFF" '
            f'stroke="#9AA" style="stroke-width:1.5"></rect><rect x="12" y="{58 - h}" width="6" height="{h}" fill="{col}"></rect>'
            f'<circle cx="15" cy="64" r="11" fill="{col}"></circle></svg>')


def label(x, y, text, color, size=26, align="left", w=380):
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; text-align: {align}; font-family: {DISPLAY}; '
            f'font-weight: 600; font-size: {size}px; line-height: 1.25; color: {color}">{text}</div>')


def step(n, text, color, numbg, numfg):
    return (f'<div style="display: flex; gap: 12px; align-items: flex-start"><span style="flex: none; width: 40px; height: 40px; border-radius: 50%; '
            f'background: {numbg}; color: {numfg}; display: flex; align-items: center; justify-content: center; font-family: {DISPLAY}; font-weight: 800; '
            f'font-size: 26px; margin-top: 2px">{n}</span><span style="font-family: {DISPLAY}; font-weight: 600; font-size: 27px; line-height: 1.27; '
            f'color: {color}">{text}</span></div>')


def slide():
    head = (f'<div data-chk="head" style="position: absolute; left: 48px; right: 48px; top: 40px">'
            f'<div style="display: flex; justify-content: space-between; font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; '
            f'text-transform: uppercase; color: {M}"><span>Sugarmaker’s Almanac · How it works</span><span>@mapletapper</span></div>'
            f'<h1 style="margin: 14px 0 0; font-family: {DISPLAY}; font-weight: 800; font-size: 86px; line-height: 0.95; letter-spacing: -0.025em; color: {M}">'
            f'What makes <span style="color: {RED}">sap run?</span></h1>'
            f'<div style="margin-top: 12px; font-family: {DISPLAY}; font-weight: 700; font-size: 30px; color: {M}">Freezing nights + thawing days. Here’s what happens inside the tree.</div></div>')
    night_head = (f'<div data-chk="nh" style="position: absolute; left: 40px; top: {SY + 26}px; display: flex; align-items: center; gap: 12px">{thermo(False)}'
                  f'<div><div style="font-family: {DISPLAY}; font-weight: 800; font-size: 50px; line-height: 1; color: #FFFFFF">NIGHT</div>'
                  f'<div style="font-family: {TYPE}; font-size: 25px; color: #CFE8FA; margin-top: 4px">In the 20s °F</div></div></div>')
    day_head = (f'<div data-chk="dh" style="position: absolute; right: 40px; top: {SY + 26}px; display: flex; align-items: center; gap: 12px">'
                f'<div style="text-align: right"><div style="font-family: {DISPLAY}; font-weight: 800; font-size: 50px; line-height: 1; color: {NAVY}">DAY</div>'
                f'<div style="font-family: {TYPE}; font-size: 25px; color: {NAVY}; margin-top: 4px">In the 40s °F</div></div>{thermo(True)}</div>')
    left = (f'<div data-chk="left" style="position: absolute; left: 34px; top: {SY + 400}px; width: 400px; display: flex; flex-direction: column; gap: 22px">'
            + step(1, "As the tree freezes, tiny air pockets in the wood get squeezed by ice. That makes suction.", "#FFFFFF", "#CFE8FA", NAVY)
            + step(2, "The suction pulls water up from the roots and refills the tree, like a sponge.", "#FFFFFF", "#CFE8FA", NAVY)
            + "</div>")
    right = (f'<div data-chk="right" style="position: absolute; right: 30px; top: {SY + 140}px; width: 400px; display: flex; flex-direction: column; gap: 18px; background: rgba(255,255,255,0.88); border-radius: 22px; padding: 18px 20px; box-sizing: border-box">'
             + step(3, "As the tree warms up, the ice melts and the squeezed air pushes back. With help from gravity, sap flows down and out the spout.", NAVY, NAVY, "#FFFFFF")
             + "</div>")
    tags = (label(318, SY + 905, "Roots", NAVY, 24, "left", 120)
            + label(132, SY + 838, "Water from the soil", NAVY, 22, "left", 200)
            + label(640, SY + 560, "Spout", NAVY, 24, "left", 120))
    sunmoon = (f'<svg aria-hidden="true" width="64" height="64" viewBox="0 0 64 64" style="position: absolute; left: 330px; top: {SY + 30}px">'
               f'<path d="M44 6 A26 26 0 1 0 58 48 A20 20 0 1 1 44 6 Z" fill="{CR}"></path></svg>'
               f'<svg aria-hidden="true" width="80" height="80" viewBox="0 0 80 80" style="position: absolute; left: 700px; top: {SY + 18}px">'
               + "".join(f'<path d="M40 40 L{40 + 34 * math.cos(a * math.pi / 6):.1f} {40 + 34 * math.sin(a * math.pi / 6):.1f}" stroke="{GOLD}" '
                         f'style="stroke-width:5;stroke-linecap:round"></path>' for a in range(12))
               + f'<circle cx="40" cy="40" r="18" fill="{GOLD}"></circle></svg>')
    bottom = (f'<div data-chk="bottom" style="position: absolute; left: 0; top: {SY + SH}px; width: {W}px; height: {H - SY - SH}px; background: {M}; '
              f'box-sizing: border-box; padding: 18px 36px 14px 48px; display: flex; align-items: center; gap: 24px">'
              f'<div style="flex: 1 1 0; color: {CR}"><div style="font-family: {DISPLAY}; font-weight: 800; font-size: 36px; line-height: 1.1">'
              f'Freeze, thaw, repeat. <span style="color: {GOLD}">The sap keeps running.</span></div>'
              f'<div style="font-family: {TYPE}; font-size: 17px; margin-top: 8px; opacity: 0.85">Sources: Massachusetts Maple Producers Assn.; UVM Proctor Maple '
              f'Research Center; UMaine and SDSU Extension</div></div>'
              f'<div style="flex: none; background: {CR}; border-radius: 20px; padding: 6px 10px"><img src="{LOGO}" alt="MapleTapper logo, www.mapletapper.com" '
              f'style="width: 112px; display: block"></div></div>')
    inner = head + scene_svg() + sunmoon + night_head + day_head + left + right + tags + bottom
    return root(CR, inner, M), "What makes sap run?"


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    markup, title = slide()
    open(os.path.join(ROOT, "preview", "SapFlow02.html"), "w").write(preview_html(title, markup))
    print("built")
