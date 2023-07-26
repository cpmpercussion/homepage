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

[^budget]: Budget was zero dollars, except, of course, for my time (possibly too much of that), and that I had equipment to hand, e.g., HDMI switcher, GoPro, Microphone, HDMI capture device, two pretty nice laptops, and an existing restream subscription. This is not really a post about cheap tech, but rather avoiding paying excessively for a poor product as I have seen at some very expensive and prestigious conferences. 

![my hybrid prduction setup at the Shine Dome, Canberra]({% link assets/blog/2023/streaming-hybrid.jpg %})

The image shows a remote talk, and Restream Studio's production interface on my laptop. (This was a great talk!)

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

## One-to-many presentation

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

There's two modes we need to cope with: an in-person talk and a remote talk. 

For the **in-person presentation** mode, the HDMI switcher is set to show the presenter's laptop on the big screen. The HDMI switcher is connected to the streaming laptop (USB) and shows up as a webcam. The switcher's signal is set to full screen in Restream Studio and the GoPro is set to a small window in the corner. So: remote attendees see and hear both the big screen and the person talking.

For **remote presentation** mode, the streaming laptop's screen goes to the HDMI switcher (over HDMI) and audio and video are sent to the big screen. The GoPro isn't sent anywhere. The remote presenter connects to Restream Studio and sends their screen sharing signal and camera.
The in-person audience sees the Restream Studio interface full screen.

The in-person view in remote mode is the only compromise here as the restream studio interface isn't _meant_ for public viewing (i.e., it has a back-channel chat window and GUI controls for which signal is shown in the stream). One option would be to have a _third_ computer playing the stream from Youtube, but I thought this got a step too complicated. There may be other solutions as well.

## The stream producer

To cope with the hybrid setup, we needed at least one person to keep an eye on the studio interface pretty much at all times.

![a screenshot of restream studio]({% link assets/blog/2023/streaming-restream-studio.png %})

Restream and other online streaming production systems let you preview the
cameras and screen sharing of presenters before switching them live on screen.
You can also chat with presenters to make sure they are ready to go.

## Remote participants

It's hard to be a remote participant and get any feeling of inclusion at a
conference. The best we can do to make the task easy is to communicate early
and regularly with remote speakers and attendees and make sure all information
for watching and giving talks is super clear.

Pre-conference rehearsals goes a long way towards helping speakers feel
included and setting expectations for the streaming system. We found a few bugs
this way and had a chance to test out difficulties with setups, networks, and
laptops. I wrote up some [Instructions for Participants]({% link
misc/remote-presentation-procedure.md %}) that I shared with all presenters.

As I wrote above, these streaming systems put more load on presenters'
computers than Zoom. This was definitely frustrating for presenters who would
rightly would question why our system seemed to be broken. There's not much
that can be done on the day of a talk, but if the expectations are set well in
advance, some of these difficulties can be smoothed out.

One efficiency would be to ask for slides well in advance. Restream can host
basic slide decks directly in their interface. This can really help if a remote
presenter's system is struggling to screen share and stream camera and audio.
Both the presenter and stream producer can control the slide deck in this case,
but animations and videos in the slides aren't supported.

Some remote participants really wanted to do pre-recorded presentations. I
understand the temptation as these are much easier to produce than a live
hybrid talk. The problem is that pre-recorded talks are terribly boring! Live
attendees regularly walk out of them. I've had great experiences with
pre-records in fully-online and asynchronous conferences, but I don't think
pre-records should be a part of live (and expensive) conference programs.  

## Doing this again, better.

I previously had experience with a great _virtual_ conference with
[ACMC2020](https://benswift.me/blog/2020/07/15/acmc2020-organising-my-first-virtual-conference/)
with all asynchronous online talks and a really active community watching. The
hybrid setup was much more complex and a huge effort to make it work within a live environment. The
majority of the effort was in managing people, the remote presenters, in-person
session chairs, and helpers who managing the chat and addressing concerns.
Everybody involved can get easily confused and stressed.  

It's possible to get a great result with a one-person setup, but it's
hard work. Next time, I'd think about:

- setting expectations even more clearly with remote participants and collecting more slide decks in advance
- experimenting with a third playback-only computer for showing the remote talks
- training another person to be the stream producer during talks


