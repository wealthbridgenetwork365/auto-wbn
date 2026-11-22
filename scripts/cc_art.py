"""Painterly vector scenes for the Content Creation series (no photos, no real people).

Every scene returns a full <svg> sized 1080 x H (default 1350) with
preserveAspectRatio="xMidYMid slice", so it can fill a full slide or a half.
"""
import math, random

W = 1080


def _svg(body, h=1350, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="100%" height="100%" '
            f'preserveAspectRatio="xMidYMid slice"><defs>{defs}'
            '<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>'
            '<filter id="blur20"><feGaussianBlur stdDeviation="20"/></filter>'
            '<filter id="blur40"><feGaussianBlur stdDeviation="40"/></filter>'
            '<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/>'
            '<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0"/></filter>'
            f'</defs>{body}<rect width="{W}" height="{h}" filter="url(#grain)"/></svg>')


def _lg(id_, stops, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def _rg(id_, stops, cx=.5, cy=.5, r=.5):
    s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o, c, a in stops)
    return f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'


def _ridge(y, amp, seed, step=40, h=1350, rough=1.0):
    r = random.Random(seed)
    pts = []
    x = -40
    v = 0
    while x <= W + 40:
        v = v * .6 + r.uniform(-1, 1) * amp * rough
        pts.append(f"{x},{y + v + math.sin(x / 170 + seed) * amp:.0f}")
        x += step
    return f"M-40,{h} L" + " L".join(pts) + f" L{W+40},{h} Z"


# ------------------------------------------------------------------ people (faceless silhouettes)
def person_stand(x, y, s=1.0, c="#0B0F0D", bag=False):
    b = (f'<circle cx="0" cy="-262" r="30" fill="{c}"/>'
         f'<path d="M-44,-222 Q0,-236 44,-222 L54,-110 L30,-110 L28,0 L6,0 L0,-96 L-6,0 L-28,0 L-30,-110 L-54,-110 Z" fill="{c}"/>')
    if bag:
        b += f'<rect x="38" y="-210" width="34" height="80" rx="10" fill="{c}"/>'
    return f'<g transform="translate({x},{y}) scale({s})">{b}</g>'


def person_desk(x, y, s=1.0, c="#06090A", slump=True):
    tilt = 18 if slump else 0
    b = (f'<g transform="rotate({tilt} 0 -150)"><circle cx="0" cy="-232" r="31" fill="{c}"/></g>'
         f'<path d="M-58,-186 Q0,-206 58,-186 L66,-40 L-66,-40 Z" fill="{c}"/>'
         + (f'<path d="M40,-180 L92,-130 L70,-200 Z" fill="{c}"/>' if slump else ""))
    return f'<g transform="translate({x},{y}) scale({s})">{b}</g>'


def person_lounge(x, y, s=1.0, c="#141210"):
    b = (f'<path d="M-170,0 L-120,-70 L120,-70 L160,-150 L176,-142 L140,-56 L-104,-56 L-150,0 Z" fill="#E9DCC6"/>'
         f'<path d="M-160,0 L-150,-60 M150,-60 L140,0" stroke="#5B4A36" stroke-width="10"/>'
         f'<circle cx="150" cy="-176" r="26" fill="{c}"/>'
         f'<path d="M128,-150 L170,-150 L120,-80 L-60,-82 L-120,-70 L-128,-90 L-60,-104 L96,-104 Z" fill="{c}"/>')
    return f'<g transform="translate({x},{y}) scale({s})">{b}</g>'


