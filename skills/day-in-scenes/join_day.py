"""Join short scenes into one film with title cards on black between them.

Edit the CARDS and SCENES lists below, then:  python3 join_day.py  ->  day.mp4
Needs ffmpeg and Pillow (pip install pillow), and a bold condensed font file. We use Anton
(free from Google Fonts, Open Font Licence): put Anton-Regular.ttf next to this script.

Each card is centred across and down on its own letters. Under the last PRE seconds of each card the next
scene's sound fades in, and the same PRE seconds come off the start of that scene's picture, so the sound
stays in sync. Check one loud hit per scene (a splat, a crash) against the scene on its own after joining."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, RATE = 854, 480, 24, 32000          # match your scenes (ffprobe them first)
FONT = os.path.join(HERE, "Anton-Regular.ttf")
INK = (244, 238, 228)                            # off-white on black
CARD_S, PRE = 2.0, 0.5                           # card length; sound lead-in under each card

OPEN = ("A RUN WITH FOXES JOINT", 2.5)           # your own opening card
SCENES = [                                       # (card before the scene, scene file, seconds to trim off its end)
    ("11 AM. 94°", "scene1.mp4", 0.5),
    ("3 PM. 98°", "scene2.mp4", 0),
    ("8 PM. 91°", "scene3.mp4", 0),
]
CLOSE = [("TOMORROW. 99°", 2.0), ("Runwithfoxes.com", 2.5)]

def run(a): subprocess.run(a, check=True)
def card_png(text, path):
    im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
    lines = text.split("\n"); size = 72 if max(len(l) for l in lines) < 15 else 58
    f = ImageFont.truetype(FONT, size); gap = int(size * 0.18)
    boxes = [d.textbbox((0, 0), l, font=f) for l in lines]
    total = sum(b[3] - b[1] for b in boxes) + gap * (len(lines) - 1); y = (H - total) / 2
    for l, b in zip(lines, boxes):
        d.text(((W - (b[2] - b[0])) / 2 - b[0], y - b[1]), l, font=f, fill=INK); y += (b[3] - b[1]) + gap
    im.save(path)
def card(text, name, length, sound_from=None):
    png, mp4 = f"{HERE}/parts/{name}.png", f"{HERE}/parts/{name}.mp4"; card_png(text, png)
    enc = ["-r", str(FPS), "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", str(RATE), "-ac", "2", "-t", str(length), mp4]
    if sound_from:
        ms = int((length - PRE) * 1000)
        af = f"[1:a]atrim=0:{PRE},afade=t=in:d={PRE},adelay={ms}|{ms},apad=whole_dur={length}[a]"
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(length), "-i", png, "-i", sound_from, "-filter_complex", af, "-map", "0:v", "-map", "[a]"] + enc)
    else:
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(length), "-i", png, "-f", "lavfi", "-t", str(length), "-i", f"anullsrc=r={RATE}:cl=stereo", "-map", "0:v", "-map", "1:a"] + enc)
    return mp4
def scene(src, name, trim_end):
    mp4 = f"{HERE}/parts/{name}.mp4"
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout) - trim_end
    fc = f"[0:v]trim={PRE},setpts=PTS-STARTPTS[v];[0:a]atrim={PRE},asetpts=PTS-STARTPTS,apad[a]"
    run(["ffmpeg", "-v", "error", "-y", "-t", str(dur), "-i", src, "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-shortest",
         "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", str(RATE), "-ac", "2", mp4])
    return mp4

os.makedirs(f"{HERE}/parts", exist_ok=True)
parts = [card(OPEN[0], "c0", OPEN[1])]
for i, (text, src, cut) in enumerate(SCENES):
    src = os.path.join(HERE, src)
    parts += [card(text, f"c{i+1}", CARD_S, sound_from=src), scene(src, f"s{i+1}", cut)]
parts += [card(t, f"z{i}", s) for i, (t, s) in enumerate(CLOSE)]
lst = f"{HERE}/parts/list.txt"; open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", f"{HERE}/day.mp4"])
print("saved day.mp4")
