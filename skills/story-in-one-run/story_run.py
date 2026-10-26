"""Make a whole story, up to 30 seconds, in one run of Seedance 2.5 on Replicate.

    python story_run.py prompt.txt out.mp4 --ref front.png --ref back.png --ref place.png [--res 480p] [--secs 30]

Needs REPLICATE_API_TOKEN in the environment. The --ref pictures are your character from the front, from behind,
and a picture of the place. Sound is made in the same run (the prompt's SOUND list says what, and "no music").
Price per second when we ran it, October 2026: about 0.10 US dollars at 480p with pictures only. A reference video
puts the run on a dearer tier. Check the model page.
"""
import argparse, os, sys, time, requests

ap = argparse.ArgumentParser()
ap.add_argument("prompt"); ap.add_argument("out")
ap.add_argument("--ref", action="append", default=[])
ap.add_argument("--res", default="480p"); ap.add_argument("--secs", type=int, default=30)
ap.add_argument("--aspect", default="16:9")
o = ap.parse_args()

TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not TOKEN:
    sys.exit("Set REPLICATE_API_TOKEN first.")
if not o.ref:
    sys.exit("Pass at least one --ref picture of your character.")
H = {"Authorization": f"Bearer {TOKEN}"}

def upload(path):
    with open(path, "rb") as f:
        r = requests.post("https://api.replicate.com/v1/files", headers=H,
                          files={"content": (os.path.basename(path), f, "image/png")})
    r.raise_for_status()
    return r.json()["urls"]["get"]

inp = {"prompt": open(o.prompt).read().strip(), "reference_images": [upload(p) for p in o.ref],
       "resolution": o.res, "aspect_ratio": o.aspect, "duration": o.secs, "generate_audio": True}
r = requests.post("https://api.replicate.com/v1/models/bytedance/seedance-2.5/predictions", headers=H,
                  json={"input": inp})
r.raise_for_status()
p = r.json()
print("started", p["id"], flush=True)
while p["status"] not in ("succeeded", "failed", "canceled"):
    time.sleep(10)
    p = requests.get(p["urls"]["get"], headers=H).json()
print(p["status"], p.get("error") or "", flush=True)

log = os.path.join(os.path.dirname(os.path.abspath(o.out)), "spend.log")
open(log, "a").write(f"{time.strftime('%Y-%m-%d %H:%M')}  seedance-2.5 {o.res} {o.secs}s {p['status']}  {o.out}\n")
if p["status"] == "succeeded":
    url = p["output"] if isinstance(p["output"], str) else p["output"][0]
    open(o.out, "wb").write(requests.get(url).content)
    print("saved", o.out)
