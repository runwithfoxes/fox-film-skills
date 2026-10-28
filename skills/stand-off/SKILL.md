---
name: stand-off
description: A stand-off between your animated character and a real animal (or anyone) over one small thing, shot the way Sergio Leone shoots the duel at the end of The Good, the Bad and the Ugly - a wide, a shared look, then extreme close-ups of eyes, hands and the prize, cut faster, and one sudden move. One run of Seedance 2.5. Use when someone wants tension and a payoff with almost no action, or names Leone, a western duel or a stand-off.
---

# The stand-off

One Seedance 2.5 run of 20 seconds, written as a shot list with seconds, in a real place. Read `film-basics`,
`story-in-one-run` and `real-world` first: this uses the same run and the same two lines that make a place look real.

In Leone's duel nobody does much. Three men look at each other for about two and a half minutes, and the tension
comes from the cutting: wides, then eyes, hands and holsters, cut faster and faster, with the music building. That
suits a video model. A still close-up of an eye is about the easiest shot there is to generate, a locked-off camera
keeps a face steady, and the only fast action comes at the very end.

## The decisions

Make it a story you can follow on mute. One small prize, two characters who want it, a long stare, and both move at
once. Ours: the fox's last half sandwich on a seafront bench and a herring gull. The gull is faster.

Pick a prize the camera can't misread. "A paper cone of chips" with "one chip left" came back as a single fry
standing in a cup with a lid, which looks like an ice cream. A sandwich on its paper reads at a glance. Give its size
against the character's body, and say what it is never ("no cup, no cone, no chips").

Keep the camera still. "Locked off and never moves; it cuts straight between shots."

Put one character on the left of the frame and the other on the right, in every wide and medium shot, and keep them
there. Then each eye close-up gets a direction: the one on the left looks to the right of the frame, the one on the
right looks to the left. When the close-ups come fast, that is how the viewer knows whose eye it is.

Write the look as its own beat, before any close-up. In a closer shot, the character slowly turns their head to the
other, the other looks back, then looks down at the prize and up again. Without it the model keeps the character
facing the camera, and the eye close-up stares into the lens. "Stay completely still" stops the head as well as the
body, so write that the body stays put and only the head turns.

Give the other one something to want, on screen. The gull looking down at the sandwich is what tells the viewer what
the stare is about.

End on what was lost. Our fox's paw lands on the empty paper, the paper flaps in the wind, and he turns to stare at
the camera.

## The music

Describe it by its instruments, never by a film: "a lone whistled melody, a twangy electric guitar with reverb, a
jaw harp, one distant trumpet, sparse with long silences between the notes, building slowly from the first look to
the grab". Ask for "an original tune, never any existing film theme", and say where it stops ("stops dead the moment
the gull grabs the sandwich, and the last shot has only wind"). Listen to it before anyone else does, for the tune
coming out too close to the real one.

## The shot list

0-3 s, wide: the place, the character sitting, the other arrives. 3-6 s, medium: the head turn and the shared look.
6-8 s, the same medium: the other looks at the prize. Then the close-ups, each 1 to 1.5 s: an eye looking right, an
eye looking left, the prize, the first eye flicking down to it, a paw creeping towards it, a beak (or a hand)
opening. 16-17.5 s, medium: both move at once and the other wins. 17.5-20 s: hold on the character and what is left.

`example-seagull-prompt.txt` is the whole prompt for our film, as it was run.

## Cutting it faster in the edit

You can trim the close-ups so each is shorter than the last (1.5, 1.3, 1.0, 0.9, 0.7, 0.65 s) with ffmpeg's trim and
concat, for nothing. We kept the run as it came out: its close-ups already ran from about 1.6 s to about 1.0, and in
the trimmed version the music is chopped at every join. If you trim, cut the sound with the picture and listen to
every join.

## What to watch for

The model will not obey every line. Our gull landed on the seat, not the backrest. Check that what it changed still
tells the story.

Read every frame at eight frames a second: the head turn, which way each eye looks, the grab, the prop's size from
shot to shot. Count the arms and paws in every second.

## Making it

    python ../story-in-one-run/story_run.py prompt.txt film.mp4 --ref front.png --ref back.png --secs 20

20 seconds at 480p, with sound.

## Credit

The technique is Sergio Leone's, from the three-way duel in The Good, the Bad and the Ugly (1966). Made with
Seedance 2.5 (ByteDance) on Replicate.
