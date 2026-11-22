"""Content Creation series renderer: illustrated full-bleed scenes + editorial type.

Usage: python3 scripts/render_cc.py content/content_creation.py posts/ [post_id ...]
Slide kinds (key "k"):
  hero   full-bleed scene (art=) with label/title/sub at the bottom (or pos="top"); optional stat=(value, text)
  split  two halves: top=dict(art,label,title,sub), bottom=dict(...); optional mid="badge text"
  panel  dark page with label/title/sub and one block: cards | flow | ranges | rows | timeline | compare
  card   full-bleed scene with a floating UI card: email | invoice | ticket
  cta    closing slide
Text: *word* = accent (italic mint in titles), **word** = bold.
"""
import html, importlib.util, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from cc_art import SCENES  # noqa

FONTS = ROOT / "fonts"
W, H = 1080, 1350
ACC = "#2FE08A"
import base64


def _b64(n):
    return base64.b64encode((FONTS / n).read_bytes()).decode()



CSS = f"""
@font-face{{font-family:'Cormorant';src:url(data:font/ttf;base64,{_b64('CormorantGaramond.ttf')});font-weight:300 700}}
@font-face{{font-family:'Cormorant';src:url(data:font/ttf;base64,{_b64('CormorantGaramond-Italic.ttf')});font-weight:300 700;font-style:italic}}
@font-face{{font-family:'Manrope';src:url(data:font/ttf;base64,{_b64('Manrope.ttf')});font-weight:200 800}}
*{{box-sizing:border-box;margin:0}}
body{{width:{W}px;height:{H}px;background:#050505;font-family:'Manrope',sans-serif;color:#fff;overflow:hidden}}
.s{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#050505}}
.art{{position:absolute;inset:0}}
.art svg{{width:100%;height:100%;display:block}}
.shade-b{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,5,5,.55) 0%,rgba(5,5,5,0) 16%,rgba(5,5,5,0) 38%,rgba(5,5,5,.78) 62%,rgba(5,5,5,.96) 100%)}}
.shade-t{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,5,5,.96) 0%,rgba(5,5,5,.8) 34%,rgba(5,5,5,0) 60%,rgba(5,5,5,0) 84%,rgba(5,5,5,.7) 100%)}}
.hdr{{position:absolute;left:72px;right:72px;top:60px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.mark .a{{font-family:'Cormorant';font-size:28px;font-weight:600;letter-spacing:.14em;line-height:1}}
.mark .b{{font-size:11px;font-weight:700;letter-spacing:.5em;color:{ACC};margin-top:5px}}
.count{{font-size:18px;font-weight:700;letter-spacing:.3em;color:rgba(255,255,255,.75)}}
.ftr{{position:absolute;left:72px;right:72px;bottom:52px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.22);padding-top:22px;z-index:5}}
.handle{{font-size:16px;font-weight:700;letter-spacing:.3em}}
.swipe{{font-size:16px;font-weight:800;letter-spacing:.3em;color:{ACC}}}
.src{{position:absolute;left:72px;right:72px;bottom:118px;font-size:18px;line-height:1.35;color:rgba(255,255,255,.62);z-index:5}}
.txt{{position:absolute;left:72px;right:72px;z-index:4;display:flex;flex-direction:column;gap:22px}}
.txt.bottom{{bottom:170px}}
.txt.top{{top:150px}}
.label{{font-size:17px;font-weight:800;letter-spacing:.36em;color:{ACC};text-transform:uppercase}}
.t{{font-family:'Cormorant';font-weight:700;font-feature-settings:'lnum' 1;font-variant-numeric:lining-nums;line-height:.95;letter-spacing:-.01em;text-wrap:balance}}
.t em{{font-style:italic;color:{ACC}}}
.sub{{font-size:30px;line-height:1.4;color:rgba(255,255,255,.86);max-width:900px}}
.sub b,.d b{{color:#fff;font-weight:800}}
.sub em,.d em{{font-style:normal;color:{ACC};font-weight:700}}
.stat{{display:flex;align-items:baseline;gap:22px;border-left:4px solid {ACC};padding:6px 0 6px 24px}}
.stat .v{{font-family:'Manrope';font-weight:800;font-size:84px;letter-spacing:-.03em;color:{ACC};line-height:1;white-space:nowrap}}
.stat .x{{font-size:26px;line-height:1.3;color:rgba(255,255,255,.88)}}
/* split */
.half{{position:absolute;left:0;right:0;height:675px;overflow:hidden}}
.half.top{{top:0}} .half.bot{{top:675px}}
.half .art{{position:absolute;inset:0}}
.half .sh{{position:absolute;inset:0}}
.half.top .sh{{background:linear-gradient(180deg,rgba(5,5,5,.7) 0%,rgba(5,5,5,.1) 30%,rgba(5,5,5,.25) 55%,rgba(5,5,5,.92) 100%)}}
.half.bot .sh{{background:linear-gradient(180deg,rgba(5,5,5,.15) 0%,rgba(5,5,5,.25) 40%,rgba(5,5,5,.92) 78%,rgba(5,5,5,.98) 100%)}}
.half .txt{{gap:14px}}
.half.top .txt{{bottom:40px}}
.half.bot .txt{{bottom:150px}}
.half .sub{{font-size:27px}}
.seam{{position:absolute;left:0;right:0;top:673px;height:4px;background:{ACC};z-index:6}}
.mid{{position:absolute;left:50%;top:675px;transform:translate(-50%,-50%);z-index:7;background:{ACC};color:#050505;font-weight:800;font-size:20px;letter-spacing:.3em;padding:16px 30px;border-radius:999px}}
.tagl{{position:absolute;left:72px;z-index:6;background:rgba(5,5,5,.7);border:1px solid rgba(255,255,255,.3);font-size:15px;font-weight:800;letter-spacing:.3em;padding:10px 18px}}
/* panel */
.panel{{position:absolute;left:72px;right:72px;top:150px;bottom:170px;display:flex;flex-direction:column;justify-content:center;gap:26px;z-index:4}}
.rings{{position:absolute;left:0;top:0}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.cards.one{{grid-template-columns:1fr}}
.c{{background:#0E1712;border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:30px 30px;display:flex;flex-direction:column;gap:10px}}
.c.hi{{border-color:{ACC}}}
.c .h{{font-size:34px;font-weight:800;line-height:1.2}}
.c .v{{font-family:'Manrope';font-weight:800;font-size:52px;color:{ACC};letter-spacing:-.02em;line-height:1.05}}
.c .d{{font-size:26px;line-height:1.38;color:rgba(255,255,255,.74)}}
.c .k{{font-size:16px;font-weight:800;letter-spacing:.3em;color:{ACC};text-transform:uppercase}}
.flow{{display:flex;flex-direction:column}}
.st{{display:flex;gap:24px;align-items:center;background:#0E1712;border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:24px 30px}}
.st.hi{{background:{ACC};color:#050505;border-color:{ACC}}}
.st .n{{font-feature-settings:'lnum' 1;font-family:'Cormorant';font-style:italic;font-weight:600;font-size:44px;color:{ACC};min-width:44px}}
.st.hi .n{{color:#050505}}
.st .h{{font-size:33px;font-weight:800;line-height:1.2}}
.st .d{{font-size:24px;line-height:1.35;color:rgba(255,255,255,.72);margin-top:3px}}
.st.hi .d{{color:#0B3B22}}
.ar{{height:30px;display:flex;justify-content:center}}
.rg{{display:flex;flex-direction:column;gap:10px}}
.rg .top{{display:flex;justify-content:space-between;align-items:baseline;font-size:31px;font-weight:700}}
.rg .top span:last-child{{font-weight:800;color:{ACC};font-size:30px}}
.rg .note{{font-size:21px;color:rgba(255,255,255,.6);margin-top:-4px}}
.trk{{position:relative;height:24px;background:#1A211D;border-radius:12px}}
.trk i{{position:absolute;top:0;bottom:0;background:{ACC};border-radius:12px}}
.axis{{display:flex;justify-content:space-between;font-size:17px;color:rgba(255,255,255,.55);font-weight:700;letter-spacing:.1em}}
.rows .r{{display:flex;gap:26px;align-items:baseline;border-bottom:1px solid rgba(255,255,255,.14);padding:20px 0}}
.rows .r:last-child{{border:none}}
.rows .n{{font-feature-settings:'lnum' 1;font-family:'Cormorant';font-style:italic;font-size:42px;color:{ACC};min-width:50px;line-height:1}}
.rows .x{{font-size:33px;line-height:1.38;color:#EDEDED}}
.rows .x b{{color:#fff}}
.tl{{position:relative;padding-left:58px;display:flex;flex-direction:column;gap:26px}}
.tl:before{{content:'';position:absolute;left:13px;top:10px;bottom:10px;width:3px;background:{ACC};opacity:.6}}
.ti{{position:relative}}
.ti:before{{content:'';position:absolute;left:-55px;top:6px;width:22px;height:22px;border-radius:50%;background:#050505;border:4px solid {ACC}}}
.ti.hi:before{{background:{ACC}}}
.ti .w{{font-size:18px;font-weight:800;letter-spacing:.3em;color:{ACC};text-transform:uppercase}}
.ti .h{{font-size:36px;font-weight:800;margin-top:6px;line-height:1.2}}
.ti .d{{font-size:26px;line-height:1.38;color:rgba(255,255,255,.72);margin-top:4px}}
.cmp{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.col{{border-radius:18px;padding:26px;display:flex;flex-direction:column;gap:14px;background:#141414;border:1px solid rgba(255,255,255,.14)}}
.col.g{{background:#0D1F15;border-color:{ACC}}}
.col .k{{font-size:15px;font-weight:800;letter-spacing:.32em;color:rgba(255,255,255,.6)}}
.col.g .k{{color:{ACC}}}
.ln{{display:flex;justify-content:space-between;font-size:25px;color:rgba(255,255,255,.82);border-bottom:1px dashed rgba(255,255,255,.18);padding-bottom:10px}}
.ln b{{color:#fff}}
.tot{{margin-top:6px}}
.tot .v{{font-weight:800;font-size:64px;letter-spacing:-.03em;line-height:1}}
.col.g .tot .v{{color:{ACC}}}
.tot .d{{font-size:19px;color:rgba(255,255,255,.65);margin-top:6px}}
.bar2{{height:16px;border-radius:8px;background:#2A2A2A;overflow:hidden}}
.bar2 i{{display:block;height:100%;background:#8A8F8C}}
.col.g .bar2 i{{background:{ACC}}}
/* floating ui cards */
.ui{{position:absolute;z-index:4;background:#FFFFFF;color:#111;border-radius:22px;box-shadow:0 30px 80px rgba(0,0,0,.55)}}
.mail{{left:110px;right:110px;top:190px;padding:30px 34px}}
.mail .bar{{display:flex;gap:10px;margin-bottom:22px}}
.mail .bar i{{width:14px;height:14px;border-radius:50%;background:#E0E0E0}}
.mail .f{{font-size:20px;color:#666;line-height:1.5}}
.mail .f b{{color:#111}}
.mail .sj{{font-size:30px;font-weight:800;margin:14px 0 16px;line-height:1.25}}
.mail .ln2{{display:flex;justify-content:space-between;font-size:23px;padding:12px 0;border-top:1px solid #EEE}}
.mail .ln2 b{{color:#139A52}}
.mail .btn{{margin-top:18px;display:inline-block;background:#139A52;color:#fff;font-weight:800;font-size:20px;letter-spacing:.12em;padding:14px 26px;border-radius:999px}}
.inv{{right:80px;top:170px;width:560px;padding:30px 34px;transform:rotate(3deg)}}
.inv .k{{font-size:15px;font-weight:800;letter-spacing:.3em;color:#139A52}}
.inv .hh{{font-size:30px;font-weight:800;margin:8px 0 16px}}
.inv .ln2{{display:flex;justify-content:space-between;font-size:23px;padding:12px 0;border-top:1px solid #EEE}}
.inv .ln2 b{{color:#139A52;font-weight:800}}
.inv .big{{display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid #111;margin-top:6px;padding-top:14px;font-size:22px;font-weight:800}}
.inv .big span:last-child{{font-size:46px;color:#139A52}}
.plus{{position:absolute;z-index:5;left:150px;top:210px;width:150px;height:150px;border-radius:50%;background:{ACC};color:#050505;font-size:110px;font-weight:800;display:flex;align-items:center;justify-content:center;line-height:1;box-shadow:0 20px 60px rgba(0,0,0,.5)}}
.tkt{{left:120px;right:120px;top:210px;display:flex;overflow:hidden;transform:rotate(-3deg)}}
.tkt .m{{flex:1;padding:28px 32px}}
.tkt .sd{{width:170px;background:#139A52;color:#fff;padding:28px 20px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:6px;font-weight:800;font-size:18px;letter-spacing:.2em}}
.tkt .k{{font-size:15px;font-weight:800;letter-spacing:.3em;color:#139A52}}
.tkt .route{{display:flex;align-items:center;gap:22px;font-size:66px;font-weight:800;letter-spacing:-.02em;margin:10px 0}}
.tkt .route i{{font-style:normal;font-size:34px;color:#139A52}}
.tkt .meta{{display:flex;gap:34px;font-size:17px;color:#666;font-weight:700;letter-spacing:.12em}}
.tkt .meta b{{display:block;color:#111;font-size:24px;letter-spacing:0;margin-top:4px}}
/* cta */
.pill{{display:inline-flex;align-items:center;background:{ACC};color:#050505;padding:24px 40px;border-radius:999px;font-size:21px;font-weight:800;letter-spacing:.2em}}
.pill.o{{background:transparent;color:#fff;border:1.5px solid #fff}}
"""

