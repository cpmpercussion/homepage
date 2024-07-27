---
layout: post
title: Duet for Vibraphone and Computer
categories: []
tags:
- Ableton Live
- Pd
- computer music
- duetforvibraphoneandcomputer
- pure data
- vibraphone
status: publish
type: post
published: true
meta: {}
description: "Performers who use computers to make music often spend a lot of time creating and learning to play new instruments. As a percussionist incorporating"
---

![Vibes, computer, and gongs for Cognition 2]({{ site.baseurl }}/assets/blogger/cognition2-setup.jpg)
![Computer setup for Cognition 2]({{ site.baseurl }}/assets/blogger/cognition2-screenshot.png)

Performers who use computers to make music often spend a lot of time creating and learning to play new instruments. As a percussionist incorporating computer music technology into my performance I have been faced with a conundrum. I want to be able to control and interact with a computer system in my performance but I don't want to abandon the incredibly expressive act of playing percussion instruments. The topic of my current research is to find solutions to this problem, that is, techniques for controlling computer music systems while playing with conventional techniques on a relatively unmodified instrument.

One of my projects is to create improvised duets for computer and vibraphone. My idea is that a computer would play short pre-recorded vibraphone sounds as a counterpoint to my live improvisation. The computer runs a custom piece of software written in the Pure Data language  (Pd) to analyse audio input from a microphone over the vibraphone. The computer software is able to recognise attacks and detect the pitch and dynamic of notes that I play. This information is used to send MIDI messages to control software such as (Ableton) Live and (Apple) Logic Studio which plays back the pre-recorded sounds and applies effects.

For example, in a particular improvised piece called, I divide the vibraphone into ten (imaginary) zones, each one consisting of 3 or 4 adjacent notes. When I strike a note in a particular zone, the Pd program hears the attack and fires off a MIDI message to Ableton Live which then plays one of ten vibraphone recordings. Thus, when I play a melodic line on the vibraphone the computer simultaneously plays a melodic line constructed from sections of the ten recordings. In practice, this simple concept produces a striking variety of sounds from the computer that have a natural and clear relationship to what I play on the vibraphone.

To spice things up, both the live vibraphone sound and the recordings on the computer can be sent to a multitude of effects. I used some interesting reverbs in Logic Studio and complex delays and resonators in Live. Of course, if the effects were on all the time it would cover up the melodic line. Again, my Pd program listens to the live sound and converts the pitch and dynamics that it hears into MIDI messages that tell Logic and Live to send more or less of the live and recorded vibraphone sounds to the effects.

The end result is a setup where I can control effects and recordings from the computer by playing an unmodified vibraphone with only one microphone. In this performance the computer acts more like a musician than the pre-recorded tape that is commonplace in pieces for "percussion and electronics". Since the sounds that the computer produces are not composed but created as a reaction a live musician this music is a true duet.
[Recording of "Duet for Vibraphone and Computer" as performed in October 2008 at The Street Theatre in Canberra](http://www.epmartin.com/cmpercussion/DuetVibraphoneComputer.mp3)
