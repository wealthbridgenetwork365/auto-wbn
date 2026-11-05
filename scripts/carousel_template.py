import math, os
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/claude/carousel_2026-11-09"
os.makedirs(OUT, exist_ok=True)
DATE = "2026-11-09"

N, W, H = 6, 1080, 1350
TW = N * W
NAVY = (8, 8, 8)
NAVY2 = (24, 24, 24)
GOLD = (34, 197, 94)
RED = (21, 128, 61)
CREAM = (255, 255, 255)
MUTED = (165, 165, 165)

GF = "/usr/share/fonts/truetype/google-fonts/"
IF = "/usr/share/fonts/opentype/inter/"
def poppins(sz, w="Bold"): return ImageFont.truetype(GF + f"Poppins-{w}.ttf", sz)
def inter(sz, w="Regular"): return ImageFont.truetype(IF + f"Inter-{w}.otf", sz)

img = Image.new("RGB", (TW, H), NAVY)
d = ImageDraw.Draw(img)

# background: subtle vertical gradient
for y in range(H):
    t = y / H
    c = tuple(int(NAVY[i] * (1 - t) + NAVY2[i] * t) for i in range(3))
    d.line([(0, y), (TW, y)], fill=c)

# ---------- continuous bridge across all slides ----------
DECK = 1185
TOWER_TOP = 1075
towers = [540 + k * W for k in range(N)]
# water
for i, y in enumerate(range(DECK + 40, H, 18)):
    d.line([(0, y), (TW, y)], fill=(30, 30, 30) if i % 2 else (22, 22, 22), width=2)
# cables (catenary between towers), plus side spans to edges
spans = [(0, towers[0])] + [(towers[i], towers[i + 1]) for i in range(N - 1)] + [(towers[-1], TW)]
for a, b in spans:
    pts = []
    for s in range(0, 101):
        x = a + (b - a) * s / 100
        u = (s / 100) * 2 - 1
        if a == 0:            # rising from deck to first tower
            y = DECK - 20 - (DECK - 20 - TOWER_TOP) * (s / 100) ** 2
        elif b == TW:         # falling to the edge
            y = DECK - 20 - (DECK - 20 - TOWER_TOP) * (1 - s / 100) ** 2
        else:
            y = TOWER_TOP + (DECK - 30 - TOWER_TOP) * (1 - u * u)
        pts.append((x, y))
    d.line(pts, fill=GOLD, width=5)
    for x, y in pts[::5]:
        d.line([(x, y), (x, DECK)], fill=(22, 140, 70), width=2)
for x in towers:
    d.rectangle([x - 14, TOWER_TOP - 10, x + 14, DECK + 30], fill=CREAM)
    d.rectangle([x - 22, TOWER_TOP - 22, x + 22, TOWER_TOP - 6], fill=GOLD)
d.rectangle([0, DECK, TW, DECK + 16], fill=CREAM)
d.rectangle([0, DECK + 16, TW, DECK + 22], fill=RED)

# ---------- helpers ----------
M = 100
def X(slide, x): return slide * W + x
def text(slide, x, y, s, font, fill=CREAM, anchor="la"):
    d.text((X(slide, x), y), s, font=font, fill=fill, anchor=anchor)
def lines(slide, x, y, arr, font, fill=CREAM, gap=1.12):
    for s in arr:
        text(slide, x, y, s, font, fill)
        y += int(font.size * gap)
    return y
def label(slide, s):
    text(slide, M, 120, s, inter(30, "SemiBold"), GOLD)
    d.rectangle([X(slide, M), 168, X(slide, M + 60), 174], fill=RED)
def source(slide, s):
    text(slide, M, 950, s, inter(26), MUTED)
def rbox(slide, x0, y0, x1, y1, fill, outline=None, r=22, w=3):
    d.rounded_rectangle([X(slide, x0), y0, X(slide, x1), y1], radius=r, fill=fill, outline=outline, width=w)

# ---------- Slide 1: hook ----------
label(0, "CHINA OPPORTUNITIES")
lines(0, M, 300, ["The biggest", "creator market", "you're not on."], poppins(112))
text(0, M, 760, "Swipe to cross the bridge  →", inter(40, "Medium"), GOLD)

