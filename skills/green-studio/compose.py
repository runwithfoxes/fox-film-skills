"""Lay the cut-out character on a film drawn in code, one clip frame to one film frame.

    python compose.py chart.mp4 keyed/ out.mp4 [--scale 0.92] [--feet X,Y] [--lift lift.csv] [--start 0]

keyed/ is the folder key.py wrote, with measure.json. --feet is where the feet land on the first frame, in film
pixels; later frames follow the clip's own feet, so a jump travels as it did in the studio. --lift is a file of
"frame,pixels" lines that raises the character by that much on that frame (for riding a growing bar). --start is
the film frame the clip begins on; before it the first keyed frame holds. After the clip ends the last frame holds.
Writes a contact sheet beside out.mp4 to read before anyone sees it.
"""
import argparse, glob, json, os, shutil, subprocess, tempfile
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("film"); ap.add_argument("keyed"); ap.add_argument("out")
ap.add_argument("--scale", type=float, default=1.0); ap.add_argument("--feet", default=None)
ap.add_argument("--lift"); ap.add_argument("--start", type=int, default=0)
o = ap.parse_args()

M = json.load(open(os.path.join(o.keyed, "measure.json")))
cut = sorted(glob.glob(os.path.join(o.keyed, "*.png")))
fps = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=r_frame_rate",
                      "-of", "csv=p=0", o.film], capture_output=True, text=True).stdout.strip()
lift = {}
if o.lift:
    for line in open(o.lift):
        if line.strip():
            f, px = line.split(",")
            lift[int(f)] = float(px)

tmp = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", o.film, os.path.join(tmp, "b%05d.png")], check=True)
frames = sorted(glob.glob(os.path.join(tmp, "b*.png")))
W, H = Image.open(frames[0]).size
fx0, fy0 = (float(v) for v in o.feet.split(",")) if o.feet else (W / 2, H * 0.85)
m0 = M[0]
cache = {}
for n, path in enumerate(frames):
    k = min(max(n - o.start, 0), len(cut) - 1)
    if k not in cache:
        im = Image.open(cut[k]).convert("RGBA")
        cache[k] = im.resize((round(im.width * o.scale), round(im.height * o.scale)), Image.LANCZOS)
    ch, m = cache[k], M[k]
    # place this frame's feet relative to the first frame's feet, so movement in the studio carries over
    x = fx0 + (m["feet_x"] - m0["feet_x"]) * o.scale - m["feet_x"] * o.scale
    y = fy0 + (m["y1"] - m0["y1"]) * o.scale - m["y1"] * o.scale - lift.get(n, 0)
    bg = Image.open(path).convert("RGBA")
    bg.alpha_composite(ch, (round(x), round(y)))
    bg.convert("RGB").save(path)

subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", fps, "-i", os.path.join(tmp, "b%05d.png"),
                "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-an", o.out], check=True)
sheet = os.path.splitext(o.out)[0] + "-sheet.png"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", o.out, "-vf", "fps=6,scale=320:-1,tile=6x6", "-frames:v", "1", sheet], check=True)
shutil.rmtree(tmp)
print(o.out, "\nnow read", sheet, "and every frame of the move full size")
