"""Doodle-style storytelling carousel renderer (white page, bold text, stick figures).

Usage: python3 scripts/render_doodle.py content/china_explained.py posts/ [post_id ...]
Each slide dict may have:
  tag   small series label (cover only)
  head  accent-coloured heading
  text  list of paragraphs; *word* = accent colour
  items numbered list
  scene SVG string drawn in a 900 x vh box (default vh=560), bottom-aligned
  src   small source line
"""
import html, importlib.util, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

W, H = 1080, 1350
ACC = "#139A52"

CSS = f"""
*{{box-sizing:border-box;margin:0}}
body{{width:{W}px;height:{H}px;background:#fff;font-family:'Poppins',sans-serif;color:#111}}
.s{{width:{W}px;height:{H}px;display:flex;flex-direction:column;padding:88px 96px 0;overflow:hidden}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0}}
.hook{{font-family:'Inter Display','Inter',sans-serif;font-weight:900;font-size:var(--hs,128px);line-height:.98;letter-spacing:-.025em;text-transform:uppercase;color:#111;margin-bottom:26px}}
.hook em{{font-style:normal;background:linear-gradient(180deg,transparent 14%,#2FE08A 14%,#2FE08A 90%,transparent 90%);padding:0 10px;margin:0 -6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.kick{{font-size:40px;font-weight:600;line-height:1.25;color:#333;margin-bottom:10px}}
.kick em{{font-style:normal;color:{ACC}}}
.swipe{{position:absolute;right:96px;bottom:150px;font-family:'Inter Display';font-weight:900;font-size:30px;letter-spacing:.12em;color:#111}}
.tag{{font-size:22px;font-weight:700;letter-spacing:.32em;color:{ACC};text-transform:uppercase;margin-bottom:26px}}
.head{{font-size:var(--hd,60px);font-weight:700;line-height:1.14;color:{ACC};letter-spacing:-.01em;margin-bottom:30px}}
.p{{font-size:var(--fs,56px);font-weight:600;line-height:1.2;letter-spacing:-.012em;margin-bottom:34px}}
.p em,.head em,.it em{{font-style:normal;color:{ACC}}}
ol{{list-style:none;padding:0;margin:0 0 10px}}
.it{{display:flex;gap:22px;font-size:var(--is,46px);font-weight:500;line-height:1.18;margin-bottom:24px}}
.it .n{{color:{ACC};font-weight:700;min-width:58px}}
.it b{{font-weight:700}}
.art{{display:flex;justify-content:center;margin-top:28px;min-height:0;flex:0 1 auto}}
.art svg{{width:100%;height:auto;max-height:var(--ah,640px);overflow:visible}}
.src{{font-size:17px;color:#8a8a8a;font-weight:500;line-height:1.3;min-height:22px;text-align:left}}
.foot{{height:132px;display:flex;align-items:center;justify-content:center;position:relative;flex:none}}
.brand{{font-size:30px;font-weight:500;letter-spacing:.34em}}
.badge{{position:absolute;right:0;top:20px;width:92px;height:92px}}
"""

LOGO = Path(__file__).resolve().parent.parent / "assets" / "logo.png"


def badge():
    if LOGO.exists():
        return f'<img class="badge" src="file://{LOGO}" style="border-radius:50%;object-fit:cover">'
    return ""


OLD_BADGE = """<svg class="badge" viewBox="0 0 92 92"><circle cx="46" cy="46" r="45" fill="#111"/>
<path d="M14,58 L78,58 M20,58 Q46,22 72,58" stroke="#2FE08A" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M33,58 L33,44 M46,58 L46,38 M59,58 L59,44" stroke="#2FE08A" stroke-width="3.5" stroke-linecap="round"/>
<text x="46" y="78" font-family="Poppins" font-weight="700" font-size="14" fill="#fff" text-anchor="middle" letter-spacing="2">WBN</text></svg>"""

FILTER = """<defs><filter id="wob" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7"/>
<feDisplacementMap in="SourceGraphic" scale="6"/></filter></defs>"""


def md(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t).replace("\n", "<br>")


def slide_html(sl):
    out = ""
    if sl.get("tag"):
        out += f'<div class="tag">{md(sl["tag"])}</div>'
    if sl.get("hook"):
        out += f'<div class="hook">{md(sl["hook"])}</div>'
    if sl.get("kick"):
        out += f'<div class="kick">{md(sl["kick"])}</div>'
    if sl.get("head"):
        out += f'<div class="head">{md(sl["head"])}</div>'
    for p in sl.get("text", []):
        out += f'<div class="p">{md(p)}</div>'
    if sl.get("items"):
        out += "<ol>" + "".join(f'<li class="it"><span class="n">{i}.</span><span>{md(t)}</span></li>'
                                for i, t in enumerate(sl["items"], 1)) + "</ol>"
    vh = sl.get("vh", 560)
    art = ""
    if sl.get("scene"):
        art = (f'<svg viewBox="0 0 900 {vh}" preserveAspectRatio="xMidYMax meet">{FILTER}'
               f'<g filter="url(#wob)">{sl["scene"]}</g></svg>')
    style = ""
    if sl.get("fs"):
        style += f"--fs:{sl['fs']}px;"
    if sl.get("is"):
        style += f"--is:{sl['is']}px;"
    if sl.get("hd"):
        style += f"--hd:{sl['hd']}px;"
    if sl.get("hs"):
        style += f"--hs:{sl['hs']}px;"
    swipe = '<div class="swipe">SWIPE &rarr;</div>' if sl.get("swipe") else ""
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="s" style="{style};position:relative"><div class="main">{out}<div class="art">{art}</div></div>'
            f'<div class="src">{md(sl.get("src", ""))}</div>'
            f'<div class="foot"><div class="brand">WEALTH BRIDGE NETWORK</div>{badge()}</div>{swipe}</div></body></html>')


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
            for i, sl in enumerate(post["slides"], 1):
                pg.set_content(slide_html(sl))
                pg.evaluate("document.fonts.ready")
                m = pg.evaluate("(()=>{const m=document.querySelector('.main');return [m.scrollHeight,m.clientHeight]})()")
                if m[0] > m[1] + 2:
                    print(f"WARN {post['id']} slide {i}: content overflows by {m[0]-m[1]}px")
                pg.screenshot(path=str(d / f"slide-{i:02d}.jpg"), type="jpeg", quality=92)
            print(post["id"], len(post["slides"]), "slides")
        b.close()


if __name__ == "__main__":
    main()
