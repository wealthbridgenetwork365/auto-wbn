"""Hand-drawn doodle library (stick figures + objects) as SVG snippets.

Every function returns an SVG <g> string. Objects are anchored at their
bottom-centre (x, y) on the ground line unless noted. Strokes are thick,
round-capped black lines; a turbulence filter in the renderer adds wobble.
"""
INK = "#111111"
RED = "#E5322D"
GREEN = "#139A52"


def _g(x, y, s, body, flip=False):
    sx = -s if flip else s
    return f'<g transform="translate({x:.1f},{y:.1f}) scale({sx},{s})">{body}</g>'


def _p(d, w=10, fill="none", color=INK):
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def _c(cx, cy, r, w=10, fill="#fff", color=INK):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="{w}"/>'


def _dot(cx, cy, r=6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{INK}"/>'


def _t(x, y, txt, size=40, weight=700, color=INK, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="Poppins" font-weight="{weight}" font-size="{size}" '
            f'fill="{color}" text-anchor="{anchor}" filter="none">{txt}</text>')


# ---------------------------------------------------------------- figure
ARMS = {
    "down":  ["M0,-228 L-50,-150", "M0,-228 L50,-150"],
    "hips":  ["M0,-228 L-58,-188 L-14,-150", "M0,-228 L58,-188 L14,-150"],
    "wave":  ["M0,-228 L-50,-150", "M0,-228 L58,-268 L78,-335"],
    "point": ["M0,-228 L-58,-188 L-14,-150", "M0,-228 L118,-246"],
    "shrug": ["M0,-228 L-62,-205 L-90,-262", "M0,-228 L62,-205 L90,-262"],
    "think": ["M0,-228 L-58,-188 L-14,-150", "M0,-228 L48,-186 L22,-258"],
    "phone": ["M0,-228 L-50,-150", "M0,-228 L52,-196 L44,-292"],
    "hold":  ["M0,-228 L44,-178 L92,-196", "M0,-228 L30,-170 L92,-176"],
    "up":    ["M0,-228 L-56,-290 L-70,-350", "M0,-228 L56,-290 L70,-350"],
}


def face(kind):
    eyes = _dot(-16, -310) + _dot(16, -310)
    if kind == "happy":
        return eyes + _p("M-22,-290 Q0,-266 22,-290", 8)
    if kind == "grin":
        return eyes + _p("M-24,-292 Q0,-262 24,-292 Z", 7, fill="#fff")
    if kind == "sad":
        return eyes + _p("M-20,-276 Q0,-292 20,-276", 8)
    if kind == "flat":
        return eyes + _p("M-16,-282 L16,-282", 8)
    if kind == "wow":
        return eyes + _c(0, -280, 10, 7)
    if kind == "angry":
        return (eyes + _p("M-30,-326 L-6,-318", 7) + _p("M30,-326 L6,-318", 7)
                + _p("M-20,-276 Q0,-292 20,-276", 8))
    if kind == "wink":
        return _dot(-16, -310) + _p("M6,-310 Q16,-320 26,-310", 6) + _p("M-22,-290 Q0,-266 22,-290", 8)
    return eyes


def figure(x, y, s=1.0, pose="down", mood="happy", tie=False, flip=False, confused=False, sweat=False):
    a1, a2 = ARMS[pose]
    b = (_p("M0,-254 L0,-130") + _p("M0,-130 L-42,0 L-64,0") + _p("M0,-130 L42,0 L64,0")
         + _p(a1) + _p(a2) + _c(0, -300, 46) + face(mood))
    if tie:
        b += _p("M0,-250 L-9,-238 L0,-196 L9,-238 Z", 6, fill="#fff")
    if confused:
        b += _p("M38,-360 q30,-6 26,-26 q-4,-20 -30,-12 q-26,8 -10,26 M44,-382 q36,-8 30,-34 q-6,-22 -38,-12", 6)
    if sweat:
        b += _p("M52,-330 q8,14 0,20 q-8,-6 0,-20", 5, fill="#fff")
    if pose == "phone":
        b += _p("M30,-330 L58,-330 L58,-280 L30,-280 Z", 7, fill="#fff")
    return _g(x, y, s, b, flip)


# ---------------------------------------------------------------- objects
def ground(x1, x2, y):
    return _p(f"M{x1},{y} L{x2},{y}", 10)


def tower(x, y, s=1.0, cols=3, rows=4):
    w = cols * 70 + 40
    h = rows * 74 + 150
    b = _p(f"M{-w/2},0 L{-w/2},{-h} L{w/2},{-h-30} L{w/2},0", 11, fill="#fff")
    b += _p(f"M{w/2},{-h-30} L{w/2+40},{-h-12} L{w/2+40},0", 10, fill="#fff")
    for r in range(rows):
        for c in range(cols):
            wx = -w/2 + 24 + c*70
            wy = -h + 30 + r*74 - (c*10)
            b += _p(f"M{wx},{wy} L{wx+46},{wy-4} L{wx+46},{wy+44} L{wx},{wy+46} Z", 8)
    b += _p("M-30,0 L-30,-80 L30,-80 L30,0 M0,-80 L0,0", 9)
    b += _p("M-46,-90 L46,-90", 9)
    b += _p(f"M{-w/2-70},0 q-4,-34 26,-30 q10,-28 38,-8 q20,-6 22,38", 8)
    b += _p(f"M{w/2+10},0 q-4,-34 26,-30 q10,-28 38,-8 q20,-6 22,38", 8)
    return _g(x, y, s, b)


def factory(x, y, s=1.0):
    b = _p("M-150,0 L-150,-140 L-90,-190 L-90,-140 L-30,-190 L-30,-140 L30,-190 L30,-140 L150,-140 L150,0 Z", 11, fill="#fff")
    b += _p("M90,-140 L90,-290 L125,-290 L125,-140", 10, fill="#fff")
    b += _p("M110,-310 q-24,-20 0,-38 q4,-26 34,-22 q22,-12 34,10 q26,6 12,30 q-10,20 -40,14", 8)
    for wx in (-120, -60, 0):
        b += _p(f"M{wx},-100 L{wx+36},-100 L{wx+36},-64 L{wx},-64 Z", 8)
    b += _p("M70,0 L70,-80 L120,-80 L120,0", 9)
    return _g(x, y, s, b)


def box(x, y, s=1.0, label="", q=False, fill="#fff"):
    b = _p("M-70,0 L-70,-120 L60,-120 L60,0 Z", 10, fill=fill)
    b += _p("M-70,-120 L-38,-150 L92,-150 L60,-120", 10, fill="#fff")
    b += _p("M60,0 L92,-30 L92,-150", 10)
    b += _p("M-5,-120 L27,-150", 8) + _p("M-5,-120 L-5,-78", 8)
    if label:
        b += _t(-5, -30, label, 40)
    if q:
        b += _t(-5, -24, "?", 70, 800)
    return _g(x, y, s, b)


def ship(x, y, s=1.0):
    b = _p("M-200,-60 L200,-60 L160,0 L-170,0 Z", 11, fill="#fff")
    for i, (cx, h) in enumerate([(-150, 1), (-90, 2), (-30, 2), (30, 1), (90, 2)]):
        for k in range(h):
            b += _p(f"M{cx},{-60-k*46} L{cx+56},{-60-k*46} L{cx+56},{-106-k*46} L{cx},{-106-k*46} Z", 8, fill="#fff")
    b += _p("M150,-60 L150,-150 L190,-150 L190,-60", 9, fill="#fff")
    b += _p("M-230,22 q20,-16 40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0", 7)
    return _g(x, y, s, b)


def coins(x, y, s=1.0, n=4):
    b = ""
    for i in range(n):
        cy = -i * 26
        b += _p(f"M-60,{cy-14} L-60,{cy} A60,18 0 0 0 60,{cy} L60,{cy-14}", 9, fill="#fff")
        b += f'<ellipse cx="0" cy="{cy-14}" rx="60" ry="18" fill="#fff" stroke="{INK}" stroke-width="9"/>'
    b += _t(0, -n*26 + 2, "$", 30, 800)
    return _g(x, y, s, b)


def moneybag(x, y, s=1.0):
    b = _p("M-30,-150 Q-100,-90 -80,-30 Q-70,0 0,0 Q70,0 80,-30 Q100,-90 30,-150 Z", 10, fill="#fff")
    b += _p("M-30,-150 L-44,-180 L44,-180 L30,-150", 9, fill="#fff")
    b += _t(0, -40, "$", 80, 800, GREEN)
    return _g(x, y, s, b)


def magnifier(x, y, s=1.0):
    b = _c(0, -150, 60, 11) + _p("M42,-108 L110,-30", 16)
    b += _p("M-30,-170 Q-20,-190 0,-196", 7)
    return _g(x, y, s, b)


def laptop(x, y, s=1.0, label=""):
    b = _p("M-120,-40 L-120,-200 L120,-200 L120,-40 Z", 10, fill="#fff")
    b += _p("M-150,0 L150,0 L120,-40 L-120,-40 Z", 10, fill="#fff")
    if label:
        b += _t(0, -106, label, 34)
    return _g(x, y, s, b)


def stall(x, y, s=1.0):
    b = _p("M-140,0 L-140,-190 M140,0 L140,-190", 10)
    b += _p("M-170,-190 L170,-190 L150,-250 L-150,-250 Z", 10, fill="#fff")
    b += _p("M-170,-190 q28,30 57,0 q28,30 57,0 q28,30 57,0 q28,30 57,0 q28,30 57,0 q28,30 57,0", 9, fill="#fff")
    b += _p("M-140,-80 L140,-80", 10)
    b += box(-80, -80, 0.4) + box(-10, -80, 0.4) + box(60, -80, 0.4)
    return _g(x, y, s, b)


def phone(x, y, s=1.0, label=""):
    b = _p("M-60,0 L-60,-220 Q-60,-240 -40,-240 L40,-240 Q60,-240 60,-220 L60,-20 Q60,0 40,0 Z", 10, fill="#fff")
    b += _p("M-15,-20 L15,-20", 8)
    if label:
        b += _t(0, -110, label, 30)
    return _g(x, y, s, b)


def camera(x, y, s=1.0):
    b = _p("M-90,0 L-90,-110 L-40,-110 L-25,-135 L25,-135 L40,-110 L90,-110 L90,0 Z", 10, fill="#fff")
    b += _c(0, -56, 36, 10) + _dot(0, -56, 10) + _p("M60,-90 L72,-90", 8)
    return _g(x, y, s, b)


def ball(x, y, s=1.0):
    b = _c(0, -70, 70, 10)
    b += _p("M-70,-70 L70,-70 M0,-140 L0,0", 7)
    b += _p("M-48,-122 Q-18,-70 -48,-18 M48,-122 Q18,-70 48,-18", 7)
    return _g(x, y, s, b)


def glasses(x, y, s=1.0):
    b = _c(-70, -50, 50, 11) + _c(70, -50, 50, 11) + _p("M-22,-60 Q0,-80 22,-60", 9)
    b += _p("M-120,-58 L-170,-80 M120,-58 L170,-80", 9)
    return _g(x, y, s, b)


def kite(x, y, s=1.0):
    b = _p("M0,-300 L70,-200 L0,-90 L-70,-200 Z", 10, fill="#fff")
    b += _p("M0,-300 L0,-90 M-70,-200 L70,-200", 7)
    b += _p("M0,-90 q30,30 0,60 q-30,30 0,60", 7)
    b += _p("M-12,-40 L12,-20 M12,-40 L-12,-20", 7)
    return _g(x, y, s, b)


def dumbbell(x, y, s=1.0):
    b = _p("M-70,-50 L70,-50", 12)
    for sx in (-1, 1):
        b += _p(f"M{sx*70},-100 L{sx*70},0 L{sx*100},0 L{sx*100},-100 Z", 10, fill="#fff")
        b += _p(f"M{sx*100},-80 L{sx*118},-80 L{sx*118},-20 L{sx*100},-20", 9)
    return _g(x, y, s, b)


def sofa(x, y, s=1.0):
    b = _p("M-130,-40 L-130,-150 Q-130,-170 -110,-170 L110,-170 Q130,-170 130,-150 L130,-40", 10, fill="#fff")
    b += _p("M-170,-20 L-170,-110 L-130,-110 L-130,-40 L130,-40 L130,-110 L170,-110 L170,-20 Z", 10, fill="#fff")
    b += _p("M0,-160 L0,-50", 7)
    b += _p("M-150,-20 L-150,0 M150,-20 L150,0", 10)
    return _g(x, y, s, b)


def brush(x, y, s=1.0):
    b = _p("M-14,0 L-14,-150 L14,-150 L14,0 Z", 10, fill="#fff")
    b += _p("M-16,-150 L-22,-190 L22,-190 L16,-150", 9, fill="#fff")
    b += _p("M-22,-190 Q-30,-250 0,-280 Q30,-250 22,-190", 10, fill="#fff")
    return _g(x, y, s, b)


def tag(x, y, s=1.0, label="$"):
    b = _p("M-60,-10 L60,-10 L60,-130 L0,-170 L-60,-130 Z", 10, fill="#fff")
    b += _c(0, -128, 10, 7) + _t(0, -45, label, 44, 800)
    return _g(x, y, s, b)


def clock(x, y, s=1.0):
    b = _c(0, -80, 80, 11) + _p("M0,-80 L0,-130 M0,-80 L36,-60", 10)
    return _g(x, y, s, b)


def pin(x, y, s=1.0, fill="#fff"):
    b = _p("M0,0 Q-60,-80 -60,-130 A60,60 0 0 1 60,-130 Q60,-80 0,0 Z", 10, fill=fill)
    b += _c(0, -132, 20, 9)
    return _g(x, y, s, b)


def noodles(x, y, s=1.0):
    b = _p("M-120,-90 L120,-90 Q110,0 0,0 Q-110,0 -120,-90 Z", 10, fill="#fff")
    b += _p("M-90,-90 q20,-30 40,0 q20,-30 40,0 q20,-30 40,0 q20,-30 40,0", 8)
    b += _p("M40,-100 L150,-240 M70,-96 L170,-228", 9)
    b += _p("M-60,-130 q-14,-22 0,-44 q14,-22 0,-44 M-20,-136 q-14,-22 0,-44 q14,-22 0,-44", 7)
    return _g(x, y, s, b)


def panda(x, y, s=1.0):
    b = _c(-62, -200, 30, 0, fill=INK) + _c(62, -200, 30, 0, fill=INK)
    b += _c(0, -140, 90, 11)
    b += f'<ellipse cx="-34" cy="-150" rx="22" ry="28" fill="{INK}" transform="rotate(25,-34,-150)"/>'
    b += f'<ellipse cx="34" cy="-150" rx="22" ry="28" fill="{INK}" transform="rotate(-25,34,-150)"/>'
    b += _c(-30, -152, 6, 0) + _c(34, -152, 6, 0)
    b += f'<ellipse cx="0" cy="-112" rx="14" ry="9" fill="{INK}"/>' + _p("M-16,-90 Q0,-78 16,-90", 7)
    return _g(x, y, s, b)


def skyline(x, y, s=1.0):
    b = _p("M-230,0 L-230,-180 L-170,-180 L-170,0", 10, fill="#fff")
    b += _p("M-160,0 L-160,-260 L-90,-290 L-90,0", 10, fill="#fff")
    # TV tower with spheres
    b += _p("M-30,0 L0,-120 L30,0", 10) + _c(0, -150, 34, 10) + _p("M0,-184 L0,-290", 10) + _c(0, -300, 18, 9) + _p("M0,-318 L0,-380", 8)
    b += _p("M70,0 L70,-330 L120,-380 L150,-380 L150,0", 10, fill="#fff")
    b += _p("M110,-300 L118,-300 M110,-240 L118,-240", 8)
    b += _p("M170,0 L170,-210 L230,-210 L230,0", 10, fill="#fff")
    return _g(x, y, s, b)


def chip(x, y, s=1.0):
    b = _p("M-80,-30 L80,-30 L80,-190 L-80,-190 Z", 11, fill="#fff")
    b += _p("M-40,-70 L40,-70 L40,-150 L-40,-150 Z", 8)
    for i in (-50, 0, 50):
        b += _p(f"M{i},-190 L{i},-225 M{i},-30 L{i},5 M-80,{-110+i*0.8} L-115,{-110+i*0.8} M80,{-110+i*0.8} L115,{-110+i*0.8}", 8)
    return _g(x, y, s, b)


def board(x, y, s=1.0, txt="ABC"):
    b = _p("M-150,-120 L150,-120 L150,-320 L-150,-320 Z", 10, fill="#fff")
    b += _p("M-110,-120 L-130,0 M110,-120 L130,0", 10)
    b += _t(0, -195, txt, 64, 800)
    return _g(x, y, s, b)


def door(x, y, s=1.0, open_=False, lock=False):
    b = _p("M-80,0 L-80,-300 L80,-300 L80,0", 11, fill="#fff")
    if open_:
        b += _p("M-80,0 L-80,-300 L-20,-270 L-20,20 Z", 10, fill="#fff")
        b += f'<path d="M-76,-296 L76,-296 L76,0 L-16,0 L-16,-268 Z" fill="{GREEN}" opacity=".18" stroke="none"/>'
    else:
        b += _c(55, -150, 8, 7, fill=INK)
    if lock:
        b += _p("M-30,-150 L30,-150 L30,-100 L-30,-100 Z", 8, fill="#fff") + _p("M-18,-150 L-18,-170 Q0,-195 18,-170 L18,-150", 8)
    return _g(x, y, s, b)


def signpost(x, y, s=1.0, labels=("", "")):
    b = _p("M0,0 L0,-320", 12)
    b += _p("M0,-300 L150,-300 L180,-275 L150,-250 L0,-250", 10, fill="#fff")
    b += _p("M0,-220 L-150,-220 L-180,-195 L-150,-170 L0,-170", 10, fill="#fff")
    b += _t(80, -263, labels[0], 26) + _t(-82, -183, labels[1], 26)
    return _g(x, y, s, b)


def bridge(x, y, s=1.0, w=520):
    h = w / 2
    b = _p(f"M{-h},0 L{-h},-60 L{h},-60 L{h},0", 10)
    b += _p(f"M{-h+30},-60 Q0,-260 {h-30},-60", 10)
    for i in range(1, 8):
        bx = -h + 30 + i * (w - 60) / 8
        t = (bx + h - 30) / (w - 60)
        top = -60 - 4 * 100 * t * (1 - t)
        b += _p(f"M{bx:.0f},-60 L{bx:.0f},{top:.0f}", 7)
    b += _p(f"M{-h-40},0 q20,-14 40,0 t40,0 t40,0" + " t40,0" * int(w / 40), 7)
    return _g(x, y, s, b)


def bubble(x, y, s=1.0, txt="", w=260, tail="left", color=INK):
    h = 110
    tl = f"L{-w/2+50},{-h/2+40} L{-w/2+20},{-h/2+90} L{-w/2+90},{-h/2+40}" if tail == "left" else f"L{w/2-90},{-h/2+40} L{w/2-20},{-h/2+90} L{w/2-50},{-h/2+40}"
    d = f"M{-w/2},{-h/2-30} Q{-w/2},{-h/2-70} {-w/2+40},{-h/2-70} L{w/2-40},{-h/2-70} Q{w/2},{-h/2-70} {w/2},{-h/2-30} L{w/2},{-h/2} Q{w/2},{-h/2+40} {w/2-40},{-h/2+40} "
    d = (f"M{-w/2+40},{-h} L{w/2-40},{-h} Q{w/2},{-h} {w/2},{-h+40} L{w/2},{-40} Q{w/2},0 {w/2-40},0 "
         + (f"L{w/2-50},0 L{w/2-20},50 L{w/2-90},0 " if tail == "right" else "")
         + (f"L{-w/2+90},0 L{-w/2+20},50 L{-w/2+50},0 " if tail == "left" else "")
         + f"L{-w/2+40},0 Q{-w/2},0 {-w/2},-40 L{-w/2},{-h+40} Q{-w/2},{-h} {-w/2+40},{-h} Z")
    b = _p(d, 9, fill="#fff") + _t(0, -h/2 + 14, txt, 38, 700, color)
    return _g(x, y, s, b)


def arrow(x1, y1, x2, y2, curve=-60, color=INK, w=10):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + curve
    import math
    ang = math.atan2(y2 - my, x2 - mx)
    a1 = (x2 - 34 * math.cos(ang - 0.5), y2 - 34 * math.sin(ang - 0.5))
    a2 = (x2 - 34 * math.cos(ang + 0.5), y2 - 34 * math.sin(ang + 0.5))
    return (_p(f"M{x1},{y1} Q{mx},{my} {x2},{y2}", w, color=color)
            + _p(f"M{a1[0]:.0f},{a1[1]:.0f} L{x2},{y2} L{a2[0]:.0f},{a2[1]:.0f}", w, color=color))


def squiggle(x1, x2, y, color=RED):
    d = f"M{x1},{y}"
    x = x1
    while x < x2:
        d += f" q10,-14 20,0 t20,0"
        x += 40
    return _p(f"M{x1-120},{y} L{x1},{y} M{x1-120},{y-22} L{x1-120},{y+22} M{x1},{y-22} L{x1},{y+22}", 10) + _p(d, 12, color=color)


def check(x, y, s=1.0, ok=True):
    if ok:
        return _g(x, y, s, _p("M-40,0 L-10,30 L50,-40", 14, color=GREEN))
    return _g(x, y, s, _p("M-35,-35 L35,35 M35,-35 L-35,35", 14, color=RED))


def trophy(x, y, s=1.0):
    b = _p("M-70,-260 L70,-260 L60,-160 Q50,-110 0,-110 Q-50,-110 -60,-160 Z", 10, fill="#fff")
    b += _p("M-68,-240 Q-120,-240 -100,-190 Q-90,-170 -60,-170 M68,-240 Q120,-240 100,-190 Q90,-170 60,-170", 9)
    b += _p("M0,-110 L0,-50 M-50,0 L-50,-50 L50,-50 L50,0 Z", 10, fill="#fff")
    return _g(x, y, s, b)


def crowd(x, y, s=1.0, n=5, mood="flat"):
    b = ""
    for i in range(n):
        cx = (i - (n - 1) / 2) * 70
        b += _p(f"M{cx-34},0 Q{cx-34},-60 {cx},-60 Q{cx+34},-60 {cx+34},0", 9, fill="#fff")
        b += _c(cx, -88, 26, 9)
    return _g(x, y, s, b)


def plane(x, y, s=1.0):
    b = _p("M-160,-20 L120,-20 Q170,-20 170,-40 Q170,-60 120,-60 L-120,-60 L-160,-110 L-180,-110 L-160,-40 Z", 10, fill="#fff")
    b += _p("M-20,-40 L-80,40 L-50,40 L40,-40", 10, fill="#fff")
    b += _p("M-20,-60 L-60,-120 L-36,-120 L30,-60", 10, fill="#fff")
    return _g(x, y, s, b)


def handshake_hands(x, y, s=1.0):
    b = _p("M-180,-60 L-80,-60 L-20,-100 L40,-60 L-20,-20 L-80,-40", 10, fill="#fff")
    b += _p("M180,-60 L80,-60 L30,-20 L0,-40 M80,-60 L20,-110", 10)
    return _g(x, y, s, b)
