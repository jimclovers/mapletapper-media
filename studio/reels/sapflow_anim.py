#!/usr/bin/env python3
"""Animated "What makes sap run?" Reel (1080x1920, 30 fps, ~36 s). Same facts and drawing as studio/sapflow02.py.
Frames are rendered by setting a time t in the page (window.render(t)) and screenshotting with system Chrome.
Usage: sapflow_anim.py [--draft] [--audio voice.mp3]
"""
import base64
import math
import os
import subprocess
import sys

from playwright.sync_api import sync_playwright

STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(STUDIO)
OUT = os.path.join(ROOT, "reels", "reel7")
os.makedirs(OUT, exist_ok=True)
NAME = "MapleTapper-Reel-SapFlow"
W, H, FPS, DUR = 1080, 1920, 30, 36.0
FONT = os.path.join(STUDIO, "fonts", "node_modules")
FONTS = (f"@font-face{{font-family:'Bricolage Grotesque';src:url('file://{FONT}/@fontsource-variable/bricolage-grotesque/files/"
         f"bricolage-grotesque-latin-standard-normal.woff2') format('woff2');font-weight:200 800;}}"
         f"@font-face{{font-family:'Special Elite';src:url('file://{FONT}/@fontsource/special-elite/files/special-elite-latin-400-normal.woff2') format('woff2');}}")
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(STUDIO, "assets", "logo.png"), "rb").read()).decode()
SY = 600   # scene top on the page

BRANCHES = [(540, 300, 380, 120, 26), (540, 300, 700, 110, 26), (540, 260, 540, 20, 24), (450, 200, 330, 190, 12), (410, 150, 400, 40, 10),
            (630, 190, 770, 200, 12), (670, 140, 690, 30, 10), (540, 120, 470, 50, 9), (540, 120, 610, 40, 9), (380, 120, 300, 90, 8),
            (700, 110, 790, 80, 8), (540, 340, 300, 290, 14), (540, 340, 790, 280, 14)]


def tree():
    br = "".join(f'<path d="M{a} {b} Q{(a + c) / 2 + (c - a) * 0.1} {(b + d) / 2 - 20} {c} {d}" fill="none" style="stroke-width:{w};stroke-linecap:round"></path>'
                 for a, b, c, d, w in BRANCHES)
    trunk = ('<path d="M512 230 Q540 210 568 230 L585 330 L600 700 Q640 760 720 780 L660 786 Q615 778 598 760 L606 800 L474 800 L482 760 '
             'Q465 778 420 786 L360 780 Q440 760 480 700 L495 330 Z"></path>')
    return br + trunk


def person(p=715):
    return (f'<ellipse cx="{p + 45}" cy="868" rx="85" ry="10" fill="#000" opacity=".08"></ellipse>'
            f'<rect x="{p + 20}" y="760" width="26" height="100" rx="10" fill="#2E3A4E"></rect>'
            f'<rect x="{p + 52}" y="760" width="26" height="100" rx="10" fill="#26303F"></rect>'
            f'<path d="M{p + 12} 860 h40 v14 h-46 z M{p + 48} 860 h40 v14 h-44 z" fill="#3B2A1E"></path>'
            f'<path d="M{p + 8} 640 Q{p + 48} 618 {p + 90} 640 L{p + 96} 775 L{p + 2} 775 Z" fill="#C8321F"></path>'
            f'<path d="M{p + 48} 640 L{p + 48} 775" stroke="#9E2617" style="stroke-width:3"></path>'
            f'<path d="M{p + 14} 660 Q{p - 30} 668 {p - 50} 690" fill="none" stroke="#C8321F" style="stroke-width:24;stroke-linecap:round"></path>'
            f'<circle cx="{p - 52}" cy="692" r="12" fill="#3B2A1E"></circle>'
            f'<circle cx="{p + 48}" cy="602" r="32" fill="#E8B58F"></circle>'
            f'<path d="M{p + 15} 598 Q{p + 48} 545 {p + 81} 598 Z" fill="#F4B63F"></path>'
            f'<rect x="{p + 13}" y="590" width="70" height="14" rx="6" fill="#7A1E1A"></rect>'
            f'<circle cx="{p + 48}" cy="560" r="9" fill="#7A1E1A"></circle>'
            f'<path d="M{p + 18} 618 q30 18 60 0" fill="none" stroke="#F4B63F" style="stroke-width:12"></path>')