# ------------------------------------------------------------------ landscapes
def zhangjiajie(h=1350):
    d = _lg("zs", [(0, "#F4D3A8"), (.5, "#DCE3D6"), (1, "#9FB5AA")])
    b = f'<rect width="{W}" height="{h}" fill="url(#zs)"/>'
    b += '<circle cx="760" cy="300" r="140" fill="#FFF1D6" opacity=".85" filter="url(#blur20)"/>'
    r = random.Random(4)
    layers = [("#B7C6BE", "#A3B5AC", 7, 380, 620, 90), ("#7F988D", "#6A8478", 6, 520, 760, 120),
              ("#4B6658", "#3A5446", 5, 660, 900, 150), ("#25392F", "#1A2B22", 4, 800, 1100, 190)]
    for li, (lit, shade, n, tmin, tmax, wd) in enumerate(layers):
        for i in range(n):
            cx = (i + r.uniform(.1, .9)) * (W + 100) / n - 50
            w = wd * r.uniform(.7, 1.25)
            top = r.uniform(tmin, tmax) - 260
            ys = list(range(int(top) + 40, h + 40, 60))
            left = [(cx - w / 2 + r.uniform(-10, 10) + (y - top) * .02, y) for y in ys]
            right = [(cx + w / 2 + r.uniform(-10, 10) - (y - top) * .01, y) for y in ys]
            path = f"M{left[0][0]:.0f},{left[0][1]} Q{cx:.0f},{top-10:.0f} {right[0][0]:.0f},{right[0][1]}"
            path += "".join(f" L{x:.0f},{y}" for x, y in right[1:]) + "".join(f" L{x:.0f},{y}" for x, y in reversed(left))
            b += f'<path d="{path} Z" fill="{lit}"/>'
            b += f'<path d="M{cx+w*.12:.0f},{top+30:.0f} L{right[0][0]:.0f},{right[0][1]}' + "".join(f" L{x:.0f},{y}" for x, y in right[1:]) + f' L{cx+w*.12:.0f},{h+40} Z" fill="{shade}"/>'
            for k in range(3, len(ys), 3):
                b += f'<path d="M{left[k][0]:.0f},{ys[k]} L{right[k][0]:.0f},{ys[k]+8}" stroke="{shade}" stroke-width="4" opacity=".6"/>'
            for k in range(5):
                tx = cx - w * .45 + k * w * .22
                b += f'<ellipse cx="{tx:.0f}" cy="{top+20+r.uniform(-6,6):.0f}" rx="{w*.17:.0f}" ry="{w*.11:.0f}" fill="{["#5E8A5A","#4C7A4C","#3A6640","#2C5233"][li]}"/>'
            for k in range(2):
                sy = top + r.uniform(80, 400)
                b += f'<ellipse cx="{cx - w/2 + r.choice([0, w]):.0f}" cy="{sy:.0f}" rx="{w*.14:.0f}" ry="{w*.08:.0f}" fill="{["#5E8A5A","#4C7A4C","#3A6640","#2C5233"][li]}"/>'
        b += f'<rect x="-60" y="{tmax-40}" width="{W+120}" height="120" fill="#F3F1EA" opacity=".6" filter="url(#blur40)"/>'
    b += f'<rect x="-40" y="{h-300}" width="{W+80}" height="260" fill="#EEF2EE" opacity=".45" filter="url(#blur40)"/>'
    return _svg(b, h, d)


def guizhou(h=1350):
    d = _lg("gs", [(0, "#BFE0E8"), (.5, "#E8F1E4"), (1, "#7FAE7A")])
    b = f'<rect width="{W}" height="{h}" fill="url(#gs)"/>'
    r = random.Random(9)
    for col, base, n, hh in [("#9CC2A6", 560, 7, 260), ("#5E9A6A", 700, 6, 300), ("#3C7A4B", 820, 5, 280)]:
        for i in range(n):
            cx = -60 + i * (W + 120) / (n - 1) + r.uniform(-40, 40)
            ww = r.uniform(180, 260)
            top = base - hh * r.uniform(.7, 1.1)
            b += f'<path d="M{cx-ww:.0f},{base+200} Q{cx-ww*.35:.0f},{top+40:.0f} {cx:.0f},{top:.0f} Q{cx+ww*.35:.0f},{top+40:.0f} {cx+ww:.0f},{base+200} Z" fill="{col}"/>'
        b += f'<rect x="-40" y="{base+20}" width="{W+80}" height="70" fill="#F4FAF5" opacity=".55" filter="url(#blur20)"/>'
    # waterfall cliff
    b += '<path d="M380,640 L700,620 L720,980 L360,990 Z" fill="#46604F"/>'
    for i in range(14):
        x = 450 + i * 14
        b += f'<path d="M{x},{632} Q{x+6},{800} {x-4},{985}" stroke="#FFFFFF" stroke-opacity="{.55+.03*(i%5):.2f}" stroke-width="{9+(i%3)*3}" fill="none"/>'
    b += '<ellipse cx="540" cy="990" rx="260" ry="60" fill="#FFFFFF" opacity=".8" filter="url(#blur20)"/>'
    # terraces
    for i in range(9):
        y = 1010 + i * 40
        col = ["#8DBF5A", "#A7CC6B", "#79AE4D"][i % 3]
        b += f'<path d="M-40,{y} Q270,{y-50} 540,{y-10} T1120,{y-30} L1120,{h} L-40,{h} Z" fill="{col}"/>'
        b += f'<path d="M-40,{y} Q270,{y-50} 540,{y-10} T1120,{y-30}" stroke="#D9EBB8" stroke-width="5" fill="none" opacity=".8"/>'
    return _svg(b, h, d)


