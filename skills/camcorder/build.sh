#!/bin/sh
# Make clean 1280 x 720 footage look like a night camcorder: shake, flat colour, grain, vignette, then the stamp.
#   ./build.sh footage.mp4 out.mp4        (run camcorder_ui.py first)
set -e
here="$(cd "$(dirname "$0")" && pwd)"
ffmpeg -v error -y -i "$1" -loop 1 -i "$here/camcorder_ui.png" -filter_complex "
[0:v]fps=24,scale=1280:720,setsar=1,crop=1248:702:16+9*sin(t*11.3)+5*sin(t*29):9+7*sin(t*7.9)+4*cos(t*21),scale=1280:720,eq=contrast=1.18:saturation=0.78:brightness=-0.03,noise=alls=13:allf=t+u,vignette=PI/4.4[deg];
[1:v]format=rgba[ui];
[deg][ui]overlay=0:0:shortest=1,format=yuv420p[out]" -map "[out]" -c:v libx264 -crf 18 -an "$2"
echo "$2"