RINGS = f"""<svg class="rings" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none" stroke="{ACC}">
<circle cx="1080" cy="230" r="360" stroke-opacity=".2" stroke-width="1.5"/><circle cx="1080" cy="230" r="470" stroke-opacity=".12" stroke-width="1.5"/>
<circle cx="1080" cy="230" r="580" stroke-opacity=".06" stroke-width="1.5"/></svg>"""
DOWN = f'<div class="ar"><svg width="20" height="26" viewBox="0 0 20 26" fill="none" stroke="{ACC}" stroke-width="2.5" stroke-linecap="round"><path d="M10 2 V23 M3 16 L10 23 L17 16"/></svg></div>'


def md(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s.replace("\n", "<br>")


def art(name, h=1350, crop=None):
    svg = SCENES[name](1350)
    if h != 1350:
        y0 = 337 if crop is None else crop
        svg = svg.replace('viewBox="0 0 1080 1350"', f'viewBox="0 {y0} 1080 {h}"', 1)
    return f'<div class="art">{svg}</div>'


def chrome(i, n, src=""):
    out = (f'<div class="hdr"><div class="mark"><div class="a">WEALTH BRIDGE</div><div class="b">NETWORK</div></div>'
           f'<div class="count">{i:02d} / {n:02d}</div></div>')
    if src:
        out += f'<div class="src">{md(src)}</div>'
    out += f'<div class="ftr"><div class="handle">@WEALTHBRIDGENETWORK</div>{"" if i == n else "<div class=swipe>SWIPE →</div>"}</div>'
    return out


def textblock(s, cls, size):
    out = f'<div class="txt {cls}">'
    if s.get("label"):
        out += f'<div class="label">{md(s["label"])}</div>'
    if s.get("title"):
        out += f'<div class="t" style="font-size:{s.get("size", size)}px">{md(s["title"])}</div>'
    if s.get("stat"):
        v, x = s["stat"]
        out += f'<div class="stat"><div class="v">{md(v)}</div><div class="x">{md(x)}</div></div>'
    if s.get("sub"):
        out += f'<div class="sub">{md(s["sub"])}</div>'
    return out + "</div>"


def k_hero(s, i, n):
    pos = s.get("pos", "bottom")
    return (art(s["art"]) + f'<div class="{"shade-t" if pos == "top" else "shade-b"}"></div>'
            + textblock(s, pos, 120 if i == 1 else 88) + chrome(i, n, s.get("src", "")))


def k_split(s, i, n):
    out = ""
    for key, cls in (("top", "top"), ("bottom", "bot")):
        h = s[key]
        out += (f'<div class="half {cls}">{art(h["art"], 675, h.get("crop"))}<div class="sh"></div>'
                + (f'<div class="tagl" style="top:{150 if cls == "top" else 40}px">{md(h["tag"])}</div>' if h.get("tag") else "")
                + textblock(h, "", 66) + "</div>")
    out += '<div class="seam"></div>'
    if s.get("mid"):
        out += f'<div class="mid">{md(s["mid"])}</div>'
    return out + chrome(i, n, s.get("src", ""))


def block(s):
    if "cards" in s:
        one = " one" if s.get("one") else ""
        return f'<div class="cards{one}">' + "".join(
            f'<div class="c{" hi" if c.get("hi") else ""}"{" style=grid-column:1/-1" if c.get("wide") else ""}>' + (f'<div class="k">{md(c["k"])}</div>' if c.get("k") else "")
            + (f'<div class="v">{md(c["v"])}</div>' if c.get("v") else "") + (f'<div class="h">{md(c["h"])}</div>' if c.get("h") else "")
            + (f'<div class="d">{md(c["d"])}</div>' if c.get("d") else "") + "</div>" for c in s["cards"]) + "</div>"
    if "flow" in s:
        parts = []
        for k, st in enumerate(s["flow"], 1):
            parts.append(f'<div class="st{" hi" if st.get("hi") else ""}"><div class="n">{k}</div><div><div class="h">{md(st["h"])}</div>'
                         + (f'<div class="d">{md(st["d"])}</div>' if st.get("d") else "") + "</div></div>")
        return '<div class="flow">' + DOWN.join(parts) + "</div>"
    if "ranges" in s:
        mx = s["max"]
        rows = "".join(f'<div class="rg"><div class="top"><span>{md(r[0])}</span><span>{md(r[3])}</span></div>'
                       f'<div class="trk"><i style="left:{100*r[1]/mx:.1f}%;width:{100*(r[2]-r[1])/mx:.1f}%"></i></div>'
                       + (f'<div class="note">{md(r[4])}</div>' if len(r) > 4 else "") + "</div>" for r in s["ranges"])
        ticks = "".join(f"<span>{t}</span>" for t in s["ticks"])
        return f'<div style="display:flex;flex-direction:column;gap:22px">{rows}<div class="axis">{ticks}</div></div>'
    if "rows" in s:
        return '<div class="rows">' + "".join(f'<div class="r"><div class="n">{k}</div><div class="x">{md(r)}</div></div>'
                                             for k, r in enumerate(s["rows"], 1)) + "</div>"
    if "timeline" in s:
        return '<div class="tl">' + "".join(f'<div class="ti{" hi" if t.get("hi") else ""}"><div class="w">{md(t["w"])}</div><div class="h">{md(t["h"])}</div>'
                                           + (f'<div class="d">{md(t["d"])}</div>' if t.get("d") else "") + "</div>" for t in s["timeline"]) + "</div>"
    if "compare" in s:
        out = '<div class="cmp">'
        for c in s["compare"]:
            lines = "".join(f'<div class="ln"><span>{md(a)}</span><b>{md(b)}</b></div>' for a, b in c["lines"])
            out += (f'<div class="col{" g" if c.get("g") else ""}"><div class="k">{md(c["k"])}</div>{lines}'
                    f'<div class="tot"><div class="v">{md(c["v"])}</div><div class="d">{md(c["d"])}</div></div>'
                    f'<div class="bar2"><i style="width:{c["pct"]}%"></i></div></div>')
        return out + "</div>"
    return ""


def k_panel(s, i, n):
    head = (f'<div class="label">{md(s["label"])}</div>' if s.get("label") else "") + \
           (f'<div class="t" style="font-size:{s.get("size", 76)}px">{md(s["title"])}</div>' if s.get("title") else "") + \
           (f'<div class="sub" style="font-size:{s.get("subsize", 27)}px">{md(s["sub"])}</div>' if s.get("sub") else "")
    tail = f'<div class="sub" style="font-size:22px;color:rgba(255,255,255,.62)">{md(s["note"])}</div>' if s.get("note") else ""
    return RINGS + f'<div class="panel">{head}<div style="zoom:{s.get("zoom", 1.12)}">{block(s)}</div>{tail}</div>' + chrome(i, n, s.get("src", ""))


def k_card(s, i, n):
    ui = ""
    if s["ui"] == "email":
        e = s["email"]
        ui = (f'<div class="ui mail"><div class="bar"><i></i><i></i><i></i></div><div class="f">From: <b>{md(e["from"])}</b></div>'
              f'<div class="f">To: <b>{md(e["to"])}</b></div><div class="sj">{md(e["subject"])}</div>'
              + "".join(f'<div class="ln2"><span>{md(a)}</span><b>{md(b)}</b></div>' for a, b in e["lines"])
              + f'<div class="btn">{md(e["button"])}</div></div>')
    elif s["ui"] == "invoice":
        v = s["invoice"]
        ui = (f'<div class="plus">+</div><div class="ui inv"><div class="k">{md(v["k"])}</div><div class="hh">{md(v["h"])}</div>'
              + "".join(f'<div class="ln2"><span>{md(a)}</span><b>{md(b)}</b></div>' for a, b in v["lines"])
              + f'<div class="big"><span>{md(v["total"][0])}</span><span>{md(v["total"][1])}</span></div></div>')
    elif s["ui"] == "ticket":
        t = s["ticket"]
        meta = "".join(f"<div>{md(a)}<b>{md(b)}</b></div>" for a, b in t["meta"])
        ui = (f'<div class="ui tkt"><div class="m"><div class="k">{md(t["k"])}</div><div class="route">{md(t["from"])} <i>✈</i> {md(t["to"])}</div>'
              f'<div class="meta">{meta}</div></div><div class="sd">ONE WAY<span style="font-size:40px">✓</span>NEW START</div></div>')
    return (art(s["art"]) + '<div class="shade-b"></div>' + ui + textblock(s, "bottom", 80) + chrome(i, n, s.get("src", "")))


def k_cta(s, i, n):
    inner = (f'<div class="label">{md(s.get("label", "Wealth Bridge Network"))}</div>'
             f'<div class="t" style="font-size:{s.get("size", 104)}px">{md(s["title"])}</div>'
             + (f'<div class="sub">{md(s["sub"])}</div>' if s.get("sub") else "")
             + '<div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:10px">'
             + "".join(f'<div class="pill{" o" if k else ""}">{md(p)}</div>' for k, p in enumerate(s.get("pills", [])))
             + "</div>")
    bg = (art(s["art"]) + '<div class="shade-b" style="background:linear-gradient(180deg,rgba(5,5,5,.6),rgba(5,5,5,.88) 45%,rgba(5,5,5,.97))"></div>') if s.get("art") else RINGS
    return bg + f'<div class="txt bottom" style="bottom:200px">{inner}</div>' + chrome(i, n, s.get("src", ""))


KINDS = dict(hero=k_hero, split=k_split, panel=k_panel, card=k_card, cta=k_cta)


def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">{body}</div></body></html>'


def main():
    spec = importlib.util.spec_from_file_location("content", sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = Path(sys.argv[2])
    only = set(sys.argv[3:])
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        for post in mod.POSTS:
            if only and post["id"] not in only:
                continue
            d = out / post["id"]
            d.mkdir(parents=True, exist_ok=True)
            n = len(post["slides"])
            for i, sl in enumerate(post["slides"], 1):
                pg.set_content(page(KINDS[sl["k"]](sl, i, n)))
                pg.evaluate("document.fonts.ready")
                over = pg.evaluate("""(()=>{const r=[];document.querySelectorAll('.txt,.panel').forEach(e=>{
                    const b=e.getBoundingClientRect();if(b.top<130||b.bottom>1350-150)r.push(Math.round(b.top)+'-'+Math.round(b.bottom))});return r})()""")
                if over:
                    print(f"WARN {post['id']} slide {i}: text block out of safe area {over}")
                pg.screenshot(path=str(d / f"slide-{i:02d}.jpg"), type="jpeg", quality=90)
            print(post["id"], n, "slides")
        b.close()


if __name__ == "__main__":
    main()
