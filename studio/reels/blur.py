#!/usr/bin/env python3
"""Blur houses in pre-rendered Reel segments (1000x750).

Each house is annotated once per segment: {"t": seconds, "box": [x0, y0, x1, y1]} in window pixels. The camera's
own motion (pans, zoom, shake) is estimated frame to frame, so the box follows the house through the whole segment.

usage: blur.py reelN            -> writes reels/reelN/segXb.mp4 for every annotated segment
       blur.py reelN --check    -> contact sheets with the tracked boxes drawn, no video written
"""
import json, subprocess, sys
from pathlib import Path
import cv2
import numpy as np

ROOT = Path("/home/claude/mt/reels")
SIGMA = 7.0          # blur strength (px at 1000 px width): softens, does not smear
FEATHER = 22         # soft edge width (px)
PAD = 10             # grow every box a little


def motion(path):
    """Cumulative 2x3 similarity transforms: frame 0 coords -> frame t coords."""
    cap = cv2.VideoCapture(str(path))
    prev, mats, frames = None, [], 0
    acc = np.eye(3)
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        if prev is None:
            mats.append(acc.copy())
        else:
            p0 = cv2.goodFeaturesToTrack(prev, maxCorners=900, qualityLevel=0.01, minDistance=8)
            m = None
            if p0 is not None and len(p0) > 20:
                p1, st, _ = cv2.calcOpticalFlowPyrLK(prev, g, p0, None, winSize=(21, 21), maxLevel=4)
                good = st.ravel() == 1
                if good.sum() > 20:
                    m, inl = cv2.estimateAffinePartial2D(p0[good], p1[good], method=cv2.RANSAC, ransacReprojThreshold=2.5)
            step = np.eye(3)
            if m is not None:
                step[:2] = m
            acc = step @ acc
            mats.append(acc.copy())
        prev = g
        frames += 1
    return mats


def boxes_at(anns, mats, fps, k):
    out = []
    n = len(mats)
    t = k / fps
    for a in anns:
        if "lerp" in a:                                   # moving object: box keyframes, linear in time
            kf = a["lerp"]
            if not (kf[0][0] <= t <= kf[-1][0]):
                continue
            for (t0, *b0), (t1, *b1) in zip(kf, kf[1:]):
                if t0 <= t <= t1:
                    u = 0 if t1 == t0 else (t - t0) / (t1 - t0)
                    b = [v0 + (v1 - v0) * u for v0, v1 in zip(b0, b1)]
                    out.append((int(max(b[0], 0)), int(max(b[1], 0)), int(min(b[2], 1000)), int(min(b[3], 750))))
                    break
            continue
        if not (a.get("from", -1) <= t <= a.get("to", 1e9)):
            continue
        if "band" in a:                                   # full-width band; follows vertical motion and zoom only
            ka = min(int(round(a["t"] * fps)), n - 1)
            T = mats[k] @ np.linalg.inv(mats[ka])
            y0, y1 = a["band"]
            q = T @ np.array([[500, 500], [y0, y1], [1, 1]], float)
            out.append((0, int(max(q[1, 0] - (PAD if y0 > 0 else 0), 0)), 1000, int(min(q[1, 1] + PAD, 750))))
            continue
        if a.get("static"):
            x0, y0, x1, y1 = a["box"]
            out.append((x0, y0, x1, y1))
            continue
        ka = min(int(round(a["t"] * fps)), n - 1)
        T = mats[k] @ np.linalg.inv(mats[ka])
        x0, y0, x1, y1 = a["box"]
        pts = np.array([[x0, y0, 1], [x1, y0, 1], [x1, y1, 1], [x0, y1, 1]], float).T
        q = (T @ pts)[:2].T
        bx0, by0 = q.min(0) - PAD
        bx1, by1 = q.max(0) + PAD
        if bx1 < 0 or by1 < 0 or bx0 > 1000 or by0 > 750:
            continue
        out.append((int(max(bx0, 0)), int(max(by0, 0)), int(min(bx1, 1000)), int(min(by1, 750))))
    return out


def apply(fr, boxes):
    if not boxes:
        return fr
    mask = np.zeros(fr.shape[:2], np.float32)
    for x0, y0, x1, y1 in boxes:
        mask[y0:y1, x0:x1] = 1.0
    mask = cv2.GaussianBlur(mask, (0, 0), FEATHER / 2.5)
    mask = np.clip(mask * 1.6, 0, 1)[..., None]       # solid inside, soft at the edges
    bl = cv2.GaussianBlur(fr, (0, 0), SIGMA)
    return (fr * (1 - mask) + bl * mask).astype(np.uint8)


def main():
    reel = sys.argv[1]
    check = "--check" in sys.argv
    work = ROOT / reel
    ann = json.load(open(ROOT / "blur" / f"{reel}.json"))
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    for seg, anns in ann.items():
        if only and seg not in only:
            continue
        src = work / f"{seg}.mp4"
        cap = cv2.VideoCapture(str(src))
        fps = cap.get(cv2.CAP_PROP_FPS)
        mats = motion(src)
        n = len(mats)
        if check:
            from PIL import Image, ImageDraw, ImageFont
            f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
            tiles = []
            step = max(1, int(fps * (0.5 if n / fps < 8 else 1.0)))
            for k in range(0, n, step):
                cap.set(cv2.CAP_PROP_POS_FRAMES, k)
                ok, fr = cap.read()
                if not ok:
                    break
                fr = apply(fr, boxes_at(anns, mats, fps, k))
                im = Image.fromarray(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB))
                d = ImageDraw.Draw(im)
                for b in boxes_at(anns, mats, fps, k):
                    d.rectangle(b, outline=(255, 0, 255), width=3)
                d.rectangle((880, 700, 1000, 750), fill="black"); d.text((890, 712), f"{k / fps:.1f}s", fill="white", font=f)
                tiles.append(im.resize((500, 375)))
            cols = 4
            S = Image.new("RGB", (cols * 504, ((len(tiles) + cols - 1) // cols) * 379), "white")
            for i, im in enumerate(tiles):
                S.paste(im, ((i % cols) * 504, (i // cols) * 379))
            S.save(work / f"check_{seg}.jpg", quality=80)
            print(f"{reel} {seg}: check sheet, {len(tiles)} frames")
            continue
        out = work / f"{seg}b.mp4"
        tmp = work / f"{seg}b.part.mp4"
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", "1000x750",
                                "-r", str(fps), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "12",
                                "-pix_fmt", "yuv420p", str(tmp)], stdin=subprocess.PIPE)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        k = 0
        while True:
            ok, fr = cap.read()
            if not ok:
                break
            enc.stdin.write(apply(fr, boxes_at(anns, mats, fps, min(k, n - 1))).tobytes())
            k += 1
        enc.stdin.close(); enc.wait()
        if enc.returncode == 0:
            tmp.replace(out)
        print(f"{reel} {seg}: wrote {out.name} ({k} frames)", flush=True)


if __name__ == "__main__":
    main()
