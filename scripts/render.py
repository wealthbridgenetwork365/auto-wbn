"""Wealth Bridge Network carousel renderer.

Builds 1080x1350 slides as HTML in the brand style (black + mint green,
Cormorant Garamond display, Manrope body) and screenshots them to JPEG
with headless Chrome.

Usage:  python3 scripts/render.py content/posts.py out/
Each post is a dict: {"id", "slot", "pillar", "title", "sources", "slides": [...]}
Each slide is a dict with a "type" (cover, stat, bars, ranges, split, flow,
timeline, list, tiles, donut, cta) and its fields. Headline text may mark an
accent phrase with *asterisks* (rendered italic, green).
"""
import html, importlib.util, os, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"
W, H = 1080, 1350

CSS = f"""
@font-face{{font-family:'Cormorant';src:url('file://{FONTS}/CormorantGaramond.ttf');font-weight:300 700;font-style:normal}}
@font-face{{font-family:'Cormorant';src:url('file://{FONTS}/CormorantGaramond-Italic.ttf');font-weight:300 700;font-style:italic}}
@font-face{{font-family:'Manrope';src:url('file://{FONTS}/Manrope.ttf');font-weight:200 800}}
:root{{--bg:#050505;--ink:#FFFFFF;--muted:#B8BDBA;--dim:#8A938E;--accent:#2FE08A;--line:rgba(255,255,255,.18);
--paper:#F2F4F1;--ink2:#0B110E;--accent2:#1F7A45;--line2:#C9D0CB;--card:#0E1712}}
*{{box-sizing:border-box}}
body{{margin:0;width:{W}px;height:{H}px;background:var(--bg);font-family:'Manrope',sans-serif;color:var(--ink)}}
.slide{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:var(--bg);display:flex;flex-direction:column;padding:76px 80px 64px}}
.rings{{position:absolute;left:0;top:0;pointer-events:none}}
.hdr{{position:relative;display:flex;justify-content:space-between;align-items:center}}
.mark .a{{font-family:'Cormorant',serif;font-size:30px;font-weight:600;letter-spacing:.14em;line-height:1}}
.mark .b{{font-size:12px;font-weight:700;letter-spacing:.5em;color:var(--accent);margin-top:5px}}
.count{{font-size:16px;font-weight:600;letter-spacing:.3em;color:var(--dim)}}
.label{{font-size:17px;font-weight:700;letter-spacing:.38em;color:var(--accent);text-transform:uppercase}}
.h1{{font-family:'Cormorant',serif;font-weight:500;line-height:.96;letter-spacing:-.01em}}
.h1 em{{font-style:italic;color:var(--accent)}}
.body{{position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:30px}}
.sub{{font-size:30px;line-height:1.42;color:var(--muted);max-width:860px}}
.sub b{{color:var(--ink)}}
.ftr{{position:relative;display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:26px}}
.handle{{font-size:17px;font-weight:700;letter-spacing:.3em}}
.swipe{{font-size:17px;font-weight:700;letter-spacing:.3em;color:var(--accent)}}
.src{{position:relative;font-size:19px;line-height:1.4;color:var(--dim);margin:0 0 20px}}
.box{{border:1px solid var(--line);padding:30px 34px}}
.box.g{{border-color:var(--accent)}}
/* bars */
.bar{{display:flex;flex-direction:column;gap:10px}}
.bar .top{{display:flex;justify-content:space-between;align-items:baseline;font-size:28px;font-weight:600}}
.bar .top span:last-child{{font-family:'Cormorant',serif;font-size:44px;font-weight:600;color:var(--accent)}}
.bar .track{{height:30px;background:#1A1F1C;border-radius:4px;position:relative;overflow:hidden}}
.bar .fill{{position:absolute;left:0;top:0;bottom:0;background:var(--accent);border-radius:4px}}
.bar .rng{{position:absolute;top:0;bottom:0;background:var(--accent);border-radius:4px}}
.bar.dim .fill,.bar.dim .rng{{background:#5E6662}}
.bar.dim .top span:last-child{{color:var(--muted)}}
/* split */
.split{{padding:0}}
.half{{height:675px;position:relative;padding:70px 80px;display:flex;flex-direction:column}}
.half.dark{{background:var(--bg)}}
.half.light{{background:var(--paper);color:var(--ink2)}}
.half.light .h1 em{{color:var(--accent2)}}
.half.light .label{{color:var(--accent2)}}
.vs{{position:absolute;left:480px;top:615px;width:120px;height:120px;border-radius:50%;background:var(--accent);color:#050505;display:flex;align-items:center;justify-content:center;font-family:'Cormorant',serif;font-style:italic;font-weight:700;font-size:50px;z-index:3}}
.pts{{display:flex;flex-direction:column;gap:16px;margin-top:30px}}
.pt{{display:flex;gap:22px;align-items:baseline;font-size:31px;line-height:1.32}}
.pt i{{display:block;width:13px;height:13px;flex-shrink:0;background:var(--accent);transform:translateY(-4px)}}
.half.light .pt i{{background:var(--accent2)}}
.best{{margin-top:auto;border:1px solid var(--line);padding:20px 28px;font-size:26px}}
.best b{{color:var(--accent)}}
.half.light .best{{border:2px solid var(--ink2)}}
.half.light .best b{{color:var(--accent2)}}
.half .ftr2{{display:flex;justify-content:space-between;margin-top:22px;font-size:16px;font-weight:700;letter-spacing:.3em}}
/* flow */
.flow{{display:flex;flex-direction:column;gap:0}}
.step{{display:flex;align-items:center;gap:28px;border:1px solid var(--line);background:var(--card);border-radius:14px;padding:24px 30px}}
.step.hi{{background:var(--accent);color:#050505;border-color:var(--accent)}}
.step .n{{font-family:'Cormorant',serif;font-style:italic;font-size:46px;font-weight:600;color:var(--accent);min-width:56px}}
.step.hi .n{{color:#050505}}
.step .t{{font-size:31px;font-weight:700;line-height:1.2}}
.step .d{{font-size:23px;color:var(--muted);margin-top:4px;line-height:1.3}}
.step.hi .d{{color:#0B3B22}}
.arrow{{height:34px;display:flex;justify-content:center}}
/* list */
.row{{display:flex;gap:30px;align-items:baseline;border-bottom:1px solid rgba(255,255,255,.14);padding:24px 0}}
.row:last-child{{border-bottom:none}}
.row .n{{font-family:'Cormorant',serif;font-style:italic;font-size:42px;color:var(--accent);min-width:60px}}
.row .t{{font-size:30px;line-height:1.36;color:#EDEDED}}
.row .t b{{color:#fff}}
/* tiles */
.tiles{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.tile{{border:1px solid var(--line);padding:30px 30px 28px;display:flex;flex-direction:column;gap:10px}}
.tile.g{{border-color:var(--accent)}}
.tile .v{{font-family:'Cormorant',serif;font-size:96px;font-weight:600;line-height:.9;color:var(--accent)}}
.tile .k{{font-size:24px;line-height:1.35;color:#E6E6E6}}
/* timeline */
.tl{{position:relative;padding-left:60px;display:flex;flex-direction:column;gap:30px}}
.tl:before{{content:'';position:absolute;left:14px;top:12px;bottom:12px;width:2px;background:var(--accent);opacity:.6}}
.ti{{position:relative}}
.ti:before{{content:'';position:absolute;left:-55px;top:8px;width:20px;height:20px;border-radius:50%;background:var(--bg);border:3px solid var(--accent)}}
.ti.hi:before{{background:var(--accent)}}
.ti .w{{font-size:18px;font-weight:700;letter-spacing:.32em;color:var(--accent);text-transform:uppercase}}
.ti .t{{font-size:31px;font-weight:600;margin-top:6px;line-height:1.25}}
.ti .d{{font-size:23px;color:var(--muted);margin-top:4px;line-height:1.35}}
/* stat */
.big{{font-family:'Cormorant',serif;font-weight:600;line-height:.85;color:var(--accent);letter-spacing:-.02em}}
.money{{display:flex;align-items:baseline;white-space:nowrap;font-family:'Manrope',sans-serif;font-weight:800;line-height:.9;letter-spacing:-.04em;color:var(--accent)}}
.money span{{font-size:.26em;font-weight:700;letter-spacing:0;color:var(--ink);margin-left:14px}}
/* cta */
.pill{{display:inline-flex;align-items:center;gap:20px;background:var(--accent);color:#050505;padding:26px 42px;border-radius:999px;font-size:22px;font-weight:800;letter-spacing:.2em}}
.pill.o{{background:transparent;color:var(--ink);border:1.5px solid var(--ink)}}
"""

