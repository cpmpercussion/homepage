---
layout: post
title: Running Pd on the Intel Galileo
categories:
- note
tags:
- Intel Galileo
- Physical Computing
- Pd
- Computer Music
status: publish
type: post
published: true
meta:
  _thumbnail_id: '848'
---

![The Intel Galileo Gen 2 - All hooked up.]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_54d2f380e4b05f7dfea88aa9_1423111098977_IMG_4488.jpg) The Intel Galileo Gen 2 - All hooked up. 

The Intel Galileo is a great little development/experiments board with an Intel Quark 32-bit x86 processor. We had some of these hanging around our office and I was inspired to make some computer music with it - so here's my process for getting Pure Data up and running.

Here's the things I needed:

* Intel Galileo Gen 2
* MicroSD card
* [$2 Ebay usb audio interface (1 in, 2 out)](http://r.ebay.com/Mtw58N)
* [Sparkfun FTDI Basic Breakout](https://www.sparkfun.com/products/9873)

And some important online resources:

* [Sparkfun Galileo Getting Started Guide](https://learn.sparkfun.com/tutorials/galileo-getting-started-guide?_ga=1.240244739.1237137420.1418594925)
* [AlexT's Package Repo Instructions](http://alextgalileo.altervista.org/package-repo-configuration-instructions.html)
* [Intel Galileo Downloads](https://communities.intel.com/docs/DOC-22226)

## Connecting up

Unlike the Raspberry Pi and kin, the Galileo doesn't have a video output or anything. You can load up a program on it using the Arduino IDE but I wanted to get a terminal up and running as soon as possible. The Galileo Gen 2 runs a terminal over serial using an 6-pin FTDI header near the ethernet port. Luckily I had a 
[Sparkfun FTDI Basic Breakout](https://www.sparkfun.com/products/9873) hanging around (I happen to have the 3.3V version, but it doesn't matter for this purpose). This plugs in with the header facing the ethernet port and the IC facing out.

I had a [super cheap USB audio interface](http://r.ebay.com/Mtw58N) from a previous project that I plugged into the USB host port and also connected the ethernet port up to my network to pull down some stuff.

At this point, I connected to the board to make sure it worked, I think the screen command is the best serial terminal on OS X so I opened a terminal and ran:

    screen /dev/tty.usbserial-A40081Q0 115200

You can run

    ls /dev/tty.*

to figure out the name of your serial to USB connection.

After running screen, you can power up the board and watch the boot sequence over the serial connection!

## Using the bigger Linux image.

The board has a tiny Linux installed in ROM (<8MB!) data-preserve-html-node="true" but to use audio you need a distribution on the SD card. Download this from [Intel's Downloads page](https://communities.intel.com/docs/DOC-22226), I used SDCard.1.0.4.tar.bz2 which is 48MB. You just have to unzip this file onto a microSD card, plug it into the board, and it will (should) boot straight off it.

One you've booted to the big Linux image, you can log in with the user name "root". You should then be able to try out the soundcard with the ALSA test tools which are already installed. When I plugged my USB sound adapter in, it wasn't recognised immediately and I had to load the correct driver module like so:

    modprobe snd-usb-audio

I like to list the sound devices to make sure it's working, a helpful command is:

    aplay -l 

which, for me, returns:

    root@clanton:~# aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

You can test the sound output using the `speaker-test` command. Or to be fancy:

    speaker-test -c2 -t wav

Woo! Sound works!

## Getting Packages

The bigger Yocto Linux distro is still missing a few packages like, oh say, a C-compliler and a text editor. A helpful community member has a package repository for the distro, there's lot of information [on AlexT's site about setting this up](http://alextgalileo.altervista.org/package-repo-configuration-instructions.html). There's also a post about installing [development tools](http://alextgalileo.altervista.org/blog/installing-development-tools-onto-official-linux-image/).

The short story is, add the repositories to the correct conf file:

    echo "src/gz all     http://repo.opkg.net/galileo/repo/all
    src/gz clanton http://repo.opkg.net/galileo/repo/clanton
    src/gz i586    http://repo.opkg.net/galileo/repo/i586" >> /etc/opkg/base-feeds.conf

(Make sure there are line breaks in the right spots for that command.)

Update the packages and install the build environment:

    opkg update
    opkg install --force-overwrite uclibc
    opkg install packagegroup-core-buildessential
    opkg install nano
    opkg install git

## Compiling Pd.

Grab the Pd source:

    git clone git://git.code.sf.net/p/pure-data/pure-data

And then follow the instructions from `INSTALL.txt`, you need to force ALSA sound to be enabled:

    ./autogen.sh
    ./configure --enable-alsa
    make
    make-install

The make command will compile Pd on the (slow) Galileo processor - this takes a while. I didn't time it but it seemed like about 30 minutes.

## Running a patch.

Getting patches on to the Galileo is can be done with 
scp over a network. You can also copy and paste the patch text into a file over the serial connection. On my main system, I run 
cat composition.pd to print the pd file onto the command line, I select all the pd commands then in the serial terminal I run 
echo "copy all the pd text here" >> composition.pd where you paste all the Pd commands in between the quotation marks. Obviously this is super great for small Pd files and impractical for big ones where you should probably use 
scp.

Having said that, here's some a hello world sine tone to try:

    #N canvas 602 140 450 300 10;
    #X obj 148 148 dac~;
    #X obj 142 77 osc~ 440;
    #X obj 150 111 *~ 0.5;
    #X obj 267 77 loadbang;
    #X msg 276 144 \; pd dsp 1;
    #X obj 254 202 print;
    #X msg 254 178 turned dsp on.;
    #X obj 270 106 delay 2000;
    #X connect 1 0 2 0;
    #X connect 2 0 0 0;
    #X connect 2 0 0 1;
    #X connect 3 0 7 0;
    #X connect 6 0 5 0;
    #X connect 7 0 4 0;
    #X connect 7 0 6 0;

I echo'd this into sine.pd and then run it on the Galileo with:

    pd -nogui -blocksize 1024 sine.pd

The sweet sound of success! 1024 is a huge blocksize compared to the default settings for Pd, I'm not sure if there's a way to reduce this and keep acceptable quality, but there might be!

A critical part of the patch is to include a `; pd dsp 1` message somewhere which will turn on DSP. You can probably also activate this by passing in a message from the command line.

## Next Steps.

Next steps for this project are accessing the Galileo's GPIO pins from Pd, particularly the analog ins! I'd also like a tool chain for loading up a Pd patch and a management program using the Arduino IDE so that the program will load at startup.

## Bonus Patches

Here's two extra patches to try out.

### Simple FM sound

    #N canvas 555 156 450 300 10;
    #X obj 78 105 osc~ 440;
    #X obj 78 128 *~ 0.5;
    #X obj 267 77 loadbang;
    #X msg 276 144 \; pd dsp 1;
    #X obj 254 202 print;
    #X msg 254 178 turned dsp on.;
    #X obj 270 106 delay 500;
    #X obj 77 81 +~ 500;
    #X obj 75 52 *~ 500;
    #X obj 74 28 osc~ 45;
    #X obj 78 154 dac~ 1;
    #X connect 0 0 1 0;
    #X connect 1 0 10 0;
    #X connect 2 0 6 0;
    #X connect 5 0 4 0;
    #X connect 6 0 3 0;
    #X connect 6 0 5 0;
    #X connect 7 0 0 0;
    #X connect 8 0 7 0;
    #X connect 9 0 8 0;

### Generative composition using additive synthesis

    #N canvas 492 59 1003 670 10;
    #X obj 370 520 dac~;
    #X obj 376 473 *~ 0.1;
    #X obj 83 87 metro;
    #X obj 83 62 tgl 15 0 empty empty empty 17 7 0 10 -262144 -1 -1 1 1
    ;
    #X floatatom 129 87 5 0 0 0 - - -;
    #X obj 122 18 bng 15 250 50 0 empty empty empty 17 7 0 10 -262144 -1
    -1;
    #X obj 82 113 bng 15 250 50 0 empty empty empty 17 7 0 10 -262144 -1
    -1;
    #X obj 410 275 osc~;
    #X obj 459 275 osc~;
    #X floatatom 397 222 5 0 0 0 - - -;
    #X obj 459 244 * 2;
    #X obj 507 273 osc~;
    #X obj 604 274 osc~;
    #X obj 507 242 * 4;
    #X obj 605 243 * 8;
    #X obj 462 394 +~;
    #X obj 478 336 +~;
    #X obj 479 361 +~;
    #X obj 393 142 random 50;
    #X obj 394 170 + 36;
    #X obj 395 197 mtof;
    #X obj 258 377 vline~;
    #X obj 259 417 *~;
    #X msg 258 350 1 25 \, 0 1000 25;
    #X obj 114 40 random 1500;
    #X obj 114 60 + 100;
    #X obj 472 169 random 100;
    #X obj 472 193 / 10;
    #X obj 543 166 random 100;
    #X obj 543 189 / 10;
    #X obj 613 166 random 100;
    #X obj 613 189 / 10;
    #X obj 542 131 bng 15 250 50 0 empty empty empty 17 7 0 10 -262144
    -1 -1;
    #X obj 682 272 osc~;
    #X obj 691 164 random 100;
    #X obj 691 187 / 10;
    #X obj 762 272 osc~;
    #X obj 771 164 random 100;
    #X obj 771 187 / 10;
    #X obj 41 27 loadbang;
    #X obj 683 241 * 9;
    #X obj 763 241 * 10;
    #X obj 454 303 *~ 0.5;
    #X obj 508 304 *~ 0.4;
    #X obj 612 300 *~ 0.3;
    #X obj 690 298 *~ 0.2;
    #X obj 770 298 *~ 0.1;
    #X obj 89 391 loadbang;
    #X msg 98 458 \; pd dsp 1;
    #X obj 76 516 print;
    #X msg 76 492 turned dsp on.;
    #X obj 92 420 delay 500;
    #X obj 318 233 print freq;
    #X connect 1 0 0 0;
    #X connect 1 0 0 1;
    #X connect 2 0 6 0;
    #X connect 3 0 2 0;
    #X connect 5 0 24 0;
    #X connect 6 0 18 0;
    #X connect 6 0 23 0;
    #X connect 6 0 24 0;
    #X connect 7 0 15 0;
    #X connect 8 0 42 0;
    #X connect 9 0 7 0;
    #X connect 9 0 10 0;
    #X connect 9 0 13 0;
    #X connect 9 0 14 0;
    #X connect 9 0 40 0;
    #X connect 9 0 41 0;
    #X connect 9 0 52 0;
    #X connect 10 0 8 0;
    #X connect 11 0 43 0;
    #X connect 12 0 44 0;
    #X connect 13 0 11 0;
    #X connect 14 0 12 0;
    #X connect 15 0 22 1;
    #X connect 16 0 17 0;
    #X connect 17 0 15 1;
    #X connect 18 0 19 0;
    #X connect 18 0 32 0;
    #X connect 19 0 20 0;
    #X connect 20 0 9 0;
    #X connect 21 0 22 0;
    #X connect 22 0 1 0;
    #X connect 23 0 21 0;
    #X connect 24 0 25 0;
    #X connect 25 0 2 1;
    #X connect 25 0 4 0;
    #X connect 26 0 27 0;
    #X connect 27 0 10 1;
    #X connect 28 0 29 0;
    #X connect 29 0 13 1;
    #X connect 30 0 31 0;
    #X connect 31 0 14 1;
    #X connect 32 0 26 0;
    #X connect 32 0 28 0;
    #X connect 32 0 30 0;
    #X connect 32 0 34 0;
    #X connect 32 0 37 0;
    #X connect 33 0 45 0;
    #X connect 34 0 35 0;
    #X connect 35 0 40 1;
    #X connect 36 0 46 0;
    #X connect 37 0 38 0;
    #X connect 38 0 41 1;
    #X connect 39 0 3 0;
    #X connect 40 0 33 0;
    #X connect 41 0 36 0;
    #X connect 42 0 16 0;
    #X connect 43 0 16 1;
    #X connect 44 0 17 1;
    #X connect 45 0 15 1;
    #X connect 46 0 15 1;
    #X connect 47 0 51 0;
    #X connect 50 0 49 0;
    #X connect 51 0 48 0;
    #X connect 51 0 50 0;
