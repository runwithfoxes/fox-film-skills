---
name: phone-witness
description: Your character caught on a stranger's phone, seen through the phone camera's own screen, a red REC dot, a counting timer, a tap-to-focus box, the shutter button, and a shaky hand. Vertical 9:16, made for Stories and Reels. One Seedance 2 clip plus a viewfinder laid over it. Use when someone asks for phone footage, a bystander video, a "caught on camera" film, or vertical found footage.
---

# Phone witness

Somebody in the street saw your character and got their phone out. The film is what their phone recorded: vertical,
held at waist height and tilted up, a bit shaky, people crossing in front, and the phone's camera screen on top.
Halfway through, the character notices the phone and gives it one slow, bored look.

It is the most believed kind of footage there is, because everyone has filmed something this way.

Read `film-basics` first.

## The footage

    Vertical smartphone video filmed by a pedestrian, phone held at waist height tilting slightly upward.
    [your character description] walks past at a three-quarter angle through [a crowded city square at dusk].
    Mid-walk the character notices the phone filming them and gives it one slow bored unimpressed glance, then looks
    away with total indifference and keeps walking. Pedestrians pass between the phone and the character, some turning
    to look. [the clothing lock, word for word].

The glance is the shot. In a documentary the character ignores the camera; here, one bored look at the lens is what
makes it witness footage. Never more than one, and never performing for it.

The character walks past at an angle, not straight at the lens. Real people film from below eye level.

Keep what the model gives you for free. It often adds other people filming the character on their own phones, and
the filmer's thumb blurred over a corner of the lens. Those are the format.

The model makes smooth footage no matter how hard you ask for shake. Do not spend takes on it; the shake goes on
afterwards.

## The viewfinder

`phone_ui.html` is the phone screen (REC dot, battery, zoom buttons with 1x lit, the shutter) and `focus_box.html`
is the yellow focus square and exposure sun. Both are 720 x 1280 transparent pages. Put the focus box where the
character's face will be about 1.5 seconds in. It stays where it was tapped, and the character walks into it, which
is how a real phone behaves.

Capture them, draw the timer, then build:

    python ../festival-cut/render_overlays.py phone_ui.html focus_box.html
    python timer.py 5
    ./build.sh footage.mp4 out.mp4

`timer.py` draws the counting "0:00", "0:01" and so on beside the REC dot as PNGs, one for each second, because
ffmpeg from Homebrew has no text filter.

`build.sh` scales the footage to 720 x 1280, adds the shake, then lays the screen on top. The shake is two sine waves
of different speeds on each axis, which reads as a human hand:

    crop=684:1216:18+11*sin(t*12.7)+6*sin(t*33):32+9*sin(t*8.3)+5*cos(t*23),scale=720:1280

The screen goes on after the shake and stays still while the world shakes. Shake the screen and it stops looking
like a phone.

## Finishing

No logo, no end card, and a deadpan caption rather than a headline ("New York, yesterday."). Dress found footage up
and nobody believes it was found.

## Credit

The look is the iPhone camera screen, as everyone has seen it. Made with Seedance 2 (ByteDance) on Replicate; the
screen drawn as web pages and captured with Playwright; put together with ffmpeg.