RINGS = """<svg class="rings" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none" stroke="#2FE08A" aria-hidden="true">
<circle cx="1080" cy="240" r="360" stroke-opacity=".22" stroke-width="1.5"/><circle cx="1080" cy="240" r="470" stroke-opacity=".13" stroke-width="1.5"/>
<circle cx="1080" cy="240" r="580" stroke-opacity=".07" stroke-width="1.5"/></svg>"""
ARROW = """<div class="arrow"><svg width="22" height="34" viewBox="0 0 22 34" fill="none" stroke="#2FE08A" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 2 V30 M3 22 L11 30 L19 22"/></svg></div>"""
RARROW = """<svg width="30" height="16" viewBox="0 0 30 16" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M1 8 H28 M21 1 L28 8 L21 15"/></svg>"""


def rich(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s.replace("\n", "<br>")


def header(i, n):
    return (f'<div class="hdr"><div class="mark"><div class="a">WEALTH BRIDGE</div><div class="b">NETWORK</div></div>'
            f'<div class="count">{i:02d} / {n:02d}</div></div>')


def footer(last, src=None):
    s = f'<div class="src">{rich(src)}</div>' if src else ""
    right = "" if last else f'<div class="swipe">SWIPE →</div>'
    return f'{s}<div class="ftr"><div class="handle">@WEALTHBRIDGENETWORK</div>{right}</div>'


def frame(inner, i, n, src=None, rings=True):
    return (f'<div class="slide">{RINGS if rings else ""}{header(i, n)}'
            f'<div class="body">{inner}</div>{footer(i == n, src)}</div>')


def s_cover(s, i, n):
    size = s.get("size", 132)
    inner = (f'<div class="label">{rich(s["label"])}</div>'
             f'<div class="h1" style="font-size:{size}px">{rich(s["title"])}</div>'
             + (f'<div class="money" style="font-size:{s.get("bsize", 210)}px">{rich(s["big"])}'
                f'<span>{rich(s.get("unit", ""))}</span></div>' if s.get("big") else "")
             + (f'<div class="sub">{rich(s["sub"])}</div>' if s.get("sub") else ""))
    return frame(inner, i, n, s.get("src"))


def s_stat(s, i, n):
    inner = (f'<div class="label">{rich(s["label"])}</div>'
             f'<div class="big" style="font-size:{s.get("size", 250)}px">{rich(s["value"])}</div>'
             f'<div class="h1" style="font-size:{s.get("tsize", 64)}px">{rich(s["title"])}</div>'
             + (f'<div class="sub">{rich(s["sub"])}</div>' if s.get("sub") else ""))
    return frame(inner, i, n, s.get("src"))


def s_bars(s, i, n):
    mx = s.get("max") or max(b[1] for b in s["bars"])
    rows = []
    for b in s["bars"]:
        lab, val, disp = b[0], b[1], b[2]
        dim = len(b) > 3 and b[3] == "dim"
        rows.append(f'<div class="bar{" dim" if dim else ""}"><div class="top"><span>{rich(lab)}</span><span>{rich(disp)}</span></div>'
                    f'<div class="track"><div class="fill" style="width:{100*val/mx:.1f}%"></div></div></div>')
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 84)}px">{rich(s["title"])}</div>'
             + (f'<div class="sub" style="font-size:24px">{rich(s["note"])}</div>' if s.get("note") else "")
             + f'<div style="display:flex;flex-direction:column;gap:{s.get("gap", 26)}px;margin-top:8px">{"".join(rows)}</div>')
    return frame(inner, i, n, s.get("src"))


