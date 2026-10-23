"""Make one still with Seedream 4.5 on Replicate.

    python seedream_still.py prompt.txt out.png [--ref character.png] [--ref layout.jpg] [--aspect 16:9] [--size 2K]

Needs REPLICATE_API_TOKEN in the environment. Every --ref picture is passed as a reference: your character, and if
you want one, a picture whose layout the still should follow. Describe what is seen, never where the camera is,
or Seedream draws a camera in the scene.
"""
import argparse, os, sys, time, requests

ap = argparse.ArgumentParser()
ap.add_argument("prompt"); ap.add_argument("out")
ap.add_argument("--ref", action="append", default=[])
ap.add_argument("--aspect", default="16:9"); ap.add_argument("--size", default="2K")
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

inp = {"prompt": open(o.prompt).read().strip(), "size": o.size, "aspect_ratio": o.aspect}
if o.ref:
    inp["image_input"] = [upload(p) for p in o.ref]
r = requests.post("https://api.replicate.com/v1/models/bytedance/seedream-4.5/predictions", headers=H, json={"input": inp}).json()
if "urls" not in r:
    sys.exit(str(r))
while r.get("status") not in ("succeeded", "failed", "canceled"):
    time.sleep(5)
    r = requests.get(r["urls"]["get"], headers=H).json()
print(r["status"], r.get("error") or "")
if r["status"] == "succeeded":
    url = r["output"][0] if isinstance(r["output"], list) else r["output"]
    open(o.out, "wb").write(requests.get(url).content)
    print(o.out)
log = os.path.join(os.path.dirname(os.path.abspath(o.out)), "spend.txt")
open(log, "a").write(f"{time.strftime('%Y-%m-%d %H:%M')}  seedream-4.5 {o.size} {o.aspect} {r['status']}  {o.out}\n")
