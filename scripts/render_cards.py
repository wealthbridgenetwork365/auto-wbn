"""Bold-card carousel renderer with per-slide colour themes (used for the membership carousel).

Usage: python3 scripts/render_cards.py content/membership_cards.py $PWD/posts/ [post_id ...]
Slide types:
  cover  title (lines, *word* = accent), sub, pills [(label, theme)]
  tier   theme, name, kicker, items, note (perks in a card with check marks)
  cta    title, sub, pills, button
Themes: free, silver, gold, green, black.
"""
import html, importlib.util, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

W, H = 1080, 1350

THEMES = {
    # bg, ink, muted, accent (gradient for big names), card bg, card border, check bg, check ink
    "free":   dict(bg="#FFFFFF", ink="#0B0B0B", muted="#55595C", acc="linear-gradient(180deg,#111 0%,#3a3a3a 100%)",
                   card="#F3F4F5", line="#E2E4E6", chk="#0B0B0B", chki="#FFFFFF", pill="#0B0B0B", pilli="#FFFFFF"),
    "silver": dict(bg="linear-gradient(160deg,#F4F6F8 0%,#D9DEE3 55%,#B9C0C7 100%)", ink="#14181C", muted="#4A525A",
                   acc="linear-gradient(180deg,#8D969F 0%,#3E464E 55%,#1C2228 100%)",
                   card="rgba(255,255,255,.72)", line="rgba(20,24,28,.12)", chk="#5E6770", chki="#FFFFFF", pill="#14181C", pilli="#FFFFFF"),
    "gold":   dict(bg="radial-gradient(120% 80% at 80% 0%,#2A2110 0%,#0D0B07 60%)", ink="#FFF8E7", muted="#CDBF9C",
                   acc="linear-gradient(180deg,#FFE7A3 0%,#E8B84A 45%,#B07F1E 100%)",
                   card="rgba(255,231,163,.07)", line="rgba(232,184,74,.35)", chk="#E8B84A", chki="#0D0B07", pill="#E8B84A", pilli="#0D0B07"),
    "green":  dict(bg="radial-gradient(120% 80% at 20% 0%,#135C3A 0%,#07291A 65%)", ink="#EFFFF6", muted="#A9D9BF",
                   acc="linear-gradient(180deg,#7CFFC0 0%,#2FE08A 50%,#16A863 100%)",
                   card="rgba(47,224,138,.08)", line="rgba(47,224,138,.35)", chk="#2FE08A", chki="#07291A", pill="#2FE08A", pilli="#07291A"),
    "black":  dict(bg="radial-gradient(110% 70% at 50% 0%,#1B1F1D 0%,#050505 70%)", ink="#FFFFFF", muted="#A9AFAC",
                   acc="linear-gradient(90deg,#FFFFFF 0%,#C9CED3 30%,#E8B84A 62%,#2FE08A 100%)",
                   card="rgba(255,255,255,.06)", line="rgba(255,255,255,.14)", chk="#2FE08A", chki="#050505", pill="#2FE08A", pilli="#050505"),
}
PILL = {  # small tier chips
    "free": ("#FFFFFF", "#0B0B0B", "#FFFFFF"),
    "silver": ("linear-gradient(180deg,#F1F3F5,#AEB6BE)", "#14181C", "transparent"),
    "gold": ("linear-gradient(180deg,#FFE7A3,#D9A53A)", "#1A1305", "transparent"),
    "green": ("linear-gradient(180deg,#7CFFC0,#22C77A)", "#06251A", "transparent"),
}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:'Poppins',sans-serif}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;display:flex;flex-direction:column;padding:84px 88px 0;background:var(--bg);color:var(--ink)}
.top{display:flex;justify-content:space-between;align-items:center}
.lbl{font-family:'Inter';font-weight:800;font-size:24px;letter-spacing:.32em;text-transform:uppercase;color:var(--muted)}
.cnt{font-family:'Inter';font-weight:700;font-size:24px;letter-spacing:.2em;color:var(--muted)}
.big{font-family:'Inter Display','Inter',sans-serif;font-weight:900;letter-spacing:-.045em;line-height:.86;text-transform:uppercase}
.grad{background:var(--acc);-webkit-background-clip:text;background-clip:text;color:transparent}
.name{font-size:250px;margin-top:70px}
.mem{font-family:'Inter Display';font-weight:900;font-size:92px;letter-spacing:-.03em;line-height:1;text-transform:uppercase;margin-top:14px}
.kick{font-size:34px;font-weight:600;color:var(--muted);margin-top:26px}
.card{margin-top:34px;margin-bottom:24px;background:var(--card);border:2px solid var(--line);border-radius:44px;padding:40px 44px;display:flex;flex-direction:column;gap:24px;backdrop-filter:blur(2px)}
.it{display:flex;align-items:center;gap:26px;font-size:var(--is,38px);font-weight:600;line-height:1.2}
.ck{flex:none;width:52px;height:52px;border-radius:50%;background:var(--chk);display:flex;align-items:center;justify-content:center}
.it em{font-style:normal;background:var(--acc);-webkit-background-clip:text;background-clip:text;color:transparent;font-weight:800}
.foot{margin-top:auto;height:150px;display:flex;align-items:center;justify-content:space-between;border-top:2px solid var(--line)}
.brand{font-family:'Inter';font-weight:700;font-size:24px;letter-spacing:.34em;color:var(--muted)}
.btn{font-family:'Inter';font-weight:800;font-size:26px;letter-spacing:.12em;text-transform:uppercase;background:var(--pill);color:var(--pilli);padding:24px 38px;border-radius:999px;display:flex;gap:14px;align-items:center}
.badge{position:absolute;right:88px;top:330px;width:170px;height:170px}
.pills{display:flex;flex-wrap:wrap;gap:18px;margin-top:48px}
.pl{font-family:'Inter';font-weight:900;font-size:34px;letter-spacing:.08em;padding:22px 40px;border-radius:999px;border:3px solid}
.sub{font-size:40px;font-weight:600;color:var(--muted);margin-top:40px;line-height:1.3;max-width:860px}
"""

CHECK = '<svg width="28" height="28" viewBox="0 0 28 28"><path d="M6 14.5 L11.5 20 L22 8.5" fill="none" stroke="{c}" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg width="30" height="22" viewBox="0 0 30 22"><path d="M2 11 H26 M17 3 L27 11 L17 19" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def md(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t).replace("\n", "<br>")


def badge(theme, letter):
    """Medal badge in the tier colour."""
    stops = {"free": ("#FFFFFF", "#D5D8DB", "#0B0B0B"), "silver": ("#FFFFFF", "#9AA3AC", "#1C2228"),
             "gold": ("#FFE7A3", "#B07F1E", "#1A1305"), "green": ("#7CFFC0", "#16A863", "#06251A")}[theme]
    ring = "#0B0B0B" if theme == "free" else "rgba(0,0,0,.25)"
    return (f'<svg class="badge" viewBox="0 0 200 200"><defs><linearGradient id="m" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{stops[0]}"/><stop offset="1" stop-color="{stops[1]}"/></linearGradient></defs>'
            f'<path d="M62 120 L40 192 L72 178 L88 200 L100 140 Z" fill="{stops[1]}" opacity=".85"/>'
            f'<path d="M138 120 L160 192 L128 178 L112 200 L100 140 Z" fill="{stops[1]}" opacity=".85"/>'
            f'<circle cx="100" cy="88" r="80" fill="url(#m)" stroke="{ring}" stroke-width="5"/>'
            f'<circle cx="100" cy="88" r="62" fill="none" stroke="{stops[2]}" stroke-opacity=".25" stroke-width="3" stroke-dasharray="4 7"/>'
            f'<text x="100" y="112" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="72" fill="{stops[2]}">{letter}</text></svg>')


def frame(theme, inner, i, n, label="Membership", foot_btn="Link in bio"):
    t = THEMES[theme]
    style = ";".join(f"--{k}:{v}" for k, v in t.items())
    style = style.replace("--line", "--line").replace("--card", "--card")
    style = style.replace("--chk", "--chk").replace("--chki", "--chki")
    style += ";--muted:" + t["muted"]
    btn = f'<div class="btn">{foot_btn} {ARROW}</div>' if foot_btn else ""
    return (f'<div class="s" style="{style}"><div class="top"><div class="lbl">{label}</div><div class="cnt">{i:02d} / {n:02d}</div></div>'
            f'{inner}<div class="foot"><div class="brand">WEALTH BRIDGE NETWORK</div>{btn}</div></div>')


def pills(items):
    out = ""
    for label, th in items:
        bg, ink, border = PILL[th]
        out += f'<div class="pl" style="background:{bg};color:{ink};border-color:{border if border != "transparent" else "transparent"}">{label}</div>'
    return f'<div class="pills">{out}</div>'


def s_cover(s, i, n):
    title = "".join(f'<div>{md(l)}</div>' for l in s["title"])
    title = title.replace("<em>", '<span class="grad">').replace("</em>", "</span>")
    inner = (f'<div class="big" style="font-size:{s.get("size", 228)}px;margin-top:120px">{title}</div>'
             f'<div class="sub">{md(s["sub"])}</div>{pills(s["pills"])}')
    return frame("black", inner, i, n, s.get("label", "Wealth Bridge Network"), "Swipe")


VERIFIED = ('<svg width="44" height="44" viewBox="0 0 24 24" style="vertical-align:-9px;margin-left:10px">'
            '<path fill="#1D9BF0" d="M12 1.5l2.4 1.8 3-.2 1 2.8 2.6 1.6-.7 2.9 1.3 2.7-2.1 2.1-.2 3-2.9.6-1.6 2.5-2.8-.9-2.8.9-1.6-2.5-2.9-.6-.2-3L1.6 13l1.3-2.7-.7-2.9 2.6-1.6 1-2.8 3 .2z"/>'
            '<path d="M7.6 12.3l3 3 5.8-6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def s_tier(s, i, n):
    th = s["theme"]
    chk = THEMES[th]["chki"]
    items = "".join(f'<div class="it"><div class="ck">{CHECK.format(c=chk)}</div><div>{md(x).replace("[v]", VERIFIED)}</div></div>' for x in s["items"])
    inner = ((badge(th, s["letter"]) if s.get("badge") else "")
             + f'<div class="big name grad" style="font-size:{s.get("size", 250)}px">{s["name"]}</div>'
             f'<div class="mem">Membership</div>'
             f'<div class="kick">{md(s["kicker"])}</div>'
             f'<div class="card" style="--is:{s.get("is", 38)}px;gap:{s.get("gap", 24)}px">{items}</div>')
    return frame(th, inner, i, n, s.get("label", "Membership"))


def s_cta(s, i, n):
    title = "".join(f'<div>{md(l)}</div>' for l in s["title"]).replace("<em>", '<span class="grad">').replace("</em>", "</span>")
    inner = (f'<div class="big" style="font-size:{s.get("size", 200)}px;margin-top:120px">{title}</div>'
             f'<div class="sub">{md(s["sub"])}</div>{pills(s["pills"])}'
             f'<div style="margin-top:56px"><div class="btn" style="display:inline-flex;font-size:34px;padding:34px 56px">{s["button"]} {ARROW}</div></div>')
    return frame("black", inner, i, n, s.get("label", "Join today"), "")


TYPES = dict(cover=s_cover, tier=s_tier, cta=s_cta)


def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def main():
    spec = importlib.util.spec_from_file_location("content", sys.argv[1])
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    out = Path(sys.argv[2]).resolve()
    only = set(sys.argv[3:])
    tmp = out / "_html"; tmp.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": W, "height": H})
        for post in mod.POSTS:
            if only and post["id"] not in only:
                continue
            d = out / post["id"]; d.mkdir(exist_ok=True)
            for old in d.glob("slide-*.jpg"):
                old.unlink()
            n = len(post["slides"])
            for k, s in enumerate(post["slides"], 1):
                hp = tmp / f'{post["id"]}_{k}.html'
                hp.write_text(page(TYPES[s["type"]](s, k, n)))
                pg.goto(f"file://{hp}")
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(80)
                pg.screenshot(path=str(d / f"slide-{k:02d}.jpg"), type="jpeg", quality=92)
            print(post["id"], n, "slides")
        b.close()
    import shutil; shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