def s_ranges(s, i, n):
    mx = s["max"]
    rows = []
    for lab, lo, hi, disp, *rest in s["bars"]:
        dim = rest and rest[0] == "dim"
        rows.append(f'<div class="bar{" dim" if dim else ""}"><div class="top"><span>{rich(lab)}</span><span>{rich(disp)}</span></div>'
                    f'<div class="track"><div class="rng" style="left:{100*lo/mx:.1f}%;width:{100*(hi-lo)/mx:.1f}%"></div></div></div>')
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 80)}px">{rich(s["title"])}</div>'
             + (f'<div class="sub" style="font-size:24px">{rich(s["note"])}</div>' if s.get("note") else "")
             + f'<div style="display:flex;flex-direction:column;gap:24px;margin-top:6px">{"".join(rows)}</div>')
    return frame(inner, i, n, s.get("src"))


def half(h, cls, last_row=""):
    pts = "".join(f'<div class="pt"><i></i><div>{rich(p)}</div></div>' for p in h["points"])
    best = f'<div class="best"><b>{rich(h["best_label"])}</b> {rich(h["best"])}</div>' if h.get("best") else ""
    lab = f'<div class="label">{rich(h["label"])}</div>' if h.get("label") else ""
    return (f'<div class="half {cls}">{lab}<div class="h1" style="font-size:{h.get("size", 84)}px;margin-top:{18 if lab else 0}px">{rich(h["title"])}</div>'
            f'<div class="pts">{pts}</div>{best}{last_row}</div>')


