---
layout: post
title: libpd - linking problems with Xcode 4.5
categories:
- note
tags:
- xcode
- iOS
- libpd
status: publish
type: post
published: true
meta: {}
---

Ran into another problem today with Xcode while updating 
[Snow Music](/apps) for iPhone 5's and found the solution 
[on CDN](http://createdigitalnoise.com/discussion/1603/libpd-linking-problems-on-xcode-4-5/p1). Turns out, Xcode 4.5 is causing 
all kinds of problems with linking static libraries, and the default build settings don't work with 
[libpd](http://libpd.cc).


The build fails with an error like:


>Undefined symbols for architecture armv7s:



And the solution is to go into Build Settings for the main application's target and change "Build Active Architecture Only" to YES in the Debug configuration (This matches how libpd is set up).


Check out 
[reakinator's explanation](http://createdigitalnoise.com/discussion/1603/libpd-linking-problems-on-xcode-4-5/p1).
