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
meta:
  _thumbnail_id: '833'
---

I recently finished my first prototype for a dedicated computer music system for vibraphone, just in time to use it at 
[Electrofringe](http://www.electrofringe.net/) at the end of September and to take with me to Sweden!

The idea is to have a battery powered computer system that can attach to a vibraphone, includes a microphone for processing the vibraphone sound and can output straight to the mixing desk at a gig.
  
       
![The whole system fits on the end of my vibraphone - compact!]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1ba1e4b0cc6f9accf943_1413094308050__img.jpg) The whole system fits on the end of my vibraphone - compact! 
  


The current setup has:

*4 electret microphones that blutack under the damper pedal in the vibraphone.


*A 
[battery powered preamp and power supply](http://www.amazon.com/Handmade-Electronic-Music-Hardware-Hacking/dp/0415998735/ref=dp_ob_title_bk) for the microphones that mixes them down to a mono signal.


*An 
[IK Multimedia iRig](http://www.ikmultimedia.com/irig/features/) dongle to make it easier to connect the microphones and the output to an iPhone


*an iPhone (or iPad) running RjDJ


*[my own custom RjDJ scene](http://rjdj.me/music/Charles%20Martin/Norra%20Vinter/399/) (programmed in Pd).


*A 
[cheap stereo DI box](http://www.behringer.com/EN/Products/DI20.aspx) to minimise the work that a sound technician has to do before I can plug into the desk.
  
       
![The microphones on the bottom of the damper bar.]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1b3de4b0f3ed25f7e5f8_1413094207883__img.jpg) The microphones on the bottom of the damper bar. 
  


![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1cf8e4b0075aa7854f08_1413094649648_1-BuildingTheMics.jpg)
  

  
   
![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1cfbe4b059ff64df5ef9_1413094653263_2-PrototypingAPreamp.jpg)
  

  
   
![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1d04e4b05c01349afc28_1413094662801_3-BatteriesAndMixingResistors.jpg)
  

  
   
![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1d0ee4b0075aa7854f23_1413094671383_4-PuttingIntoProjectBox.jpg)
  

  
   
![]({{ site.baseurl }}/squarespace_images/500bb0b2e4b042ea6e35b13f_543a1d08e4b05c01349afc2d_1413094665671_5-iPhoneInterface.jpg)

Of course, each part of this could be much higher quality: the elecret microphones could be condenser clip on mics, the preamp could a less noisy design with higher gain possibilities, the iRig and iPhone could be a 
[Beagle board computer system](http://beagleboard.org/hardware-xM) running 
[Satellite CCRMA](https://ccrma.stanford.edu/~eberdahl/Satellite/).

I’ve seen a pickup design where the mics are suspended from an elastic band attached with binder clips to the vibes frame, but I haven’t had a chance to experiment with that yet! It might reduce the amount of noise caused by the moving pedal.

But my first goal with this kind of system was for it to exist and work - which it does - and there is every possibility of upgrading it as I find out the best ways to use it.

There’s some more documentation in the 
[Flickr set](http://www.flickr.com/photos/chuck_notorious/sets/72157627854258763/)!

Here's a video of these pickups in action:
 
   

 

Updated! 2012-11-04


So I've had a few questions about how to make the actual microphones. I don't have good pictures to go into a total tutorial, but the microphones themselves are cheap 
[electret capsules](http://www.jaycar.com.au/productView.asp?ID=AM4011&keywords=electret+mics&form=KEYWORD), connected to a long audio cable and then to a simple power supply circuit.


There are good walkthroughs about the power supply circuit in the free version of 
[Hardware Hacking](http://www.nicolascollins.com/texts/originalhackingmanual.pdf) and on this 
[website](http://webpages.charter.net/tidmarsh/binmic/).


Have fun!
