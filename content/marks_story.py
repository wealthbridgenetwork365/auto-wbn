# Mark's story (post 54), doodle storytelling style with split-screen "then vs now" scenes.
# Mark is an illustrative character (a stick figure), labelled as an illustrative story.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from doodle import *  # noqa
from doodle import _p, _t, _c, _g, INK, RED, GREEN

SIGN = "Building Bridges | Creating Access"
TAGS = "#china #explore #chinatravel #Guangzhou"
NOTE = "Fictional example based on typical teaching contracts (ESL Base, Oct 2026). Pay and benefits vary by employer"


# ---------------------------------------------------------------- extra doodles
def cap(x, y, s=1.0):
    b = _p("M-110,-60 L0,-100 L110,-60 L0,-20 Z", 10, fill=INK)
    b += _p("M-60,-40 L-60,0 Q0,24 60,0 L60,-40", 10, fill="#fff")
    b += _p("M0,-60 L90,-40 L90,10", 7) + _c(90, 18, 10, 6, fill=GREEN)
    return _g(x, y, s, b)


def bills(x, y, s=1.0, label="DEBT"):
    b = ""
    for i in range(4):
        b += _p(f"M{-90+i*6},{-i*22} L{90+i*6},{-i*22} L{90+i*6},{-110-i*22} L{-90+i*6},{-110-i*22} Z", 9, fill="#fff")
    b += _t(18, -112, label, 40, 800, RED)
    b += _p("M-50,-90 L80,-90 M-50,-70 L40,-70", 6, color="#BBBBBB")
    return _g(x, y, s, b)


def palm(x, y, s=1.0):
    b = _p("M0,0 Q-10,-160 30,-300", 14)
    for d in ("M30,-300 q-80,-40 -150,10", "M30,-300 q-60,-80 -130,-80", "M30,-300 q30,-90 110,-90",
              "M30,-300 q90,-20 140,40", "M30,-300 q10,-60 -10,-130"):
        b += _p(d, 12)
    b += _c(20, -290, 14, 8, fill=INK) + _c(44, -284, 14, 8, fill=INK)
    return _g(x, y, s, b)


def sun(x, y, s=1.0):
    b = _c(0, 0, 54, 10, fill="#FFE27A")
    for k in range(8):
        import math
        a = k * math.pi / 4
        b += _p(f"M{78*math.cos(a):.0f},{78*math.sin(a):.0f} L{108*math.cos(a):.0f},{108*math.sin(a):.0f}", 9)
    return _g(x, y, s, b)


def lounger(x, y, s=1.0, mood="grin"):
    """Stick figure lying back on a beach chair, sunglasses, drink."""
    b = _p("M-170,0 L-130,-70 L120,-70 L180,-170", 10)                 # chair
    b += _p("M-130,-70 L-150,0 M120,-70 L140,0", 9)
    b += _c(150, -200, 40) + _p("M126,-206 L174,-206", 12) + _p("M128,-186 Q150,-172 172,-186", 7)  # head + shades + smile
    b += _p("M130,-160 L20,-96") + _p("M20,-96 L-80,-110 L-150,-86")     # body + legs
    b += _p("M90,-136 L40,-170 L10,-150")                                  # arm behind head-ish
    b += _p("M70,-124 L120,-110 L150,-130")                                # arm with drink
    b += _p("M140,-160 L166,-160 L160,-126 L146,-126 Z", 6, fill="#fff") + _p("M158,-160 L170,-186", 5)
    return _g(x, y, s, b)


def umbrella(x, y, s=1.0):
    b = _p("M0,0 L0,-300", 10)
    b += _p("M-170,-280 Q0,-420 170,-280 Q130,-300 85,-280 Q42,-300 0,-280 Q-42,-300 -85,-280 Q-130,-300 -170,-280 Z", 10, fill="#FFB3A7")
    return _g(x, y, s, b)


def payslip(x, y, s=1.0, rows=(), total=("", "")):
    h = 120 + 64 * len(rows) + 80
    b = _p(f"M-200,0 L200,0 L200,{-h} L-200,{-h} Z", 10, fill="#fff")
    b += _t(-170, -h + 66, "PAYSLIP · JULY", 30, 800, GREEN, "start")
    yy = -h + 130
    for a, v in rows:
        b += _t(-170, yy, a, 28, 600, INK, "start") + _t(170, yy, v, 32, 800, GREEN, "end")
        b += _p(f"M-170,{yy+20} L170,{yy+20}", 4, color="#DDDDDD")
        yy += 64
    b += _p(f"M-170,{yy-14} L170,{yy-14}", 7)
    b += _t(-170, yy + 40, total[0], 30, 800, INK, "start") + _t(170, yy + 44, total[1], 48, 800, GREEN, "end")
    return _g(x, y, s, b)


