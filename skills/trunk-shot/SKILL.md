---
name: trunk-shot
description: Quentin Tarantino's trunk shot. The camera sits inside a car boot looking up, the lid opens on a black screen, and your character is standing there looking down into it, unimpressed, against a hard blue desert sky. A Seedream still, then Kling animating from a black frame to that still. Use when someone asks for a Tarantino shot, a trunk or boot shot, a reveal from black, or a Pulp Fiction style opening.
---

# Trunk shot (Tarantino)

The screen is black. The boot opens and light floods in, and there is your character, in a black suit, hands on the
rim, looking down into the boot as if you are the problem. Blue sky, empty desert road behind. Ours had Paul standing
beside the fox.

It is built differently from the other films here. A video model cannot start inside a closed boot, and it cannot
make a black frame. So the end picture is made first as a still, the black frame is made in code, and a model that
takes a first and a last frame animates the opening between them.

Read `film-basics` first.

## 1. The still

Describe what is seen, never where the camera is, or Seedream draws a camera into the scene:

    The inside of an open car boot fills the edges of the frame: the dark lid edge across the top, carpet at the
    bottom, dark walls left and right, framing a bright rectangle of sky. [your character description], in a black
    suit, white shirt and black tie, stands at the back of the car, leaning over and looking straight down into the
    boot, both hands resting on the rim. A cold, completely unimpressed expression. Wide angle, low from below chin
    height. Blue sky, blinding desert sun, a dusty empty highway behind. 35mm film, heavy grain, warm amber tint,
    slightly overexposed highlights, a gritty 1990s crime film look.

    python ../film-basics/seedream_still.py still.txt end.png --ref character.png --aspect 16:9

To put a real person in it as well, add their photo as a second `--ref` and describe them in the prompt. Only ever
with that person's say-so.

Check the still before you animate it: hands on the rim, the count of hands and arms, and the face.

## 2. The black frame

    python black.py end.png start.png

`black.py` makes a near-black frame the same size as the still. Seedream cannot make "the inside of a closed boot",
so this frame is made in code.

## 3. The opening

Kling takes a start picture and an end picture and moves between them. Its prompt is about the movement only. It can
see the pictures, so don't describe the character again:

    The car boot lid lifts open from darkness and bright daylight floods in, revealing the figure leaning over the
    boot looking down. The figure stays still, hands do not lift from the rim. The expression stays cold and
    unimpressed throughout, no smiling. The figure holds the pose.

    python kling_reveal.py prompt.txt start.png end.png out.mp4

Kling's rules, from our takes. One movement that peaks and holds, never a list of actions. Lock what touches
something: "hands do not lift from the rim", "feet do not move". End with "holds the pose". Two or three sentences,
no more. Put the expression in plainly every time, because the model drifts to a smile.

## Other sizes

A landscape shot with dark edges goes into a vertical frame well: scale it to the width, centre it, and fill above
and below with black. The dark boot walls blend into the bars.

## Credit

The shot is Quentin Tarantino's, from Reservoir Dogs and Pulp Fiction, and it has become his signature. Still made
with Seedream 4.5 (ByteDance) on Replicate. The opening made with Kling 2.6 (Kuaishou) on fal.ai, which was the
version we used in April 2026; check fal.ai for the current version and its price before you run it.
