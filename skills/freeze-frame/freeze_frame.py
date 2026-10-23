"""Cut a freeze frame with a title into a clip: part one, a 2 frame white flash, a 2 second titled freeze, part two.

    python freeze_frame.py clip.mp4 <freeze second> "Title in sentence case" out.mp4 [--font Anton-Regular.ttf] [--size 110] [--y 0.5]

--y is where the title sits, as a share of the frame height (0.5 is the middle). Move it if it lands on the face.
Writes freeze_plain.png and freeze_titled.png beside out.mp4 so you can check that.
"""
import argparse, os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("clip"); ap.add_argument("at", type=float); ap.add_argument("title"); ap.add_argument("out")
ap.add_argument("--font"); ap.add_argument("--size", type=int, default=110); ap.add_argument("--y", type=float, default=0.5)
ap.add_argument("--hold", type=float, default=2.0)
o = ap.parse_args()

FPS, FLASH = 24, "#F5F2EB"
tmp = tempfile.mkdtemp()
here = os.path.dirname(os.path.abspath(o.out))
enc = ["-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]
run = lambda *a: subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)

p1, p2 = os.path.join(tmp, "p1.mp4"), os.path.join(tmp, "p2.mp4")
run("-i", o.clip, "-t", str(o.at), *enc, p1)
run("-ss", str(o.at), "-i", o.clip, *enc, p2)

plain = os.path.join(here, "freeze_plain.png")
run("-sseof", "-0.05", "-i", p1, "-frames:v", "1", "-update", "1", plain)   # the exact last frame of part one

im = Image.open(plain).convert("RGBA")
W, H = im.size
font = ImageFont.truetype(o.font, o.size) if o.font else ImageFont.load_default(size=o.size)
d = ImageDraw.Draw(im)
tw = d.textlength(o.title, font=font)
x, y = (W - tw) / 2, H * o.y - o.size / 2
shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
ds = ImageDraw.Draw(shadow)
for dx, dy, a in ((0, 4, 150), (0, 2, 110)):
    ds.text((x + dx, y + dy), o.title, font=font, fill=(0, 0, 0, a))
im = Image.alpha_composite(im, shadow.filter(ImageFilter.GaussianBlur(6)))
ImageDraw.Draw(im).text((x, y), o.title, font=font, fill=(250, 250, 248, 255))
titled = os.path.join(here, "freeze_titled.png")
im.convert("RGB").save(titled)

flash, hold = os.path.join(tmp, "flash.mp4"), os.path.join(tmp, "hold.mp4")
run("-f", "lavfi", "-i", f"color=c={FLASH}:s={W}x{H}:r={FPS}", "-frames:v", "2", *enc, flash)
run("-loop", "1", "-i", titled, "-t", str(o.hold), *enc, hold)

lst = os.path.join(tmp, "list.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in (p1, flash, hold, p2)))
run("-f", "concat", "-safe", "0", "-i", lst, *enc, o.out)
print(o.out, "\nnow look at", titled, "full size: is the title clear of the face?")
