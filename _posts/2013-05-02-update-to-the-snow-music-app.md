---
layout: post
title: Update to the Snow Music app
categories:
- news
tags:
- iOS
- iPad
- Snow Music
- libpd
status: publish
type: post
published: true
---

I pushed an update out to the Snow Music app on the iTunes store a few weeks ago but forgot to post it!

Long story short:

* The app now has Core MIDI support for external MIDI accessories - the MIDI device will trigger the bell and cymbal sounds!
* The app supports iPhone 5 screen sizes properly
* It's still free and still fun to improvise with!

[Go check it out!](https://itunes.apple.com/us/app/snow-music/id560849530?mt=8)

The app still uses [libpd](http://libpd.cc) for driving the Pure Data sound engine and now uses [PGMidi](https://github.com/petegoodliffe/PGMidi) to help with CoreMIDI.
