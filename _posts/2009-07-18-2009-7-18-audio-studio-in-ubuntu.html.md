---
layout: post
title: Audio Studio in Ubuntu
categories: []
tags:
- computer music
- jack
- supercollider
- ubuntu
status: publish
type: post
published: true
meta: {}
---

I'm going to use an Ubuntu system to do some audio projects, so I wanted to figure out how to use Jack and some other applications that come with Ubuntu Studio.

Jack Resources:

[Ubuntu Wiki - preparing a studio computer](https://help.ubuntu.com/community/UbuntuStudioPreparation) - includes help on realtime settings

[Ubuntu Wiki - Howto Jack Configuration](https://help.ubuntu.com/community/HowToJACKConfiguration)

[Ubustu - How to configure Jack](http://www.ubustu.com/globe/2007/05/29/how-to-configure-jack-in-ubuntu-studio/)

[Linux Journal article about Ubuntu Studio setup](http://www.linuxjournal.com/content/judgement-day-studio-dave-tests-ubuntu-studio-904)Supercollider resources:

[Tutorial for installing SuperCollider on Ubuntu](http://artfwo.blogspot.com/2008/05/supercollider-for-human-beings.html)
[Apt Repository for Supercollider](https://launchpad.net/%7Esupercollider/+archive/ppa)
[Using the SuperCollider plugin for the gedit text editor](http://artfwo.googlepages.com/sced)
[SuperCollider swiki](http://swiki.hfbk-hamburg.de:8888/MusicTechnology/6)

*update* My computer won't boot with Ubuntu Studio 9.04's realtime kernel (linux-rt). Other people have a 
[similar problem](https://bugs.launchpad.net/ubuntu/+source/linux-rt/+bug/366352). Discussion threads have had success with a custom kernel build that I will try out. 
[Instructions here](https://bugs.launchpad.net/ubuntu/+source/linux-rt/+bug/290498/comments/51).
