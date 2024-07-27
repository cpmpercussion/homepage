---
layout: post
title: iOS networked metronome proof of concept
categories:
- news
- note
tags:
- iOS
- Pure Data
- RjDj
- network
- Pd
- metronome
- work in progress
status: publish
type: post
published: true
meta: {}
description: "Somebody asked me whether it was possible to have a metronome synchronised between a bunch of iPhones... it turns out it is! I made this little demo with"
---

Somebody asked me whether it was possible to have a metronome synchronised between a bunch of iPhones... it turns out it is!

<!-- https://vimeo.com/21969515 -->
{% include vimeoPlayer.html id="21969515" %}

I made this little demo with Pd and RjDj, the computer controls the tempo and sends a message on each beat to the iOS devices which beep and flash a visual cue accordingly.

It works pretty well, but there are a few problems that I'd have to address in making it ready for a performance... first of all, it's annoying to set up the IP of each iOS device in Pd, but the netsend object doesn't seem to support UDP broadcast. Secondly, there's some occasional problems with latency messing up the nice steady rhythm on the devices. Experience tells me this could get worse in a performance venue with lots of wires and walls and things to mess up the Wifi signal. I'm sure I could think of something to fix it.

I wonder if it would be better to make a production version as a native iOS app? RjDj is probably easiest from a distribution standpoint, but it's a complex app to accomplish a simple task...
