---
name: film-basics
description: The shared base for every character film skill in this repo. How to set up your own character so it stays the same in every shot, how to call Seedance 2 and Seedream on Replicate, what a clip costs, and what these models do wrong and how to stop it. Use it before any of the format skills (hyperspeed, freeze-frame, one-take, waterslide, character-walk, festival-cut, phone-witness, camcorder, green-studio, trunk-shot), or when someone asks how to keep an AI video character consistent.
---

# Film basics

Every format in this repo puts one recurring character into a short film made with a video model. This file is what
they all share. Read it first, then read the format's own SKILL.md.

## What you need

A Replicate account and its key in the environment as `REPLICATE_API_TOKEN`. Python 3 with `requests`. ffmpeg.
Pillow for any title or overlay drawn on a frame. The trunk shot also uses Kling on fal.ai, with its key as `FAL_KEY`.

Never paste a key into a prompt, a script or a file in a folder you might share. Read it from the environment.

## Your character

The model has to see the same character in every clip, or it drifts: the face changes, the body grows, the clothes
swap between shots. Two things hold it.

The first is one reference picture. Make it once: your character standing, whole body, facing three-quarters to
camera, on a plain white background, saved as RGB with no transparency. Pass it to the model as a reference, and pass
the same file every time. `your-character.md` walks through making it.

The second is a fixed description, a paragraph that names what must never change: the head, the eyes, the mouth, the
build, the colours, and the clothes. Write it once, then paste it word for word into every prompt. Do not reword it
between clips. The words you keep the same are what keep the character the same.

## Calling the models

`seedance_clip.py` makes one clip with Seedance 2 (`bytedance/seedance-2.0` on Replicate):

    python seedance_clip.py prompt.txt out.mp4 --ref character.png --res 480p --secs 5 --aspect 16:9 --seed 11

`--first` and `--last` instead of `--ref` make a clip that starts on one picture and ends on another. That is how
two clips join without a cut, and how a film loops.

`seedream_still.py` makes one still with Seedream 4.5 (`bytedance/seedream-4.5`), for formats that start from a
picture:

    python seedream_still.py prompt.txt out.png --ref character.png --aspect 16:9

Both log what they spent to `spend.txt` beside the output.

## What it costs

Seedance 2 on Replicate is priced by the second of film. When we checked in September 2026 it was 8 cents a second at
480p (40 cents for a 5 second test clip), 18 cents at 720p and 45 cents at 1080p. Check the model's page on Replicate
before you run anything, because prices change. Test at 480p. A 720p clip of the same prompt is a new take, not the
same take made sharper. Allow five or six takes for a new idea.

## What these models do wrong, and the words that stop it

Each of these came from a take of ours that went wrong in 2026.

Seedance makes a character bigger and heavier once it is clothed and upright. "Compact small frame" in every prompt
holds the size. If it still comes back stocky, add "slim build, narrow shoulders" rather than taking clothes off.

An animal character with no clothes comes back as a real animal on all fours. Clothing keeps it human. Say "walks
upright on two legs like a person for the entire shot, never on all fours" whenever it moves.

Energy words drive the face more than any description of the face. "Aggressive stare" and "quickly turns" make anger.
For a bored or deadpan character write "completely bored, unimpressed expression", "total indifference", "casually",
"slowly glances".

"Slouched" is read as lying down. Write "sitting upright in a chair".

Props come back the wrong way round unless you say which side faces the lens: "card backs facing camera".

The first second of most clips is the model setting the scene, with arms pulling up and the body settling. Trim it.

A character drifts or vanishes after about seven seconds. Make 5 second clips and cut them together.

Lock the clothes. Use the same clothing words in every prompt for one film, down to "full-length dark blue jeans that
reach down to his ankles, the same full-length jeans throughout the entire shot". Without that, jeans turn into
shorts between takes.

The word "realistic" changes the species. Put it on the fur, the skin or the light, never on the character itself.
"Rendered with realistic fur texture" keeps your character. "A realistic fox" gets you a real one.

People near the camera look generated. Keep people far back, small, out of focus, seen from behind or side-on, with
no faces visible, and nobody walking between the lens and your character unless the format needs it.

Pass the character picture as `reference_images` (a list), not `image`. `image` locks the first frame and bleeds its
white background into the scene. The one exception is `--first` and `--last`, where the first frame is meant to be
locked.

Seedream draws a camera into the scene if you describe where the camera is. Describe what is seen, not where the lens
stands.

Seedream cannot make a near-black frame. Make it in code.

## Before anyone sees a take

Count the arms, hands, legs and feet out loud on every take. Throw away any with a third hand. Then lay out every
frame of the film at a size you can read and look at it yourself: the face, the clothes, the size, the hands. A
contact sheet of every third frame is not enough, and a script passing is not the same as the film being right.

    ffmpeg -i take.mp4 -vf "fps=6,scale=320:-2,tile=6x5" -frames:v 1 sheet.png

## Finishing

Every clip that goes into one film is re-encoded the same way before it is joined: `libx264`, `-crf 18`,
`yuv420p`, 24 fps, no sound (`-an`). If ffmpeg complains about an odd height, add
`scale=trunc(iw/2)*2:trunc(ih/2)*2`.

LinkedIn's encoder stutters on the first frame of an upload. Put half a second of the first frame, frozen, in front,
and force a key frame at zero:

    ffmpeg -loop 1 -i first.png -t 0.5 -r 24 -pix_fmt yuv420p freeze.mp4
    ffmpeg -f concat -safe 0 -i list.txt -c:v libx264 -crf 18 -force_key_frames 0 out.mp4

ffmpeg from Homebrew has no `drawtext` filter. Draw any words with Pillow onto a PNG and lay the PNG over the film.