def s_split(s, i, n):
    top_hdr = (f'<div class="hdr" style="margin-bottom:34px"><div class="mark"><div class="a">WEALTH BRIDGE</div><div class="b">NETWORK</div></div>'
               f'<div class="count">{i:02d} / {n:02d}</div></div>')
    top = s["top"]
    tpts = "".join(f'<div class="pt"><i></i><div>{rich(p)}</div></div>' for p in top["points"])
    tbest = f'<div class="best"><b>{rich(top["best_label"])}</b> {rich(top["best"])}</div>' if top.get("best") else ""
    top_html = (f'<div class="half dark">{top_hdr}<div class="label">{rich(top["label"])}</div>'
                f'<div class="h1" style="font-size:{top.get("size", 84)}px;margin-top:16px">{rich(top["title"])}</div>'
                f'<div class="pts" style="margin-top:24px">{tpts}</div>{tbest}</div>')
    src = f'<div style="font-size:17px;color:#4F5852;margin-top:14px;line-height:1.35">{rich(s["src"])}</div>' if s.get("src") else ""
    last = i == n
    ftr = (f'{src}<div class="ftr2"><span>@WEALTHBRIDGENETWORK</span>'
           f'<span style="color:var(--accent2)">{"" if last else "SWIPE →"}</span></div>')
    bot = s["bottom"]
    bpts = "".join(f'<div class="pt"><i></i><div>{rich(p)}</div></div>' for p in bot["points"])
    bbest = f'<div class="best" style="margin-top:22px"><b>{rich(bot["best_label"])}</b> {rich(bot["best"])}</div>' if bot.get("best") else ""
    bot_html = (f'<div class="half light" style="padding-top:84px">'
                f'<div class="h1" style="font-size:{bot.get("size", 84)}px">{rich(bot["title"])}</div>'
                f'<div class="pts" style="margin-top:24px">{bpts}</div>{bbest}<div style="margin-top:auto">{ftr}</div></div>')
    return f'<div class="slide split">{top_html}{bot_html}<div class="vs" aria-hidden="true">{rich(s.get("join", "vs"))}</div></div>'


def s_flow(s, i, n):
    parts = []
    for k, st in enumerate(s["steps"]):
        hi = " hi" if st.get("hi") else ""
        d = f'<div class="d">{rich(st["d"])}</div>' if st.get("d") else ""
        parts.append(f'<div class="step{hi}"><div class="n">{k+1:02d}</div><div><div class="t">{rich(st["t"])}</div>{d}</div></div>')
        if k < len(s["steps"]) - 1:
            parts.append(ARROW)
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 80)}px">{rich(s["title"])}</div>'
             f'<div class="flow" style="margin-top:6px">{"".join(parts)}</div>')
    return frame(inner, i, n, s.get("src"))


def s_list(s, i, n):
    rows = "".join(f'<div class="row"><div class="n">{k+1:02d}</div><div class="t">{rich(t)}</div></div>' for k, t in enumerate(s["items"]))
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 88)}px">{rich(s["title"])}</div>'
             f'<div style="margin-top:4px">{rows}</div>'
             + (f'<div class="box g" style="font-size:25px;line-height:1.45;color:#E6E6E6">{rich(s["note"])}</div>' if s.get("note") else ""))
    return frame(inner, i, n, s.get("src"))


