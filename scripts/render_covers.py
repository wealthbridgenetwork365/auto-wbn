"""Instagram Highlight covers (1080 x 1920): bold label + doodle palm tree, kept inside the centre circle.

Usage: python3 scripts/render_covers.py stories/covers
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

INK, GREEN, MINT = "#111", "#139A52", "#2FE08A"
COVERS = [("creators", "CREATORS"), ("affiliate", "AFFILIATE"), ("network", "JOIN US")]

FILTER = """<filter id="wob" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7"/>
<feDisplacementMap in="SourceGraphic" scale="6"/></filter>"""


def leaf(d_tip, rot, fill="#fff", vein=INK):
    """One frond: a filled leaf shape from the crown, rotated."""
    L = d_tip
    return (f'<g transform="rotate({rot})">'
            f'<path d="M0,0 Q{L*0.45},{-L*0.32} {L},{-L*0.05} Q{L*0.5},{L*0.06} 0,0 Z" fill="{fill}" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
            f'<path d="M6,-2 Q{L*0.5},{-L*0.16} {L*0.95},{-L*0.05}" fill="none" stroke="{vein}" stroke-width="5" stroke-linecap="round"/>'
            + "".join(f'<path d="M{L*t},{-L*0.12*(1-abs(t-0.5))} l{L*0.06},{-L*0.1}" stroke="{vein}" stroke-width="4" stroke-linecap="round"/>'
                      for t in (0.3, 0.45, 0.6, 0.75)) + "</g>")


def palm(fill="#fff", island=MINT, vein=INK, waves="#111"):
    # island + trunk + crown, origin = base of trunk
    b = f'<path d="M-230,0 Q0,-70 230,0 Z" fill="{island}" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
    b += f'<path d="M-260,8 L260,8" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<path d="M-200,40 q30,-14 60,0 t60,0 M90,44 q30,-14 60,0" fill="none" stroke="{waves}" stroke-width="6" stroke-linecap="round"/>'
    b += f'<path d="M-18,-40 Q-40,-200 40,-360 L74,-352 Q4,-200 22,-40 Z" fill="{fill}" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
    for i in range(1, 8):  # trunk rings
        t = i / 8
        y = -40 - 320 * t
        x = -18 + (58 * t) + (-22 * (1 - t) * t * 4)
        b += f'<path d="M{x-2},{y} q20,-12 38,2" fill="none" stroke="{vein}" stroke-width="5" stroke-linecap="round"/>'
    crown = '<g transform="translate(57,-360)">'
    for L, r in ((250, -170), (230, -140), (210, -100), (200, -60), (230, -25), (250, 5), (190, -205)):
        crown += leaf(L, r, fill, vein)
    crown += f'<circle cx="-8" cy="14" r="20" fill="{INK}"/><circle cx="24" cy="20" r="20" fill="{INK}"/><circle cx="6" cy="40" r="18" fill="{INK}"/></g>'
    return b + crown


def _q(p0, c, p1, t):
    return tuple((1-t)**2*a + 2*(1-t)*t*b + t*t*d for a, b, d in zip(p0, c, p1))


def frond2(L, tilt, side=1, ink=INK):
    """A drooping sketch frond: one arched rib with leaflets hanging off it."""
    p0, c, p1 = (0, 0), (L*0.55, -L*0.42), (L, L*0.28)
    rib = f'<path d="M0,0 Q{c[0]},{c[1]} {p1[0]},{p1[1]}" fill="none" stroke="{ink}" stroke-width="10" stroke-linecap="round"/>'
    leafs = ""
    for i in range(3, 19):
        t = i / 19
        x, y = _q(p0, c, p1, t)
        ln = 70 * (1 - t) + 22
        leafs += f'<path d="M{x:.1f},{y:.1f} q{ln*0.15:.1f},{ln*0.5:.1f} {ln*0.05:.1f},{ln:.1f}" fill="none" stroke="{ink}" stroke-width="6" stroke-linecap="round"/>'
        if t < 0.75:
            leafs += f'<path d="M{x:.1f},{y:.1f} q{-ln*0.25:.1f},{-ln*0.3:.1f} {-ln*0.15:.1f},{-ln*0.7:.1f}" fill="none" stroke="{ink}" stroke-width="5" stroke-linecap="round"/>'
    return f'<g transform="rotate({tilt}) scale({side},1)">{rib}{leafs}</g>'


def one_palm(h, lean, ink, trunk_fill):
    """Curved trunk of height h leaning by `lean` px, crown of drooping fronds at the top."""
    tx, ty = lean, -h
    b = (f'<path d="M-20,0 Q{lean*0.15-26},{-h*0.55} {tx-14},{ty} L{tx+14},{ty+4} Q{lean*0.15+18},{-h*0.55} 20,0 Z" '
         f'fill="{trunk_fill}" stroke="{ink}" stroke-width="9" stroke-linejoin="round"/>')
    for i in range(1, 9):
        t = i / 9
        x, y = _q((0, 0), (lean*0.15, -h*0.55), (tx, ty), t)
        b += f'<path d="M{x-16:.1f},{y:.1f} l12,10 l12,-10 l8,6" fill="none" stroke="{ink}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    crown = f'<g transform="translate({tx},{ty})">'
    for L, tilt, side in ((230, -12, 1), (200, 22, 1), (170, -48, 1), (230, 12, -1), (200, -22, -1), (170, 48, -1)):
        crown += frond2(L, tilt, side, ink)
    crown += (f'<circle cx="-12" cy="16" r="17" fill="{ink}"/><circle cx="14" cy="20" r="17" fill="{ink}"/>'
              f'<circle cx="0" cy="40" r="15" fill="{ink}"/></g>')
    return b + crown


def palm2(trunk_fill="#fff", island=MINT, ink=INK, waves="#111"):
    """Two leaning sketch palms on a small island."""
    b = f'<path d="M-250,0 Q0,-80 250,0 Z" fill="{island}" stroke="{ink}" stroke-width="9" stroke-linejoin="round"/>'
    b += f'<path d="M-280,8 L280,8" stroke="{ink}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<path d="M-220,42 q30,-14 60,0 t60,0 M100,46 q30,-14 60,0" fill="none" stroke="{waves}" stroke-width="6" stroke-linecap="round"/>'
    b += f'<g transform="translate(-70,-30)">{one_palm(270, -90, ink, trunk_fill)}</g>'
    b += f'<g transform="translate(40,-40)">{one_palm(380, 70, ink, trunk_fill)}</g>'
    return b


def sun():
    rays = "".join(f'<path d="M0,-78 L0,-104" transform="rotate({a})" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>' for a in range(0, 360, 45))
    return f'<circle r="60" fill="#FFE27A" stroke="{INK}" stroke-width="9"/>{rays}'


def page(label):
    fs = 128 if len(label) <= 8 else 112
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{MINT};display:flex;align-items:center;justify-content:center}}
.c{{width:780px;display:flex;flex-direction:column;align-items:center;justify-content:center}}
svg{{width:560px;height:490px;overflow:visible}}
h1{{font-family:'Inter Display','Inter',sans-serif;font-weight:900;font-size:{fs}px;letter-spacing:-.03em;line-height:1;color:{INK};margin-top:6px}}
h1 span{{display:inline-block;background:#fff;border:10px solid {INK};border-radius:22px;padding:10px 26px 14px;box-shadow:12px 14px 0 {INK}}}
</style></head><body><div class="c">
<svg viewBox="-320 -560 640 640"><defs>{FILTER}</defs><g filter="url(#wob)">
<g transform="translate(235,-500)">{sun()}</g><g transform="translate(-10,40)">{palm2()}</g></g></svg>
<h1><span>{label}</span></h1></div></body></html>"""


