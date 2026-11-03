"""Report any location / device / date metadata in images, videos and zip contents."""
import sys, os, io, zipfile, subprocess, json, struct
from PIL import Image
GPS_HINTS = [b"\xa9xyz", b"ISO6709", b"com.apple.quicktime.location", b"GPSLatitude", b"<exif:GPS", b"photoshop:City", b"Iptc4xmpCore:Location"]

def check_image_bytes(name, data):
    out = []
    try:
        im = Image.open(io.BytesIO(data))
        ex = im.getexif()
        if ex:
            gps = ex.get_ifd(0x8825)
            if gps: out.append(f"GPS IFD ({len(gps)} tags)")
            tags = {k: v for k, v in ex.items() if k in (0x010F, 0x0110, 0x0132)}
            if tags: out.append("EXIF device/date " + ", ".join(str(v)[:24] for v in tags.values()))
        info_keys = [k for k in im.info.keys() if k not in ("dpi", "gamma", "srgb", "icc_profile", "transparency", "aspect", "jfif", "jfif_version", "jfif_unit", "jfif_density", "progressive", "progression", "adobe", "adobe_transform")]
        if info_keys: out.append("info keys " + ",".join(map(str, info_keys)))
    except Exception as e:
        out.append(f"(unreadable: {e})")
    for h in GPS_HINTS:
        if h in data: out.append(f"contains {h!r}")
    return out

def check_video(path):
    out = []
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format_tags:stream_tags", "-of", "json", path], capture_output=True, text=True)
    j = json.loads(r.stdout or "{}")
    tags = dict(j.get("format", {}).get("tags", {}))
    for s in j.get("streams", []): tags.update({f"s:{k}": v for k, v in s.get("tags", {}).items()})
    bad = {k: v for k, v in tags.items() if any(x in k.lower() for x in ("location", "creation", "make", "model", "date", "xyz", "gps"))}
    if bad: out.append("tags " + json.dumps(bad)[:200])
    data = open(path, "rb").read()
    for h in GPS_HINTS:
        if h in data: out.append(f"contains {h!r}")
    return out

def walk(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                for f in sorted(files): yield os.path.join(root, f)
        else:
            yield p

problems, n = 0, 0
for path in walk(sys.argv[1:]):
    ext = path.lower().rsplit(".", 1)[-1]
    res = []
    if ext in ("jpg", "jpeg", "png", "webp", "heic"):
        res = check_image_bytes(path, open(path, "rb").read())
    elif ext in ("mp4", "mov", "m4v"):
        res = check_video(path)
    elif ext == "zip":
        with zipfile.ZipFile(path) as z:
            for zi in z.infolist():
                e2 = zi.filename.lower().rsplit(".", 1)[-1]
                if e2 in ("jpg", "jpeg", "png"):
                    r2 = check_image_bytes(zi.filename, z.read(zi))
                    n += 1
                    if r2: problems += 1; print(f"!! {path} :: {zi.filename}: {'; '.join(r2)}")
        continue
    else:
        continue
    n += 1
    if res:
        problems += 1
        print(f"!! {path}: {'; '.join(res)}")
print(f"checked {n} files, {problems} with metadata")