def xinjiang(h=1350):
    d = _lg("xs", [(0, "#2E5E9E"), (.5, "#8DBBE6"), (1, "#E7F1FA")]) + _lg("xl", [(0, "#4FC3C9"), (1, "#1E7F96")])
    b = f'<rect width="{W}" height="{h}" fill="url(#xs)"/>'
    peaks = [(-80, 700, 300), (220, 700, 230), (520, 700, 360), (820, 700, 260), (1100, 700, 320)]
    for cx, base, top in peaks:
        b += f'<path d="M{cx-330},{base} L{cx},{top} L{cx+330},{base} Z" fill="#6A7F9C"/>'
        b += f'<path d="M{cx-120},{top+100} L{cx},{top} L{cx+120},{top+100} L{cx+70},{top+80} L{cx+30},{top+120} L{cx-20},{top+86} L{cx-70},{top+116} Z" fill="#FFFFFF"/>'
        b += f'<path d="M{cx},{top} L{cx+330},{base} L{cx+90},{base} Z" fill="#4E627F" opacity=".6"/>'
    b += _ridge(720, 18, 2, h=h).replace("Z", "Z") and f'<path d="{_ridge(720, 18, 2, h=h)}" fill="#3F6B4F"/>'
    b += f'<rect x="0" y="760" width="{W}" height="230" fill="url(#xl)"/>'
    for i in range(10):
        b += f'<rect x="{80+i*90}" y="{790+i*19}" width="{180-i*6}" height="4" fill="#FFFFFF" opacity=".35"/>'
    b += f'<path d="{_ridge(990, 14, 5, h=h)}" fill="#C9A45C"/>'
    b += f'<path d="{_ridge(1080, 22, 8, h=h)}" fill="#B08540"/>'
    b += f'<path d="{_ridge(1200, 26, 11, h=h)}" fill="#8A6430"/>'
    # yurt
    b += '<g transform="translate(250,1040)"><path d="M-70,0 L-70,-50 Q0,-100 70,-50 L70,0 Z" fill="#F4ECDD"/><path d="M-70,-50 Q0,-100 70,-50" stroke="#B5543C" stroke-width="8" fill="none"/><rect x="-14" y="-38" width="28" height="38" fill="#B5543C"/></g>'
    return _svg(b, h, d)


def chengdu(h=1350):
    d = _lg("cs", [(0, "#1B2340"), (.55, "#C46A5A"), (1, "#F2B27A")])
    b = f'<rect width="{W}" height="{h}" fill="url(#cs)"/>'
    r = random.Random(3)
    x = 0
    while x < W:
        w = r.uniform(50, 110)
        top = r.uniform(520, 760)
        b += f'<rect x="{x:.0f}" y="{top:.0f}" width="{w:.0f}" height="{h}" fill="#2A2238"/>'
        for yy in range(int(top) + 20, 980, 34):
            for xx in range(int(x) + 10, int(x + w) - 10, 22):
                if r.random() < .35:
                    b += f'<rect x="{xx}" y="{yy}" width="10" height="14" fill="#FFD48A" opacity=".75"/>'
        x += w + r.uniform(4, 16)
    b += '<path d="M600,560 L610,300 L622,300 L632,560 Z" fill="#2A2238"/><circle cx="616" cy="300" r="6" fill="#FF6B5A"/>'
    b += f'<rect x="0" y="940" width="{W}" height="{h}" fill="#141120"/>'
    # lanterns
    b += '<path d="M-20,880 Q540,960 1100,870" stroke="#3A2A2A" stroke-width="4" fill="none"/>'
    for i in range(9):
        lx = 40 + i * 125
        ly = 900 + 22 * math.sin(i / 8 * math.pi)
        b += f'<g transform="translate({lx},{ly:.0f})"><line x1="0" y1="-20" x2="0" y2="0" stroke="#3A2A2A" stroke-width="3"/><ellipse cx="0" cy="28" rx="24" ry="30" fill="#E2412E"/><ellipse cx="0" cy="28" rx="34" ry="40" fill="#FF6B4A" opacity=".35" filter="url(#blur8)"/><rect x="-10" y="56" width="20" height="8" fill="#F2B84B"/></g>'
    # bamboo foreground
    for bx, col in [(60, "#1E4D2B"), (140, "#2B6A3A"), (960, "#1E4D2B"), (1030, "#2B6A3A")]:
        b += f'<rect x="{bx}" y="560" width="26" height="{h}" fill="{col}"/>'
        for yy in range(600, h, 120):
            b += f'<rect x="{bx-3}" y="{yy}" width="32" height="7" fill="#163A20"/>'
            b += f'<path d="M{bx+26},{yy} q60,-20 110,10 q-60,0 -110,-10" fill="{col}"/>'
    # panda
    b += ('<g transform="translate(780,1240)"><ellipse cx="0" cy="-70" rx="96" ry="82" fill="#F5F3EE"/>'
          '<ellipse cx="0" cy="-30" rx="110" ry="56" fill="#111"/>'
          '<circle cx="0" cy="-180" r="66" fill="#F5F3EE"/><circle cx="-54" cy="-236" r="24" fill="#111"/><circle cx="54" cy="-236" r="24" fill="#111"/>'
          '<ellipse cx="-24" cy="-186" rx="15" ry="20" fill="#111" transform="rotate(-20 -24 -186)"/><ellipse cx="24" cy="-186" rx="15" ry="20" fill="#111" transform="rotate(20 24 -186)"/>'
          '<ellipse cx="0" cy="-160" rx="11" ry="7" fill="#111"/>'
          '<path d="M-70,-110 Q-120,-60 -60,-30" stroke="#111" stroke-width="40" fill="none" stroke-linecap="round"/>'
          '<path d="M70,-110 Q130,-140 120,-190" stroke="#111" stroke-width="38" fill="none" stroke-linecap="round"/>'
          '<rect x="112" y="-330" width="14" height="220" fill="#3B8A4A" transform="rotate(12 119 -220)"/></g>')
    return _svg(b, h, d)


