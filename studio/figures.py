"""Shared flat-drawn figures for the sap-flow graphic and Reel.
Both stand at x=p..p+100 (feet at y~874), facing the bucket on their left,
with the near arm reaching to the bucket at about (p-52, 692)."""

RED_ = "#C8321F"

PLAID = ('<pattern id="plaid" width="36" height="36" patternUnits="userSpaceOnUse">'
         '<rect width="36" height="36" fill="#B8281A"></rect>'
         '<rect x="0" y="0" width="36" height="18" fill="#1A1A1A" opacity=".55"></rect>'
         '<rect x="0" y="0" width="18" height="36" fill="#1A1A1A" opacity=".55"></rect>'
         '<path d="M27 0 V36 M0 27 H36" stroke="#1A1A1A" style="stroke-width:2;opacity:.35"></path></pattern>')


def sugarmaker(p=715):
    PL, PANTS, BOOT, SKIN, BEARD, GLOVE = "url(#plaid)", "#5B4636", "#3B2A1E", "#E8B58F", "#7A5A40", "#6B4A2E"
    return (f'<defs>{PLAID}</defs>'
            f'<ellipse cx="{p + 45}" cy="874" rx="90" ry="10" fill="#000" opacity=".08"></ellipse>'
            # legs + boots
            f'<rect x="{p + 20}" y="760" width="27" height="100" rx="8" fill="{PANTS}"></rect>'
            f'<rect x="{p + 52}" y="760" width="27" height="100" rx="8" fill="#4E3B2D"></rect>'
            f'<path d="M{p + 10} 846 h40 v24 h-46 z M{p + 50} 846 h40 v24 h-44 z" fill="{BOOT}"></path>'
            f'<path d="M{p + 4} 868 h46 M{p + 46} 868 h44" stroke="#22170F" style="stroke-width:6"></path>'
            # far arm, hanging, with glove
            f'<path d="M{p + 86} 656 Q{p + 108} 700 {p + 104} 750" fill="none" stroke="{PL}" style="stroke-width:26;stroke-linecap:round"></path>'
            f'<path d="M{p + 86} 656 Q{p + 108} 700 {p + 104} 750" fill="none" stroke="#1A1A1A" style="stroke-width:26;stroke-linecap:round;opacity:.18"></path>'
            f'<circle cx="{p + 104}" cy="760" r="13" fill="{GLOVE}"></circle>'
            # plaid coat
            f'<path d="M{p + 4} 640 Q{p + 48} 616 {p + 94} 640 L{p + 102} 784 L{p - 4} 784 Z" fill="{PL}"></path>'
            f'<path d="M{p + 4} 640 Q{p + 48} 616 {p + 94} 640 L{p + 102} 784 L{p - 4} 784 Z" fill="none" stroke="#5E140C" style="stroke-width:3"></path>'
            f'<path d="M{p + 48} 646 L{p + 48} 784" stroke="#2A0C08" style="stroke-width:4"></path>'
            + "".join(f'<circle cx="{p + 56}" cy="{y}" r="4.5" fill="#2A1A10"></circle>' for y in (672, 706, 740))
            + f'<path d="M{p + 24} 630 L{p + 48} 662 L{p + 72} 630" fill="#7A1E1A" stroke="#5E140C" style="stroke-width:3;stroke-linejoin:round"></path>'
            # near arm reaching to the bucket, with glove
            f'<path d="M{p + 14} 662 Q{p - 28} 670 {p - 48} 690" fill="none" stroke="{PL}" style="stroke-width:26;stroke-linecap:round"></path>'
            f'<circle cx="{p - 52}" cy="693" r="13" fill="{GLOVE}"></circle>'
            # head, beard, face
            f'<circle cx="{p + 48}" cy="600" r="32" fill="{SKIN}"></circle>'
            f'<path d="M{p + 17} 604 Q{p + 16} 650 {p + 48} 656 Q{p + 80} 650 {p + 79} 604 Q{p + 66} 618 {p + 48} 616 Q{p + 30} 618 {p + 17} 604 Z" fill="{BEARD}"></path>'
            f'<path d="M{p + 36} 620 q12 6 24 0" fill="none" stroke="#5A3F2B" style="stroke-width:4;stroke-linecap:round"></path>'
            f'<circle cx="{p + 37}" cy="604" r="3.6" fill="#2A2A2A"></circle><circle cx="{p + 59}" cy="604" r="3.6" fill="#2A2A2A"></circle>'
            f'<circle cx="{p + 48}" cy="612" r="5" fill="#D9997A"></circle>'
            # plaid cap with ear flaps and a short brim
            f'<path d="M{p + 15} 588 Q{p + 14} 552 {p + 48} 550 Q{p + 82} 552 {p + 81} 588 Z" fill="{PL}"></path>'
            f'<path d="M{p + 15} 588 Q{p + 14} 552 {p + 48} 550 Q{p + 82} 552 {p + 81} 588 Z" fill="none" stroke="#5E140C" style="stroke-width:3"></path>'
            f'<rect x="{p + 10}" y="582" width="76" height="11" rx="5" fill="#7A1E1A"></rect>'
            f'<path d="M{p + 12} 588 L{p + 10} 618 Q{p + 18} 624 {p + 22} 616 L{p + 22} 590 Z" fill="{PL}" stroke="#5E140C" style="stroke-width:2"></path>'
            f'<path d="M{p + 84} 588 L{p + 86} 618 Q{p + 78} 624 {p + 74} 616 L{p + 74} 590 Z" fill="{PL}" stroke="#5E140C" style="stroke-width:2"></path>'
            f'<path d="M{p + 8} 592 Q{p + 48} 600 {p + 88} 592" fill="none" stroke="#5E140C" style="stroke-width:5;stroke-linecap:round"></path>')


