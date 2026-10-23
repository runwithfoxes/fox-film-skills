#!/bin/sh
# Join clips with hard cuts: drop each clip's first second, keep the next N seconds, re-encode all the same way.
#   ./stitch.sh out.mp4 2.5 c1.mp4 c2.mp4 c3.mp4
set -e
out="$1"; keep="$2"; shift 2
tmp=$(mktemp -d)
i=0
for c in "$@"; do
  i=$((i+1))
  ffmpeg -v error -y -ss 1 -t "$keep" -i "$c" -vf "fps=24,scale=trunc(iw/2)*2:trunc(ih/2)*2" \
    -c:v libx264 -crf 18 -pix_fmt yuv420p -an "$tmp/$i.mp4"
  echo "file '$tmp/$i.mp4'" >> "$tmp/list.txt"
done
ffmpeg -v error -y -f concat -safe 0 -i "$tmp/list.txt" -c copy "$out"
rm -r "$tmp"
echo "$out"