def hainan(h=1350, sunset=True, lounger=False):
    d = (_lg("hs", [(0, "#2C6FB7"), (.45, "#F6B47A"), (.62, "#FFD9A0")] if sunset else [(0, "#4BA3E3"), (.6, "#BDE3F7"), (1, "#E8F6FC")])
         + _lg("hw", [(0, "#2BA6B8"), (1, "#0E5F7E")]) + _lg("hb", [(0, "#F2DDB2"), (1, "#E1BF86")]))
    b = f'<rect width="{W}" height="{h}" fill="url(#hs)"/>'
    b += '<circle cx="560" cy="640" r="96" fill="#FFF3D6"/><circle cx="560" cy="640" r="190" fill="#FFE3A8" opacity=".45" filter="url(#blur40)"/>'
    for i, (cx, cy, rx) in enumerate([(220, 300, 160), (820, 240, 200), (520, 420, 120)]):
        b += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{rx*.22:.0f}" fill="#FFFFFF" opacity=".45" filter="url(#blur8)"/>'
    b += f'<rect x="0" y="700" width="{W}" height="360" fill="url(#hw)"/>'
    for i in range(16):
        b += f'<rect x="{470 - i*4}" y="{712 + i*20}" width="{180 + i*8}" height="5" rx="2" fill="#FFE7B5" opacity="{.8 - i*.04:.2f}"/>'
    b += f'<path d="M-40,1060 Q300,1010 560,1050 T1120,1030 L1120,{h} L-40,{h} Z" fill="url(#hb)"/>'
    b += '<path d="M-40,1060 Q300,1010 560,1050 T1120,1030" stroke="#FFFFFF" stroke-width="10" fill="none" opacity=".8"/>'

    def palm(x, y, s, flip=1):
        g = f'<path d="M0,0 Q{20*flip},-200 {70*flip},-420" stroke="#2E2218" stroke-width="22" fill="none" stroke-linecap="round"/>'
        for a in (-150, -110, -60, -20, 20, 60):
            rad = math.radians(a)
            ex, ey = 70 * flip + 230 * math.cos(rad) * flip, -420 + 230 * math.sin(rad) * .55 + 60
            g += f'<path d="M{70*flip},-420 Q{(70*flip+ex)/2:.0f},{-500+ (a>0)*60} {ex:.0f},{ey:.0f}" stroke="#1F3A1E" stroke-width="26" fill="none" stroke-linecap="round"/>'
        return f'<g transform="translate({x},{y}) scale({s})">{g}</g>'
    b += palm(90, 1200, 1.25) + palm(990, 1160, 1.05, -1) + palm(880, 1230, .8, -1)
    if lounger:
        b += ('<g transform="translate(560,1240)"><path d="M-10,-120 L-10,-300" stroke="#5B4A36" stroke-width="10"/>'
              '<path d="M-200,-280 Q-10,-400 180,-280 Z" fill="#E9573F"/><path d="M-200,-280 Q-110,-330 -10,-300 Q80,-330 180,-280" fill="#F4E6D0" opacity=".25"/></g>')
        b += person_lounge(560, 1240, 1.15)
    return _svg(b, h, d)


# ------------------------------------------------------------------ city / interiors
def skyline_dusk(h=1350):
    d = _lg("ks", [(0, "#0B1A2C"), (.6, "#1F4E5F"), (1, "#E0915E")])
    b = f'<rect width="{W}" height="{h}" fill="url(#ks)"/>'
    r = random.Random(12)
    b += '<path d="M480,1000 L500,420 L512,330 L524,420 L544,1000 Z" fill="#0E2130"/>'
    b += '<circle cx="512" cy="560" r="40" fill="#0E2130"/><circle cx="512" cy="760" r="62" fill="#0E2130"/><circle cx="512" cy="760" r="20" fill="#FF7A6A" opacity=".9"/>'
    b += '<path d="M700,1000 L716,360 L760,300 L800,360 L812,1000 Z" fill="#102638"/>'
    b += '<path d="M260,1000 L270,470 L330,440 L340,1000 Z" fill="#102638"/>'
    x = 0
    while x < W:
        w = r.uniform(40, 90)
        top = r.uniform(680, 860)
        b += f'<rect x="{x:.0f}" y="{top:.0f}" width="{w:.0f}" height="400" fill="#0A1824"/>'
        for yy in range(int(top) + 14, 1000, 26):
            for xx in range(int(x) + 8, int(x + w) - 8, 16):
                if r.random() < .3:
                    b += f'<rect x="{xx}" y="{yy}" width="7" height="10" fill="#FFE1A0" opacity=".7"/>'
        x += w + r.uniform(2, 10)
    b += f'<rect x="0" y="1000" width="{W}" height="{h}" fill="#071019"/>'
    for i in range(30):
        b += f'<rect x="{r.uniform(0, W):.0f}" y="{1010 + r.uniform(0, 300):.0f}" width="{r.uniform(20, 120):.0f}" height="3" fill="#FFD48A" opacity=".25"/>'
    return _svg(b, h, d)


