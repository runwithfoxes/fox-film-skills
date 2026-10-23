---
name: one-take
description: The Goodfellas walk. Your character walks toward a camera that backs away in front of them, and the place changes behind them with hard cuts, a corridor, a kitchen, a stage, while the walk carries on. Three to five Seedance 2 clips stitched together. Use when someone asks for a tracking shot, a Goodfellas or Copacabana walk, a one-take montage, or a character walking through several places.
---

# One-take

The camera walks backwards in front of your character, who walks straight at it, never stopping. Every couple of
seconds the place behind them changes with a hard cut, a service corridor, then a kitchen, then a stage, and the walk
and the stare carry straight on. Done well, it feels like one long take through a building.

Read `film-basics` first.

## The camera words

This is the line that makes it work, word for word:

    CAMERA: directly in front of the character, facing them, moving backward at their walking pace. We see their face
    the entire time. Walking toward the camera on two legs like a person. Anthropomorphic upright human posture.

Add "compact small frame, fills the lower centre of frame" for the size.

## Rules

Make three to five clips of about 5 seconds, one per place, and use about 2.5 seconds of each. Trim the first second
of each clip, where the model is still setting up.

Hard cuts. No dissolves or wipes; the walk is the join.

The clothes must not change between places, so the same clothing words go in every prompt. Using the same seed for
every clip helps.

A picture of a place can go in as a second reference, after the character picture. A photo with a real person's face
in it gets blocked by the model's filter.

21:9 looks the most like film.

A shot from behind, following the character, only works under a hard lock: the character clothed, "walks upright on
two legs like a person for the entire shot, never on all fours", and "their back is to the camera at all times, they
never turn their body toward the camera, their face is never seen". Without all three they come back as a real
animal on four legs. Never ask for a glance over the shoulder in a shot from behind: the model turns the whole body
round and the character changes the moment the face is in view.

## Making it

    python ../film-basics/seedance_clip.py corridor.txt c1.mp4 --ref character.png --aspect 21:9 --seed 7
    python ../film-basics/seedance_clip.py kitchen.txt  c2.mp4 --ref character.png --aspect 21:9 --seed 7
    python ../film-basics/seedance_clip.py stage.txt    c3.mp4 --ref character.png --aspect 21:9 --seed 7
    ./stitch.sh out.mp4 2.5 c1.mp4 c2.mp4 c3.mp4

`stitch.sh` drops the first second of each clip, keeps the next 2.5 seconds, re-encodes them all the same way and
joins them with hard cuts.

## A better way we haven't finished

Make the walk once, on a plain background, cut the character out of it (a video matting model such as SAM 2 does
this), and lay that one walk over real plates of each place. The clothes, the size and the stride then cannot change
between places. We have proved the idea, not built it.

## Credit

The shot is Martin Scorsese's Copacabana tracking shot in Goodfellas (1990), filmed by Michael Ballhaus. Made with
Seedance 2 (ByteDance) on Replicate.
