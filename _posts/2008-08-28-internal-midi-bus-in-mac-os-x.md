---
layout: post
title: Internal MIDI Bus in Mac OS X
categories: []
tags:
- Mac OS X
- midi
status: publish
type: post
published: true
meta: {}
description: "Suppose that you have a Pd program which outputs midi data that you want Ableton Live to receive. In Mac OS X you can create an internal midi bus and then"
---

![]({{ site.baseurl }}/assets/blogger/IAC-audio-midi-setup.jpg)

Suppose that you have a Pd program which outputs midi data that you want Ableton Live to receive. In Mac OS X you can create an internal midi bus and then set it as the output for Pd and the input for Live! First, go into Applications/Utilities/Audio Midi Setup. The IAC Driver (Inter Application Connection or something like that?) is Mac OS X's internal midi device designed for this very purpose! Double click on the icon to look at its properties.

![]({{ site.baseurl }}/assets/blogger/IACDriver.png)

Now in the Ports section you can press "+" to add a new port, you can rename it if you like. Finally make sure that the "Device is online" checkbox is selected.

Now just set the midi output in Pd to the new IAC bus and activate track and remote (or whatever) in Live. All done!