def office_night(h=1350, slump=True):
    d = _lg("os", [(0, "#0A1120"), (1, "#162238")]) + _rg("mon", [(0, "#BFE6FF", .55), (1, "#BFE6FF", 0)], .5, .5, .5)
    b = f'<rect width="{W}" height="{h}" fill="url(#os)"/>'
    # window with city
    b += '<rect x="90" y="120" width="900" height="560" fill="#0D1B2E" stroke="#2A3550" stroke-width="10"/>'
    r = random.Random(7)
    for i in range(60):
        bx = 100 + i * 15
        top = r.uniform(330, 600)
        b += f'<rect x="{bx}" y="{top:.0f}" width="13" height="{680-top:.0f}" fill="#13233A"/>'
        for yy in range(int(top) + 6, 670, 18):
            if r.random() < .3:
                b += f'<rect x="{bx+3}" y="{yy}" width="6" height="8" fill="#FFD48A" opacity=".6"/>'
    b += '<line x1="540" y1="120" x2="540" y2="680" stroke="#2A3550" stroke-width="10"/>'
    # clock
    b += '<circle cx="900" cy="770" r="0"/>'
    # desk
    b += f'<rect x="0" y="960" width="{W}" height="40" fill="#2B2F3A"/><rect x="0" y="1000" width="{W}" height="{h}" fill="#151821"/>'
    # monitor glow + monitor
    b += '<ellipse cx="640" cy="800" rx="360" ry="260" fill="url(#mon)"/>'
    b += '<rect x="470" y="660" width="340" height="230" rx="10" fill="#0E1626" stroke="#3A4560" stroke-width="8"/>'
    b += '<rect x="486" y="676" width="308" height="198" fill="#9CCFF0" opacity=".85"/>'
    for i in range(6):
        b += f'<rect x="506" y="{696+i*28}" width="{240 - (i%3)*50}" height="10" fill="#FFFFFF" opacity=".7"/>'
    b += '<rect x="620" y="890" width="40" height="70" fill="#3A4560"/>'
    # coffee cups
    for cx in (860, 920):
        b += f'<path d="M{cx-26},920 L{cx+26},920 L{cx+20},960 L{cx-20},960 Z" fill="#E8E2D6"/>'
    # papers
    b += '<rect x="120" y="930" width="200" height="30" fill="#E8E8E8" transform="rotate(-4 220 945)"/><rect x="140" y="912" width="200" height="30" fill="#D8D8D8" transform="rotate(3 240 927)"/>'
    b += person_desk(360, 1010, 1.6, slump=slump)
    # clock on wall
    b += '<g transform="translate(160,780)"><circle r="54" fill="#E8E2D6"/><circle r="54" fill="none" stroke="#2A3550" stroke-width="8"/><line x1="0" y1="0" x2="0" y2="-36" stroke="#111" stroke-width="6"/><line x1="0" y1="0" x2="26" y2="12" stroke="#111" stroke-width="6"/></g>'
    return _svg(b, h, d)


def laptop_night(h=1350):
    d = _rg("lg", [(0, "#9FE8C4", .5), (1, "#9FE8C4", 0)], .5, .5, .5)
    b = f'<rect width="{W}" height="{h}" fill="#070B10"/>'
    b += '<ellipse cx="560" cy="820" rx="480" ry="380" fill="url(#lg)"/>'
    b += '<path d="M330,980 L360,660 L760,660 L790,980 Z" fill="#1A2230"/>'
    b += '<path d="M372,676 L748,676 L770,960 L350,960 Z" fill="#CFF5E2"/>'
    for i in range(7):
        b += f'<rect x="{410+i*4}" y="{720+i*32}" width="{300 - (i%3)*60}" height="12" rx="6" fill="#0D3B25" opacity=".55"/>'
    b += '<path d="M260,980 L860,980 L900,1010 L220,1010 Z" fill="#2A3445"/>'
    b += f'<rect x="0" y="1010" width="{W}" height="{h}" fill="#0C0F14"/>'
    b += person_desk(560, 1180, 1.9, c="#020304", slump=False)
    b += '<circle cx="880" cy="260" r="70" fill="#E8EEF5" opacity=".9"/><circle cx="905" cy="245" r="66" fill="#070B10"/>'
    return _svg(b, h, d)


