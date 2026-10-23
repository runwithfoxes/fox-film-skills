"""Make one clip with Seedance 2 on Replicate.

    python seedance_clip.py prompt.txt out.mp4 --ref character.png [--res 480p] [--secs 5] [--aspect 16:9] [--seed 11]
    python seedance_clip.py prompt.txt out.mp4 --first a.png --last b.png      (starts on one picture, ends on another)

Needs REPLICATE_API_TOKEN in the environment. Extra --ref pictures (a place, a prop) go in the same list.
Prices per second as checked in September 2026: 480p 0.08, 720p 0.18, 1080p 0.45 US dollars. Check the model page.
"""
import argparse, os, sys, time, requests

ap = argparse.ArgumentParser()
ap.add_argument("prompt"); ap.add_argument("out")
ap.add_argument("--ref", action="append", default=[])
ap.add_argument("--first"); ap.add_argument("--last")
ap.add_argument("--res", default="480p"); ap.add_argument("--secs", type=int, default=5)
ap.add_argument("--aspect", default="16:9"); ap.add_argument("--seed", type=int, default=11)
o = ap.parse_args()

TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not TOKEN:
    sys.exit("Set REPLICATE_API_TOKEN first.")
H = {"Authorization": f"Bearer {TOKEN}"}

def upload(path):
    with open(path, "rb") as f:
        r = requests.post("https://api.replicate.com/v1/files", headers=H,
                          files={"content": (os.path.basename(path), f, "image/png")})
    r.raise_for_status()
    return r.json()["urls"]["get"]

inp = {"prompt": open(o.prompt).read().strip(), "resolution": o.res, "duration": o.secs,
       "generate_audio": False, "seed": o.seed}
if o.first:
    # the one place `image` is right: the first frame is meant to be locked
    inp["image"] = upload(o.first)
    if o.last:
        inp["last_frame_image"] = upload(o.last)
else:
    if not o.ref:
        sys.exit("Pass --ref character.png (or --first and --last).")
    inp["reference_images"] = [upload(p) for p in o.ref]   # a list, never `image`
    inp["aspect_ratio"] = o.aspect

r = requests.post("https://api.replicate.com/v1/models/bytedance/seedance-2.0/predictions", headers=H, json={"input": inp}).json()
if "urls" not in r:
    sys.exit(str(r))
while r.get("status") not in ("succeeded", "failed", "canceled"):
    time.sleep(6)
    r = requests.get(r["urls"]["get"], headers=H).json()
print(r["status"], r.get("error") or "")
cost = 0.0
if r["status"] == "succeeded":
    url = r["output"][0] if isinstance(r["output"], list) else r["output"]
    open(o.out, "wb").write(requests.get(url).content)
    cost = {"480p": .08, "720p": .18, "1080p": .45}.get(o.res, 0) * o.secs
    print(o.out)
log = os.path.join(os.path.dirname(os.path.abspath(o.out)), "spend.txt")
open(log, "a").write(f"{time.strftime('%Y-%m-%d %H:%M')}  seedance-2.0 {o.res} {o.secs}s seed {o.seed} {r['status']}  about {cost:.2f} USD  {o.out}\n")