def page_sunset(label):
    """Design 2: black background, palm silhouette against a big sun, label on a mint marker stripe."""
    fs = 132 if len(label) <= 8 else 116
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{INK};display:flex;align-items:center;justify-content:center}}
.c{{width:780px;display:flex;flex-direction:column;align-items:center}}
svg{{width:600px;height:520px;overflow:visible}}
h1{{font-family:'Inter Display','Inter',sans-serif;font-weight:900;font-size:{fs}px;letter-spacing:-.03em;line-height:1;color:{INK};margin-top:-6px}}
h1 span{{background:{MINT};padding:4px 22px 10px;transform:rotate(-3deg);display:inline-block}}
</style></head><body><div class="c">
<svg viewBox="-320 -580 640 660"><defs>{FILTER}</defs><g filter="url(#wob)">
<circle cx="0" cy="-250" r="265" fill="#FFE27A"/>
<circle cx="0" cy="-250" r="300" fill="none" stroke="{MINT}" stroke-width="10" stroke-dasharray="4 30" stroke-linecap="round"/>
<g transform="translate(15,40) scale(.82)">{palm2(INK, INK, INK, MINT)}</g></g></svg>
<h1><span>{label}</span></h1></div></body></html>"""


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "stories/covers")
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for slug, label in COVERS:
            pg.set_content(page(label))
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=str(out / f"cover-{slug}.jpg"), type="jpeg", quality=92)
            pg.set_content(page_sunset(label))
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=str(out / f"cover2-{slug}.jpg"), type="jpeg", quality=92)
            print("cover", slug)
        b.close()


if __name__ == "__main__":
    main()
