"""Animate between a start picture and an end picture with Kling on fal.ai.

    python kling_reveal.py prompt.txt start.png end.png out.mp4 [--model fal-ai/kling-video/v2.6/pro/image-to-video] [--secs 5]

Needs FAL_KEY in the environment. The model path is the one we used in April 2026; check fal.ai for the current one.
"""
import argparse, os, sys, time, requests

ap = argparse.ArgumentParser()
ap.add_argument("prompt"); ap.add_argument("start"); ap.add_argument("end"); ap.add_argument("out")
ap.add_argument("--model", default="fal-ai/kling-video/v2.6/pro/image-to-video")
ap.add_argument("--secs", default="5")
o = ap.parse_args()

KEY = os.environ.get("FAL_KEY")
if not KEY:
    sys.exit("Set FAL_KEY first.")
H = {"Authorization": f"Key {KEY}", "Content-Type": "application/json"}

def upload(path):
    r = requests.post("https://rest.alpha.fal.ai/storage/upload/initiate", headers=H,
                      json={"content_type": "image/png", "file_name": os.path.basename(path)}).json()
    requests.put(r["upload_url"], headers={"Content-Type": "image/png"}, data=open(path, "rb").read()).raise_for_status()
    return r["file_url"]

job = requests.post(f"https://queue.fal.run/{o.model}", headers=H, json={
    "prompt": open(o.prompt).read().strip(),
    "start_image_url": upload(o.start),
    "end_image_url": upload(o.end),
    "duration": o.secs,
    "generate_audio": False,
    "negative_prompt": "blurry, distorted, extra limbs, morphing, melting, smiling",
}).json()
if "status_url" not in job:
    sys.exit(str(job))
auth = {"Authorization": f"Key {KEY}"}
for _ in range(120):
    time.sleep(10)
    st = requests.get(job["status_url"], headers=auth).json().get("status")
    print(st)
    if st == "COMPLETED":
        video = requests.get(job["response_url"], headers=auth).json()["video"]["url"]
        open(o.out, "wb").write(requests.get(video).content)
        print(o.out)
        break
    if st in ("FAILED", "ERROR"):
        sys.exit("failed")
