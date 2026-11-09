"""Make a hand-printed, watercolor-ish version of the MapleTapper logo (same colors, softer)."""
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
rng = np.random.default_rng(7)
src = Image.open("assets/logo.png").convert("RGBA")
w, h = src.size
rgb = src.convert("RGB"); a = np.asarray(src.split()[3]).astype(float) / 255

def noise(scale, amp):
    n = rng.random((h // scale + 2, w // scale + 2))
    n = Image.fromarray((n * 255).astype("uint8")).resize((w, h), Image.BICUBIC)
    return (np.asarray(n).astype(float) / 255 - .5) * amp

# 1. soften color: a bit less saturated, warmer, lighter
import sys
STRONG = "--strong" in sys.argv
rgb = ImageEnhance.Color(rgb).enhance(0.88)
c = np.asarray(rgb).astype(float)
paper = np.array([247, 244, 238.])
c = c * 0.92 + paper * 0.08
if STRONG:
    # tame bright blues toward a soft watercolor blue
    r_, g_, b_ = c[..., 0], c[..., 1], c[..., 2]
    blue = np.clip((b_ - r_ - 20) / 60, 0, 1)[..., None]
    c = c * (1 - .6 * blue) + np.array([160, 190, 205.]) * (.6 * blue)
    # near-black lettering -> warm dark brown ink
    dark = np.clip((110 - c.mean(-1)) / 110, 0, 1)[..., None]
    c = c * (1 - .55 * dark) + np.array([74, 50, 38.]) * (.55 * dark)
# 2. uneven watercolor/ink density (blotchy wash + fine grain)
dens = 1 + noise(60, .16) + noise(14, .10) + noise(2, .10) + (noise(30, .14) if STRONG else 0)
c = paper - (paper - c) * dens[..., None]
# 3. rough, slightly bled edges
ab = np.asarray(Image.fromarray((a * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(2.2))).astype(float) / 255
ab = np.clip((ab + noise(6, .45) + noise(2, .25) - .5) * 3.2 + .5, 0, 1)
a2 = np.minimum(ab, np.clip(a * 1.4, 0, 1)) * 0.94
# darker pooled pigment just inside edges
edge = np.clip(np.asarray(Image.fromarray((a2 * 255).astype("uint8")).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1.5))).astype(float) / 255 * 2, 0, 1)
c = c * (1 - .12 * edge[..., None])
out = np.dstack([np.clip(c, 0, 255), a2 * 255]).astype("uint8")
Image.fromarray(out, "RGBA").save("assets/logo_rough2.png" if STRONG else "assets/logo_rough.png")
print("ok")