def arrow(i, cls):
    return (f'<path class="{cls}" id="{cls}{i}" d="M0 -23 L0 23 M-13 -8 L0 -23 L13 -8" fill="none" '
            f'style="stroke-width:8;stroke-linecap:round;stroke-linejoin:round"></path>')


def page():
    stars = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff"></circle>' for x, y, r in
                    ((70, 60, 3), (160, 30, 2), (250, 90, 2.5), (330, 40, 2), (420, 110, 3), (110, 150, 2), (470, 30, 2),
                     (640, 50, 2.5), (760, 120, 2), (880, 40, 3), (990, 100, 2), (820, 200, 2)))
    frost = "".join(f'<g transform="translate({x} {y})" stroke="#fff" style="stroke-width:3;stroke-linecap:round"><path d="M-8 0 L8 0 M0 -8 L0 8 M-6 -6 L6 6 M-6 6 L6 -6"></path></g>'
                    for x, y in ((515, 360), (565, 430), (510, 520), (570, 600), (520, 680), (560, 300), (505, 610)))
    water = "".join(f'<circle class="wd" cx="0" cy="0" r="8" fill="#6FB3E6"></circle>' for _ in range(6))
    svg = f'''
<svg id="scene" width="1080" height="960" viewBox="0 0 1080 960" style="position:absolute;left:0;top:{SY}px">
 <defs><clipPath id="L"><rect x="0" y="0" width="540" height="960"/></clipPath><clipPath id="R"><rect x="540" y="0" width="540" height="960"/></clipPath></defs>
 <rect id="bgL" x="0" y="-480" width="540" height="1440"/><rect id="bgR" x="540" y="-480" width="540" height="1440"/>
 <g id="stars">{stars}</g>
 <g id="moon"><path d="M44 6 A26 26 0 1 0 58 48 A20 20 0 1 1 44 6 Z" fill="#FFF5DE" transform="translate(300 40) scale(1.3)"/></g>
 <g id="sun"><g transform="translate(0 0)">{"".join(f'<path d="M0 0 L{38 * math.cos(a * math.pi / 6):.1f} {38 * math.sin(a * math.pi / 6):.1f}" stroke="#F4B63F" style="stroke-width:6;stroke-linecap:round"/>' for a in range(12))}<circle r="22" fill="#F4B63F"/></g></g>
 <path id="gL" d="M0 760 Q270 730 540 745 L540 960 L0 960 Z"/><path id="gR" d="M540 745 Q810 735 1080 760 L1080 960 L540 960 Z"/>
 <g clip-path="url(#L)" id="treeL">{tree()}</g><g clip-path="url(#R)" id="treeR">{tree()}</g>
 {"".join(f'<path d="M{x} 320 L{x + 2} 760" stroke="#000" style="stroke-width:3;opacity:.12"/>' for x in (505, 525, 560, 578))}
 {"".join(f'<path d="{d}" fill="none" stroke="#8C6A52" style="stroke-width:12;stroke-linecap:round;opacity:.85"/>' for d in ("M500 800 Q440 840 360 870", "M540 800 Q545 860 530 920", "M580 800 Q640 840 720 870"))}
 <g id="water">{water}</g>
 <g id="frost">{frost}</g>
 <g id="upA" stroke="#CFE8FA">{"".join(arrow(i, "u") for i in range(5))}</g>
 <g id="dnA" stroke="#FFF5DE">{"".join(arrow(i, "d") for i in range(5))}</g>
 <rect x="596" y="612" width="34" height="11" rx="3" fill="#2A2A2A"/>
 <clipPath id="B"><path d="M612 626 L606 696 L668 696 L662 626 Z"/></clipPath>
 <path d="M612 626 L606 696 L668 696 L662 626 Z" fill="#B9C3CC" stroke="#7D8A96" style="stroke-width:3"/>
 <rect id="fill" x="600" y="696" width="80" height="0" fill="#D9ECF8" clip-path="url(#B)"/>
 <path d="M608 626 L666 626" stroke="#7D8A96" style="stroke-width:5"/>
 <path id="drop" d="M0 -8 q5 9 0 14 q-5 -5 0 -14" fill="#7FC0EC"/>
 <g id="person">{person()}</g>
 <path id="split" d="M540 0 L540 960" stroke="#fff" style="stroke-width:3;opacity:.6" stroke-dasharray="10 10"/>
</svg>'''
    css = (f"{FONTS} html,body{{margin:0}} #root{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#FFF5DE}}"
           f" .cap{{position:absolute;left:64px;right:64px;top:150px;font-family:'Bricolage Grotesque';color:#7A1E1A}}"
           f" .cap h2{{margin:0;font-weight:800;font-size:86px;line-height:.98;letter-spacing:-.02em}}"
           f" .cap p{{margin:16px 0 0;font-weight:600;font-size:43px;line-height:1.22}}"
           f" .k{{font-family:'Special Elite';font-size:30px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:12px}}")
    caps = {
        "c0": ("Sugarmaker’s Almanac", 'What makes <span style="color:#C8321F">sap run?</span>', "It’s all about the weather."),
        "c1": ("Night · in the 20s °F", 'The tree <span style="color:#C8321F">soaks it up.</span>', "Ice squeezes tiny air pockets in the wood. That suction pulls water up from the roots."),
        "c2": ("Day · in the 40s °F", 'The sap <span style="color:#C8321F">runs out.</span>', "The ice melts, the squeezed air pushes back, and sap flows down and out the spout."),
        "c3": ("Every day of sap season", 'Freeze, thaw, <span style="color:#C8321F">repeat.</span>', "Every cold night refills the tree. Every warm day lets it run."),
    }
    capdivs = "".join(f'<div class="cap" id="{k}" style="opacity:0"><div class="k">{a}</div><h2>{b}</h2><p>{c}</p></div>' for k, (a, b, c) in caps.items())
    ground = '<div id="below" style="position:absolute;left:0;top:1560px;width:1080px;height:360px"></div>'
    end = (f'<div id="end" style="position:absolute;inset:0;background:#7A1E1A;opacity:0;display:flex;flex-direction:column;align-items:center;'
           f'justify-content:center;gap:40px;font-family:Bricolage Grotesque;color:#FFF5DE;text-align:center">'
           f'<div style="font-weight:800;font-size:96px;line-height:1">That’s<br><span style="color:#F4B63F">sap season!</span></div>'
           f'<div id="badge" style="background:#FFF5DE;border-radius:44px;padding:26px 30px"><img src="{LOGO}" style="width:340px;display:block"></div>'
           f'<div style="font-family:Special Elite;font-size:34px;letter-spacing:.06em;text-transform:uppercase">Get ready at mapletapper.com</div></div>')
    js = r'''
const NIGHT=[27,47,80], DAY=[191,224,244], GN=[221,230,242], GD=[255,255,255], BN=[60,53,80], BD=[122,82,54];
const mix=(a,b,k)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*k)).join(',')})`;
const cl=(x)=>Math.max(0,Math.min(1,x)); const ease=(x)=>x*x*(3-2*x);
const $=(id)=>document.getElementById(id);
function seg(t,a,b,f=0.6){return cl(Math.min((t-a)/f,(b-t)/f));}
window.render=function(t){
  // day amount: 0 night, 1 day. split mode in title + repeat segments
  let dayK = t<4?0.5 : t<14?0 : t<15.5?ease((t-14)/1.5) : t<25?1 : 0.5;
  const split = (t<4.0)||(t>=25);
  const kL = split?0:dayK, kR = split?1:dayK;
  $('bgL').setAttribute('fill',mix(NIGHT,DAY,kL)); $('bgR').setAttribute('fill',mix(NIGHT,DAY,kR));
  $('gL').setAttribute('fill',mix(GN,GD,kL)); $('gR').setAttribute('fill',mix(GN,GD,kR));
  $('treeL').setAttribute('fill',mix(BN,BD,kL)); $('treeL').setAttribute('stroke',mix(BN,BD,kL));
  $('treeR').setAttribute('fill',mix(BN,BD,kR)); $('treeR').setAttribute('stroke',mix(BN,BD,kR));
  $('below').style.background = split? 'linear-gradient(90deg,#DDE6F2 50%,#fff 50%)' : mix(GN,GD,dayK);
  $('split').style.opacity = split?0.6:0;
  $('stars').style.opacity = split?1:(1-dayK); $('stars').setAttribute('clip-path', split?'url(#L)':'');
  $('moon').style.opacity = split?1:(1-dayK);
  // sun rises on the right during the day segment
  const sunUp = split?1:dayK; $('sun').firstElementChild.setAttribute('transform',`translate(820 ${260-190*sunUp})`); $('sun').style.opacity = split?1:dayK;
  // night arrows + frost + water uptake
  const nightOn = split?1:(1-dayK), dayOn = split?1:dayK;
  $('upA').style.opacity = (t<4)?0.0:nightOn; $('dnA').style.opacity = (t<4)?0.0:dayOn;
  $('frost').style.opacity = ((t<4)?0:nightOn)*(0.6+0.4*Math.sin(t*5));
  for(let i=0;i<5;i++){ const y=760-((t*90+i*96)%480); const a=$('u'+i); a.setAttribute('transform',`translate(515 ${y})`); a.style.opacity=cl(Math.min((760-y)/60,(y-300)/60)); }
  for(let i=0;i<5;i++){ const y=300+((t*90+i*96)%330); const a=$('d'+i); a.setAttribute('transform',`translate(565 ${y}) rotate(180)`); a.style.opacity=cl(Math.min((y-300)/60,(630-y)/60)); }
  const wd=document.querySelectorAll('.wd'); const roots=[[360,870,500,800],[530,920,540,800],[720,870,580,800]];
  wd.forEach((c,i)=>{const r=roots[i%3]; const k=((t*0.45+i*0.17)%1); c.setAttribute('cx',r[0]+(r[2]-r[0])*k); c.setAttribute('cy',r[1]+(r[3]-r[1])*k); c.style.opacity=((t<4)?0:nightOn)*cl(Math.min(k/0.15,(1-k)/0.15));});
  // drips + bucket filling during day
  const dk=(t*1.6)%1; $('drop').setAttribute('transform',`translate(626 ${630+62*dk})`); $('drop').style.opacity=((t<4)?0:dayOn)*cl((1-dk)/0.2);
  const fillH = t<14?6 : t<25? 6+48*cl((t-14)/11) : 54; $('fill').setAttribute('y',696-fillH); $('fill').setAttribute('height',fillH);
  $('person').style.opacity = 1;
  // captions
  [['c0',-1,4.0],['c1',4.0,14.0],['c2',14.0,25.0],['c3',25.0,31.0]].forEach(([id,a,b])=>{$(id).style.opacity=seg(t,a,b,0.5);});
  // end card
  const e=cl((t-31)/0.6); $('end').style.opacity=e; const s=t<31.6?0.6+0.5*cl((t-31)/0.45):1+0.08*Math.max(0,1-(t-31.6)/0.25)-0.08; $('badge').style.transform=`scale(${Math.min(1.08,s)})`;
};
'''
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body><div id='root'>{ground}{svg}{capdivs}{end}</div>"
            f"<script>{js}</script></body></html>")


def main():
    draft = "--draft" in sys.argv
    audio = sys.argv[sys.argv.index("--audio") + 1] if "--audio" in sys.argv else None
    html = os.path.join(OUT, "sapflow_anim.html")
    open(html, "w").write(page())
    out = os.path.join(OUT, NAME + ("-voice" if audio else "") + ".mp4")
    n = int(DUR * FPS)
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-"]
    if audio:
        cmd += ["-i", audio, "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "160k", "-shortest"]
    else:
        cmd += ["-f", "lavfi", "-t", str(DUR), "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-shortest"]
    cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "26" if draft else "19", "-g", "60", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", "-map_metadata", "-1", out]
    enc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport=dict(width=W, height=H))
        pg.goto("file://" + html)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        for i in range(n):
            pg.evaluate(f"render({i / FPS})")
            enc.stdin.write(pg.screenshot(type="jpeg", quality=92))
            if i == int(6 * FPS):
                pg.screenshot(path=os.path.join(OUT, NAME + "-cover.jpg"), type="jpeg", quality=90)
        b.close()
    enc.stdin.close(); enc.wait()
    print("wrote", out)


if __name__ == "__main__":
    main()
