---
name: camcorder
description: Your character filmed at night on an old camcorder, doing something they shouldn't, like spray-painting their own logo on a wall. Grainy, shaky, an amber date stamp in the corner and a red REC dot. After Exit Through the Gift Shop. One Seedance 2 clip plus a camcorder look added in ffmpeg. Use when someone asks for camcorder footage, a street art film, a night-time guerrilla film, or a found-footage look.
---

# Camcorder

Someone is quietly filming your character at work at night: a back street, a pool of orange streetlight, steam from
a vent, and your character spray-painting their own logo on a brick wall. Once, they glance over their shoulder at
the camera, bored, and carry on. The footage looks like a camcorder from twenty years ago.

The best version of this has the character making their own fame with their own hands, which is why ours paints his
own fox on the wall.

Read `film-basics` first.

## Lock the character before anything else

This is the format where the character drifts most. Night light, a side-on pose, an action and the word "realistic"
together make the model swap your character for a real animal. Two things stop it.

Put your full character description in, with "rendered with realistic fur texture" (or skin, or whatever your
character has) so that "realistic" only touches the surface.

Keep the face three-quarter toward the camera while they work: "angled so the face stays three-quarter toward the
camera". A pure side view is where it goes wrong.

Check the character on the first take before you judge anything else.

## The footage

    Handheld camcorder footage filmed at night, lo-fi documentary video, grainy low light, filmed from a few metres
    back. [your character description, rendered with realistic fur texture], spray-painting [a simple bright logo
    shape] on a weathered brick wall, a spray can in one hand, angled so the face stays three-quarter toward the
    camera. They glance once over the shoulder toward the camera with a completely bored unimpressed expression, then
    go back to painting. A pool of orange streetlight, parked cars, faint steam from a vent. [the clothing lock].

The model ignored "hood up" on both our takes. Hood down shows the ears, which suits a character with ears anyway.

The model shoots too clean. Don't fight it in the prompt; the camcorder look goes on afterwards.

## The camcorder look

    python camcorder_ui.py "11:52 PM" "JUL. 3 2026"
    ./build.sh footage.mp4 out.mp4

`camcorder_ui.py` draws the amber date stamp bottom left and a red REC dot top right as one transparent PNG.
`build.sh` does the rest in one ffmpeg pass: a hand shake (two sine waves per axis), more contrast and less colour,
moving grain, a vignette, then the stamp on top.

## Finishing

No logo, no end card. A deadpan caption ("He doesn't wait to be talked about."). Found footage dies the moment it is
dressed up.

## Credit

After Exit Through the Gift Shop (2010), the street art documentary credited to Banksy. Made with Seedance 2
(ByteDance) on Replicate; the camcorder look built in ffmpeg and Pillow.
