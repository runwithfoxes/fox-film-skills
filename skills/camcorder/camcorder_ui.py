"""Draw the camcorder screen: an amber time and date stamp bottom left and a red REC dot top right, on a transparent PNG.

    python camcorder_ui.py "11:52 PM" "JUL. 3 2026" [--size 1280x720] [--font path/to/mono.ttf]

Writes camcorder_ui.png beside this file. On a Mac the default font is Courier.
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("time"); ap.add_argument("date")
ap.add_argument("--size", default="1280x720"); ap.add_argument("--font")
o = ap.parse_args()
W, H = (int(v) for v in o.size.split("x"))
u = W / 1280
path = o.font or "/System/Library/Fonts/Courier.ttc"
font = ImageFont.truetype(path, int(26 * u)) if os.path.exists(path) else ImageFont.load_default(size=int(26 * u))
small = ImageFont.truetype(path, int(20 * u)) if os.path.exists(path) else ImageFont.load_default(size=int(20 * u))
AMBER = (255, 190, 70, 255)

shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ds = ImageDraw.Draw(shadow)
x, y = 48 * u, H - 104 * u
for dy, line in ((0, o.time), (34 * u, o.date)):
    ds.text((x + 2, y + dy + 2), line, font=font, fill=(0, 0, 0, 180))
im = Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), shadow.filter(ImageFilter.GaussianBlur(2)))
d = ImageDraw.Draw(im)
for dy, line in ((0, o.time), (34 * u, o.date)):
    d.text((x, y + dy), line, font=font, fill=AMBER)
r, cx, cy = 9 * u, W - 118 * u, 46 * u
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(230, 40, 40, 255))
d.text((cx + 16 * u, cy - 11 * u), "REC", font=small, fill=(255, 255, 255, 230))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "camcorder_ui.png")
im.save(out)
print(out)
