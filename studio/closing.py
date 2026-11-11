"""Standard MapleTapper closing card (Jim, Nov 11 2026) - DRAFT, waiting on Jim's approval.
Last slide of every carousel / last 5-8 s of every video. Warm invitation, no prices, no "buy now".
Pattern: 1) "[Topic] is just the start."  2) what people find at mapletapper.com  3) who it's for.
Real MapleTapper photo on top, big logo + website readable on a phone.
Usage: python3 closing.py "Two-tone maples are just the start."  -> preview/Closing-reel.html, preview/Closing-post.html
"""
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, preview_html  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
M, CR, G = C["maroon"], C["cream"], C["gold"]
PHOTO = os.path.join(ROOT, "photos", "products", "kids_kit_snow_jugs.jpg")  # real photo from the Kid's Kit box: tubing into jugs in snow

FIND = "Tapping kits, food-grade spiles, tubing and buckets, plus our tapping guide and kids’ book."
WHO = "Everything a family needs to make its own syrup."


def uri(p, mime="image/jpeg"):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def card(topic, w=1080, h=1920, find=FIND, who=WHO):
    reel = h > 1500
    photo_h = 760 if reel else 440
    s = 1.0 if reel else 0.9
    logo = uri(os.path.join(ROOT, "assets", "logo.png"), "image/png")
    return (
        f'<div data-root style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: {CR}; font-family: {DISPLAY}">'
        f'<img src="{uri(PHOTO)}" alt="Blue tubing running from maple taps into jugs in the snow" '
        f'style="position: absolute; left: 0; top: 0; width: {w}px; height: {photo_h}px; object-fit: cover; object-position: 50% 30%">'
        f'<div style="position: absolute; left: 0; right: 0; top: {photo_h - 6}px; height: 12px; background: {G}"></div>'
        f'<div style="position: absolute; left: 70px; right: 70px; top: {photo_h + int(56 * s)}px; display: flex; flex-direction: column; gap: {int(26 * s)}px">'
        f'<h1 data-chk="topic" style="margin: 0; font-weight: 800; font-size: {int(84 * s)}px; line-height: .98; letter-spacing: -.02em; color: {M}">{topic}</h1>'
        f'<p data-chk="find" style="margin: 0; font-weight: 600; font-size: {int(44 * s)}px; line-height: 1.22; color: {M}">{find}</p>'
        f'<p data-chk="who" style="margin: 0; font-weight: 700; font-size: {int(44 * s)}px; line-height: 1.22; color: {C["red"]}">{who}</p></div>'
        f'<div data-chk="brand" style="position: absolute; left: 70px; right: 70px; bottom: {330 if reel else 70}px; display: flex; align-items: center; '
        f'justify-content: center; gap: {int(36 * s)}px">'
        f'<img src="{logo}" alt="MapleTapper logo" style="width: {int(260 * s)}px; display: block">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: {int(74 * s)}px; letter-spacing: -.01em; color: {M}">mapletapper.com</div></div>'
        f'</div>'
    )


if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "Two-tone maples are just the start."
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    open(os.path.join(ROOT, "preview", "Closing-reel.html"), "w").write(preview_html("Closing", card(topic)))
    open(os.path.join(ROOT, "preview", "Closing-post.html"), "w").write(preview_html("Closing", card(topic, 1080, 1350)))
    print("built")
