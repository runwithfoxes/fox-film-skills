"""Cut a character off a green studio, frame by frame.

    python key.py <frames dir> <out dir> [props]

Add the word props as a third argument to keep a thing the character carries.
Green is hue 35 to 90 with some colour in it. If your character wears or is green, this will not work: dress them
in something else for the studio.
Writes RGBA frames and measure.json: for each frame the box round the character and the lowest point of the feet.
Needs opencv-python and numpy."""
import sys, os, json, glob
import numpy as np, cv2
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
PROPS = len(sys.argv) > 3 and sys.argv[3] == "props"     # keep a thing they carry too: every piece over 600 px, not only the character
rows = []
for p in sorted(glob.glob(os.path.join(src, "*.png"))):
    bgr = cv2.imread(p); hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    h, s, v = hsv[..., 0].astype(int), hsv[..., 1].astype(int), hsv[..., 2].astype(int)
    hue = (h > 35) & (h < 90)
    # the studio green is bright. A floor shadow is the same green, darker but still strong in colour. Dark clothes
    # pick up dark green too, but weak in colour or nearly black, and it must stay.
    green = (hue & (s > 70) & (v > 105)) | (hue & (s > 150) & (v > 55))
    green = green.astype(np.uint8)
    fg = 1 - green
    # keep the one big piece that is the character; small specks are the block's edge or noise
    n, lab, st, _ = cv2.connectedComponentsWithStats(fg, 8)
    big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    fg = (lab == big).astype(np.uint8)
    if PROPS:
        for i in range(1, n):
            if st[i, cv2.CC_STAT_AREA] > 600:
                fg[lab == i] = 1
    # a hole under 150 px inside the character is a keying miss, never a real gap between an arm and the body
    hn, hl, hs, _ = cv2.connectedComponentsWithStats(1 - fg, 4)
    for i in range(1, hn):
        if hs[i, cv2.CC_STAT_AREA] < 150:
            fg[hl == i] = 1
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((4, 1), np.uint8))   # a line under 4 px tall is the block's edge or a floor shadow, never the character
    fg = cv2.erode(fg, np.ones((2, 2), np.uint8))                      # take the green fringe off the fur
    a = cv2.GaussianBlur(fg.astype(np.float32), (0, 0), 0.8)
    b, g, r = [bgr[..., i].astype(np.float32) for i in range(3)]
    g = np.minimum(g, np.maximum(r, b) * 1.02)                          # despill: green never above the other two
    rgba = np.dstack([b, g, r, a * 255]).astype(np.uint8)
    cv2.imwrite(os.path.join(out, os.path.basename(p)), rgba)
    ys, xs = np.where(fg > 0)
    feet = ys.max(); fx = xs[ys > feet - 6]
    rows.append(dict(f=len(rows), x0=int(xs.min()), x1=int(xs.max()), y0=int(ys.min()), y1=int(feet), feet_x=float(fx.mean()), area=int(fg.sum())))
json.dump(rows, open(os.path.join(out, "measure.json"), "w"))
for r in rows[::4]: print(r)