def santa(p=715):
    R, Wt = '#C8321F', '#FFFFFF'
    return (f'<ellipse cx="{p + 45}" cy="868" rx="90" ry="10" fill="#000" opacity=".08"></ellipse>'
            f'<rect x="{p + 18}" y="770" width="30" height="92" rx="10" fill="{R}"></rect><rect x="{p + 52}" y="770" width="30" height="92" rx="10" fill="#B02A19"></rect>'
            f'<path d="M{p + 8} 846 h46 v28 h-54 z M{p + 48} 846 h46 v28 h-50 z" fill="#1C1C1C"></path>'
            # far arm, resting on his belly, with mitten and cuff
            f'<path d="M{p + 96} 654 Q{p + 120} 700 {p + 112} 748" fill="none" stroke="#B02A19" style="stroke-width:28;stroke-linecap:round"></path>'
            f'<rect x="{p + 98}" y="740" width="30" height="12" rx="5" fill="{Wt}"></rect>'
            f'<circle cx="{p + 113}" cy="762" r="13" fill="#1C1C1C"></circle>'
            f'<path d="M{p - 6} 640 Q{p + 48} 610 {p + 102} 640 L{p + 112} 790 L{p - 16} 790 Z" fill="{R}"></path>'
            f'<path d="M{p + 48} 640 L{p + 48} 790" stroke="{Wt}" style="stroke-width:14"></path><rect x="{p - 16}" y="778" width="128" height="16" rx="6" fill="{Wt}"></rect>'
            f'<rect x="{p - 12}" y="712" width="120" height="20" fill="#1C1C1C"></rect><rect x="{p + 36}" y="708" width="26" height="28" rx="3" fill="#F4B63F"></rect>'
            # near arm reaching to the bucket, with cuff and mitten
            f'<path d="M{p + 6} 660 Q{p - 34} 668 {p - 46} 688" fill="none" stroke="{R}" style="stroke-width:28;stroke-linecap:round"></path>'
            f'<circle cx="{p - 40}" cy="684" r="14" fill="{Wt}"></circle>'
            f'<circle cx="{p - 52}" cy="692" r="13" fill="#1C1C1C"></circle>'
            f'<circle cx="{p + 48}" cy="598" r="32" fill="#F2C4A0"></circle>'
            f'<path d="M{p + 14} 600 Q{p + 10} 672 {p + 48} 684 Q{p + 86} 672 {p + 82} 600 Q{p + 48} 622 {p + 14} 600 Z" fill="{Wt}"></path>'
            f'<path d="M{p + 14} 584 Q{p + 40} 520 {p + 108} 548 L{p + 82} 584 Z" fill="{R}"></path><circle cx="{p + 110}" cy="550" r="11" fill="{Wt}"></circle>'
            f'<rect x="{p + 10}" y="578" width="76" height="16" rx="8" fill="{Wt}"></rect>'
            f'<circle cx="{p + 36}" cy="602" r="3.5" fill="#333"></circle><circle cx="{p + 60}" cy="602" r="3.5" fill="#333"></circle>'
            f'<circle cx="{p + 48}" cy="612" r="6" fill="#E59A8A"></circle>')


