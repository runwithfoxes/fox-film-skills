---
name: character-walk
description: Your character walks, toward the camera on a beach, or away from it down a stadium tunnel toward the light. One Seedance 2 clip per place, the same walk every time, so a set of films can swap the background and keep the character. Use when someone asks for a character walking, a walk-on, a tunnel walk-out, or the same character in many places.
---

# Character walk

The simplest film in the set, and the one that is used most. Your character walks, and nothing else happens. Toward
the camera, it is a confident arrival: a beach, a street, an office. Away from the camera, it is a walk-out: a tunnel
toward a pitch, a corridor toward a stage.

Because the walk is the same every time, one character can turn up in any number of places, and a set of short films
can change only the background.

Read `film-basics` first, and the camera rules in `one-take`, which this shares.

## Toward the camera

    [your character description]. Walking toward the camera on two legs like a person across [a wide empty beach at
    golden hour, footprints in the sand behind], hands in the hoodie pockets, a completely bored unimpressed
    expression. CAMERA: directly in front of the character, facing them, moving backward at their walking pace, low
    angle at hip height. Compact small frame, fills the lower centre of frame.

Never a statue. If the character stands still in a film it looks like a picture with a moving background. Something
always moves: the walk, a head turn, a glance.

## Away from the camera

This is the hard one. An animal character seen from behind turns into a real animal unless you lock it three ways,
all in the same prompt:

    The character is fully clothed in [clothes]. They walk upright on two legs like a person for the entire shot,
    never on all fours. Their back is to the camera at all times, they never turn their body toward the camera, their
    face is never seen.

Then the place and the light: "a long concrete stadium tunnel, strip lights overhead, the bright pitch and the crowd
at the far end, the character walks toward the light and grows smaller". Never ask for a look back over the shoulder.

## Making it

    python ../film-basics/seedance_clip.py beach.txt beach.mp4 --ref character.png --secs 5
    python ../film-basics/seedance_clip.py tunnel.txt tunnel.mp4 --ref character.png --secs 5

## What to check

Feet. Walks go wrong at the feet first: a step that slides, a foot that swaps sides, a third leg for a frame. Read the
walk frame by frame from the knees down. From behind, check every frame that the body has not turned.

## Credit

Made with Seedance 2 (ByteDance) on Replicate.
