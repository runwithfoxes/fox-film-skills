---
name: hyperspeed
description: A character film where the camera flies at speed through a whole place, over a coast, through a town, across a rooftop, and lands on your character sitting perfectly still. The world moves, the character doesn't. One Seedance 2 clip. Use when someone asks for a hyperspeed shot, a drone fly-through that ends on a character, or a fast reveal.
---

# Hyperspeed

The camera does all the moving. It sweeps in from far away, fast, through the scene, and slows to a stop on your
character, who has not moved at all. The joke is the contrast: a huge, energetic camera move that arrives at someone
who could not care less.

Read `film-basics` first. It has the character set-up, the model call, the prices and the fixes for what goes wrong.

## The prompt

Start with your character description, word for word. Then the scene, written as a path the camera travels, from far
to near. Then anchor the character: where they sit, what they hold, and that they stay still. Then the move.

The shape that worked for us, with the character left out:

    [your character description]. [Where the character is: sitting on a low stone wall on a sunny rooftop terrace,
    holding a book against the chest with both hands]. The character stays completely still for the entire shot,
    a completely bored unimpressed expression. Cinematic sweeping camera movement: the camera starts high above
    [the wide place: a Mediterranean coastline with cliffs and a white town], flies fast and low over [what it passes:
    the sea, the rocks, the rooftops], and slows to a stop facing the character at eye level. Golden late afternoon
    light. Photorealistic environment.

Three things matter. The character is anchored to something solid (a wall, a chair, a ledge), or the model lets them
float. "Stays completely still" goes in plainly. The camera path is written in order, so the model has a route rather
than a list of places.

## Making it

    python ../film-basics/seedance_clip.py prompt.txt take1.mp4 --ref character.png --res 480p --secs 7 --aspect 16:9

Seven seconds gives the fly-through room to build. Look at the take, then make the 720p or 1080p version of the one
you like as a new take with the same prompt and seed.

## What to check

The landing is the shot. Look at the last two seconds frame by frame: the character's face, hands and size, and that
nothing has crept into their lap or hands. The fly-through can be loose; the landing cannot.

Leave room for a headline in the sky or the sea if the film is an ad, and decide where the words go before you write
the prompt, so the picture leaves space for them.

## Credit

The move is the drone and FPV fly-through that travel and property films use. Ours were made with Seedance 2 from
ByteDance, run on Replicate.