def reindeer_cart(x0=870, gy=862):
    """A reindeer (facing left, toward Santa) pulling a small wooden cart of sap buckets."""
    FUR, FUR_D, LEG, ANT, WOOD, WOOD_D = "#9A6A43", "#7C522F", "#5E3D22", "#C9A57A", "#A8743F", "#7E5328"
    o = [f'<ellipse cx="{x0 + 110}" cy="{gy + 4}" rx="118" ry="8" fill="#000" opacity=".08"></ellipse>']
    # shafts from the cart to the reindeer (behind the body)
    o.append(f'<path d="M{x0 + 118} {gy - 48} L{x0 + 34} {gy - 64}" stroke="{WOOD_D}" style="stroke-width:6;stroke-linecap:round"></path>')
    # cart: buckets, box, wheel
    for bx in (x0 + 128, x0 + 166):
        o.append(f'<path d="M{bx} {gy - 96} L{bx + 4} {gy - 60} L{bx + 30} {gy - 60} L{bx + 34} {gy - 96} Z" fill="#B9C3CC" stroke="#7D8A96" style="stroke-width:3"></path>'
                 f'<path d="M{bx - 3} {gy - 98} L{bx + 37} {gy - 98}" stroke="#7D8A96" style="stroke-width:5;stroke-linecap:round"></path>'
                 f'<path d="M{bx + 4} {gy - 98} Q{bx + 17} {gy - 120} {bx + 30} {gy - 98}" fill="none" stroke="#7D8A96" style="stroke-width:3"></path>')
    o.append(f'<rect x="{x0 + 114}" y="{gy - 66}" width="100" height="34" rx="4" fill="{WOOD}" stroke="{WOOD_D}" style="stroke-width:3"></rect>'
             f'<path d="M{x0 + 114} {gy - 49} H{x0 + 214}" stroke="{WOOD_D}" style="stroke-width:2"></path>')
    wx, wy = x0 + 164, gy - 22
    o.append(f'<circle cx="{wx}" cy="{wy}" r="22" fill="none" stroke="{WOOD_D}" style="stroke-width:6"></circle>'
             + "".join(f'<path d="M{wx} {wy} l{dx} {dy}" stroke="{WOOD_D}" style="stroke-width:3"></path>' for dx, dy in ((20, 0), (-20, 0), (0, 20), (0, -20), (14, 14), (-14, -14), (14, -14), (-14, 14)))
             + f'<circle cx="{wx}" cy="{wy}" r="5" fill="{WOOD_D}"></circle>')
    # reindeer: legs, body, tail, neck, head, antlers
    for lx, c in ((x0 + 38, LEG), (x0 + 50, FUR_D), (x0 + 82, LEG), (x0 + 94, FUR_D)):
        o.append(f'<rect x="{lx}" y="{gy - 52}" width="8" height="50" rx="3" fill="{c}"></rect><rect x="{lx - 1}" y="{gy - 6}" width="10" height="7" rx="2" fill="#2A1C10"></rect>')
    o.append(f'<ellipse cx="{x0 + 68}" cy="{gy - 62}" rx="40" ry="20" fill="{FUR}"></ellipse>'
             f'<ellipse cx="{x0 + 70}" cy="{gy - 52}" rx="26" ry="8" fill="#E8D4B8"></ellipse>'
             f'<ellipse cx="{x0 + 108}" cy="{gy - 70}" rx="7" ry="5" fill="#F4ECE0"></ellipse>'
             f'<path d="M{x0 + 30} {gy - 70} L{x0 + 18} {gy - 104} L{x0 + 34} {gy - 108} L{x0 + 48} {gy - 72} Z" fill="{FUR}"></path>'
             f'<path d="M{x0 + 26} {gy - 80} Q{x0 + 36} {gy - 72} {x0 + 46} {gy - 80}" fill="none" stroke="{RED_}" style="stroke-width:6"></path>'
             f'<circle cx="{x0 + 36}" cy="{gy - 72}" r="5" fill="#F4B63F"></circle>'
             f'<ellipse cx="{x0 + 22}" cy="{gy - 108}" rx="15" ry="11" fill="{FUR}"></ellipse>'
             f'<ellipse cx="{x0 + 6}" cy="{gy - 103}" rx="11" ry="7" fill="{FUR}"></ellipse>'
             f'<circle cx="{x0 - 3}" cy="{gy - 104}" r="4" fill="#2A1C10"></circle>'
             f'<circle cx="{x0 + 18}" cy="{gy - 111}" r="2.6" fill="#1A1A1A"></circle>'
             f'<path d="M{x0 + 30} {gy - 114} l12 -6 l-4 10 z" fill="{FUR_D}"></path>')
    for d in (f"M{x0 + 20} {gy - 118} Q{x0 + 14} {gy - 136} {x0 + 2} {gy - 148} M{x0 + 15} {gy - 132} L{x0 + 26} {gy - 146} M{x0 + 7} {gy - 142} L{x0 + 4} {gy - 156}",
              f"M{x0 + 28} {gy - 118} Q{x0 + 34} {gy - 138} {x0 + 46} {gy - 150} M{x0 + 33} {gy - 132} L{x0 + 24} {gy - 146} M{x0 + 41} {gy - 144} L{x0 + 46} {gy - 158}"):
        o.append(f'<path d="{d}" fill="none" stroke="{ANT}" style="stroke-width:5;stroke-linecap:round"></path>')
    return "".join(o)


