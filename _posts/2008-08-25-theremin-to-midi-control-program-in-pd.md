---
layout: post
title: Theremin to MIDI Control program in Pd
categories: []
tags:
- Pd
- duetforvibraphoneandcomputer
- music
- pure data
- theremin
status: publish
type: post
published: true
meta: {}
description: "Update throughout 2008 and 2009 I used these techniques with the vibraphone in my piece Duet for Vibraphone and Computer Over the weekend I wrote a"
---

![]({{ site.baseurl }}/assets/blogger/ThereminController.jpg)

*Update:* throughout 2008 and 2009 I used these techniques with the vibraphone in my piece "Duet for Vibraphone and Computer"

Over the weekend I wrote a simple program in Pd that analyses an audio input and then uses pitch and amplitude information to output a midi control value.

My idea was to use my little theremin as the audio input and send the midi data to an internal midi bus which is received by Ableton Live for controlling parameters of some effects. Since the theremin has such a simple sound the pitch and amplitude analysis works extremely well. To achieve this feat I use the excellent fiddle~ object (written by Miller Puckette) and... well not much else really! A few * and + objects adjust the output values so that they are sensibly distributed between 0-127.

Here's the code (or just copy from the picture!):

    #N canvas 738 31 442 441 10;
    #X obj 88 21 adc~ 1;
    #X obj 88 44 *~ 1;
    #X obj 29 91 *~;
    #X obj 59 91 tgl 15 0 empty empty empty 17 7 0 10 -262144 -1 -1 0 1;
    #X obj 29 114 dac~ 1;
    #X text 9 146 Audio Output!;
    #X obj 147 114 unpack;
    #X obj 188 177 moses 1;
    #X floatatom 219 214 5 0 0 0 Note - -;
    #X floatatom 109 214 5 0 0 0 Amplitude - -;
    #X obj 117 83 fiddle~ 1024;
    #X obj 50 411 ctlout 14;
    #X obj 195 411 ctlout 15;
    #X obj 222 303 tgl 15 0 empty on empty 17 7 0 10 -262144 -1 -1 1 1;
    #X obj 192 303 *;
    #X obj 54 245 *;
    #X obj 54 268 +;
    #X floatatom 91 245 5 0 100 0 - ampmult -;
    #X floatatom 91 265 5 -127 127 0 - ampshift -;
    #X obj 190 240 *;
    #X obj 190 263 +;
    #X floatatom 227 242 5 0 100 0 - pitchmult -;
    #X floatatom 227 265 5 0 0 0 - pitchshift -;
    #X obj 232 368 tgl 15 0 empty on empty 17 7 0 10 -262144 -1 -1 1 1;
    #X obj 201 368 *;
    #X floatatom 212 328 5 0 0 0 - - -;
    #X obj 84 303 tgl 15 0 empty on empty 17 7 0 10 -262144 -1 -1 1 1;
    #X obj 54 303 *;
    #X obj 94 368 tgl 15 0 empty on empty 17 7 0 10 -262144 -1 -1 1 1;
    #X obj 63 368 *;
    #X floatatom 74 328 5 0 0 0 - - -;
    #X text 147 14 Theremin Controller;
    #X obj 303 162 loadbang;
    #X msg 302 184 \; pitchmult 2 \; pitchshift -80 \; ampmult 1 \; ampshift
    20 \;;
    #X obj 302 253 loadbang;
    #X obj 303 275 s on;
    #X text 147 34 Output midi controller data;
    #X text 146 49 from pitch and amplitude input.;
    #X text 292 402 Charles Martin;
    #X text 293 414 25/08/08;
    #X text 301 145 Default Settings;
    #X connect 0 0 1 0;
    #X connect 1 0 2 0;
    #X connect 1 0 10 0;
    #X connect 2 0 4 0;
    #X connect 3 0 2 1;
    #X connect 6 0 7 0;
    #X connect 6 1 9 0;
    #X connect 7 1 8 0;
    #X connect 8 0 19 0;
    #X connect 9 0 15 0;
    #X connect 10 2 6 0;
    #X connect 13 0 14 1;
    #X connect 14 0 25 0;
    #X connect 15 0 16 0;
    #X connect 16 0 27 0;
    #X connect 17 0 15 1;
    #X connect 18 0 16 1;
    #X connect 19 0 20 0;
    #X connect 20 0 14 0;
    #X connect 21 0 19 1;
    #X connect 22 0 20 1;
    #X connect 23 0 24 1;
    #X connect 24 0 12 0;
    #X connect 25 0 24 0;
    #X connect 26 0 27 1;
    #X connect 27 0 30 0;
    #X connect 28 0 29 1;
    #X connect 29 0 11 0;
    #X connect 30 0 29 0;
    #X connect 32 0 33 0;
    #X connect 34 0 35 0;

To check it out, copy and paste the code into a text editor, save it as a .pd file, then open in Pd! Click the little toggle boxes to first to view the data and then to send it to the midi output. This way you can shut off output of one parameter while you have Live (for example) learn the assignment.

**Update:** The program was a little bit wrong. Fixed now! Hello internet!
