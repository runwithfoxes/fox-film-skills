---
name: festival-cut
description: Your character filmed as live-action documentary in a real place, then dressed as an award-winning film trailer, letterbox bars, festival laurels and a title that fades in as the character walks into the final poster. One Seedance 2 clip plus overlays made as web pages. Use when someone asks for a Cannes trailer, a festival cut, a film poster moment, or a premium documentary look.
---

# Festival cut

Your character walks toward the camera through a real, busy place, filmed like a documentary from across the street
on a long lens, with people and traffic crossing in front. Then the film dresses itself as a trailer: black bars top
and bottom, two laurels ("Winner" and "Official Selection") at three seconds, and the title and a line under it at
four seconds, at chest height, so the character walks into the finished poster.

Read `film-basics` first.

## The footage

Long-lens documentary words are what sell it as real:

    Photorealistic live-action documentary footage, long telephoto lens from across the street, compressed
    perspective, shallow depth of field. [your character description], realistic dense fur, individual strands
    catching the light, walks toward the camera through [a busy crossing in a big city at dusk]. Pedestrians and taxis
    pass between the camera and the character. [the clothing lock, word for word]. A completely bored unimpressed
    expression.

The people crossing between the lens and the character are what sell the realism hardest. Keep them as blurred shapes
in the foreground, never close enough to show a face.

"Realistic" goes on the fur, never on the character. The character keeps their designed face and gets real fur and
real light, which is the look of Paddington.

The character walks. Never a statue.

## The overlays

The overlays are web pages with a transparent background, saved as PNGs and laid over the film with ffmpeg.
`laurels.html` and `title.html` in this folder are the templates: edit the words, then

    python render_overlays.py              (needs Playwright: pip install playwright, then playwright install chromium)
    ./build.sh footage.mp4 out.mp4

`build.sh` adds the letterbox (2.35 to 1: bars 88 px high on a 1280 x 720 frame), fades the laurels in at 3.0
seconds and the title in at 4.0, and makes two films.

## Rules

The title appears once and stays. Nothing fades out and comes back.

No freeze frame here. A freeze only works cutting into a scene, and this is one long glide.

The title sits at chest height so the face is never covered.

Make two films every time. The straight one ends when the footage ends. The loop one holds the final poster frame
for 2.5 seconds, because anywhere that loops a video (a newsletter, a feed) eats a late title if the film restarts
the moment it appears.

Ours gave the fox a joke award, the Palme d'Orange. The templates carry placeholder words for you to change.

## Credit

The dress is the festival trailer, with laurels in the style of the Cannes Film Festival's. The Paddington films set
the bar for a designed character with real fur. Made with Seedance 2 (ByteDance) on Replicate; overlays drawn as web
pages and captured with Playwright; put together with ffmpeg.
