#!/usr/bin/env python3
"""Build a MapleTapper Reel: Jim's landscape clips in a maroon 9:16 frame, synced word-highlight captions,
header fact cards, and a closing call to action. Usage: build_reel.py reel1|reel2 [--draft]"""
import json, subprocess, sys, shutil, base64
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path("/home/claude/mt")
U = "/mnt/user-data/uploads/"
WORDS = json.load(open(ROOT / "talk/words.json"))
SHIFT, FPS = 0.08, 30
C = dict(maroon="#7A1E1A", red="#C8321F", gold="#F4B63F", cream="#FFF5DE")
DIM = "rgba(255,245,222,0.42)"
DISPLAY = "'Bricolage Grotesque', 'Helvetica Neue', Arial, sans-serif"
TYPE = "'Special Elite', 'Courier New', monospace"
FONTS = ("@font-face{font-family:'Bricolage Grotesque';src:url('file:///home/claude/mt/fonts/node_modules/@fontsource-variable/"
         "bricolage-grotesque/files/bricolage-grotesque-latin-standard-normal.woff2') format('woff2');font-weight:200 800;"
         "font-stretch:75% 100%;}@font-face{font-family:'Special Elite';src:url('file:///home/claude/mt/fonts/node_modules/"
         "@fontsource/special-elite/files/special-elite-latin-400-normal.woff2') format('woff2');font-weight:400;}")
W, H = 1080, 1920
WIN = dict(x=40, y=470, w=1000, h=750)
HEAD_Y, HEAD_H = 226, 238
CAP_Y, CAP_H = 1250, 300
NB = " "
GOLD = lambda s: f'<span style="color: {C["gold"]}">{s}</span>'

