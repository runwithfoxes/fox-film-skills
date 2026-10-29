---
name: day-in-scenes
description: Join three short films of one character into one day, with time and temperature cards on black between them, the way Do the Right Thing tracks the heat on one block. Each scene is one Seedance 2.5 run; the joining and the cards are a free script. Use when someone wants a longer film from short ones, a day in the life, chapter cards, or names Spike Lee.
---

# A day in scenes

Three scenes of about 15 to 20 seconds each, made one at a time, then joined into one film of about a minute with
cards on black between them. Read `film-basics`, `story-in-one-run` and `real-world` first: each scene is made the
same way as those.

## Plan the scenes so they join

Write every scene from the same style block: the same place, the same year and film stock, the same camera position,
and your character as the only animated thing in a real street. If the style block is the same, the scenes look like
one place before you have edited anything. Ours is one Brooklyn block in 1989, a low wide camera with a slight tilt.

Give the scenes the same kind of joke. In ours the fox wants one small thing on a hot day, gets right up to it, and
loses it. Told once it is a gag. Three times across a day it is a pattern: this is how his days go.

Put them in time order and change the light for each one. Morning, afternoon and dusk. At dusk, name each light by
where it comes from: the sky over the rooftops, the street lights, the lit window. That keeps the evening real.

Open every scene the same way. All three of ours open from a rooftop high above the block, so you see the same street
three times at three times of day, and the change of light tells you time has passed.

End the day with the biggest version of the joke. Ours ends with a shop shutter coming down when he reaches the front
of the queue. A shop shutting is also what the end of a day looks like, so the scene closes the film as well.

## The cards

Open with your own title card. Lee's films open with "A Spike Lee Joint". Ours opens with "A Run with Foxes Joint".

Between the scenes, put the time and the temperature. 11 AM, 94 degrees, then 3 PM, 98 degrees, then 8 PM, 91. A time
and a temperature say more than a title, and in Do the Right Thing it is the radio DJ who keeps telling the block how
hot it is. Make the numbers rise through the day and drop a little at night.

Close on a forecast. "TOMORROW. 99°" carries on from the other cards, so it reads as the end of the day and adds one
more joke: tomorrow will be hotter. Then your web address.

Set the cards in a bold condensed face, off-white on black, centred across and down on the letters themselves (the
script measures each line's ink, so tall and short letters still sit in the middle). Keep words off the pictures.

## Sound across the cards

Under the last half second of each card, the next scene's street sound fades in, so you hear the place before you see
it. `join_day.py` takes that half second off the start of the scene's picture as well as its sound. If you trim only
the sound, every scene's sound runs half a second ahead of its picture, and you will hear it on every splat and crash.

## Cutting each scene

The model doesn't time things to the second. When it does the joke's moment badly, cut to the moment just after and
let the sound tell you what happened. Our shutter came in sideways and slowly, so the film cuts from the fox at the
bright window straight to the shutter already shut, with the crash of it landing on the cut. Our hydrant swung its jet
across the road instead of stopping, so the film cuts to the hand on the hydrant before the swing.

Find the cuts with ffmpeg's scene detection:

    ffmpeg -i scene.mp4 -vf "select='gt(scene,0.25)',metadata=print" -an -f null - 2>&1 | grep pts_time

Trim a scene's end in `SCENES` if its last stare holds too long before the card.

## What to watch for

Clothes change between runs. Our fox's trainers came out different in every scene, though every prompt asked for the
same ones. Say the shoes in the prompt, and still expect it.

Lettering on signs and menus comes out as made-up letters. Ask for none, and blur what's left.

Write the character's size against the people in the scene. "The top of his cap comes up to the grown-ups' waists"
works. Comparing him with a young child got one of our runs refused by the model's safety filter.

After joining, find one loud sound in each scene in the joined film and in the scene on its own, and check it lands at
the same moment.

`example-ice-cream-prompt.txt`, `example-hydrant-prompt.txt` and `example-hot-dog-prompt.txt` are our three scenes'
prompts, as they were run.
