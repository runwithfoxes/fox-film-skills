#!/bin/sh
# Footage seen through a phone: shake the footage, then lay the still phone screen, the focus box and the timer on top.
#   ./build.sh footage.mp4 out.mp4       (run render_overlays.py and timer.py first)
set -e
here="$(cd "$(dirname "$0")" && pwd)"
src="$1"; out="$2"
n=$(ls "$here"/timer_*.png | wc -l | tr -d ' ')
inputs=""; chain=""; last="b"
i=0
while [ $i -lt "$n" ]; do
  inputs="$inputs -loop 1 -i $here/timer_$i.png"
  k=$((i+3)); nxt=$((i+1))
  if [ $nxt -lt "$n" ]; then en="between(t,$i,$nxt)"; else en="gte(t,$i)"; fi
  chain="$chain[$k:v]format=rgba[t$i];[$last][t$i]overlay=0:0:shortest=1:enable='$en'[c$i];"
  last="c$i"; i=$((i+1))
done
ffmpeg -v error -y -i "$src" -loop 1 -i "$here/phone_ui.png" -loop 1 -i "$here/focus_box.png" $inputs -filter_complex "
[0:v]fps=24,scale=720:1280,setsar=1,crop=684:1216:18+11*sin(t*12.7)+6*sin(t*33):32+9*sin(t*8.3)+5*cos(t*23),scale=720:1280[shaken];
[1:v]format=rgba[ui];
[2:v]format=rgba,fade=t=in:st=1.2:d=0.12:alpha=1,fade=t=out:st=2.3:d=0.25:alpha=1[fb];
[shaken][ui]overlay=0:0:shortest=1[a];[a][fb]overlay=0:0:shortest=1[b];
$chain[$last]format=yuv420p[out]" -map "[out]" -c:v libx264 -crf 18 -an "$out"
echo "$out"
