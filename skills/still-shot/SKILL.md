---
name: still-shot
description: A short comedy in one still shot - a plain camera that never moves, a long shot, washed-out colour and a deadpan character losing to something absurd, the way the Coen brothers might shoot it. One run of Seedance 2.5. Use when someone wants a simple, dry, one-joke film, names the Coens or Fargo, or wants a film with no cuts.
---

# The still shot

One Seedance 2.5 run of about 15 seconds, one unbroken shot, in a real place. Read `film-basics`, `story-in-one-run`
and `real-world` first: this uses the same run and the same two lines that make a place look real.

The Coen brothers' comedy comes from a plain camera watching something absurd. In Fargo the camera barely moves, some
interior scenes play out in a single shot, and long shots make the lead look small against his trouble. Nothing in the
frame tells you it is funny. Their colour follows the place: Fargo is drained white and grey, so the few strong colours
jump out.

## The story

One place, one indignity, and the joke is on your character. Ours: supermarket doors that will not open for the fox,
then open for a pigeon. It works on mute, and there are no props to keep the same size and no extras to go wrong.

## Why the prompt is written the way it is

Write the director's choices, never the name. A model does not know "Coen brothers" as a set of decisions.

"ONE SINGLE CONTINUOUS SHOT for the whole film, no cuts", at the top in capitals and again in the negatives. The
model's habit is to cut a 15 second prompt into shots.

"A plain, observational camera on a tripod that never moves, never pans, never zooms." A still camera says this is
nothing worth noticing, which is the joke, and it keeps the character's face steady.

"A long shot from across the street at eye level, framed square-on ... level and centred, like a dull record of an
ordinary afternoon." The long shot keeps the character small. The last phrase gives the model the attitude.

"Washed-out desaturated colour ... The only strong colour in the whole frame is the fox's orange fur." Drain everything
else and the eye goes to the one warm thing.

A line for every second, in small plain movements: stands still, one step back, lifts one paw. A model with empty
seconds fills them with fidgeting and passers-by. Say the street is empty too.

Say the thing the joke depends on every time it matters. "The doors stay shut" after each attempt, and "The doors never
open for the fox" in the negatives. A model opens doors for whoever walks up to them.

Give every action its cause in the frame. "Much shorter than the doors" and "a small plain grey sensor box above them"
are why he waves at the top of the door.

Slow animals. "Walking, never flying." Fast movement is where the model breaks.

No lettering on the shop front, or it comes out as made-up letters.

"Real street sound only ... Long silences. No music." Music would tell you it is a joke.

End with the character turning to stare at the camera, held, so the viewer has a moment to laugh.

`example-door-prompt.txt` is the whole prompt for our film, as it was run.

## What to watch for

The model follows most lines and changes a few. Ours stood side-on, not facing the doors, came out bigger than asked,
and held the doors open longer. Check what changed still tells the story.

Check for cuts with ffmpeg's scene detection (`select='gt(scene,0.3)'`), read the key moment at six frames a second,
and count the arms and paws.

## Making it

    python ../story-in-one-run/story_run.py prompt.txt film.mp4 --ref front.png --ref back.png --secs 15

15 seconds at 480p, with sound.

## Credit

The look is the Coen brothers', after Fargo (1996), shot by Roger Deakins. Made with Seedance 2.5 (ByteDance) on
Replicate.