def plane_window(h=1350):
    d = _lg("ps", [(0, "#2C5C9A"), (.6, "#F3B57E"), (1, "#FCE2B8")])
    b = f'<rect width="{W}" height="{h}" fill="#D8D4CC"/>'
    b += '<rect x="190" y="180" width="700" height="960" rx="300" fill="#ECE8E0"/>'
    b += '<rect x="250" y="250" width="580" height="820" rx="250" fill="url(#ps)"/>'
    b += '<clipPath id="win"><rect x="250" y="250" width="580" height="820" rx="250"/></clipPath>'
    inner = '<circle cx="660" cy="720" r="80" fill="#FFF1D2" opacity=".9" filter="url(#blur8)"/>'
    for i in range(6):
        inner += f'<ellipse cx="{300 + i*110}" cy="{860 + (i%2)*40}" rx="170" ry="60" fill="#FFFFFF" opacity=".85" filter="url(#blur8)"/>'
    inner += '<path d="M250,820 L830,700 L830,760 L250,900 Z" fill="#B9C2CC"/><path d="M700,725 L760,640 L790,642 L770,735 Z" fill="#9AA6B3"/>'
    b += f'<g clip-path="url(#win)">{inner}</g>'
    b += '<rect x="250" y="250" width="580" height="820" rx="250" fill="none" stroke="#BDB7AC" stroke-width="16"/>'
    return _svg(b, h, d)


def classroom(h=1350):
    b = f'<rect width="{W}" height="{h}" fill="#F1E9DC"/>'
    b += '<rect x="0" y="0" width="1080" height="160" fill="#E4D7C2"/>'
    b += '<rect x="150" y="260" width="780" height="420" fill="#1F4D3A" stroke="#8A6A46" stroke-width="18"/>'
    b += '<text x="540" y="430" font-family="Manrope" font-weight="800" font-size="88" fill="#F5F3EA" text-anchor="middle">Hello, class!</text>'
    b += '<text x="540" y="540" font-family="Manrope" font-weight="600" font-size="48" fill="#CFE8DA" text-anchor="middle">你好 · nǐ hǎo</text>'
    b += '<rect x="0" y="980" width="1080" height="400" fill="#C9A77E"/>'
    for i, x in enumerate([90, 330, 570, 810]):
        b += f'<rect x="{x}" y="1040" width="190" height="24" fill="#8A6A46"/><rect x="{x+20}" y="1064" width="12" height="120" fill="#5E4630"/><rect x="{x+158}" y="1064" width="12" height="120" fill="#5E4630"/>'
        b += f'<circle cx="{x+95}" cy="960" r="34" fill="#2B2B33"/><path d="M{x+45},1040 Q{x+95},970 {x+145},1040 Z" fill="#2B2B33"/>'
    b += person_stand(820, 980, 1.25, c="#1A1F2B")
    b += '<path d="M770,740 L700,660" stroke="#1A1F2B" stroke-width="22" stroke-linecap="round"/>'
    for x in (60, 960):
        b += f'<rect x="{x}" y="300" width="60" height="300" fill="#E9F3FA" stroke="#B7A27E" stroke-width="10"/>'
    return _svg(b, h)


def graduation(h=1350):
    d = _lg("gr", [(0, "#14213D"), (1, "#2C3E66")])
    b = f'<rect width="{W}" height="{h}" fill="url(#gr)"/>'
    r = random.Random(5)
    for i in range(50):
        b += f'<rect x="{r.uniform(0,W):.0f}" y="{r.uniform(0,700):.0f}" width="14" height="6" fill="{r.choice(["#F2C14E","#FFFFFF","#2FE08A"])}" transform="rotate({r.uniform(0,180):.0f})" opacity=".7"/>'
    # caps flying
    for cx, cy, rot, s in [(300, 300, -18, 1.1), (720, 220, 14, .9), (560, 470, -6, .7)]:
        b += (f'<g transform="translate({cx},{cy}) rotate({rot}) scale({s})"><path d="M-130,0 L0,-50 L130,0 L0,50 Z" fill="#0B0F1A"/>'
              f'<path d="M-70,22 L-70,70 Q0,100 70,70 L70,22" fill="#0B0F1A"/><path d="M0,0 L100,30 L100,90" stroke="#F2C14E" stroke-width="6" fill="none"/></g>')
    b += f'<rect x="0" y="900" width="{W}" height="{h}" fill="#0E1626"/>'
    # diploma + bills
    b += '<g transform="translate(300,1010) rotate(-8)"><rect x="-150" y="-40" width="300" height="80" rx="40" fill="#F4ECD8"/><rect x="-20" y="-44" width="40" height="88" fill="#B5543C"/></g>'
    for i in range(5):
        b += f'<rect x="{600+i*8}" y="{940+i*24}" width="300" height="140" rx="6" fill="#F7F4EC" stroke="#C9C2B0" stroke-width="3"/>'
    b += '<text x="770" y="1060" font-family="Manrope" font-weight="800" font-size="34" fill="#B42318" text-anchor="middle">LOAN STATEMENT</text>'
    b += '<text x="770" y="1110" font-family="Manrope" font-weight="800" font-size="44" fill="#111" text-anchor="middle">BALANCE DUE</text>'
    b += '<rect x="660" y="1140" width="240" height="12" fill="#D9D3C3"/><rect x="660" y="1166" width="180" height="12" fill="#D9D3C3"/>'
    return _svg(b, h, d)


