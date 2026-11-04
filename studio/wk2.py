"""Shared bits for the Nov 9-15 posts (Almanac No. 05-10): cover with a weekly countdown, badges, render helpers."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, W, H, ROOT, footer_row, swipe, headline, body, preview_html  # noqa: E402
from post02 import pill, with_images  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
M, CR, RED, GOLD = C["maroon"], C["cream"], C["red"], C["gold"]
GREEN = "#5F8F4E"
BARK = "#6B4A2E"
PHOTO_H = 780
WEEKS = 16  # Nov 9-15: 16 weeks to sap season (Oct 30-Nov 8 posts said 17)
SPACER = '<div style="flex-grow: 1"></div>'


def stamp(big1, small, top=PHOTO_H - 68):
    return (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: {top}px; z-index: 3; transform: rotate(-3deg); background: {GOLD}; '
        f'border: 6px solid {CR}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 16px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 72px; letter-spacing: -0.02em; line-height: 1; color: {M}">'
        f'{big1}<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">{small}</span></div>'
    )


def cover(img_key, alt, left_pill, stamp_html, title_html, sub, title_size=98, obj_pos="50% 50%", weeks=WEEKS):
    photo = (
        f'<img src="@@IMG_{img_key}@@" alt="{alt}" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-fit: cover; object-position: {obj_pos}; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill(left_pill, CR, M)}{pill(f"{weeks} weeks to sap season", GOLD, M)}</div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 100px 72px 60px; display: flex; flex-direction: column; gap: 20px; background: {M}">'
        + headline(title_html, title_size, CR, chk="title")
        + body(sub, 36, GOLD, "sub", "; font-weight: 700")
        + SPACER
        + footer_row(CR, swipe(CR))
        + "</div>"
    )
    return photo + top + stamp_html + bottom


def circle_badge(svg_inner, bg, size=104, ring="#EAD9B5", vb=80):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; display: flex; align-items: center; '
            f'justify-content: center; flex: none; box-shadow: inset 0 0 0 3px {ring}"><svg aria-hidden="true" width="{size - 14}" '
            f'height="{size - 14}" viewBox="0 0 {vb} {vb}">{svg_inner}</svg></div>')


def check_mark(color, w=6):
    return (f'<path d="M20 41 L34 55 L60 27" fill="none" stroke="{color}" '
            f'style="stroke-width:{w};stroke-linecap:round;stroke-linejoin:round"></path>')


def x_mark(color, w=6):
    return (f'<path d="M24 24 L56 56 M56 24 L24 56" fill="none" stroke="{color}" '
            f'style="stroke-width:{w};stroke-linecap:round"></path>')


def row(badge_html, title, note, color, title_size=44, note_size=31, chk=None):
    c = f' data-chk="{chk}"' if chk else ""
    return (
        f'<div{c} style="display: flex; gap: 26px; align-items: center">{badge_html}<div style="display: flex; flex-direction: column; gap: 4px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: {title_size}px; line-height: 1.04; color: {color}">{title}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: {note_size}px; line-height: 1.22; color: {color}">{note}</div></div></div>'
    )


def build_preview(slides, assets, prefix=""):
    local = {k: "file://" + os.path.join(PHOTO_DIR, v) if not v.startswith("/") else "file://" + v for k, v in assets.items()}
    names = []
    for name, fn in slides:
        markup, title = fn()
        path = os.path.join(ROOT, "preview", name + ".html")
        open(path, "w").write(preview_html(title, with_images(markup, local)))
        names.append(path)
    return names


def cover_custom(top_html, left_pill, stamp_html, title_html, sub, title_size=98, weeks=WEEKS, top_bg=None):
    """Like cover() but the 1080x780 top area holds custom HTML/SVG instead of a photo."""
    top_bg = top_bg or GOLD
    art = (f'<div style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; background: {top_bg}; display: flex; '
           f'align-items: center; justify-content: center; overflow: hidden">{top_html}</div>')
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill(left_pill, CR, M)}{pill(f"{weeks} weeks to sap season", M, CR)}</div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 100px 72px 60px; display: flex; flex-direction: column; gap: 20px; background: {M}">'
        + headline(title_html, title_size, CR, chk="title")
        + body(sub, 36, GOLD, "sub", "; font-weight: 700")
        + SPACER
        + footer_row(CR, swipe(CR))
        + "</div>"
    )
    return art + top + stamp_html + bottom
