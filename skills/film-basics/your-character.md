# Making your character

Our films use the Grumpy Fox. He is ours and he is not in this repo: not his reference picture, not his description,
not his prompts. You make your own once, and every skill here uses it.

## 1. The fixed description

Write one paragraph that a stranger could draw from. Name the things that must never change, in this order: what the
character is and the style it is drawn in, the head, the eyes, the mouth and its usual expression, the build, the
colours, and the clothes. Then add the two lines every film needs: "compact small frame" and "exactly two arms and two
legs".

A made-up example, to show the shape (not ours):

    Mabel, a stylised cartoon badger rendered with realistic fur texture: a long narrow head with a white stripe from
    nose to crown, small black eyes that are always half closed, a straight unimpressed mouth, a compact small frame,
    exactly two arms and two legs, grey fur with a white chest. She wears a mustard yellow raincoat, dark green
    full-length trousers that reach her ankles and black wellington boots, the same clothes throughout the entire shot.

Save it as `character.txt`. Every prompt starts with it, word for word.

## 2. The reference picture

Make it with Seedream from the description, then pick the best of four:

    python seedream_still.py character-sheet.txt character.png --aspect 1:1

where `character-sheet.txt` is the description followed by: "Standing, whole body in frame, three-quarter view
toward the camera, plain pure white background, soft even studio light, no shadow, no props, no text."

Check it before you use it: count the arms and legs, look at the hands, and make sure the clothes match the words.
Save it as RGB with no transparency (a transparent cut-out confuses the video model). This one file is the reference
for every clip from now on.

## 3. Keep it the same

Never regenerate the reference picture halfway through a set of films. Never reword the description between clips of
one film. If the character drifts, change the scene words, the energy words or the camera words, not the character.

If you have already designed the character elsewhere (an illustration, a mascot, a 3D model), use a clean render of
it on white as the reference picture and write the description from it.
