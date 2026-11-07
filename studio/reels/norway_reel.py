#!/usr/bin/env python3
"""MapleTapper photo-montage Reel ("Every tree here is a maple"): full-bleed photos with a slow zoom,
lower-third color labels, a 'check the leaf' lesson card and a closing call to action.
Usage: photo_reel.py [--draft]   (draft = fast preview, lower quality)"""
import subprocess, sys, base64
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path("/home/claude/mt")
P6 = ROOT / "photos/norway"
OUT = ROOT / "reels/reel6"
OUT.mkdir(parents=True, exist_ok=True)
NAME = "MapleTapper-Reel-NorwayMaple"
W, H, FPS, XF = 1080, 1920, 30, 0.25
C = dict(maroon="#7A1E1A", red="#C8321F", gold="#F4B63F", cream="#FFF5DE")
DISPLAY = "'Bricolage Grotesque', 'Helvetica Neue', Arial, sans-serif"
TYPE = "'Special Elite', 'Courier New', monospace"
FONTS = ("@font-face{font-family:'Bricolage Grotesque';src:url('file:///home/claude/mt/fonts/node_modules/@fontsource-variable/"
         "bricolage-grotesque/files/bricolage-grotesque-latin-standard-normal.woff2') format('woff2');font-weight:200 800;"
         "font-stretch:75% 100%;}@font-face{font-family:'Special Elite';src:url('file:///home/claude/mt/fonts/node_modules/"
         "@fontsource/special-elite/files/special-elite-latin-400-normal.woff2') format('woff2');font-weight:400;}")
GOLD = lambda s: f'<span style="color: {C["gold"]}">{s}</span>'

# (photo key, crop centre as a fraction of width, seconds, lower-third label, zoom direction)
# Jim's Norway maple photos. 927b8690 is cropped at 0.38 so the red fence on the right edge stays out of frame.
SEQ = [
    ("3e162b3d", 0.50, 3.0, None, +1),                      # hook
    ("927b8690", 0.38, 2.2, "Pointy leaves", -1),
    ("9e0bfd28", 0.50, 2.2, "Criss-cross bark", +1),
    ("49899519", 0.50, 2.0, "Yellow in fall", -1),
    ("a12ff134", 0.50, 2.0, "A street favorite", +1),
]
LESSON_S, CTA_S, POP_S = 4.6, 3.4, 3.0


def photo_path(key):
    return P6 / f"n_{key}.jpg"


def b64(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


def page(body, bg="transparent"):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS} html,body{{margin:0;background:{bg}}}"
            f"</style></head><body><div id='root' style='position: relative; width: {W}px; height: {H}px; overflow: hidden; "
            f"background: {bg}'>{body}</div></body></html>")


def chip(text, size=28, pad="12px 24px 10px", bg=None, fg=None):
    return (f'<span style="background: {bg or C["cream"]}; color: {fg or C["maroon"]}; border-radius: 999px; padding: {pad}; '
            f'font-family: {TYPE}; font-size: {size}px; letter-spacing: 0.06em; text-transform: uppercase; white-space: nowrap">'
            f'{text}</span>')


TOPBAR = (f'<div style="position: absolute; left: 64px; right: 64px; top: 150px; display: flex; justify-content: space-between; '
          f'align-items: center">{chip("Norway maple")}{chip("@mapletapper", 26, "10px 22px 8px", C["maroon"], C["cream"])}</div>')


def label_html(text, size=34):
    return (f'<div style="font-family: {TYPE}; font-size: {size}px; letter-spacing: 0.06em; text-transform: uppercase; '
            f'color: {C["gold"]}">{text}</div>')


def hook_overlay():
    card = (f'<div data-chk="1" style="position: absolute; left: 64px; top: 1190px; width: 820px; background: {C["maroon"]}; '
            f'border-radius: 36px; padding: 30px 40px 34px; box-sizing: border-box">{label_html("Can you tap it?")}'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 92px; line-height: 0.98; letter-spacing: -0.02em; '
            f'color: {C["cream"]}; margin-top: 10px">This is a<br>{GOLD("Norway maple.")}</div></div>')
    return page(TOPBAR + card)


def label_overlay(text):
    pill = (f'<div data-chk="1" style="position: absolute; left: 64px; top: 1250px; background: {C["maroon"]}; border-radius: 36px; '
            f'padding: 22px 40px 26px; font-family: {DISPLAY}; font-weight: 800; font-size: 76px; line-height: 1; '
            f'letter-spacing: -0.015em; text-transform: uppercase; color: {C["cream"]}; white-space: nowrap">{text}</div>')
    return page(TOPBAR + pill)


