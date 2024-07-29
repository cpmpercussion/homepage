---
layout: post
title: Speedier saveFrame() in Processing
categories: []
tags: []
status: publish
type: post
published: true
description: "I've been writing some very simple Processing sketches to visualise logs of OSC messages for my Metatone project and I've wanted to turn these"
---

I've been writing some very simple Processing sketches to visualise logs of OSC messages for my 
Metatone project and I've wanted to turn these visualisations into videos to match up with the performances.

No problem right? Just use Processing's saveFrame() method at the end of every draw() loop and then use the "Movie Maker" tool on the resulting folder of image files.

Wrong - turns out that using saveframe to PNG images like so:

    saveFrame("######.png");

will process 1024x768 frames at about 7fps. So rendering a 12 minute performance at 30fps will take about 51 minutes + a long time for "Movie Maker" to stitch the images together. Not fun at all.

## Small improvement solution

The best solution I have so far is to use the TGA format for saveFrame:

    saveFrame("######.tga");

Which bumps the speed up to about 27fps. This is still extremely slow but it's a bit more bearable. A new problem is that Movie Maker doesn't work with TGA files (come on Processing! It's in the core library!). 

[More speed comparisons here in the Processing Forum](http://forum.processing.org/topic/saveframe-framerate-comparison-discussion-on-capturing-high-resolution-sketch-output).

A faster solution than Movie Maker is to use ffmpeg from the terminal to stitch the frames together. With [some help from the forums](http://forum.processing.org/topic/add-file-capture-sketch-output-threaded-for-less-slowdown) I've put together this one-liner to run in the folder of images:

    ffmpeg -f image2 -framerate 30 -i %06d.tga -vcodec qtrle -r 30  output.mov

The switches here tell FFMPEG to:

- read the input as a bunch of images
- that the input framerate should be 30fps
- that the input are of format 000001.tga, 000002.tga,
- that the video codec should be Quicktime "Animation" which works best for TGA files.
- that the output framerate should be 30fps