REELS = {
    "reel0": dict(
        name="MapleTapper-Reel-WhyHalfRed",
        kicker="Tree ID · Sugar maple",
        title=f"Why is half<br>this maple {GOLD('red?')}",
        label="Jim's video",
        segs=[dict(src=U + "IMG_2264.mov", key=None, a=0.0, b=18.6, mute=True, text="")],
        header=[],
        cards=[
            dict(kind="text", seg=0, a=0.6, bseg=0, b=9.1, label="Hint", html="Watch where<br>the sunlight hits."),
            dict(kind="text", seg=0, a=9.5, bseg=0, b=18.6, label="Answer", html="Red color needs<br>sunlight to form.",
                 sub="Sunny leaves turn red. Shaded leaves inside show their gold."),
        ],
        cta=None,
    ),
    "reel1": dict(
        name="MapleTapper-Reel-PerfectTappingSpot",
        kicker="Scouting trees",
        title=f"The perfect<br>tapping {GOLD('spot.')}",
        label="Jim's video",
        segs=[
            dict(src=U + "IMG_1463.mov", key="IMG_1463", a=1.40, b=34.00,
                 text="Yeah, so here's a good example | of some beautiful sugar maples | planted in a row here on the road | "
                      "about, I don't know, 80 years ago, | maybe more. | Some farmer had the good sense | "
                      "to plant these trees in front of his house, | and now look at them. They're beautiful. | "
                      "This is a perfect spot to tap. | You've got multiple trees | lined up in a row, | "
                      "and it'll be really easy | to collect the sap | right on the side of the road."),
            dict(src=U + "35887356-IMG_1471.mov", key="IMG_1471", a=1.15, b=9.60, insert=[("six", 7.05)],
                 text="But right in a row here, | you've got one, two, three, | four, five, six, | seven, eight trees."),
            dict(src=U + "IMG_1464.mov", key="IMG_1464", a=1.30, b=29.30,
                 text=f"But unless you want to go | trekking through the woods, | a spot like this is just perfect{NB}— | "
                      "could drive your vehicle right up, | empty the buckets quite regularly | without any trouble. | "
                      "So there's a good example. | You can look for this around your area | and walk in and ask these people | "
                      "who live there | if they'd be interested | in having their maple trees tapped. | "
                      "And I guess their pay | would be maple syrup."),
            dict(src=U + "c361a8bd-IMG_1458.mov", key=None, a=0.40, b=4.60, vol=0.5, text="", crop="691:518:384:0"),
        ],
        header=[
            dict(kind="fact", seg=2, a=4.5, b=13.9, label="Safety first",
                 html="Park well off the road and watch for traffic."),
            dict(kind="fact", seg=2, a=18.3, b=29.3, label="Ask first",
                 html="Trees along the street often belong to the town."),
        ],
        cta=dict(seg=3, a=0.55, label="Your move", html=f"Scout your trees now.<br>Tap in late winter."),
        cover=dict(src=U + "IMG_1463.mov", t=7.0, focus=0.5),
    ),
    "reel2": dict(
        name="MapleTapper-Reel-SugarMapleOrNot",
        kicker="Tree ID",
        title=f"Sugar maple<br>or {GOLD('not?')}",
        label="Jim's video",
        segs=[
            dict(src=U + "IMG_1479.mov", key="IMG_1479", a=1.30, b=9.75,
                 text="When you get used to looking for them, | you can start to tell | which is the sugar maple tree | "
                      "and which is a silver."),
            dict(src=U + "IMG_1479.mov", key="IMG_1479", a=11.45, b=24.00,
                 text="Sugar maple has kind of a rounded top, | and it's got that yellowish orange, | that bronze look to it, | "
                      "as opposed to this. | See, look across there."),
            dict(src=U + "IMG_1482.mov", key="IMG_1482", a=0.90, b=17.85,
                 text=f"Probably a red maple. | You{NB}can tell from the leaves. | See, it has that serrated leaf. | "
                      "Beautiful, no question about it. | I can see why people plant these: | faster-growing, | "
                      "resistant to disease."),
            dict(src=U + "IMG_1482.mov", key="IMG_1482", a=23.15, b=33.30,
                 text="They are beautiful, | absolutely glorious to look at | right now and all summer, | but not a sugar maple."),
            dict(src=U + "IMG_1481.mov", key="IMG_1481", a=17.12, b=48.52,
                 text="Newer developments | are not planting the sugar maples | because they're slower growing. | "
                      "So you see a lot of silvers, | a lot of red maples being planted, | and they are beautiful. | "
                      "Look at the color on them. | But they don't have quite | the concentration of sugar | "
                      "that sugar maples do. | They're definitely tappable, | and I've tapped a lot of red maples | "
                      "and silver maples | and gotten plenty of syrup. | A little more boiling involved, though. | "
                      "If you can find the sugar maples, | that's the way to go."),
            dict(src=U + "IMG_1479.mov", key=None, a=32.60, b=36.80, mute=True, text=""),
        ],
        header=[
            dict(kind="fact", seg=2, a=4.4, b=11.4, label="Leaf check",
                 html=f"Saw-tooth edges {GOLD('→')} red or silver<br>Smooth edges {GOLD('→')} could be sugar"),
            dict(kind="stats", seg=4, a=30.5, b=45.2, label="Sap for 1 gallon of syrup · approx.",
                 stats=[("40", "Sugar maple", True), ("50", "Red maple", False), ("57", "Silver maple", False)]),
        ],
        cta=dict(seg=5, a=0.25, label="Your move", html="Spot your sugar maples<br>while the leaves are on."),
        cover=dict(photo=U + "ebff1f38-image.jpg"),
    ),
    "reel3": dict(
        name="MapleTapper-Reel-LeafDetective", uniform=True, final_target=-18.0,
        kicker="Family fun",
        title="Before you bag<br>the leaves…",
        label="Family video",
        # gray-shirt kid: run, trampoline bounce, flip, buried, "Nice one!", pops out
        # striped-shirt kid: run, bounce, flip, buried; hold the last frame for the closing cards
        segs=[
            dict(src=U + "IMG_4425.mov", key=None, a=2.50, b=9.20, text=""),
            dict(src=U + "8b06bdc6-IMG_4423.mov", key=None, a=8.50, b=14.30, freeze=3.8, text=""),
        ],
        header=[dict(kind="bigtitle", seg=0, a=5.20, b=None, html=f"Play leaf<br>{GOLD('detective!')} 🔍")],
        cards=[
            dict(kind="compare", seg=0, a=5.40, bseg=0, b=9.10, label="Step 1 · Check the edges",
                 rows=[(str(ROOT / "reels/assets/leaf_sugar.jpg"), "Smooth edges", "could be a sugar maple"),
                       (str(ROOT / "reels/assets/leaf_red.jpg"), "Saw-tooth edges", "red or silver maple")]),
            dict(kind="icon", icon="drop", seg=0, a=9.10, bseg=1, b=11.90, label="Step 2 · Snap test",
                 html="Snap a fresh leaf stem. A milky drop? That's a Norway maple."),
            dict(kind="icon", icon="ribbon", seg=1, a=11.90, bseg=1, b=15.40, label="Step 3 · Mark it",
                 html="Sugar maple? Find its tree and tie on a ribbon. Tap it in late winter!"),
        ],
        cta=dict(seg=1, a=6.90, label="Your move", html="Go leaf hunting<br>this weekend!"),
    ),
}


