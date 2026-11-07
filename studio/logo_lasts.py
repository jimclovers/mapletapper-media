"""Re-render the last slide of posts 04-10 with the www.mapletapper.com logo beside the Next up box (Jim, Nov 7 2026).
Photos used on post 08/09 last slides are cropped back out of the already-published slide JPGs (originals didn't carry over).
Post 04's teaser now points to the Norway maple (black maple moved later).
Usage: python3 logo_lasts.py   -> writes preview/PostNN-last-logo.html
"""
import base64
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import ROOT, preview_html, footer_row  # noqa: E402
from post02 import with_images  # noqa: E402

LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()
LOGO_IMG = f'<img data-chk="logo" src="{LOGO}" alt="MapleTapper logo, www.mapletapper.com" style="width: 200px; flex: none; display: block">'


def with_logo(box_html, badge=False, width=200):
    """Put a box and the logo side by side; the box stretches to fill the row. badge=True puts the logo on a cream tile (for maroon slides)."""
    box_html = box_html.replace('style="', 'style="flex: 1 1 0; ', 1)
    img = LOGO_IMG.replace("width: 200px", f"width: {width}px")
    if badge:
        img = (f'<div style="flex: none; background: #FFF5DE; border-radius: 28px; padding: 12px 14px">'
               + img.replace('data-chk="logo" ', "") + "</div>")
    return f'<div style="display: flex; align-items: center; gap: 28px">{box_html}{img}</div>'


def no_url_footer(color):
    return footer_row(color, "<span></span>")


# module, last-slide function name, extra image keys -> local file
JOBS = {
    "post04": ("slide4", {}),
    "post05": ("slide5", {}),
    "post06": ("slide6", {}),
    "post07": ("slide4", {}),
    "post08": ("slide4", {"jar": os.path.join(ROOT, "photos", "crops", "post08_jar.jpg")}),
    "post09": ("slide4", {"leaves": os.path.join(ROOT, "photos", "crops", "post09_leaves.jpg")}),
    "post10": ("slide4", {}),
}


def build(name):
    fn_name, imgs = JOBS[name]
    mod = importlib.import_module(name)
    orig_teaser = getattr(mod, "teaser", None)
    if orig_teaser:
        def teaser(when, what, *a, **k):
            if name == "post04":
                what = "Tree ID bonus: Norway maple"
            return with_logo(orig_teaser(when, what, *a, **k), badge=(name == "post05"),
                             width=170 if name == "post04" else (180 if name == "post05" else 200))
        mod.teaser = teaser
    if hasattr(mod, "site_footer"):
        mod.site_footer = no_url_footer
    markup, title = getattr(mod, fn_name)()
    if name == "post10":   # no Next up box: put the logo beside the "Save this post" box
        markup = re.sub(r'(<div data-chk="save".*?</div>)', lambda m: with_logo(m.group(1)), markup, count=1, flags=re.S)
    local = {k: "file://" + v for k, v in imgs.items()}
    path = os.path.join(ROOT, "preview", f"{name.capitalize()}-last-logo.html")
    open(path, "w").write(preview_html(title, with_images(markup, local)))
    return path


if __name__ == "__main__":
    for n in (sys.argv[1:] or JOBS):
        print(build(n))
