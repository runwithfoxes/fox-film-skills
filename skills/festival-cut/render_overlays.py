"""Capture every overlay page in this folder as a transparent PNG of the same name.

    python render_overlays.py [page.html ...]       (default: every .html file here)

Needs Playwright for Python: pip install playwright, then playwright install chromium.
The pages set their own size on html and body; the capture uses that size and keeps the transparency.
"""
import sys, os, glob
from playwright.sync_api import sync_playwright

here = os.path.dirname(os.path.abspath(__file__))
pages = sys.argv[1:] or sorted(glob.glob(os.path.join(here, "*.html")))
with sync_playwright() as p:
    b = p.chromium.launch()
    for page_path in pages:
        page = b.new_page()
        page.goto("file://" + os.path.abspath(page_path))
        w, h = page.evaluate("(() => { const s = getComputedStyle(document.body); return [parseInt(s.width), parseInt(s.height)]; })()")
        page.set_viewport_size({"width": w, "height": h})
        out = os.path.splitext(os.path.abspath(page_path))[0] + ".png"
        page.screenshot(path=out, omit_background=True)
        print(out, w, "x", h)
    b.close()