def page(body, w, h):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS} html,body{{margin:0;background:transparent}}"
            f"</style></head><body><div id='root' style='position: relative; width: {w}px; height: {h}px; overflow: hidden'>"
            f"{body}</div></body></html>")


def chip(text, size=28, pad="12px 24px 10px"):
    return (f'<span style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; padding: {pad}; '
            f'font-family: {TYPE}; font-size: {size}px; letter-spacing: 0.06em; text-transform: uppercase; white-space: nowrap">{text}</span>')


def base_html(spec):
    win = (f'<div style="position: absolute; left: {WIN["x"]}px; top: {WIN["y"]}px; width: {WIN["w"]}px; height: {WIN["h"]}px; '
           f'border-radius: 36px; box-shadow: 0 0 0 2400px {C["maroon"]}"></div>')
    top = (f'<div style="position: absolute; left: 72px; right: 72px; top: 150px; display: flex; justify-content: space-between; '
           f'align-items: center">{chip(spec["kicker"])}<span style="font-family: {TYPE}; font-size: 28px; color: {C["cream"]}">'
           f'@mapletapper</span></div>')
    lab = (f'<div style="position: absolute; left: {WIN["x"] + 24}px; top: {WIN["y"] + WIN["h"] - 64}px">'
           f'{chip(spec["label"], 22, "8px 18px 6px")}</div>')
    return page(win + top + lab, W, H)


def title_html(spec):
    return page(f'<div data-chk="1" style="position: absolute; left: 72px; top: 10px; font-family: {DISPLAY}; font-weight: 800; '
                f'font-size: 104px; line-height: 0.95; letter-spacing: -0.025em; color: {C["cream"]}">{spec["title"]}</div>', W, HEAD_H)


def label_html(text, color=None):
    return (f'<div style="font-family: {TYPE}; font-size: 30px; letter-spacing: 0.06em; text-transform: uppercase; '
            f'color: {color or C["gold"]}">{text}</div>')


def fact_html(item):
    if item["kind"] == "bigtitle":
        return page(f'<div data-chk="1" style="position: absolute; left: 72px; top: 10px; font-family: {DISPLAY}; font-weight: 800; '
                    f'font-size: 104px; line-height: 0.95; letter-spacing: -0.025em; color: {C["cream"]}">{item["html"]}</div>', W, HEAD_H)
    if item["kind"] == "stats":
        cols = "".join(
            f'<div style="display: flex; flex-direction: column; gap: 2px"><div style="font-family: {DISPLAY}; font-weight: 800; '
            f'font-size: 112px; line-height: 0.92; letter-spacing: -0.03em; color: {C["gold"] if hi else C["cream"]}">{n}'
            f'<span style="font-size: 38px; letter-spacing: 0; margin-left: 8px">gal.</span></div>'
            f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.05em; text-transform: uppercase; '
            f'color: {C["cream"]}">{name}</div></div>' for n, name, hi in item["stats"])
        inner = f'{label_html(item["label"])}<div style="display: flex; gap: 52px; margin-top: 14px">{cols}</div>'
    else:
        inner = (f'{label_html(item["label"])}<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 60px; '
                 f'line-height: 1.04; letter-spacing: -0.015em; color: {C["cream"]}; margin-top: 12px">{item["html"]}</div>')
    return page(f'<div data-chk="1" style="position: absolute; left: 72px; top: 14px; width: 936px">{inner}</div>', W, HEAD_H)


