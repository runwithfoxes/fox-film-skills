---
name: story-in-one-run
description: A whole short story with your character, up to 30 seconds, made in one run of Seedance 2.5, so the character's face stays the same from first frame to last. The prompt is written like a shot list with seconds. Use when someone wants a 30 second character film, a story with several beats, or a film where the face drifted between joined clips.
---

# A story in one run

Seedance 2.5 makes up to 30 seconds in one go. Before, a 30 second film was three or four short clips joined, and
each clip painted the character's face a little differently. In one run there is one face from start to end.

Read `film-basics` first for the character description and the reference pictures.

## The prompt

Write it like a shot list, with the seconds for each beat. Five parts, in this order.

STYLE. One paragraph: what kind of film, the character "exactly as the references", the place, the light, the camera.

CHARACTER. The fixed description from `film-basics`, then the expression in plain words, then "Keep his exact face,
fur colour, outfit and size the same in every shot." Say which reference shows the back.

THE BEATS. One paragraph per beat, starting with the seconds: `0-4s:`, `4-10s:` and so on to the end. Say what the
character does and what the camera does. A story that is a small joke with a payoff works better than a list of
stunts.

SOUND. A list of the sounds you want, then "No music, no dialogue, no narration", so you choose the music later.

NEGATIVE. What must not happen. Always include "No words or writing on screen". The model cannot spell, so every
title goes on afterwards in the edit.

`example-canyon-prompt.txt` is the whole prompt for our canyon film, as it was run: the fox climbs a tower, holds his
phone up for a signal, steps off, glides down in a wingsuit, lands and starts climbing again. The film is at
runwithfoxes.com/craft/a-30-second-film-in-one-run.

## Three things to write in

Ask for a short fall before anything opens or catches the character, or they hang standing in the air for a second.

Describe a costume change in detail. "The hoodie spreads into a wingsuit" came out as a grey slab. Say where the wings
go: from the arms to the legs.

If something should be revealed behind the character, have them land or stop facing away from it, so the camera turns
with them and finds it.

## Making it

    python story_run.py prompt.txt story.mp4 --ref front.png --ref back.png --ref place.png

Three pictures is enough: the character from the front, from behind, and the place. A frame from an earlier film of
yours makes a good place picture, so the new film matches it.

## What to check

Watch it through once for the story, then read it frame by frame. Look at the face in every beat, the hands or paws
when they hold something, and the moment anything changes shape. Then cut it: titles, the opening and the ending go
on in your own edit, never in the prompt.

## Credit

Made with Seedance 2.5 (ByteDance) on Replicate. The shot list way of writing it we first saw in a film posted on X
by @AIwithkhan.
