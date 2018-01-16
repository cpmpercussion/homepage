---
layout: post
title: Finding a good OSC library for iOS
categories:
- news
tags:
- OSC
- iOS
- programming
- research
status: publish
type: post
published: true
meta: {}
---

**Updates:**
 I found 
[F53OSC](http://github.com/Figure53/F53OSC), the simplest Objective-C OSC library I've come across. My fork - 
[MetatoneOSC](https://github.com/cpmpercussion/MetatoneOSC) - is updated for ARC and even easier to deal with - I'm going to use it from now on.


I've been trying to find a good OSC library to use in my iOS apps for some upcoming projects.


I would prefer to use a library with a neat objective-C api so that I don't have to mess with any C++, but there isn't an obvious winner (probably because the established C++ libraries are so good).


So here's a (probably incomplete) list of the OSC library options for iOS as of today.


##Objective-C libraries.



*[MetatoneOSC](https://github.com/cpmpercussion/MetatoneOSC): Fork of F53OSC - easiest to setup and use in this list.


*[F53OSC](http://github.com/Figure53/F53OSC): A nice little Objective-C library for sending, receiving, and parsing OSC messages.


*[bbosc](http://code.google.com/p/bbosc/) "a cocoa implementation of the OSC protocol"


*[vvosc](http://code.google.com/p/vvopensource/) part of vvopensource "frameworks for working with OSC and MIDI data on OS X"


*[CocoaOSC](https://github.com/danieldickison/CocoaOSC) "an Objective-C library for sending and receiving Open Sound Control 1.0"


##(popular) C++ libraries



*[oscpack](http://www.rossbencina.com/code/oscpack), a common favourite, basis for popular openFrameworks library ofxOSC, works well and looks like it might be refreshed soon.


*[liblo](http://liblo.sourceforge.net) "Lightweight OSC implementation" - used in a number of older OSC sending iOS apps.


*[oscpkt](http://gruntthepeon.free.fr/oscpkt/) "Ultra minimalistic OSC library".


*[oscpp](https://github.com/kaoskorobase/oscpp) "a header-only C++11 library for constructing and parsing OpenSoundControl packets"


One of the problems with the objective-C libraries seems to be the rapid changes in Xcode. Of the four options, CocoaOSC seems to be the best maintained but it is "incomplete" according the author. I've had best experience with bbosc, but not with the included Xcode project.


The long term solution might be to learn more about C++ and integrate one of the C++ libraries into my projects…


In order to do this, I'd have to setup a UDP socket in the Objective-C code and the established way to do that in iOS would be with...


*[CocoaAsyncSocket](https://github.com/robbiehanson/CocoaAsyncSocket) "easy-to-use and powerful asynchronous socket libraries for Mac and iOS"
