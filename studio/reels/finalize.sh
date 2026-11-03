#!/bin/sh
# finalize.sh reelN NAME : build the Reel, then remux with the final audio trim into deliver/ (no metadata)
set -e
cd /home/claude/mt
python3 reels/build_reel.py "$1" 2>&1 | grep -v "^\s*$"
ffmpeg -v error -y -i "reels/$1/$2.mp4" -i "reels/$1/voice.wav" -map 0:v -map 1:a -c:v copy \
  -af "volume=-2dB,alimiter=limit=0.79:attack=3:release=50:level=disabled" -c:a aac -b:a 160k -ar 48000 -shortest \
  -movflags +faststart -map_metadata -1 -map_metadata:s:v -1 -map_metadata:s:a -1 -map_chapters -1 \
  -metadata:s:v handler_name= -metadata:s:a handler_name= "deliver/$2.mp4"
echo "FINAL $2: $(ffprobe -v error -show_entries format=duration -of csv=p=0 deliver/$2.mp4) s"