def owl(open_wings=False, ids=False):
    """Great horned-style owl drawn with its feet at (0, 0). With ids=True the parts get ids for the Reel:
    owlWO (open wings), owlWF (folded wings), owlLid (eyelids)."""
    FB, FD, BL, FACE = "#8B6A4A", "#6E5034", "#E2CFAE", "#E9DCC2"
    i = (lambda n: f' id="{n}"') if ids else (lambda n: "")
    wo = (f'<g{i("owlWO")} style="display:{"inline" if open_wings else "none"}">'
          f'<g{i("owlWL")}><path d="M-12 -42 Q-62 -78 -86 -40 Q-70 -44 -60 -34 Q-52 -42 -40 -26 Z" fill="{FD}"></path></g>'
          f'<g{i("owlWR")}><path d="M12 -42 Q62 -78 86 -40 Q70 -44 60 -34 Q52 -42 40 -26 Z" fill="{FD}"></path></g></g>')
    body = (f'<ellipse cx="0" cy="-30" rx="22" ry="28" fill="{FB}"></ellipse>'
            f'<ellipse cx="0" cy="-24" rx="14" ry="18" fill="{BL}"></ellipse>'
            + "".join(f'<path d="M{x - 4} {y} l4 4 l4 -4" fill="none" stroke="{FD}" style="stroke-width:2"></path>'
                      for x, y in ((-5, -34), (5, -34), (0, -26), (-6, -18), (6, -18), (0, -11))))
    wf = (f'<g{i("owlWF")} style="display:{"none" if open_wings else "inline"}">'
          f'<ellipse cx="-19" cy="-28" rx="9" ry="21" fill="{FD}"></ellipse><ellipse cx="19" cy="-28" rx="9" ry="21" fill="{FD}"></ellipse></g>')
    head = (f'<path d="M-20 -66 L-14 -86 L-6 -70 Z M20 -66 L14 -86 L6 -70 Z" fill="{FD}"></path>'
            f'<ellipse cx="0" cy="-58" rx="23" ry="18" fill="{FB}"></ellipse>'
            f'<circle cx="-9" cy="-58" r="10.5" fill="{FACE}"></circle><circle cx="9" cy="-58" r="10.5" fill="{FACE}"></circle>'
            f'<circle cx="-9" cy="-58" r="7" fill="#F4B63F"></circle><circle cx="9" cy="-58" r="7" fill="#F4B63F"></circle>'
            f'<circle cx="-8" cy="-58" r="3.6" fill="#1A1A1A"></circle><circle cx="8" cy="-58" r="3.6" fill="#1A1A1A"></circle>'
            f'<g{i("owlLid")} style="display:none"><circle cx="-9" cy="-58" r="7.5" fill="{FB}"></circle><circle cx="9" cy="-58" r="7.5" fill="{FB}"></circle>'
            f'<path d="M-15 -57 h12 M3 -57 h12" stroke="{FD}" style="stroke-width:2"></path></g>'
            f'<path d="M-4 -54 L4 -54 L0 -45 Z" fill="#E08A2E"></path>')
    feet = '<path d="M-10 -2 l-3 4 M-7 -2 v5 M-4 -2 l3 4 M4 -2 l-3 4 M7 -2 v5 M10 -2 l3 4" stroke="#E08A2E" style="stroke-width:2.5;stroke-linecap:round"></path>'
    return wo + body + wf + head + feet
