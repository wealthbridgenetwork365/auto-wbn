"""Build the review/calendar page for a month of posts: python3 scripts/review.py content/posts.py out/"""
import importlib.util, datetime, html, calendar, json, sys
spec=importlib.util.spec_from_file_location("c",sys.argv[1]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
out=sys.argv[2]; posted=set(json.loads(sys.argv[3])) if len(sys.argv)>3 else set()
cap="Building Bridges | Creating Access\n\n#china #explore #chinatravel #Guangzhou"
cards=[]; by={}
for k,p in enumerate(m.POSTS,1):
    dt=datetime.datetime.fromisoformat(p["slot"]); by.setdefault(dt.day,[]).append((k,dt,p))
    when=dt.strftime("%a %b %-d · %-I %p")+" ET"
    st='<span class="pill live">Posted</span>' if p["id"] in posted else ""
    imgs="".join(f'<img src="p/{p["id"]}/slide-{i:02d}.jpg" alt="{html.escape(p["title"])}, slide {i}" loading="lazy" width="1080" height="1350">' for i in range(1,len(p["slides"])+1))
    cards.append(f'<article class="post" id="post-{k:02d}"><header><span class="n">{k:02d}</span><div class="meta"><div class="when">{when}</div><h2>{html.escape(p["title"])}</h2></div>{st}<span class="pill">{html.escape(p["pillar"])}</span></header>'
                 f'<div class="strip">{imgs}</div><div class="foot">{len(p["slides"])} slides · Swipe the row to see every slide</div></article>')
cells=[]
for d in calendar.Calendar(firstweekday=6).itermonthdays(2026,11):
    if d==0: cells.append('<div class="day empty" aria-hidden="true"></div>'); continue
    items="".join(f'<a class="slot{" ok" if p["id"] in posted else ""}" href="#post-{k:02d}"><img src="p/{p["id"]}/slide-01.jpg" alt="" width="1080" height="1350"><span><b>{dt.strftime("%-I %p")}</b>{html.escape(p["title"])}</span></a>' for k,dt,p in by.get(d,[]))
    if d==5: items+='<div class="done">Posted: The creator market</div>'
    cells.append(f'<div class="day{" has" if items else ""}"><div class="dn">{d}</div>{items}</div>')
n=len(m.POSTS); ns=sum(len(p["slides"]) for p in m.POSTS)
page=f'''<title>November Instagram Plan</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Manrope:wght@400;600;700&display=swap">
<style>
/* layout: calendar first, then one column of posts, each a horizontal strip of its slides */
:root{{--bg:#050505;--panel:#0E1712;--fg:#FFFFFF;--muted:#A9B1AC;--line:rgba(255,255,255,.14);--accent:#2FE08A;
--display:'Cormorant Garamond',Georgia,serif;--body:'Manrope',system-ui,sans-serif;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.5}}
.wrap{{max-width:1180px;margin:0 auto;padding-block:40px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.eyebrow{{font-size:12px;font-weight:700;letter-spacing:.38em;color:var(--accent);text-transform:uppercase}}
h1{{font-family:var(--display);font-weight:500;font-size:clamp(40px,7vw,72px);line-height:1;margin:12px 0 16px;text-wrap:balance}}
h1 em{{color:var(--accent)}}
.lede{{color:var(--muted);max-width:62ch;margin:0}}
.facts{{display:flex;flex-wrap:wrap;gap:10px 28px;margin:24px 0 8px;font-variant-numeric:tabular-nums}}
.facts div{{border-top:1px solid var(--line);padding-top:10px;min-width:150px}}
.facts b{{display:block;font-family:var(--display);font-size:34px;font-weight:600;color:var(--accent);line-height:1}}
.facts span{{color:var(--muted);font-size:13px}}
.cap{{margin:28px 0 36px;border:1px solid var(--accent);padding:18px 20px;white-space:pre-line;font-size:15px}}
.cap small{{display:block;color:var(--accent);font-weight:700;letter-spacing:.3em;font-size:11px;margin-bottom:8px}}
.cal{{margin:28px 0 8px}}.calhead{{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px;margin-bottom:12px}}
.ch{{font-family:var(--display);font-size:34px;margin:0}}.legend{{color:var(--muted);font-size:13px}}
.grid{{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}}
.wd{{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);padding:4px 6px}}
.day{{min-height:110px;border:1px solid var(--line);padding:6px;display:flex;flex-direction:column;gap:6px;min-width:0}}
.day.empty{{border:none}}.day.has{{border-color:rgba(47,224,138,.45);background:var(--panel)}}
.dn{{font-variant-numeric:tabular-nums;font-size:13px;color:var(--muted)}}
.slot{{display:flex;gap:6px;align-items:flex-start;color:var(--fg);text-decoration:none;font-size:11.5px;line-height:1.25;min-width:0}}
.slot img{{width:34px;height:auto;flex:0 0 auto;border:1px solid var(--line)}}
.slot span{{min-width:0;overflow-wrap:anywhere}}.slot b{{display:block;color:var(--accent);font-size:11px}}
.slot.ok b:after{{content:" · posted"}}
.slot:hover span,.slot:focus-visible span{{text-decoration:underline}}.slot:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.done{{font-size:11px;color:var(--accent)}}
.post{{border-top:1px solid var(--line);padding:26px 0 30px;scroll-margin-top:16px}}
.post header{{display:flex;align-items:center;gap:12px 16px;flex-wrap:wrap}}
.n{{font-family:var(--display);font-style:italic;font-size:34px;color:var(--accent);min-width:42px}}
.meta{{flex:1;min-width:0}}
.when{{font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}}
h2{{font-family:var(--display);font-weight:600;font-size:28px;margin:2px 0 0;line-height:1.1}}
.pill{{border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:12px;color:var(--muted)}}
.pill.live{{border-color:var(--accent);color:var(--accent)}}
.strip{{display:flex;gap:12px;overflow-x:auto;margin-top:16px;padding-bottom:8px;scroll-snap-type:x mandatory}}
.strip img{{width:216px;height:auto;flex:0 0 auto;scroll-snap-align:start;border:1px solid var(--line)}}
.foot{{color:var(--muted);font-size:12px;margin-top:4px}}
@media (max-width:760px){{.grid{{grid-template-columns:1fr}}.wd,.day.empty,.day:not(.has){{display:none}}.day{{min-height:0}}.slot{{font-size:14px}}.slot img{{width:44px}}}}
@media (max-width:520px){{.strip img{{width:62vw}}}}
</style>
<main class="wrap">
<div class="eyebrow">Wealth Bridge Network · Content calendar</div>
<h1>November <em>posting plan</em></h1>
<p class="lede">Every scheduled carousel for @wealthbridgenetwork, posting Mon, Wed, Fri and Sun at 11 AM and 8 PM Eastern. Tap a post in the calendar to see its slides. Every stat carries its source on the slide.</p>
<div class="facts"><div><b>{n}</b><span>posts</span></div><div><b>{ns}</b><span>slides</span></div><div><b>8</b><span>posts a week</span></div><div><b>Nov 6–30</b><span>schedule</span></div></div>
<section class="cal" aria-label="November 2026 posting calendar"><div class="calhead"><h2 class="ch">November 2026</h2><span class="legend">Mon · Wed · Fri · Sun · 11 AM and 8 PM ET</span></div>
<div class="grid">{"".join(f'<div class="wd">{w}</div>' for w in ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"])}{"".join(cells)}</div></section>
<div class="cap"><small>CAPTION ON EVERY POST</small>{html.escape(cap)}</div>
{"".join(cards)}
</main>'''
open(f"{out}/review.html","w").write(page)
print(json.dumps({f"p/{p['id']}/slide-{i:02d}.jpg":f"{p['id']}/slide-{i:02d}.jpg" for p in m.POSTS for i in range(1,len(p["slides"])+1) if p["id"] in ("04-jobs-5k","08-alipay","09-csc")}))
