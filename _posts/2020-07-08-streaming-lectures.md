---
layout: post
title: A note on streaming lectures
date: 2020-07-08
---

So it's been a _rough year_. After starting the semester in February with half my [class](https://cs.anu.edu.au/courses/comp2300) of 400 stuck at home in China, we ended up fully-online in March and managed to get the class over the finish line in June---phew! In the few short weeks (days?) before starting all over again at the end of July, I'll just set down a bit of info for how my online teaching setup works.

This post is about my approach to lectures, and I'll have another about tutorials/labs soon.

## Lecture Setup

Recorded lectures are _hard_; there's always the temptation to do more takes, and video editing is really time consuming. I know that I'm a better performer just delivering lectures live and accepting a few small mistakes, so I chose to focus on streaming engaging and entertaining lectures synchronously, tracking with the normal class timetable. This gives my students opportunities to have live (or almost live) Q&A during lectures and provides a bit more structure in their week.

Here's the key parts for my streaming setup:

- [OBS studio](https://obsproject.com) - for video and screen capture, [chroma keying](https://en.wikipedia.org/wiki/Chroma_key), scenes, and streaming to...
- [restream.io](https://restream.io) - to send the stream to multiple endpoints; I send to YouTube, Twitch, and...
- [Microsoft Stream](https://www.microsoft.com/en-us/microsoft-365/microsoft-stream) - to provide an "official" way for ANU students to watch the lectures, and to integrate with...
- [Microsoft Teams](https://www.microsoft.com/en-au/microsoft-365/microsoft-teams/group-chat-software) gives the students an "official" chat platform and a first port of call for interaction with me and my tutors. You can add a Microsoft Stream channel as a tab within a Team so that the latest lecture is just a click away for the students.

Here's what this all looks like:

![A diagram of my streaming setup from OBS to restream to multiple platforms with feedback through Teams]({{site.baseurl}}/assets/blog/2020/2020-ANU-streaming-rig.png)

And here's a short video about how it works:

<!-- Youtube Link: https://youtu.be/n2cNtVcfB48 -->
{% include youtubePlayer.html id="n2cNtVcfB48" %}

## Some more details...

Here's a few more details about each part of the system.

### OBS Scene Switching

I've set up a couple of "scenes" within OBS; e.g., one with me superimposed on the right, one on the left, one where I fill the screen for an intro. I also have some "static" scenes for starting and finishing lectures so that I can start streaming before I actually start talking.

There's lots of ways to switch scenes in OBS (e.g., key combinations, or [extra keyboard controllers](https://www.elgato.com/en/gaming/stream-deck)) but I've found using my iPad and [OBS websocket](https://github.com/Palakis/obs-websocket) is most convenient.

### Teams

[Teams](https://www.microsoft.com/en-au/microsoft-365/microsoft-teams/group-chat-software) has ended up being the centre of our synchronous online teaching. It's great to get chat with students and to see their "real names" (not screen names), and it's neat that you can integrate a Microsoft Stream channel.

### Streaming to multiple endpoints

It's hard to get students to watch lectures, so I thought I'd try going to where the students live for their normal online content: YouTube and Twitch. Twitch in particular is a really fun platform with lots of inspirational live content (e.g., [Jonong](https://www.twitch.tv/jonathanong) and [Lara6683](https://www.twitch.tv/lara6683)).

Some students tell me they enjoy seeing classes come up in their feed and a few did tend to jump into the Twitch chat. After a few lectures we came up with a good system: "Twitch chat for memes, Teams chat for serious questions", just so that I didn't have to monitor all chat channels simultaneously.

Restream makes streaming to multiple platforms very easy. OBS has a preset included for [streaming to Restream](https://support.restream.io/en/articles/111656-how-to-connect-obs-studio-to-restream), and then Restream takes care of connecting to all the other platforms. Restream also automatically creates new live events on YouTube, Twitch, and many other platforms, can update titles and descriptions automatically. It can even collate the chat across multiple platforms.

### Microsoft Stream

[Stream](https://www.microsoft.com/en-us/microsoft-365/microsoft-stream) is a slightly wacky corner of Office365 which pretty much does what it says on the tin: host live streamed and pre-recorded video events.

Unfortunately, and unlike YouTube and Twitch, Stream doesn't integrate with Restream.io, so each live event has to be set up manually, creating a new RTMP address to stream to which needs to be copied into restream before each lecture.

There's [a bit of info in Stream's docs](https://resources.techcommunity.microsoft.com/live-event-with-obs/) about connecting directly to OBS, which also applies to working with Restream.

I've found Stream works perfectly well with 1080p30 streams.

I've found it helpful to [add Microsoft Stream as a "tab"](https://support.microsoft.com/en-gb/office/add-and-use-a-stream-tab-in-teams-fb6cebb8-0d4f-4034-88a6-7dafdb5f0a3f) within the Microsoft Team for my class so that each lecture has an associated chat stream in Teams.

### But what about Echo360

[Echo360](https://echo360.com) is the automated lecture recording system installed at the ANU. It works well for zero-hassle recordings in lecture halls and has many interactive learning features that can be used online.

Even though Echo360 provides streaming, I don't use it because **you can't stream to it from OBS studio** (they only support [their own streaming tool](https://echo360.com/universal-capture-demo/), which, among other issues, doesn't work on Linux). 

If Echo360 ever want to make RTMP endpoints available to users then I would _love_ to include it in my system, but at the moment, I'm stuck uploading the streamed videos after each lecture (😐).

{%comment%}

## Tutorial Setup

Our computing students attend 

## Help when they need it


I guess I had a few high-level goals when putting together this setup:

- **synchrony and asynchrony**:

- **a place to study, when and where the students needed it**: 

I was very lucky to be teaching from good source material (mostly written by Ben Swift and Uwe Zimmer)

{%endcomment%}

