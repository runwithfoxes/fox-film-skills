---
name: waterslide
description: An action montage where your character does something fast and fun, a waterslide, a ride, a chase, and stays completely deadpan the whole way down. Several short Seedance 2 clips from different angles, cut together with energy, ending on a close-up. Use when someone asks for an action montage, a waterslide film, or a character film with energy.
---

# Waterslide

Your character rides a waterslide in a rubber ring through a suburban back garden: wide shots of the slide, a shot
from behind going round the bend, a big splash, and a close-up at the bottom, soaked and still bored. The fun is
everything around the character moving fast while their face never changes.

Read `film-basics` first.

## How it is built

It is a montage of four to six clips, each from a different camera position: in front at the top, behind on a bend,
from high up and wide, a splash from low down, and a close-up to finish. Each clip is one simple move. Cut them
together on the action, with hard cuts, about one to one and a half seconds each, so the film moves fast.

Write every clip's prompt with the same character description, the same ring, the same slide and the same garden,
or the slide changes colour between cuts. Only the camera words change.

The face is the joke, so every prompt carries the same energy words: "completely bored unimpressed expression,
total indifference, even as the water splashes over him". The model wants the character to look thrilled on a
waterslide. Say it twice if you have to.

The last shot is a close-up, wet fur or hair, flat stare at the lens. That is the frame people remember, and the
frame a headline sits on if it is an ad.

## Making it

    python ../film-basics/seedance_clip.py top.txt   s1.mp4 --ref character.png --seed 3
    python ../film-basics/seedance_clip.py bend.txt  s2.mp4 --ref character.png --seed 3
    python ../film-basics/seedance_clip.py splash.txt s3.mp4 --ref character.png --seed 3
    python ../film-basics/seedance_clip.py close.txt s4.mp4 --ref character.png --seed 3
    ../one-take/stitch.sh out.mp4 1.2 s1.mp4 s2.mp4 s3.mp4 s4.mp4

Give the close-up longer than the rest: cut it on its own with a longer keep and join it last.

## What to check

Water hides hands. Count them anyway in every shot where the character holds the ring. Check the ring and the
clothes are the same in every cut.

## Credit

The method here uses Seedance 2 (ByteDance) on Replicate.
