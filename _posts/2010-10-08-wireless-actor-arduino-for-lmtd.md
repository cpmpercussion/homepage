---
layout: post
title: Wireless Actor Arduino for LMTD.
categories: []
tags: []
status: publish
type: post
published: true
meta: {}
---

At NIME someone asked if I had tried using Xbee with my wearable Arduino setup for Last Man to Die. I hadn't then, but after today.... now I have!

I bought the Xbee starter set from sparkfun after failed attempts to get a WiFi shield to speak OSC and tonight was our first show with an unwired actor. It really made a huge difference to the performance, Hanna's movement was immediately more free and interesting. 

The setup is Wii nunchuck + buzzing motors + LEDs --> Arduino --> xBee ~~ xBee --> USB xBee explorer (Serial interface) --> processing --> OSC --> LMTD! 

I had a bit of a false start with this idea by overthinking the xBees and trying to use the xBee library for Processing. Maybe this is really for the xBee 2.5 or something... I have the cheapest ones and they work just fine with the serial library and no special treatment in my point to point setup. 

This is waay more complicated that using a wire... Mainly because we need a whole computer just to run Processing. My next plan is to use ANOTHER Arduino to receive the xBee signals, translate to OSC and send over an Ethernet cable which would be quite elegant. 

I can see an Arduino Pro Mini in my future... The ultimate minimal arduino! So cool!

[![](http://posterous.com/getfile/files.posterous.com/charlesmartin/T0IkZttk2RPE4BwBA1C0HIjl60dpxkLwB2jKH0FdLNGEUDUBZVFrJcthqgvk/photo_1.jpg.scaled.500.jpg)](http://posterous.com/getfile/files.posterous.com/charlesmartin/lnFEsiVds13avt1HNspVIOPZJOWf2oqmDd9joelObQufyxQOyPDqXsFNle2v/photo_1.jpg.scaled.1000.jpg) 
[![](http://posterous.com/getfile/files.posterous.com/charlesmartin/E9mcoWbKgSqJaK6viJ3DcvAwtmcfnd8isDZCusgNfQpcdZahj7yA7e8XxulY/photo_2.jpg.scaled.500.jpg)](http://posterous.com/getfile/files.posterous.com/charlesmartin/oPWitVnO3FDCsHdrVIDLFsLwy5v6rpMfCizqJpSBMe4Nbrdt0m7LjtAmvGdO/photo_2.jpg.scaled.1000.jpg) 
[![](http://posterous.com/getfile/files.posterous.com/charlesmartin/LYGNF9YtyTrlyHHc9S6Zz8LlMa6Mr0rJYIpyNGZU9Nq3bhBS4VaG3Gqi9Upd/photo_3.jpg.scaled.500.jpg)](http://posterous.com/getfile/files.posterous.com/charlesmartin/tpy161ydvL4CPoULe9ywhYhFxLCvuT39yb8FnKzkZcL0ny43bLcSgBaPQaXZ/photo_3.jpg.scaled.1000.jpg)

[See and download the full gallery on posterous](http://charlesmartin.posterous.com/wireless-actor-arduino-for-lmtd) 
[Posted via email](http://posterous.com)  from 
[charles martin](http://charlesmartin.posterous.com/wireless-actor-arduino-for-lmtd)
