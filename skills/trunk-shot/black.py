"""Make the near-black start frame for a reveal, the same size as the end still.

    python black.py end.png start.png
"""
import sys
from PIL import Image

end, out = sys.argv[1], sys.argv[2]
W, H = Image.open(end).size
Image.new("RGB", (W, H), (8, 7, 6)).save(out)
print(out, W, "x", H)