def cta_html(spec):
    c = spec["cta"]
    inner = (f'{label_html(c["label"])}<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 60px; line-height: 1.06; '
             f'letter-spacing: -0.015em; color: {C["cream"]}; margin-top: 12px">{c["html"]}</div>'
             f'<div style="margin-top: 18px">{chip("mapletapper.com", 30, "12px 26px 10px")}</div>')
    return page(f'<div data-chk="1" style="position: absolute; left: 72px; top: 18px; width: 900px">{inner}</div>', W, CAP_H)


def b64(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


ICONS = {
    "drop": (f'<svg width="150" height="150" viewBox="0 0 150 150"><circle cx="75" cy="75" r="75" fill="{C["cream"]}"/>'
             '<path d="M28 116 L96 54" stroke="#8A5A2B" stroke-width="10" stroke-linecap="round"/>'
             '<path d="M101 70 C101 70 85 90 85 101 A16 16 0 0 0 117 101 C117 90 101 70 101 70 Z" fill="#FFFFFF" '
             f'stroke="{C["maroon"]}" stroke-width="4"/></svg>'),
    "ribbon": (f'<svg width="150" height="150" viewBox="0 0 150 150"><circle cx="75" cy="75" r="75" fill="{C["cream"]}"/>'
               '<rect x="56" y="14" width="38" height="124" rx="6" fill="#7B5A3C"/>'
               f'<rect x="52" y="62" width="46" height="18" rx="4" fill="{C["red"]}"/>'
               f'<path d="M98 71 L124 54 L122 86 Z" fill="{C["red"]}"/><path d="M98 71 L116 104 L104 108 Z" fill="{C["red"]}"/>'
               f'<circle cx="98" cy="71" r="7" fill="#9E2416"/></svg>'),
}


def card_html(cd):
    if cd["kind"] == "compare":
        def row(img, big, small):
            return (f'<div style="display: flex; align-items: center; gap: 24px"><img src="{b64(img)}" style="width: 108px; '
                    f'height: 108px; border-radius: 999px; object-fit: cover; box-shadow: 0 0 0 5px {C["cream"]}">'
                    f'<div style="display: flex; flex-direction: column; gap: 4px"><div style="font-family: {DISPLAY}; '
                    f'font-weight: 800; font-size: 48px; line-height: 1.0; color: {C["cream"]}">{big}</div>'
                    f'<div style="font-family: {TYPE}; font-size: 31px; letter-spacing: 0.02em; color: {C["gold"]}">{small}</div>'
                    f'</div></div>')
        inner = (label_html(cd["label"]) + '<div style="display: flex; flex-direction: column; gap: 14px; margin-top: 12px">'
                 + "".join(row(*r) for r in cd["rows"]) + '</div>')
        return page(f'<div data-chk="1" style="position: absolute; left: 76px; top: 8px; width: 860px">{inner}</div>', W, CAP_H)
    if cd["kind"] == "text":
        sub = (f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 42px; line-height: 1.22; color: {C["gold"]}">'
               f'{cd["sub"]}</div>') if cd.get("sub") else ""
        inner = (f'{label_html(cd["label"]) if cd.get("label") else ""}<div style="font-family: {DISPLAY}; font-weight: 800; '
                 f'font-size: 60px; line-height: 1.04; color: {C["cream"]}; margin-top: 10px">{cd["html"]}</div>'
                 f'<div style="margin-top: 14px">{sub}</div>')
        return page(f'<div data-chk="1" style="position: absolute; left: 72px; top: 14px; width: 860px">{inner}</div>', W, CAP_H)
    inner = (f'<div style="display: flex; gap: 28px; align-items: flex-start">{ICONS[cd["icon"]]}'
             f'<div style="display: flex; flex-direction: column; gap: 10px; width: 680px">{label_html(cd["label"])}'
             f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.06; letter-spacing: -0.01em; '
             f'color: {C["cream"]}">{cd["html"]}</div></div></div>')
    return page(f'<div data-chk="1" style="position: absolute; left: 72px; top: 14px; width: 860px">{inner}</div>', W, CAP_H)


def caption_html(words, spoken, current):
    spans = []
    for i, w in enumerate(words):
        col = C["gold"] if (i == current) else (C["cream"] if i < spoken else DIM)
        spans.append(f'<span style="color: {col}">{w}</span>')
    return page(f'<div id="cap" data-chk="1" style="position: absolute; left: 72px; top: 20px; width: 860px; font-family: {DISPLAY}; '
                f'font-weight: 800; font-size: 64px; line-height: 1.12; letter-spacing: -0.01em">{" ".join(spans)}</div>', W, CAP_H)


def timeline(spec):
    t, segs = 0.0, []
    for s in spec["segs"]:
        d = round(s["b"] - s["a"] + s.get("freeze", 0), 3)
        segs.append(dict(s, off=round(t, 3), dur=d, real=round(s["b"] - s["a"], 3)))
        t += d
    return segs, round(t, 3)


def otime(segs, i, src_t):
    return segs[i]["off"] + (src_t - segs[i]["a"])


def snap(t):
    return round(t * FPS) / FPS


def phrases_for(segs, total):
    """Return list of phrases: dict(words=[...], times=[...]) on the output timeline."""
    out = []
    for i, s in enumerate(segs):
        if not s.get("key"):
            continue
        ws = [(w, t) for w, t in WORDS[s["key"]] if s["a"] <= t < s["b"]] + list(s.get("insert", []))
        ws.sort(key=lambda x: x[1])
        toks = [x for x in s["text"].split(" ") if x]
        flat = [x for x in toks if x != "|"]
        if len(flat) != len(ws):
            raise SystemExit(f"word count mismatch in {s['key']} {s['a']}: text {len(flat)} vs timed {len(ws)}\n"
                             f"timed: {' '.join(w for w, _ in ws)}")
        k, cur = 0, []
        for x in toks + ["|"]:
            if x == "|":
                if cur:
                    out.append(dict(words=[c[0] for c in cur], times=[c[1] for c in cur], seg=i))
                cur = []
                continue
            cur.append((x.replace(NB, "&nbsp;"), otime(segs, i, ws[k][1]) + SHIFT))
            k += 1
    return out


def caption_states(phr, total):
    """Timed states (t0, t1, phrase_idx, spoken_count, current_idx)."""
    states = []
    for p, ph in enumerate(phr):
        start = ph["times"][0] - 0.06
        nxt = phr[p + 1]["times"][0] - 0.06 if p + 1 < len(phr) else total
        end = min(ph["times"][-1] + 0.9, nxt - 0.02, total)
        n = len(ph["words"])
        for k in range(n):
            t0 = start if k == 0 else ph["times"][k]
            t1 = ph["times"][k + 1] if k + 1 < n else end
            hl = min(t1, t0 + 0.7)
            states.append((t0, hl, p, k, k))
            if t1 > hl + 0.01:
                states.append((hl, t1, p, k + 1, -1))
    # snap + fill gaps with blank
    timed, t = [], 0.0
    for t0, t1, p, sp, cu in states:
        t0, t1 = max(snap(t0), t), snap(t1)
        if t0 > t + 1e-6:
            timed.append((t, t0, None))
        if t1 > t0:
            timed.append((t0, t1, (p, sp, cu)))
            t = t1
    if t < total:
        timed.append((t, snap(total) + 1.0, None))
    return timed


def render_all(spec, segs, total, work):
    phr = phrases_for(segs, total)
    states = caption_states(phr, total)
    uniq = sorted({s[2] for s in states if s[2]})
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport=dict(width=W, height=H), device_scale_factor=1)

        def shot(html, path, w, h):
            pg.set_viewport_size(dict(width=w, height=h))
            pg.set_content(html)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(30)
            bad = pg.evaluate("""() => [...document.querySelectorAll('[data-chk]')].map(e => {const r = e.getBoundingClientRect();
                return (r.right > innerWidth - 40 || r.bottom > innerHeight - 4) ? `${Math.round(r.right)}x${Math.round(r.bottom)}` : null}).filter(Boolean)""")
            if bad:
                print("  OVERFLOW", path.name, bad)
            pg.screenshot(path=str(path), omit_background=True)
            return pg.evaluate("() => { const c = document.getElementById('cap'); return c ? c.getBoundingClientRect().height : 0 }")

        shot(base_html(spec), work / "base.png", W, H)
        shot(title_html(spec), work / "title.png", W, HEAD_H)
        for j, item in enumerate(spec["header"]):
            shot(fact_html(item), work / f"fact{j}.png", W, HEAD_H)
        if spec.get("cta"):
            shot(cta_html(spec), work / "cta.png", W, CAP_H)
        for j, cd in enumerate(spec.get("cards", [])):
            shot(card_html(cd), work / f"card{j}.png", W, CAP_H)
        shot(page("", W, CAP_H), work / "blank.png", W, CAP_H)
        # caption phrases: check line count once per phrase
        for p, ph in enumerate(phr):
            hgt = shot(caption_html(ph["words"], len(ph["words"]), -1), work / f"_full{p}.png", W, CAP_H)
            if hgt > 150:
                print(f"  3+ LINES: phrase {p}: {' '.join(ph['words'])}")
        names = {}
        for (p, sp, cu) in uniq:
            f = work / f"cap_{p:03d}_{sp:02d}_{cu:+03d}.png"
            shot(caption_html(phr[p]["words"], sp, cu), f, W, CAP_H)
            names[(p, sp, cu)] = f
        br.close()
    with open(work / "caps.ffconcat", "w") as fh:
        fh.write("ffconcat version 1.0\n")
        last = None
        for t0, t1, key in states:
            f = names[key] if key else work / "blank.png"
            fh.write(f"file '{f}'\nduration {t1 - t0:.4f}\n")
            last = f
        fh.write(f"file '{last}'\n")
    json.dump([dict(words=p["words"], times=[round(t, 2) for t in p["times"]]) for p in phr], open(work / "phrases.json", "w"), indent=0)
    return phr


