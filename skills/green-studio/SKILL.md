---
name: green-studio
description: Your character acts on a flat green studio, then gets cut out and laid on anything drawn in code, a chart, a diagram, a page. The body comes from one Seedance 2 clip; the chart, the numbers and the timing are code. Ours rides a bar of a chart up and jumps to the next one. Use when someone wants a character inside a chart or figure, a mascot that reacts to data, or a green screen character from a video model.
---

# Green studio

A video model is good at a body moving and bad at charts. Code is the opposite. So split the job: ask the model for
your character doing one move on an empty green studio, cut them off the green on every frame, and lay them on a
chart or diagram drawn in code, timed and sized to fit.

Ours: the fox stands on the first bar of a chart, rides it up as it grows, crouches, jumps and lands on the taller
bar beside it. One paid clip, 40 cents, first try.

Read `film-basics` first. For drawing the chart itself in code, see the `motion-by-numbers` skill in our
motion-skills repo.

## The clip

    [your character description, with "exactly two arms and two legs", the clothes, "upright on two legs for the
    entire shot"]. An empty chroma key studio. The wall and the floor are one flat, even, pure bright green, no
    shadows on the floor, no props, no text. [Anything they step on: a plain block in the same flat green.]
    Locked off static camera on a tripod, no pan, no tilt, no zoom. Three-quarter side view, the whole body in frame
    for the entire shot with clear green space above and on both sides. [One move, as one continuous take: they
    stand, glance, crouch a little, jump in one arc onto the block, land, straighten and stand, bored, as if it was
    nothing.]

    python ../film-basics/seedance_clip.py prompt.txt clip.mp4 --ref character.png --aspect 1:1 --res 480p --secs 5

Why each part matters. Seedance 2 has no setting for a still camera, so the prompt has to say it. A real block to
jump onto gives a real jump, with knees tucking and weight landing; a hop on a flat floor lifted in code floats. The
block is the same green, so it is cut away with the studio, and its height becomes the gap between the two bars.
Ask for one move only. Keep the whole body in frame with space round it.

Don't trim the first second here. The standing frames at each end are the idle loop.

## Cutting out

    mkdir frames && ffmpeg -i clip.mp4 frames/%03d.png
    python key.py frames keyed

`key.py` takes out bright green only, which matters: a dark hoodie picks up dark green from the studio, and a plain
colour key punches holes in it. It also takes out a floor shadow (the same green, darker, strong in colour), fills
any hole smaller than 150 pixels inside the character, pulls the green fringe off the edges, and writes
`measure.json` with a box round the character and where the feet are on every frame. Lay four cut frames on your
background colour and look before going on.

## Putting them on the chart

Measure three numbers off the clip: where the feet stand before the jump, how high the top of the block is, and how
far across they travel. Draw the chart to fit those, never the other way round: the difference between the two bars
is the block's height, scaled.

Render the chart with no character on it, then lay the character on:

    python compose.py chart.mp4 keyed out.mp4 --scale 0.92 --feet 310,820 --lift lift.csv

`--feet` is where the character's feet go on the first frame. `--lift` is optional: a file of frame number and pixels
up, one per line, so the character rides up with a growing bar. One clip frame goes on each film frame. If the clip is
24 frames a second and the film 30, the character plays a little faster, which takes the float out of a jump.

To make standing time, play the idle frames forward and back before the move and after it. Pick the loop so the
first frame is not a blink.

## Joining two clips, and a loop

`seedance_clip.py --first a.png --last b.png` makes a clip that starts on one picture and ends on another. Give it the
last frame of the first clip and the first frame of the first clip, and the second move ends where the film began,
so the film loops.

## What to check

Every frame of the move, laid out at a size you can read: two arms, two legs, one tail if there is one, the same head
and face throughout. The first and last frames. The head clear of any title at the top of the jump. And the size: if
the character is too big, the chart looks small. Ours was right at 0.92 of the clip size and wrong at 1.15.

## Credit

Green screen is old film craft. Made with Seedance 2 (ByteDance) on Replicate, keyed with OpenCV, put together with
Pillow and ffmpeg. Our chart was drawn in code and rendered with HyperFrames.
