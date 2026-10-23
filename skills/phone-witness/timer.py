"""Draw the phone's counting REC timer, one transparent 720 x 1280 PNG per second: timer_0.png, timer_1.png ...

    python timer.py <seconds> [--font path/to/font.ttf]

White, 27 px, with a soft shadow, just right of the centred REC dot. On a Mac the default is Helvetica.
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("seconds", type=int); ap.add_argument("--font")
o = ap.parse_args()
here = os.path.dirname(os.path.abspath(__file__))
path = o.font or "/System/Library/Fonts/Helvetica.ttc"
font = ImageFont.truetype(path, 27) if os.path.exists(path) else ImageFont.load_default(size=27)
for s in range(o.seconds):
    txt = f"0:{s:02d}"
    shadow = Image.new("RGBA", (720, 1280), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((382, 51), txt, font=font, fill=(0, 0, 0, 160))
    im = Image.alpha_composite(Image.new("RGBA", (720, 1280), (0, 0, 0, 0)), shadow.filter(ImageFilter.GaussianBlur(2)))
    ImageDraw.Draw(im).text((382, 50), txt, font=font, fill=(255, 255, 255, 255))
    im.save(os.path.join(here, f"timer_{s}.png"))
print(o.seconds, "timer frames written")
