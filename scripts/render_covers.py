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


def leaf(d_tip, rot):
    """One frond: a filled leaf shape from the crown, rotated."""
    L = d_tip
    return (f'<g transform="rotate({rot})">'
            f'<path d="M0,0 Q{L*0.45},{-L*0.32} {L},{-L*0.05} Q{L*0.5},{L*0.06} 0,0 Z" fill="#fff" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
            f'<path d="M6,-2 Q{L*0.5},{-L*0.16} {L*0.95},{-L*0.05}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            + "".join(f'<path d="M{L*t},{-L*0.12*(1-abs(t-0.5))} l{L*0.06},{-L*0.1}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
                      for t in (0.3, 0.45, 0.6, 0.75)) + "</g>")


def palm():
    # island + trunk + crown, origin = base of trunk
    b = f'<path d="M-230,0 Q0,-70 230,0 Z" fill="{MINT}" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
    b += f'<path d="M-260,8 L260,8" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
    b += '<path d="M-200,40 q30,-14 60,0 t60,0 M90,44 q30,-14 60,0" fill="none" stroke="#111" stroke-width="6" stroke-linecap="round"/>'
    b += f'<path d="M-18,-40 Q-40,-200 40,-360 L74,-352 Q4,-200 22,-40 Z" fill="#fff" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
    for i in range(1, 8):  # trunk rings
        t = i / 8
        y = -40 - 320 * t
        x = -18 + (58 * t) + (-22 * (1 - t) * t * 4)
        b += f'<path d="M{x-2},{y} q20,-12 38,2" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    crown = '<g transform="translate(57,-360)">'
    for L, r in ((250, -170), (230, -140), (210, -100), (200, -60), (230, -25), (250, 5), (190, -205)):
        crown += leaf(L, r)
    crown += f'<circle cx="-8" cy="14" r="20" fill="{INK}"/><circle cx="24" cy="20" r="20" fill="{INK}"/><circle cx="6" cy="40" r="18" fill="{INK}"/></g>'
    return b + crown


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
<g transform="translate(235,-500)">{sun()}</g><g transform="translate(-30,40)">{palm()}</g></g></svg>
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
            print("cover", slug)
        b.close()


if __name__ == "__main__":
    main()
