---
layout: post
title: A computer music system for vibraphone
categories:
- news
tags:
- vibrpahone
- rjdj
- computer music
- vibraphone
status: publish
type: post
published: true
---

I recently finished my first prototype for a dedicated computer music system for vibraphone, just in time to use it at 
[Electrofringe](http://www.electrofringe.net/) at the end of September and to take with me to Sweden!

The idea is to have a battery powered computer system that can attach to a vibraphone, includes a microphone for processing the vibraphone sound and can output straight to the mixing desk at a gig.
  
       
![The whole system fits on the end of my vibraphone - compact!]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes1.jpg) 

The whole system fits on the end of my vibraphone - compact! 
  
The current setup has:


* 4 electret microphones that blutack under the damper pedal in the vibraphone.
* A [battery powered preamp and power supply](http://www.amazon.com/Handmade-Electronic-Music-Hardware-Hacking/dp/0415998735/ref=dp_ob_title_bk) for the microphones that mixes them down to a mono signal.
* An [IK Multimedia iRig](http://www.ikmultimedia.com/irig/features/) dongle to make it easier to connect the microphones and the output to an iPhone
* an iPhone (or iPad) running RjDJ
* [my own custom RjDJ scene](http://rjdj.me/music/Charles%20Martin/Norra%20Vinter/399/) (programmed in Pd).
* A [cheap stereo DI box](http://www.behringer.com/EN/Products/DI20.aspx) to minimise the work that a sound technician has to do before I can plug into the desk.
  

![The microphones on the bottom of the damper bar.]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes2.jpg) The microphones on the bottom of the damper bar.
![]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes3.jpg)   
![]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes4.jpg)
![]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes5.jpg)
![]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes6.jpg)
![]({{ site.baseurl }}/assets/squarespace_images/2011-10-28-CMSVibes7.jpg)

Of course, each part of this could be much higher quality: the elecret microphones could be condenser clip on mics, the preamp could a less noisy design with higher gain possibilities, the iRig and iPhone could be a [Beagle board computer system](http://beagleboard.org/hardware-xM) running [Satellite CCRMA](https://ccrma.stanford.edu/~eberdahl/Satellite/).

I’ve seen a pickup design where the mics are suspended from an elastic band attached with binder clips to the vibes frame, but I haven’t had a chance to experiment with that yet! It might reduce the amount of noise caused by the moving pedal.

But my first goal with this kind of system was for it to exist and work - which it does - and there is every possibility of upgrading it as I find out the best ways to use it.

There’s some more documentation in the 
[Flickr set](http://www.flickr.com/photos/chuck_notorious/sets/72157627854258763/)!

Here's a video of these pickups in action:

<!-- https://youtu.be/wNW5EN0eCd8 -->
{% include youtubePlayer.html id="wNW5EN0eCd8" %}

### Updated! 2012-11-04

So I've had a few questions about how to make the actual microphones. I don't have good pictures to go into a total tutorial, but the microphones themselves are cheap [electret capsules](http://www.jaycar.com.au/productView.asp?ID=AM4011&keywords=electret+mics&form=KEYWORD), connected to a long audio cable and then to a simple power supply circuit.

There are good walkthroughs about the power supply circuit in the free version of [Hardware Hacking](http://www.nicolascollins.com/texts/originalhackingmanual.pdf) and on this [website](http://webpages.charter.net/tidmarsh/binmic/).

Have fun!
