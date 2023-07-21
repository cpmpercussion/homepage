---
layout: post
title: One-person hybrid conference toolkit 
date: 2023-07-20
category: note
tags: hybrid, conference, setup
---

Hybrid events are **hard**, even more now that they are kind of _expected_,
especially within the academic community. This post is about my one-person
hybrid setup.

Last year I was part of the organising team for OzCHI 2022 in Canberra, a
single track conference. Here's approached doing _hybrid_ aspects of the
conference right, or as well as possible, within a very small budget[^budget].

[^budget]: Budget was zero dollars, except, of course, for my time (possibly too much of that), and that I had an awesome HDMI switcher, GoPro, Microphone, HDMI capture device, and two pretty nice laptops. This is not really a post about cheap tech, but rather avoiding paying excessively for a poor product as I have seen at some very expensive and prestigious conferences. 

![my hybrid prduction setup at the Shine Dome, Canberra]({% link assets/blog/2023/streaming-hybrid.jpg %})

Here's a few principles for the event:

- make the experience easy and inclusive for hybrid attendees
- use our own equipment, don't hire a production company 
- have high quality audio and video
- keep the focus on attendees in the room

The tl;dr here is: we used [restream.io](https://restream.io) as a streaming
and production platform, not Zoom. The endpoints were unlisted youtube streams
sent to remote attendees over Slack. We used a dedicated computer for streaming
and an HDMI switcher to grab the signal from presenter's laptops. It was
helpful to have a good quality camera and microphone connected ot the streaming
computer to capture the speaker at the lectern. The main takeaways are:

- browser-based streaming platforms use more resources (CPU + network) than
  Zoom and folks aren't usually prepared for it.
- streaming platforms are _much better_ than Zoom from an audience perspective
- in-person audiences don't like pre-recorded presentations

## One-to-Many presentation

Conference presentations are 1-to-N presentations, so not a great fit for video
conferencing software (e.g., Zoom calls). Listeners want good audio and video
quality and not to be annoyed by software that wants to see you and takeover
your computer. A good solution is a high quality stream to an easy to use
endpoint like YouTube where attendees can view videos in a browser window or on
any device.

One of the difficulties of a hybrid conference is switching between a live view
and remote presenters. Amazingly, there are streaming products out there that
give you a little TV studio for bringing in live guests, switching on shared
screens, and turning cameras on and off all within a web browser (I'm literally
still amazed this all works).

From online teaching I had a subscription to [restream](https://restream.io)
and was ready to try out it's production features for this conference.
Streamyard is another similar option. Restream gives you a browser-based
interface to produce a stream and invite guest presenters. You can choose which
presenter is "live" on the stream and who's screen is shown. There are neat
options to arrange multiple presenter's videos side-by-side or next to a shared
screen.

The upside of these streaming systems is that they work _really_, _really_ well
under many circumstances. The downside is that they aren't as forgiving as Zoom
and presenters do not usually have experience outside of Zoom or Teams.

It turns out that these browser-based systems tend to use more system and
network resources than Zoom and are a little less reliable at capturing your
screen and audio (depending on your OS). This means that it's **crucial** to do
some kind of rehearsal or test with presenters to check their setup.

## The setup

![a signal diagram for my setup]({% link assets/blog/2023/streaming-conference-setup.png %})

This setup is designed to slot into a regular conference or lecture hall with
HDMI sending video to a big screen and audio to big speakers. We need four
pieces of hardware:

1. An HDMI switcher to go in between the presenter's laptop and the screen. We used an [ATEM Mini Extreme](https://www.blackmagicdesign.com/au/products/atemmini) (already had for teaching). This lets us take an output signal to a dedicated streaming computer, and to easily put the streaming computer's screen on the big screen during remote presentations.

2. A dedicated straming computer. I used a (now old) 2016 MacBook Pro. A fairly powerful laptop is needed as it will need to handle multiple video streams. The internet connection should be stable and fast.

3. A dedicated camera and microphone to point at the live presenter. I used a GoPro with a Rode VideoMicro microphone. The GoPro has an HDMI output (using the "Media Mod" for this model). A regular/nice webcam could work but I like the extreme wide-angle of the GoPro for capturing presenters who tend to move around a bit. The neat little microphone seemed to work well to pick up the presenter and definitely made them feel super pro[^1].

[^1]: Anecdotal evidence can be supplied on request.

4. _Another_ laptop used by "the producer" (see below). 

There's two modes we need to cope with: an in-person talk and a remote talk



## The producer

![a screenshot of restream studio]({% link assets/blog/2023/streaming-restream-studio.png %})

## Doing this again, better.

[ACMC2020](https://benswift.me/blog/2020/07/15/acmc2020-organising-my-first-virtual-conference/)