def arena(h=1350):
    d = _lg("as", [(0, "#05070B"), (1, "#16233A")]) + _rg("spot", [(0, "#FFFFFF", .55), (1, "#FFFFFF", 0)], .5, .5, .5)
    b = f'<rect width="{W}" height="{h}" fill="url(#as)"/>'
    for x in (160, 540, 920):
        b += f'<path d="M{x-30},0 L{x+30},0 L{x+260},1100 L{x-260},1100 Z" fill="#FFFFFF" opacity=".06"/>'
        b += f'<circle cx="{x}" cy="40" r="26" fill="#FFFFFF"/><circle cx="{x}" cy="40" r="90" fill="url(#spot)"/>'
    r = random.Random(2)
    for i in range(240):
        b += f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(380,700):.0f}" r="{r.uniform(3,6):.0f}" fill="#9FB0C8" opacity="{r.uniform(.15,.4):.2f}"/>'
    b += f'<path d="M-60,{h} L240,820 L840,820 L1140,{h} Z" fill="#C88A4A"/>'
    for i in range(12):
        x0 = 240 + i * 54
        b += f'<path d="M{x0},820 L{-60 + i*110},{h}" stroke="#B57A3D" stroke-width="3"/>'
    b += '<path d="M240,820 L840,820 L1140,1350 L-60,1350 Z" fill="none" stroke="#FFFFFF" stroke-width="6"/>'
    b += '<ellipse cx="540" cy="1080" rx="220" ry="90" fill="none" stroke="#FFFFFF" stroke-width="6"/>'
    b += '<line x1="70" y1="1080" x2="1010" y2="1080" stroke="#FFFFFF" stroke-width="6"/>'
    # ball
    b += ('<g transform="translate(780,330)"><circle r="92" fill="#E26B21"/>'
          '<path d="M-92,0 L92,0 M0,-92 L0,92 M-66,-64 Q0,0 -66,64 M66,-64 Q0,0 66,64" stroke="#3A1A08" stroke-width="7" fill="none"/>'
          '<circle r="92" fill="none" stroke="#3A1A08" stroke-width="5"/></g>')
    # soccer ball
    b += ('<g transform="translate(290,420)"><circle r="70" fill="#F5F5F5"/><path d="M0,-26 L25,-8 L15,22 L-15,22 L-25,-8 Z" fill="#111"/>'
          '<path d="M0,-26 L0,-70 M25,-8 L64,-24 M15,22 L40,58 M-15,22 L-40,58 M-25,-8 L-64,-24" stroke="#111" stroke-width="5"/><circle r="70" fill="none" stroke="#111" stroke-width="5"/></g>')
    return _svg(b, h, d)


def campus(h=1350):
    d = _lg("us", [(0, "#F5D9A8"), (.6, "#F7E9CF"), (1, "#E9D2A8")])
    b = f'<rect width="{W}" height="{h}" fill="url(#us)"/>'
    b += '<circle cx="820" cy="260" r="110" fill="#FFF4DA" opacity=".9" filter="url(#blur20)"/>'
    # modern tower behind
    b += '<rect x="700" y="340" width="220" height="700" fill="#C8B79C"/><rect x="100" y="420" width="180" height="620" fill="#D3C4AA"/>'
    for yy in range(370, 1000, 40):
        b += f'<rect x="720" y="{yy}" width="180" height="16" fill="#A99878"/><rect x="118" y="{yy+50}" width="144" height="14" fill="#B8A88B"/>'
    # traditional gate (generic paifang)
    g = '<g transform="translate(540,1060)">'
    g += '<rect x="-330" y="-380" width="40" height="380" fill="#9E2B25"/><rect x="290" y="-380" width="40" height="380" fill="#9E2B25"/>'
    g += '<rect x="-160" y="-430" width="36" height="430" fill="#9E2B25"/><rect x="124" y="-430" width="36" height="430" fill="#9E2B25"/>'
    g += '<path d="M-400,-380 Q0,-420 400,-380 L380,-350 L-380,-350 Z" fill="#2E3A33"/>'
    g += '<path d="M-220,-470 Q0,-520 220,-470 L200,-440 L-200,-440 Z" fill="#2E3A33"/>'
    g += '<rect x="-200" y="-440" width="400" height="40" fill="#C9A23A"/><rect x="-370" y="-350" width="740" height="30" fill="#2F6B5A"/>'
    g += '</g>'
    b += g
    b += f'<rect x="0" y="1060" width="{W}" height="{h}" fill="#BFA783"/>'
    b += '<path d="M380,1060 L700,1060 L900,1350 L180,1350 Z" fill="#D8C4A0"/>'
    # ginkgo trees
    for tx, s in [(70, 1.2), (1010, 1.1), (220, .8), (860, .8)]:
        b += f'<g transform="translate({tx},1080) scale({s})"><rect x="-10" y="-200" width="20" height="200" fill="#5B4630"/>'
        b += '<circle cx="0" cy="-260" r="100" fill="#E9B23A"/><circle cx="-60" cy="-210" r="70" fill="#F2C552"/><circle cx="60" cy="-220" r="70" fill="#D99A22"/></g>'
    b += person_stand(470, 1240, .9, c="#2B2F3A", bag=True) + person_stand(610, 1260, .95, c="#1E2A26")
    return _svg(b, h, d)