def plus(x, y, s=1.0):
    return _g(x, y, s, _c(0, 0, 70, 10, fill="#2FE08A") + _p("M-34,0 L34,0 M0,-34 L0,34", 16))


def divider(x, y1, y2):
    return f'<path d="M{x},{y1} L{x},{y2}" stroke="{INK}" stroke-width="8" stroke-dasharray="4 22" stroke-linecap="round" fill="none"/>'


def lbl(x, y, txt, color=INK, size=40, weight=800):
    return _t(x, y, txt, size, weight, color)


def envelope_phone(x, y, s=1.0):
    """Phone showing a job-offer email."""
    w, h = 420, 640
    b = _p(f"M{-w/2},0 L{-w/2},{-h} Q{-w/2},{-h-30} {-w/2+30},{-h-30} L{w/2-30},{-h-30} Q{w/2},{-h-30} {w/2},{-h} L{w/2},-30 Q{w/2},0 {w/2-30},0 Z", 11, fill="#fff")
    b += _p(f"M-150,{-h+30} L150,{-h+30} L150,{-h+150} L-150,{-h+150} Z M-150,{-h+30} L0,{-h+100} L150,{-h+30}", 8, fill="#fff")
    lines = [("From: Agent, China", 26, 600, INK), ("English Teacher", 36, 800, INK), ("$3,500 / month", 40, 800, GREEN),
             ("Housing covered", 30, 700, INK), ("Flights paid", 30, 700, INK), ("Paid holidays", 30, 700, INK)]
    yy = -h + 210
    for t, sz, wt, col in lines:
        b += _t(0, yy, t, sz, wt, col)
        yy += sz + 26
    b += f'<rect x="-120" y="{yy-20}" width="240" height="62" rx="31" fill="{GREEN}" stroke="{INK}" stroke-width="7"/>'
    b += _t(0, yy + 22, "ACCEPT", 30, 800, "#fff")
    return _g(x, y, s, b)


def caption():
    return "Jobs in China 🇨🇳\n\nFollow @wealthbridgenetwork"