def lesson_card():
    def row(big, small):
        return (f'<div style="display: flex; flex-direction: column; gap: 8px; border-left: 10px solid {C["gold"]}; padding-left: 30px">'
                f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 64px; line-height: 1.0; color: {C["cream"]}">{big}</div>'
                f'<div style="font-family: {TYPE}; font-size: 36px; line-height: 1.3; color: {C["gold"]}">{small}</div></div>')
    body = (f'<div data-chk="1" style="position: absolute; left: 72px; top: 400px; width: 860px">{label_html("Can you tap it?")}'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 120px; line-height: 0.95; letter-spacing: -0.025em; '
            f'color: {C["cream"]}; margin-top: 16px">{GOLD("Yes!")}</div>'
            f'<div style="display: flex; flex-direction: column; gap: 48px; margin-top: 60px">'
            f'{row("2.2–2.8% sugar", "in a Utah State study")}'
            f'{row("~35 gallons of sap", "= 1 gallon of syrup (sugar maple: ~40)")}'
            f'{row("The catch: slow drip", "about 2–2½ gallons of sap per tree")}</div></div>')
    return page(TOPBAR + body, C["maroon"])


def cta_card():
    thumbs = "".join(
        f'<img src="{b64(photo_path(k))}" style="width: 250px; height: 330px; object-fit: cover; border-radius: 22px; '
        f'box-shadow: 0 0 0 5px {C["cream"]}">' for k in ("3e162b3d", "9e0bfd28", "49899519"))
    body = (f'<div data-chk="1" style="position: absolute; left: 72px; top: 420px; width: 860px">{label_html("Quick test")}'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 100px; line-height: 0.97; letter-spacing: -0.025em; '
            f'color: {C["cream"]}; margin-top: 16px">Snap a leaf stem.<br>{GOLD("Milky sap?")}<br>It’s Norway.</div>'
            f'<div style="display: flex; gap: 22px; margin-top: 60px">{thumbs}</div>'
            f'<div style="margin-top: 56px">{chip("mapletapper.com", 34, "14px 30px 12px")}</div></div>')
    return page(TOPBAR + body, C["maroon"])


def pop_card():
    body = (f'<div data-chk="1" style="position: absolute; left: 72px; top: 400px; width: 860px; text-align: center">'
            f'<div style="font-family: {TYPE}; font-size: 44px; letter-spacing: 0.08em; text-transform: uppercase; color: {C["maroon"]}">Get ready!</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 330px; line-height: 0.9; letter-spacing: -0.04em; color: {C["maroon"]}; margin-top: 20px">16</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 104px; line-height: 0.95; letter-spacing: -0.02em; color: {C["maroon"]}">weeks to<br><span style="color: {C["red"]}">sap season!</span></div>'
            f'<div style="margin: 50px auto 0; width: 380px; height: 380px; border-radius: 48px; background: {C["cream"]}; display: flex; align-items: center; justify-content: center">'
            f'<img src="data:image/png;base64,{base64.b64encode(open("/home/claude/mt/studio/assets/logo.png","rb").read()).decode()}" style="width: 320px; display: block"></div></div>')
    return page(body, "transparent")