# ---------- Slide 2: the scale ----------
label(1, "THE GAP")
text(1, M, 260, "1.125", poppins(230), GOLD)
text(1, M, 520, "billion", poppins(90), GOLD)
lines(1, M, 660, ["people online in China"], poppins(60))
# dot diagram: 100 dots, each = ~11M people
for r in range(4):
    for c in range(25):
        cx, cy = M + 12 + c * 35, 790 + r * 35
        d.ellipse([X(1, cx - 11), cy - 11, X(1, cx + 11), cy + 11], fill=GOLD)
text(1, M, 935, "Each dot ≈ 11 million people", inter(28, "Medium"), CREAM)
source(1, "").__class__
text(1, M, 985, "Source: CNNIC 57th report, as of Dec 2025", inter(26), MUTED)

# ---------- Slide 3: the barriers ----------
label(2, "THE TENSION")
lines(2, M, 230, ["So why aren't", "more creators there?"], poppins(78))
bricks = [("Different apps", 0), ("Language", 1), ("Payments", 0), ("Brand contracts", 1)]
by = 470
for i, (s, off) in enumerate(bricks):
    x0 = M + (60 if off else 0)
    rbox(2, x0, by, x0 + 760, by + 105, RED, r=14)
    text(2, x0 + 40, by + 52, s, poppins(46), CREAM, "lm")
    by += 125
text(2, M, 960, "A wall, not a lack of opportunity.", inter(34, "Medium"), MUTED)

# ---------- Slide 4: the attention ----------
label(3, "THE PROOF")
lines(3, M, 230, ["714 million", "open Douyin daily"], poppins(80))
text(3, M, 450, "Avg. minutes per user per day (July 2026)", inter(32, "Medium"), MUTED)
scale = 6.2  # px per minute
def rangebar(y, name, lo, hi, col):
    text(3, M, y, name, poppins(42), CREAM)
    yb = y + 70
    d.rounded_rectangle([X(3, M), yb, X(3, M + int(hi * scale)), yb + 70], radius=12, fill=(48, 48, 48))
    d.rounded_rectangle([X(3, M), yb, X(3, M + int(lo * scale)), yb + 70], radius=12, fill=col)
    text(3, M + int(hi * scale) + 20, yb + 35, f"{lo}–{hi}", poppins(40), col, "lm")
rangebar(530, "Douyin", 112, 120, GOLD)
rangebar(720, "WeChat", 82, 85, MUTED)
source(3, "Source: Nomura via TechNode, Sep 2026")

# ---------- Slide 5: the bridge (process) ----------
label(4, "THE BRIDGE")
lines(4, M, 220, ["We connect you", "to Chinese brands"], poppins(72))
steps = ["You: creator or athlete", "Us: your China team", "Brand match", "Campaign", "You get paid"]
sy = 420
for i, s in enumerate(steps):
    fill = GOLD if i in (1,) else NAVY2
    col = NAVY if i == 1 else CREAM
    rbox(4, M, sy, W - M, sy + 80, fill, outline=GOLD, r=18)
    text(4, M + 36, sy + 40, s, poppins(40, "Medium" if i != 1 else "Bold"), col, "lm")
    if i < len(steps) - 1:
        cx = W // 2
        d.polygon([(X(4, cx - 16), sy + 86), (X(4, cx + 16), sy + 86), (X(4, cx), sy + 104)], fill=GOLD)
    sy += 112

# ---------- Slide 6: close ----------
label(5, "THE CROSSING")
lines(5, M, 240, ["Creators &", "athletes:"], poppins(96))
lines(5, M, 480, ["we're signing for", "China brand deals."], poppins(62), GOLD)
rbox(5, M, 690, M + 420, 790, RED, r=50)
text(5, M + 210, 740, "DM us", poppins(50), CREAM, "mm")
text(5, M, 900, "Building Bridges | Creating Access", inter(36, "SemiBold"), CREAM)

# ---------- export ----------
img.save(os.path.join(OUT, f"{DATE}_panorama.jpg"), quality=92)
for k in range(N):
    sl = img.crop((k * W, 0, (k + 1) * W, H))
    sl.save(os.path.join(OUT, f"{DATE}_slide-{k+1:02d}.jpg"), quality=92)
prev = img.resize((TW // 3, H // 3))
pd = ImageDraw.Draw(prev)
for k in range(1, N):
    pd.line([(k * W // 3, 0), (k * W // 3, H // 3)], fill=(255, 0, 0), width=1)
prev.save("/tmp/claude-0/-home-claude/f4a4e75d-f846-5403-ac53-b6cc7dc8872e/scratchpad/preview_seams.png")
print("done")
