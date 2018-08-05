---
layout: post
title: cool things at NIME2011
categories:
- News
tags:
- NIME
- travel
- Oslo
- Flickr
- computer music
- HCI
- conference
- Strike On Stage
status: publish
type: post
published: true
meta: {}
---

I went to [NIME2011](http://www.nime2011.org/) in Oslo a few weeks ago, it was a really fun opportunity to catch up with some contacts in computer music and interactive media and to see what’s going on in the research world at the moment. Here’s a (non-exhaustive) list of things that stuck in my mind.

## Satellite CCRMA.

![Satellite CCRMA](http://farm6.static.flickr.com/5034/5885840133_f1f9af3661.jpg)Two CCRMA-lites (Edgar Berdahl and Wendy Ju) presented their [ideas](https://ccrma.stanford.edu/~eberdahl/Satellite/) about using [Beagleboard](http://beagleboard.org/) (tiny computers on a board) to teach interface design. Broadly, they thought that the longevity of DIY music interfaces and other physical-computing projects is really held back by being tethered to a computer that is often used for other tasks. Their answer is to add a Beagleboard to the Arduinos they already use to create a self-contained system for running sensors, making and processing sounds and even doing video output and computer vision.

I was kind of skeptical about the idea until their talk… the thing which really got me was they’ve setup a Linux distribution for the Beagleboard which can run Pd patches or any other common computer music language. It seems like they’ve really got the whole process for setting up the board with a patch worked out and there were a few projects in the demo sessions from their class.

Now it’s just a matter of time before I crack and buy one of those boards...

I realised watching their talk that CCRMA is really a special place for this kind of stuff to happen and develop REALLY quickly. The two presenters clearly have a lot of passion for making it happen and must have put a huge amount of work into getting the kinks out of their system, the institution supports them figuring it all out and by the time NIME rolls around they’ve taught one class using this technology and are preparing a new version for the summer course and next semester’s students. I think it’s very rare in this field to have a place where this stuff can proceed so rapidly… great teachers, supportive institution and lots of students to test it on.

## HIDUINO – MIDI enabled firmware for Arduino UNO

Some really cool [work](http://mtiid.calarts.edu/research/hiduino)[here](http://code.google.com/p/hiduino/). They’ve written a firmware for the Arduino UNO so that it can work as a driverless MIDI interface (and maybe one day to send OSC as well through network over USB!!). This will make a big difference in the quality of work that Arduino hackers can produce. It totally sucks to mess around with software to convert serial to MIDI, much easier and more elegant to go straight to the useful protocol (yes, often MIDI is more useful that OSC...).

## “The Shells” by [Alex Nowitz](http://www.nowitz.de/)

![The shells](http://farm7.static.flickr.com/6004/5886405510_7d55e5a38a.jpg)A really compelling performance by this guy who sings and controls a computer using handheld controllers in the STEIM “The Hands” style. The controllers themselves had a really cute stand that also had a tiny display connected to his Mac Mini (offstage). It’s bizarre and embarrassing how refreshing it is to see people really getting deep into interface design that doesn’t require a laptop on stage… just moving the mac mini offstage and having a tiny display makes a huge difference to the potential for stage presence.

## Sergi Jordà

Sergi Jordà (of [Reactable](http://www.reactable.com/) fame) gave a great keynote presentation discussing his career in art, HCI and now product design. One comment he made about Reactable that struck me was (something like) “after the first paper, we haven’t been to NIME, because we’ve been focussing on making the product better, not creating new interfaces to write papers about”. From what I can see, NIME gets a huge number of papers about prototype style interfaces, instruments and performances and many fewer papers about really mature, successful and high quality projects. I think there’s probably an interesting story to tell about how a research project Reactable becomes a system that you can ship off to a museum and trust that it will actually work when set up by an amateur.

I also noticed that his earlier work in cross-artform performance with networked interfaces and interactive elements was kind of similar to my own work with [Last Man to Die](http://www.lastmantodie.net/). Except his was [CRAZY SCARY](http://www.youtube.com/watch?v=Wabsr8Eouts).

## Strike on Stage

![SOS](http://farm6.static.flickr.com/5158/5886406746_e9576e5b2a.jpg)Chi-Hsia and I gave a demo of our [Strike on Stage](https://charles-martin.squarespace.com/strikeonstage) system which is about a year old now. I was actually a bit surprised by how good the reception was, lots of people asking about the details and interested in how the performance works. I thought that the NIME crowd might have been a bit fickle about older presentations especially since we actually performed the piece at NIME2010 in Sydney. I think the demo is actually MORE fulfilling than more prestigious paper presentations because you can physically and musically explain design decisions and how everything works.
