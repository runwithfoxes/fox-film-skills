---
name: real-world
description: Your animated character in a real, photographic place, made in one run of Seedance 2.5. Real light, real surfaces, the character touching real things, with a small joke as the story. Use when someone wants the character out of an animated world and into a real one, like a computer-animated bear in a live-action family film.
---

# The character in a real world

The same method as `story-in-one-run`, one Seedance 2.5 run written as a shot list with seconds, pointed at a real
place. Read `film-basics` and `story-in-one-run` first.

A real place is a harder test than an animated one. In an animated world nobody notices if the fur or the shadows are
a bit off. Next to a real steel dryer under strip lights, they show.

## The decisions

Pick an ordinary place, not a famous one. A landmark looks like a postcard. A launderette, a bus stop or a hardware
shop feels real because of the small things in it, and the model has seen far more of them.

Give no photo of the place. Two pictures of the character, front and back, and the place comes from the words. A
photo as the first frame tends to get repainted softer as the film goes on.

Make the story a joke that reads with the sound off. Most films are watched on mute.

If the character's usual costume changes, say why in the prompt ("his hoodie is in the dryer"). The reference
pictures show the usual costume, and without a reason the model puts it back on.

Give every extra one job and say what they never do ("she never comes over and never speaks").

## The two lines that make it real

In STYLE: "Photorealistic live-action documentary footage, shot on a real camera in a real ..." with the real light
named, and the character "placed into this real world the way a computer-animated bear is placed into a live-action
family film", with realistic fur and real contact shadows under the feet.

In NEGATIVE, first: "No cartoon or animated set, no painted background, no game look, everything except the [character]
is real."

`example-launderette-prompt.txt` is the whole prompt for our launderette film, as it was run.

## What to watch for

Give the joke object a size against the body. "Shrunk to the size of a doll's top" gave a hoodie a size or two small,
which nearly fitted. "No bigger than his own head" and "stops high on his chest like a crop top" gave the joke.

Give the payoff its own held shot, two seconds of the character standing still in it, or the film rushes past it.

The model picks shots of its own. When you like a run, write its best shots into the next prompt by name and change
one thing.

Shots from two runs only mix where extras and costume match. Each run invents its own extras.

Signs come out as made-up letters even when the prompt asks for none. Blur them in the edit.

Count the arms and paws in every second before anyone sees it.

## Making it

    python ../story-in-one-run/story_run.py prompt.txt film.mp4 --ref front.png --ref back.png --secs 20

20 seconds at 480p, with sound.

## Credit

Made with Seedance 2.5 (ByteDance) on Replicate.
