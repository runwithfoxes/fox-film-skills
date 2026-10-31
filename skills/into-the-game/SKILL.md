---
name: into-the-game
description: A short film where your character goes from a real place into a video game and becomes a chunky pixel character, in one run of Seedance 2.5. The game level is drawn in code first, so the model has an exact picture to copy. Use when someone wants a character to move from live action into pixel art, a video game, an arcade or a retro game.
---

# From the real world into a video game

Your character stands in a real place, the world breaks into big square blocks, and they end up as a pixel character in a game. Our film is 12 seconds: the fox drops a coin into a cabinet in a real 1984 arcade, the room starts to break into red blocks, and on a game screen he taps a block and gets one coin back.

Read `film-basics` first for the character description and the reference pictures, and `story-in-one-run` for how to run a whole film in one go.

## Draw the game first

Don't ask the model for pixel art in words alone. Draw the level as a picture and give it that.

Work on a coarse grid. Ours is 213 by 120, with every pixel blown up six times to 1278 by 720. Use flat colours and hard edges, with no gradients. Put your character in a game world, with ground, blocks, coins and hearts, because a character on a white page looks like an illustration. `draw_level.py` draws ours, and changing the look is a matter of changing its list of colours.

Trace your character from their reference picture. Read the points off the picture, as `sprite.py` does, and don't draw them from memory. There is very little room at that size, and a character drawn from memory stops being your character. We drew the head a bit bigger than life, as game characters are, which gives the face room. Then place the eyes, nose and mouth by hand, one pixel at a time. Those few pixels hold the expression, so compare them with the reference at full size.

Keep the small things that make the character theirs. For our fox that is the half-closed eyes, the big ears, the hoodie strings and pocket, the turned-up jeans and the cream tip on the tail. The fox in the film is 72 pixels tall. A fox of 46 pixels drawn from memory didn't look like ours.

## The prompt

Give the model two reference pictures, your character and the level, and no first or last frame. Locking the last frame leaves no room for the action.

Write it as a shot list with seconds, as in `story-in-one-run`, then add these.

CHARACTER. Say "rendered with realistic fur" if your character is an animal. The word realistic should only apply to the fur, or you may get a real animal. Say how many arms and paws. Say they are bored, or whatever they are, and never surprised, if the joke needs them not to react.

LOOK. If you want the look of a film or show, write out the choices that make it: the film stock, the lens, what the light comes from, the two main colours, the year.

THE CHANGE. Write it as a route. Say where the blocks start and which way they travel: "starting at the screen and travelling outward across the cabinet, the carpet and the walls". Then the character, "from their feet to their ears".

THE GAME. Name what is in the level so the model sticks to it, and ban its habits: "flat colours, big square pixels, hard edges, no blur, no smooth shading". Give it one action. Five seconds holds one idea.

SOUND. Ask for the sound to change when the picture does.

## What to check

Compare each frame with the next to find cuts, and open the frames either side of any jump. A sheet of stills can hide a cut. Our prompt said "never cuts" and the model still made a hard cut to the game at 7.2 seconds, so the room doesn't finish turning on screen and the fox changes direction in the cut. It works as a cut, but it isn't one shot.

We don't know why it cut. Our guess, from one take, is the words "seen on an old CRT screen", which describe a new viewpoint. If you want one shot, try leaving that out and tell us how it goes.

Describe a take from the take, never from the prompt. We asked for the lights to flicker and go out one after another, and they went out together.

Count the arms, paws and feet, and read the character's face in both halves. The model may move things in your level, as it moved our bricks. It also wrote on the signs in the room in spite of "no words", so blur them or accept them.

Each run comes out differently, so a sharper version is a new film.

## Credit

The way of working, drawing something, looking at it and fixing it, is the one Hugo Duprez sets out in [How to make (good) pixel art effects with Claude](https://www.spritefusion.com/blog/how-to-make-good-pixel-art-effects-with-claude).
