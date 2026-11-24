"""Doodle storytelling renderer for Instagram Stories / Highlights (1080 x 1920).

Same look as render_doodle.py, with a taller page and safe zones for the story UI.
Usage: python3 scripts/render_story.py content/highlights.py stories/ [id ...]
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_doodle as rd

rd.H = 1920
rd.CSS = (rd.CSS.replace(f"height:1350px", "height:1920px")
          .replace("padding:88px 96px 0", "padding:240px 90px 170px")
          + ".hook{line-height:.96}.kick{font-size:var(--ks,52px);font-weight:700}"
          + ".head{font-size:var(--hd,76px);font-weight:800;text-transform:uppercase}"
          + ".it{font-weight:700}")

_slide_html = rd.slide_html


def slide_html(sl):
    out = _slide_html(sl)
    extra = "".join(f"--{k}:{sl[k]}px;" for k in ("ks", "hd", "ah") if sl.get(k))
    if sl.get("check"):
        import re
        box = ('<span class="n" style="min-width:76px"><svg viewBox="0 0 64 64" width="58" height="58" style="margin-top:4px">'
               '<rect x="4" y="4" width="56" height="56" rx="14" fill="#2FE08A" stroke="#111" stroke-width="6"/>'
               '<path d="M17,33 L28,44 L48,20" fill="none" stroke="#111" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
               '</svg></span>')
        out = re.sub(r'<span class="n">\d+\.</span>', box, out)
    return out.replace('<div class="s" style="', f'<div class="s" style="{extra}', 1)


rd.slide_html = slide_html

if __name__ == "__main__":
    rd.main()
