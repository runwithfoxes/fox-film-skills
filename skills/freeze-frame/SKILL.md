---
name: freeze-frame
description: The character introduction from Rounders, Trainspotting and Guy Ritchie films. The camera pushes in on your character mid-action, a white flash, the picture freezes with a title on it for two seconds, then the film carries on. One Seedance 2 clip plus a script that cuts the freeze. Use when someone asks for a freeze frame, a character intro, a Rounders or Snatch style title, or a film that stops on a line.
---

# Freeze frame

Your character is doing something. Mid-action, the picture flashes white for two frames and stops dead, with a short
title across it, held for two seconds. Then the title goes and the film moves again. It reads as the film
interrupting itself to tell you who this is.

Read `film-basics` first.

## The rules that make it work

Movement before the freeze is what makes it land. The character has to be doing something (flicking a chip, turning
their head, putting a card down) so the stop feels like an interruption. A freeze on a still picture is just a still.

It only works cutting into a scene. If the film is one long elegant glide, a freeze fights it. Fade the title over
the moving picture instead.

The title shows up with the freeze and leaves with it. When the picture moves again, the words are gone.

Sentence case, "Think in bets", never capitals, which read as shouting. No underline bar under it, which makes it look
like a subtitle.

Hold for 2 seconds. 1.5 feels rushed.

The flash is 2 frames of warm white (#F5F2EB), which reads as a film splice.

The freeze frame is the exact last frame of the first part, taken with `ffmpeg -sseof`, never a frame grabbed
separately, or the picture jumps.

Build it with ffmpeg, not a web page. A browser cannot freeze on an exact frame.

The title must not sit on the character's face. Look at the titled frame and move the title into empty background if
it does.

## Making it

1. Make the clip. Write the scene with an action in it and a slow push in:

        [your character description]. Sitting upright in a chair at a poker table in a smoky back room, thin smoke
        haze hanging in the air, a single lamp overhead. The character flicks a poker chip with one paw, card backs
        facing camera, then slowly glances up with a completely bored unimpressed expression. The camera pushes in
        slowly from a medium shot to a close-up.

        python ../film-basics/seedance_clip.py prompt.txt clip.mp4 --ref character.png --secs 5

   "Thin smoke haze hanging in the air" keeps the smoke in the air; without "in the air" it rises off the table.
   "Sitting upright" not "slouched", which the model reads as lying down.

2. Pick the freeze point, the second where the action peaks, by stepping through the clip.

3. Cut it:

        python freeze_frame.py clip.mp4 2.4 "Think in bets" out.mp4 --font Anton-Regular.ttf

   The script trims the first part, takes its exact last frame, draws the title on it with Pillow (a heavy condensed
   face at 110 px with a soft shadow; we use Anton, free from Google Fonts), makes the 2 frame flash and the 2 second
   hold, and joins the four pieces. It also saves `freeze_plain.png` and `freeze_titled.png` so you can check the
   title is clear of the face.

## Credit

We call it Rounders, after the poker film that set the mood for our first one. The device itself is the
freeze-frame character introduction that Danny Boyle's Trainspotting and Guy Ritchie's Lock, Stock and Snatch made
famous. Made with Seedance 2 (ByteDance) on
Replicate, cut with ffmpeg, titled with Pillow.