def s_tiles(s, i, n):
    tiles = "".join(f'<div class="tile{" g" if k == 0 else ""}"><div class="v" style="font-size:{s.get("vsize", 96)}px">{rich(v)}</div><div class="k">{rich(kk)}</div></div>'
                    for k, (v, kk) in enumerate(s["tiles"]))
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 84)}px">{rich(s["title"])}</div>'
             f'<div class="tiles" style="margin-top:8px">{tiles}</div>')
    return frame(inner, i, n, s.get("src"))


def s_timeline(s, i, n):
    items = "".join(f'<div class="ti{" hi" if it.get("hi") else ""}"><div class="w">{rich(it["w"])}</div><div class="t">{rich(it["t"])}</div>'
                    + (f'<div class="d">{rich(it["d"])}</div>' if it.get("d") else "") + '</div>' for it in s["items"])
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 84)}px">{rich(s["title"])}</div>'
             f'<div class="tl" style="margin-top:10px">{items}</div>')
    return frame(inner, i, n, s.get("src"))


def s_donut(s, i, n):
    p = s["pct"]
    r, c = 170, 2 * 3.14159265 * 170
    svg = (f'<svg width="420" height="420" viewBox="0 0 420 420" role="img" aria-label="{p}%">'
           f'<circle cx="210" cy="210" r="{r}" fill="none" stroke="#1A1F1C" stroke-width="44"/>'
           f'<circle cx="210" cy="210" r="{r}" fill="none" stroke="#2FE08A" stroke-width="44" stroke-dasharray="{c*p/100:.1f} {c:.1f}" transform="rotate(-90 210 210)"/>'
           f'<text x="210" y="238" text-anchor="middle" font-family="Cormorant" font-weight="600" font-size="104" fill="#FFFFFF">{s.get("center", str(p) + "%")}</text></svg>')
    inner = (f'<div class="label">{rich(s["label"])}</div><div class="h1" style="font-size:{s.get("tsize", 80)}px">{rich(s["title"])}</div>'
             f'<div style="display:flex;align-items:center;gap:48px">{svg}<div class="sub" style="font-size:29px">{rich(s["side"])}</div></div>')
    return frame(inner, i, n, s.get("src"))


def s_cta(s, i, n):
    lines = "".join(f'<div class="pt"><i></i><div>{rich(t)}</div></div>' for t in s.get("points", []))
    inner = (f'<div class="label">{rich(s.get("label", "Building Bridges · Creating Access"))}</div>'
             f'<div class="h1" style="font-size:{s.get("tsize", 112)}px">{rich(s["title"])}</div>'
             + (f'<div class="sub">{rich(s["sub"])}</div>' if s.get("sub") else "")
             + (f'<div class="pts" style="margin-top:0">{lines}</div>' if lines else "")
             + f'<div style="display:flex;gap:22px;flex-wrap:wrap;margin-top:14px"><div class="pill">FOLLOW US {RARROW}</div>'
               f'<div class="pill o">DM US TO WORK WITH US</div></div>')
    return frame(inner, i, n, s.get("src"))


TYPES = dict(cover=s_cover, stat=s_stat, bars=s_bars, ranges=s_ranges, split=s_split, flow=s_flow,
             list=s_list, tiles=s_tiles, timeline=s_timeline, donut=s_donut, cta=s_cta)


def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def render_posts(posts, out_dir, only=None):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    tmp = out / "_html"; tmp.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for post in posts:
            if only and post["id"] not in only:
                continue
            d = out / post["id"]; d.mkdir(exist_ok=True)
            n = len(post["slides"])
            for k, s in enumerate(post["slides"], 1):
                hp = tmp / f'{post["id"]}_{k}.html'
                hp.write_text(page(TYPES[s["type"]](s, k, n)))
                pg.goto(f"file://{hp}")
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(60)
                pg.screenshot(path=str(d / f"slide-{k:02d}.jpg"), type="jpeg", quality=90,
                              clip={"x": 0, "y": 0, "width": W, "height": H})
            print("rendered", post["id"], n)
        b.close()


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("content", sys.argv[1])
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    only = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
    render_posts(mod.POSTS, sys.argv[2], only)
