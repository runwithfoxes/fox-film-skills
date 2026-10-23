#!/bin/sh
# Dress 1280 x 720 footage as a festival trailer: letterbox, laurels at 3.0 s, title at 4.0 s, nothing fades out.
# Makes two films: <out>.mp4 (ends with the footage) and <out>-loop.mp4 (holds the last frame 2.5 s more).
#   ./build.sh footage.mp4 out
set -e
here="$(cd "$(dirname "$0")" && pwd)"
src="$1"; out="${2%.mp4}"
ffmpeg -v error -y -i "$src" -loop 1 -i "$here/laurels.png" -loop 1 -i "$here/title.png" -filter_complex "
[0:v]fps=24,scale=1280:720,setsar=1,drawbox=x=0:y=0:w=1280:h=88:color=black:t=fill,drawbox=x=0:y=632:w=1280:h=88:color=black:t=fill[base];
[1:v]format=rgba,fade=t=in:st=3.0:d=0.8:alpha=1[l];
[2:v]format=rgba,fade=t=in:st=4.0:d=0.9:alpha=1[t];
[base][l]overlay=0:0:shortest=1[a];[a][t]overlay=0:0:shortest=1,format=yuv420p[v]" \
  -map "[v]" -c:v libx264 -crf 18 -an "$out.mp4"
ffmpeg -v error -y -i "$out.mp4" -vf "tpad=stop_mode=clone:stop_duration=2.5" -c:v libx264 -crf 18 -pix_fmt yuv420p "$out-loop.mp4"
echo "$out.mp4  $out-loop.mp4"