def pop_frames(img, secs, bg):
    """Bounce-in: scale 0.55 -> 1.08 -> 1.0 over ~0.5 s, then hold."""
    n = round(secs * FPS)
    for i in range(n):
        t = i / FPS
        if t < 0.33: z = 0.55 + (1.08 - 0.55) * (t / 0.33)
        elif t < 0.5: z = 1.08 - 0.08 * ((t - 0.33) / 0.17)
        else: z = 1.0
        fr = Image.new("RGBA", (W, H), bg)
        w, h = round(W * z), round(H * z)
        sm = img.resize((w, h), Image.LANCZOS)
        fr.alpha_composite(sm, ((W - w) // 2, (H - h) // 2)) if z <= 1 else fr.alpha_composite(sm.crop(((w - W) // 2, (h - H) // 2, (w - W) // 2 + W, (h - H) // 2 + H)))
        yield fr.convert("RGB")


def render(pages):
    out = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport=dict(width=W, height=H))
        for name, (html, transparent) in pages.items():
            pg.set_content(html)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            # overflow check: every data-chk block must sit inside the frame and keep clear of Instagram's UI
            boxes = pg.eval_on_selector_all("[data-chk]", "els => els.map(e => { const r = e.getBoundingClientRect(); "
                                            "return [r.left, r.top, r.right, r.bottom]; })")
            for l, t, r, btm in boxes:
                flag = "" if (l >= 40 and r <= 940 and t >= 140 and btm <= 1500) else "  <-- CHECK SAFE ZONE"
                print(f"  {name}: box {int(l)},{int(t)} → {int(r)},{int(btm)}{flag}")
            path = OUT / f"{name}.png"
            pg.screenshot(path=str(path), omit_background=transparent)
            out[name] = Image.open(path).convert("RGBA")
        b.close()
    return out


def photo_frames(key, cx, secs, zdir, overlay):
    """Yield RGB frames: 9:16 crop of the photo with a slow zoom (in or out), overlay composited on top."""
    src = Image.open(photo_path(key)).convert("RGB")
    sw, sh = src.size
    cw = sh * 9 / 16
    x0 = min(max(cx * sw - cw / 2, 0), sw - cw)
    base = src.crop((round(x0), 0, round(x0 + cw), sh)).resize((1350, 2400), Image.LANCZOS)
    n = round(secs * FPS)
    for i in range(n):
        u = i / max(n - 1, 1)
        z = 1.0 + 0.07 * (u if zdir > 0 else 1 - u)
        w, h = 1350 / z, 2400 / z
        l, t = (1350 - w) / 2, (2400 - h) / 2
        fr = base.transform((W, H), Image.EXTENT, (l, t, l + w, t + h), Image.BICUBIC).convert("RGBA")
        fr.alpha_composite(overlay)
        yield fr.convert("RGB")


def card_frames(img, secs):
    fr = img.convert("RGB")
    for _ in range(round(secs * FPS)):
        yield fr


def main():
    draft = "--draft" in sys.argv
    pages = {"hook": (hook_overlay(), True), "lesson": (lesson_card(), False), "cta": (cta_card(), False), "pop": (pop_card(), True)}
    for key, *_rest in SEQ:
        lab = _rest[2]
        if lab:
            pages[f"label_{key}"] = (label_overlay(lab), True)
    ov = render(pages)

    streams = []
    for key, cx, secs, lab, zdir in SEQ:
        streams.append(photo_frames(key, cx, secs + XF, zdir, ov["hook"] if lab is None else ov[f"label_{key}"]))
    streams.append(card_frames(ov["lesson"], LESSON_S + XF))
    streams.append(card_frames(ov["cta"], CTA_S + XF))
    streams.append(pop_frames(ov["pop"], POP_S, C["gold"]))

    out = OUT / f"{NAME}.mp4"
    total = sum(s[2] for s in SEQ) + LESSON_S + CTA_S + POP_S
    enc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
         "-f", "lavfi", "-t", f"{total:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
         "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "26" if draft else "18",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart",
         "-map_metadata", "-1", str(out)], stdin=subprocess.PIPE)
    nx = round(XF * FPS)
    tail = []   # last frames of the previous clip, crossfaded into the start of the next
    written = 0
    cover = None
    for si, gen in enumerate(streams):
        frames = list(gen) if si == len(streams) - 1 else None
        it = iter(frames) if frames is not None else gen
        head = []
        for _ in range(nx if tail else 0):
            head.append(next(it))
        for k, (a, b2) in enumerate(zip(tail, head)):
            enc.stdin.write(Image.blend(a, b2, (k + 1) / (nx + 1)).tobytes()); written += 1
        buf = []
        for fr in it:
            buf.append(fr)
            if si < len(streams) - 1 and len(buf) > nx:
                f0 = buf.pop(0)
                enc.stdin.write(f0.tobytes()); written += 1
                if si == 0 and cover is None and written >= 30:
                    cover = f0.copy()
            elif si == len(streams) - 1:
                enc.stdin.write(buf.pop(0).tobytes()); written += 1
        tail = buf
    for fr in tail:
        enc.stdin.write(fr.tobytes()); written += 1
    enc.stdin.close(); enc.wait()
    cover.save(OUT / f"{NAME}-cover.jpg", "JPEG", quality=90)
    print(f"wrote {out} ({written} frames ≈ {written / FPS:.2f} s, planned {total:.2f} s)")


if __name__ == "__main__":
    main()