def seg_loudness(s):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-ss", f"{s['a']}", "-t", f"{s['real']}", "-i", s["src"],
                        "-af", "highpass=f=80,ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float([l for l in e.splitlines() if l.strip().startswith("I:")][-1].split()[1])


def build_audio(spec, segs, total, work):
    """Each segment is gain-matched (speech to -16 LUFS, ambience to -32), faded, concatenated and limited."""
    if all(s.get("mute") for s in segs):
        out = work / "voice.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", f"{total}", "-i", "anullsrc=r=48000:cl=stereo",
                        str(out)], check=True)
        print("  audio: silent")
        return out
    args, fl = ["ffmpeg", "-v", "error", "-y"], []
    for i, s in enumerate(segs):
        if s.get("mute"):
            args += ["-f", "lavfi", "-t", f"{s['dur']}", "-i", "anullsrc=r=48000:cl=mono"]
            fl.append(f"[{i}:a]atrim=duration={s['dur']},asetpts=PTS-STARTPTS[a{i}]")
        else:
            I = seg_loudness(s)
            target = s.get("target", -32.0 if s.get("vol") else -16.0)
            g = 0.0 if spec.get("uniform") else min(target - I, 20.0)
            print(f"  seg {i}: {I:.1f} LUFS -> gain {g:+.1f} dB")
            args += ["-ss", f"{s['a']}", "-t", f"{s['real']}", "-i", s["src"]]
            fo = 0.6 if s.get("freeze") else 0.07
            pad = f",apad=pad_dur={s['freeze']}" if s.get("freeze") else ""
            fl.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=mono,atrim=duration={s['real']},asetpts=PTS-STARTPTS,"
                      f"highpass=f=80,volume={g:.2f}dB,afade=t=in:d=0.03,afade=t=out:st={s['real'] - fo:.3f}:d={fo}{pad}[a{i}]")
    fl.append("".join(f"[a{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1,highpass=f=80[out]")
    raw = work / "voice_raw.wav"
    subprocess.run(args + ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "48000", "-c:a", "pcm_f32le", str(raw)], check=True)
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "ebur128=peak=true", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    I = float([l for l in meas.splitlines() if l.strip().startswith("I:")][-1].split()[1])
    gain = spec.get("final_target", -16.0) - I
    out = work / "voice.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af",
                    f"volume={gain:.2f}dB,alimiter=limit=0.84:attack=5:release=60:level=disabled,pan=stereo|c0=c0|c1=c0",
                    "-ar", "48000", str(out)], check=True)
    print(f"  audio: measured {I:.1f} LUFS, gain {gain:+.1f} dB")
    return out