def passport_scene(h=1350):
    b = f'<rect width="{W}" height="{h}" fill="#06100B"/>'
    r = random.Random(1)
    # dotted globe
    for i in range(1400):
        th = r.uniform(0, math.pi)
        ph = r.uniform(-math.pi / 2, math.pi / 2)
        x = 540 + 430 * math.cos(ph) * math.cos(th) * 1
        y = 520 + 430 * math.sin(ph)
        if 0 < math.cos(ph):
            b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3" fill="#2FE08A" opacity="{r.uniform(.08,.35):.2f}"/>'
    b += '<circle cx="540" cy="520" r="430" fill="none" stroke="#2FE08A" stroke-opacity=".25" stroke-width="2"/>'
    b += '<ellipse cx="540" cy="520" rx="200" ry="430" fill="none" stroke="#2FE08A" stroke-opacity=".15" stroke-width="2"/>'
    b += '<line x1="110" y1="520" x2="970" y2="520" stroke="#2FE08A" stroke-opacity=".15" stroke-width="2"/>'
    # passport
    b += ('<g transform="translate(400,560) rotate(-10)"><rect x="-150" y="-210" width="300" height="420" rx="18" fill="#1F2E5A"/>'
          '<circle cx="0" cy="-40" r="66" fill="none" stroke="#D9B54A" stroke-width="6"/><path d="M-66,-40 L66,-40 M0,-106 Q40,-40 0,26 Q-40,-40 0,-106" stroke="#D9B54A" stroke-width="4" fill="none"/>'
          '<text x="0" y="90" font-family="Manrope" font-weight="800" font-size="34" fill="#D9B54A" text-anchor="middle" letter-spacing="6">PASSPORT</text></g>')
    # tax form
    b += ('<g transform="translate(690,540) rotate(7)"><rect x="-170" y="-230" width="340" height="460" rx="8" fill="#F4F1E8"/>'
          '<text x="-140" y="-170" font-family="Manrope" font-weight="800" font-size="30" fill="#111">US INCOME TAX</text>'
          + "".join(f'<rect x="-140" y="{-140 + k*40}" width="{280 - (k%3)*60}" height="12" fill="#D6D1C2"/>' for k in range(6))
          + '<rect x="-140" y="120" width="280" height="80" rx="6" fill="none" stroke="#139A52" stroke-width="5"/>'
          '<text x="0" y="178" font-family="Manrope" font-weight="800" font-size="52" fill="#139A52" text-anchor="middle">$0</text></g>')
    return _svg(b, h)


def vlog_scene(h=1350):
    """Creator filming Zhangjiajie with a phone on a gimbal (back view)."""
    base = zhangjiajie(h)
    over = ('<g transform="translate(700,1350)">'
            '<path d="M-150,0 L-130,-420 Q-120,-470 -60,-480 L60,-480 Q120,-470 130,-420 L150,0 Z" fill="#101614"/>'
            '<circle cx="0" cy="-540" r="70" fill="#101614"/>'
            '<path d="M100,-400 L190,-560" stroke="#101614" stroke-width="40" stroke-linecap="round"/>'
            '<rect x="150" y="-700" width="20" height="160" fill="#1A1F1D"/>'
            '<g transform="translate(160,-800) rotate(-6)"><rect x="-110" y="-200" width="220" height="380" rx="26" fill="#0B0F0E"/>'
            '<rect x="-98" y="-186" width="196" height="352" rx="18" fill="#7E9A90"/>'
            '<circle cx="-62" cy="-156" r="11" fill="#E5322D"/><text x="-42" y="-146" font-family="Manrope" font-weight="800" font-size="26" fill="#fff">REC</text></g></g>')
    return base.replace('<rect width="1080" height="1350" filter="url(#grain)"/></svg>', over + '<rect width="1080" height="1350" filter="url(#grain)"/></svg>')


SCENES = dict(zhangjiajie=zhangjiajie, guizhou=guizhou, xinjiang=xinjiang, chengdu=chengdu, hainan=hainan,
              hainan_lounge=lambda h=1350: hainan(h, True, True), skyline=skyline_dusk, office=office_night,
              laptop=laptop_night, plane=plane_window, classroom=classroom, graduation=graduation, arena=arena,
              campus=campus, passport=passport_scene, vlog=vlog_scene)
