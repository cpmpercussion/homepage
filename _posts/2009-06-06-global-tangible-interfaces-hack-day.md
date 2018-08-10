---
layout: post
title: Global Tangible Interfaces Hack Day
categories: []
tags:
- Pd
- computer music
- hackday
- supercollider
- trackmate
status: publish
type: post
published: true
meta: {}
---

![]({{ site.baseurl }}/assets/blogger/tangible-interfaces-drum.jpg)

My goal for today's hackday is to connect the trackmate system to supercollider. Tricky! (But it works!)

Trackmate sends OSC messages to port 3333 of any other program listening. As it turns out, Supercollider's OSCresponder will only receive on port 57120. So we're at an impasse!

*update* Yes it really doesn't work! Quote from SuperCollider help: Messages from external clients that should be processed by OSCresponders must be sent to the language port, 57120 by default. Use NetAddr.langPort to confirm which port the SuperCollider language is listening on.

Maybe... I can hack the Trackmate tracker source to send from port 57120? That would certainly solve the problem.

Discussion with Adam (Trackmate creator) about changing the port: [link](https://sourceforge.net/apps/phpbb/trackmate/viewtopic.php?f=4&t=17).

*update* - It's going to work! I hope!

*update* - I compiled the tracker application and SuperCollider can now receive the LusidOSC messages.

*update* - I wrote a sort-of implementation of the lusidOSC receiver specification in SuperCollider. It works, but I'm not sure if it's the best way to do things. I plan to use this technology in a performance soon, so I guess I'll have to straighten these problems out!

In other news, Pd's dumpOSC object can listen on any port, so it was easy to see the LusidOSC messages rolling in.

My first problem with trackmate was setting up the hardware and software. I've used a tom with a clear skin at my studio, and I have a little downwards looking setup at home. These setups worked well with the test client apps in processing, but I'm keen on using supercollider!

BTW the binary release SuperCollider is so far incompatible with Safari 4 (at least the help browser), however there is a patch that can be applied to the source to correct the problem. Maybe I should post a howto?

![]({{ site.baseurl }}/assets/blogger/tangible-interfaces-desk.jpg)

### SuperCollider Test Script.

I put together a test script in SuperCollider that uses the (x,y) position of a tag to change the frequency of two sine oscillators. Very simple, but it shows how the OSCresponder needs to be setup.

![]({{ site.baseurl }}/assets/blogger/tangible-interfaces-trackmate-demo.jpg)


    // Super Simple SuperCollider LusidOSC script. (SuperSimpleCollider?)
    // First boot the server
    
    (
    s = Server.local;
    s.boot;
    )
    
    (
    var id, thetaToFreq, alive;
    var xVal = 0;
    var yVal = 0;
    var theta = 0;
    id = "0xBF82C7B4F1DA"; //Hard coded id of one trackmate tag.
    alive = false;
    
    // Definition of a synth
    // One sine oscillator in each channel
    SynthDef("sine", { arg freqX, freqY;
    var osc;
    osc = SinOsc.ar([freqX,freqY], 0, 0.1);
    Out.ar(0, osc);
    }).send(s);
    
    // Starts a synth
    s.sendMsg("/s_new", "sine", a = s.nextNodeID, 1, 1, "freqX", 440, "freqY", 440);
    // The important bit!
    // This code listens to OSC messages from the Trackmate Tracker
    o = OSCresponderNode.new(NetAddr.new("127.0.0.1", nil), "/lusid/1.0", {
    arg time,responder,msg;
    (msg[1].asString == "set").if({
    (msg[2].asString == id).if({
    xVal = 100 + (msg[3]);
    yVal = 100 + (msg[4]);
    theta = msg[8];
    //("Location:" + xVal + yVal + theta).postln; // debug
    s.sendMsg("/n_set", a, "freqX", xVal * 16); // set x oscillator
    s.sendMsg("/n_set", a, "freqY", yVal * 16); // set y oscillator
    // nothing mapped to rotation yet!
    });
    });
    }).add;
    )
    
    // Stop the Responder!
    (
    s.sendMsg("/n_free", a);
    o.remove;
    )