def prep_segments(spec, segs, work, force=False):
    for i, s in enumerate(segs):
        out = work / f"seg{i}.mp4"
        if out.exists() and not force:
            continue
        crop = s.get("crop", "1440:1080:240:0")
        frz = f",tpad=stop_mode=clone:stop_duration={s['freeze']}" if s.get("freeze") else ""
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s['a']}", "-t", f"{s['real']}", "-i", s["src"], "-an",
                        "-vf", f"fps={FPS},crop={crop},scale={WIN['w']}:{WIN['h']}:flags=lanczos,setsar=1,format=yuv420p,"
                               f"trim=duration={s['real']},setpts=PTS-STARTPTS{frz}",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "12", "-pix_fmt", "yuv420p", str(out)], check=True)
        print(f"  prepped seg{i}.mp4 ({s['dur']:.2f} s)")


def sheets(work, nsegs, step=1.0):
    """Annotation sheets: one frame per `step` seconds, 100-px grid in window coordinates (1000x750)."""
    from PIL import Image, ImageDraw, ImageFont
    import cv2
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    for i in range(nsegs):
        cap = cv2.VideoCapture(str(work / f"seg{i}.mp4"))
        fps = cap.get(cv2.CAP_PROP_FPS) or FPS
        nfr = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        tiles, t = [], 0.0
        while int(t * fps) < nfr:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * fps))
            ok, fr = cap.read()
            if not ok:
                break
            im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB))
            d = ImageDraw.Draw(im)
            for x in range(100, 1000, 100):
                d.line([(x, 0), (x, 750)], fill=(255, 255, 0), width=1)
                d.text((x + 3, 3), str(x), fill=(255, 255, 0), font=f)
            for y in range(100, 750, 100):
                d.line([(0, y), (1000, y)], fill=(0, 255, 255), width=1)
                d.text((3, y + 3), str(y), fill=(0, 255, 255), font=f)
            d.rectangle((900, 700, 1000, 750), fill="black"); d.text((908, 712), f"{t:.1f}s", fill="white", font=f)
            tiles.append(im.resize((500, 375)))
            t += step
        cols = 4
        rows = (len(tiles) + cols - 1) // cols
        S = Image.new("RGB", (cols * 504, rows * 379), "white")
        for k, im in enumerate(tiles):
            S.paste(im, ((k % cols) * 504, (k // cols) * 379))
        S.save(work / f"sheet_seg{i}.jpg", quality=80)
        print(f"  sheet_seg{i}.jpg: {len(tiles)} frames")


def build_video(spec, segs, total, work, out, draft=False):
    args, fl, n = ["ffmpeg", "-v", "error", "-y"], [], 0
    for i, s in enumerate(segs):
        sb, sp = work / f"seg{i}b.mp4", work / f"seg{i}.mp4"
        src = sb if sb.exists() else sp
        print(f"  seg {i}: using {src.name}")
        args += ["-i", str(src)]
        fl.append(f"[{i}:v]setpts=PTS-STARTPTS,format=yuv420p,trim=duration={s['dur']}[v{i}]")
        n += 1
    fl.append("".join(f"[v{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=0[vc]")
    loop = lambda p: ["-loop", "1", "-framerate", str(FPS), "-t", f"{total}", "-i", str(p)]
    args += loop(work / "base.png"); ib = n; n += 1
    fl.append(f"color=c=0x7A1E1A:s={W}x{H}:r={FPS}:d={total}[bg]")
    fl.append(f"[bg][vc]overlay={WIN['x']}:{WIN['y']}:eof_action=repeat[s0]")
    fl.append(f"[s0][{ib}:v]overlay=0:0[s1]")
    cur = "s1"
    # header windows: title fills the gaps between fact cards
    facts = [(snap(otime(segs, it["seg"], it["a"])), total if it.get("b") is None else snap(otime(segs, it["seg"], it["b"])),
              f"fact{j}.png") for j, it in enumerate(spec["header"])]
    wins, t = [], 0.0
    for a, b, f in facts:
        if a > t:
            wins.append((t, a, "title.png"))
        wins.append((a, b, f))
        t = b
    if t < total - 0.01:
        wins.append((t, total, "title.png"))
    F = 0.25
    for k, (a, b, f) in enumerate(wins):
        args += loop(work / f); idx = n; n += 1
        fades = []
        if a > 0:
            fades.append(f"fade=t=in:st={a:.3f}:d={F}:alpha=1")
        if b < total - 0.01:
            fades.append(f"fade=t=out:st={b - F:.3f}:d={F}:alpha=1")
        fl.append(f"[{idx}:v]format=rgba{',' if fades else ''}{','.join(fades)}[h{k}]")
        fl.append(f"[{cur}][h{k}]overlay=0:{HEAD_Y}:enable='between(t,{a:.3f},{b:.3f})'[x{k}]")
        cur = f"x{k}"
    for j, cd in enumerate(spec.get("cards", [])):
        a, b = snap(otime(segs, cd["seg"], cd["a"])), snap(otime(segs, cd["bseg"], cd["b"]))
        args += loop(work / f"card{j}.png"); idx = n; n += 1
        fl.append(f"[{idx}:v]format=rgba,fade=t=in:st={a:.3f}:d={F}:alpha=1,fade=t=out:st={b - F:.3f}:d={F}:alpha=1[k{j}]")
        fl.append(f"[{cur}][k{j}]overlay=0:{CAP_Y}:enable='between(t,{a:.3f},{b:.3f})'[y{j}]")
        cur = f"y{j}"
        wins.append((a, b, f"card{j}.png"))
    args += ["-f", "concat", "-safe", "0", "-i", str(work / "caps.ffconcat")]; ic = n; n += 1
    fl.append(f"[{ic}:v]fps={FPS},format=rgba[cap]")
    fl.append(f"[{cur}][cap]overlay=0:{CAP_Y}:eof_action=pass[c1]")
    if spec.get("cta"):
        tc = snap(otime(segs, spec["cta"]["seg"], segs[spec["cta"]["seg"]]["a"] + spec["cta"]["a"]))
        args += loop(work / "cta.png"); it = n; n += 1
        fl.append(f"[{it}:v]format=rgba,fade=t=in:st={tc:.3f}:d=0.35:alpha=1[cta]")
        fl.append(f"[c1][cta]overlay=0:{CAP_Y}:enable='gte(t,{tc:.3f})',format=yuv420p[vout]")
    else:
        tc = None
        fl.append("[c1]format=yuv420p[vout]")
    args += ["-i", str(work / "voice.wav")]; ia = n; n += 1
    enc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "30" if draft else "20"]
    args += ["-filter_complex", ";".join(fl), "-map", "[vout]", "-map", f"{ia}:a", *enc, "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-t", f"{total}", "-movflags", "+faststart",
             "-map_metadata", "-1", "-map_metadata:s:v", "-1", "-map_metadata:s:a", "-1", "-map_chapters", "-1",
             "-metadata", "title=", "-metadata:s:v", "handler_name=", "-metadata:s:a", "handler_name=", str(out)]
    subprocess.run(args, check=True)
    return wins, tc


def main():
    key = sys.argv[1]
    draft = "--draft" in sys.argv
    spec = REELS[key]
    work = ROOT / "reels" / key
    work.mkdir(parents=True, exist_ok=True)
    for f in list(work.glob("*.png")) + list(work.glob("*.ffconcat")):
        f.unlink()
    segs, total = timeline(spec)
    print(f"{spec['name']}: {total:.2f} s, {len(segs)} segments")
    prep_segments(spec, segs, work, force="--reprep" in sys.argv)
    if "--prep" in sys.argv:
        sheets(work, len(segs))
        return
    phr = render_all(spec, segs, total, work)
    build_audio(spec, segs, total, work)
    out = work / f"{spec['name']}.mp4"
    wins, tc = build_video(spec, segs, total, work, out, draft)
    json.dump(dict(total=total, segs=[{k: v for k, v in s.items() if k != "text"} for s in segs], header=wins, cta=tc),
              open(work / "timeline.json", "w"), indent=1)
    print("  header windows:", [(round(a, 2), round(b, 2), f) for a, b, f in wins], "cta at", tc)
    print("  wrote", out)


if __name__ == "__main__":
    main()