POSTS = [
dict(id="54-marks-story", pillar="Job offers", title="What if you taught in China? Mark's example", caption=caption(),
 slides=[
 # 1 · HOOK: split screen then / now
 dict(hook="Saving *$300*\na month?\nIt could be\n*$2,000+.*", hs=100, swipe=True, kick="Here's how that could happen.",
      scene=lbl(215, 40, "THEN", RED) + lbl(680, 40, "NOW", GREEN) + divider(450, 0, 470)
      + ground(40, 410, 470) + laptop(170, 470, 0.7) + figure(330, 470, 0.85, "down", "sad", tie=True, sweat=True) + tag(150, 280, 0.6, "$300")
      + ground(490, 880, 470) + palm(840, 470, 0.85) + lounger(640, 470, 0.85) + moneybag(560, 330, 0.6), vh=490),
 # 2 · BACKSTORY
 dict(text=["Picture Mark. He's not real, but *his story is common.*", "Grew up in the West. Got the degree.", "Got the *debt*, too."], fs=56,
      scene=ground(60, 840, 400) + figure(260, 400, 0.95, "up", "grin") + cap(262, 60, 0.55) + arrow(420, 220, 560, 260, -50) + bills(700, 400, 1.05), vh=420),
 # 3 · CORPORATE (split: work / home)
 dict(head="Then straight into corporate.", items=["*40+ hours* a week", "Out of shape", "Paycheck to paycheck", "*No free time*"], **{"is": 48},
      scene=lbl(215, 34, "9 TO 7", INK, 34) + lbl(680, 34, "AFTER WORK", INK, 34) + divider(450, 0, 360)
      + ground(40, 410, 360) + laptop(150, 360, 0.6) + clock(330, 200, 0.6) + figure(330, 360, 0.7, "phone", "sad", tie=True, sweat=True)
      + ground(490, 880, 360) + sofa(740, 360, 0.85) + figure(580, 360, 0.7, "down", "sad") + _t(760, 150, "z z z", 40, 800), vh=380),
 # 4 · THE MATH (diagram)
 dict(head="Where his paycheck goes:", text=["Rent, loans, car, bills… *$300* left. Every month."], fs=48,
      scene=f'<rect x="60" y="40" width="780" height="80" rx="18" fill="#fff" stroke="{INK}" stroke-width="9"/>' + _t(450, 96, "PAYCHECK", 40, 800)
      + "".join(f'<rect x="{60+i*200}" y="170" width="180" height="140" rx="14" fill="#fff" stroke="{INK}" stroke-width="9"/>'
                + _t(150 + i * 200, 252, w, 34, 800, RED) for i, w in enumerate(["RENT", "LOANS", "CAR", "BILLS"]))
      + arrow(450, 330, 450, 410, 0)
      + f'<rect x="330" y="420" width="240" height="90" rx="45" fill="#2FE08A" stroke="{INK}" stroke-width="9"/>' + _t(450, 480, "$300", 48, 800), vh=530),
 # 5 · THE EMAIL
 dict(text=["Say one night he searches for *something different.*", "An agent in China emails him a *teaching offer.*"], fs=50,
      scene=ground(60, 840, 700) + figure(170, 700, 0.95, "phone", "wow") + envelope_phone(560, 700, 1.0), vh=720),
 # 6 · THE FLIGHT
 dict(text=["What if he says *yes?*", "Packs two bags. Takes the flight. Starts the job."], fs=56,
      scene=ground(60, 840, 400) + pin(140, 400, 0.6) + lbl(140, 440, "HOME", INK, 30)
      + _p("M140,240 Q450,-40 760,240", 8) + plane(450, 130, 0.55) + pin(760, 400, 0.6, GREEN) + lbl(760, 440, "CHINA", GREEN, 30)
      + figure(330, 400, 0.65, "wave", "grin") + box(470, 400, 0.6, "") + box(570, 400, 0.5, ""), vh=460),
 # 7 · THEN vs NOW (split screen)
 dict(head="Same Mark. What could change:",
      scene=lbl(215, 40, "THEN", RED) + lbl(680, 40, "NOW", GREEN) + divider(450, 0, 760)
      + figure(215, 330, 0.8, "down", "sad", tie=True, sweat=True)
      + lbl(215, 420, "Office job", INK, 34, 600) + lbl(215, 490, "$300/mo", RED, 64) + lbl(215, 550, "saved", INK, 30, 600)
      + lbl(215, 640, "≈ $3,600 a year", INK, 32, 700)
      + board(600, 330, 0.55, "ABC") + figure(770, 330, 0.8, "point", "grin", flip=True)
      + lbl(680, 420, "Teaching in China", INK, 34, 600) + lbl(680, 490, "$2,000+/mo", GREEN, 64) + lbl(680, 550, "could be saved", INK, 30, 600)
      + lbl(680, 640, "$20K+ a year", GREEN, 36, 800) + lbl(680, 700, "$3,500/mo · housing covered", INK, 26, 600), vh=760,
      src=NOTE),
 # 8 · SUMMER + CLOSE
 dict(text=["Summer at his office job? *Still working.* He can't take time off, so he keeps *saving up his PTO.*",
            "Teaching in China, summer break is often *still paid.* That's the *bridge to freedom.*"], fs=44,
      scene=lbl(215, 34, "OFFICE · JULY", RED, 32) + lbl(680, 34, "CHINA · JULY", GREEN, 32) + divider(450, 0, 520)
      + f'<rect x="70" y="80" width="190" height="120" rx="16" fill="#fff" stroke="{INK}" stroke-width="8"/>'
      + _t(165, 128, "PTO", 34, 800, RED) + _t(165, 172, "saving it up", 24, 700)
      + sun(370, 120, 0.4) + ground(40, 410, 440) + laptop(140, 440, 0.6) + figure(320, 440, 0.75, "down", "sad", tie=True, sweat=True)
      + lbl(215, 500, "Can't take time off", RED, 30, 700)
      + sun(840, 120, 0.4) + ground(490, 880, 440) + umbrella(640, 440, 0.6) + lounger(660, 440, 0.62)
      + lbl(680, 500, "Summer break: paid", GREEN, 30, 700), vh=530,
      src="Not financial advice. Mark is a fictional example; paid holidays and bonuses depend on the contract"),
 # 9 · CTA
 dict(hook="Ready to cross\nthe *bridge?*", hs=104,
      kick="There are *tons of global opportunities* that could change your life. *Join our community today.* Link in bio.",
      scene=ground(60, 840, 560) + figure(230, 560, 1.15, "point", "grin") + follow_phone(600, 560, 1.15), vh=580,
      src="Not financial advice. Mark is a fictional example"),
]),
]
