---
layout: post
title: Video workflow for terrible AVCHD cameras
categories:
- Note
tags:
- Script
- Shell
- walkthrough
- AVCHD
- Quicktime
- video
status: publish
type: post
published: true
---

My friends and I in [Ensemble Evolution](ensevolution) had a great idea for our [Piteå Percussion Repertoire Festival](ensevolution/pages/percussion-repertoire-festival): “Let’s record ALL of the seminars and concerts!! We can just use the little camcorders from the school service centre.”

The result? About 140GB of messed up AVCHD MTS files and separate audio recordings. There are lots of problems with doing this much recording with these kind of cameras but for now I have a reasonable workflow for making something useful out of all the mess!

### Problem 1 – capturing from the camera

If you can plug the camera directly into a computer, iMovie or Final Cut Pro (7) can usually import all of the recordings which takes a LONG time. In our case, we used three cameras which needed to be returned so I copied the contents of their hard drives onto my external drive to deal with later. As it turns out, iMovie won’t import from the copied file systems and FCP will sometimes using Log and Transfer. One of the three cameras worked with FCP and the other two were no good. So I had to do something else!!

### Problem 2 – joining split MTS files

If you dive into the file system of the Sony cameras I was using, you find lots of huge .MTS files. These are the videos saved in AVCHD format! Unfortunately, each recording was split up into 2.12GB chunks… (FAT32 maximum filesize attack… hurr durr). Luckily, you can join them together using “cat” in terminal.

    compy:STREAM charles$ cat 00000.MTS 00001.MTS 00002.MTS > joined.MTS

(It’s easy to see where each scene ends, because the last chunk has a filesize of less than 2.12GB.)

Now, MTS chunks are back together as they were meant to be and they can be played back in VLC if you want to check them out. BUT, they won’t play in Quicktime so you can’t import them to iMovie or FCP the way they are.

### Problem 3 – fixing AVCHD for Quicktime

The MTS files are a perfectly normal video format (H.264 with AC3 sound) but Quicktime doesn’t know what to do with them. I use [Remux](http://www.nef.wh.uni-dortmund.de/~mt/remux/) (free) to repackage the MTS files into an mp4 file with AAC audio (since I’m replacing the audio later anyway...).

It’s not exactly quick to use remux on a 12GB file, but it’s a lot faster than transcoding into mp4 using Handbrake.

After remuxing the file you can play it in Quicktime and import into iMovie FCP or anything else easily! YAY!

Lots of the finished videos are going up on our [Vimeo page](http://vimeo.com/ensembleevolution) now!
