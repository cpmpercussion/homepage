---
layout: post
title: "Video as an assessment format from 10 to 300  students"
date: 2026-03-30
category: teaching
tags:
- teaching
- assessment
- video
- hci
- sound-and-music-computing
- laptop-ensemble
- computing education
description: "From Ben Swift's video scripting for ACMC 2020 to GitLab CI checks on 300 student video submissions in 2025: how video assessment evolved across laptop ensemble, SMC, and HCI, and why it produces something more authentic and more enjoyable to mark than a written submission."
---

My use of video as an assessment format goes back to 2020 and [Ben Swift](https://benswift.me)'s work organising [ACMC 2020](https://benswift.me/blog/2020/07/15/acmc2020-organising-my-first-virtual-conference/) as a fully online conference. Ben wrote FFMPEG scripts to ingest, normalise, and assemble video submissions from presenters — consistent audio levels, name overlays, everything compiled into a single watchable reel. Ben and I were already collaborating on the ANU Laptop Ensemble, and those scripts became the foundation for how we handled video in the course from 2020 onwards.

This is the story of how that foundation grew from 9 students to almost 300.

## computer music diary

In 2020, Ben and I introduced the **Computer Music Diary** to the laptop ensemble: a weekly 1-minute screencast showing whatever students had been working on that week. The idea came from a paper by Benjamin Murphy on "beat cyphers" — new music students need to make *many* pieces to develop skill, not one big one. The diary gave the course a weekly rhythm: make something, record it, watch everyone else's, discuss.

The format is both easy and hard. Easy because it only takes a minute to record. Hard because you can't fill a minute with nothing — students have to have actually done something. You can't fake a 1-minute screencast of code that doesn't work.

With 9 students in 2020 and 11 in 2021, Ben led the video pipeline and a lot could be managed by hand. The format was clearly working though: students were creating 11 pieces over a semester instead of one, improvisation started in week 1, and watching the diary submissions together became the best 20 minutes of each class. I wrote about this in more detail in [Teaching 14 Laptop Ensembles]({% link _posts/2023-10-16-teaching-14-laptop-ensembles.md %}).

## growing the pipeline: 2022 and 2023

From 2022 I took over leading and extending the video pipeline. [Lucy](https://comp.anu.edu.au/docs/lucy/) is a GitLab-based course management tool that's been developed by ANU Computing academics since 2017, originating with Ben's work. I took over as lead from 2022 and extended it with a command to build crit videos for each class. Students submitted screencasts to Teams; I or a tutor would run the Lucy command, which picked up submissions via OneDrive, ran FFMPEG to assemble them into a combined reel with normalised audio and name overlays, and produced a single file ready to play at the start of class.

With 21 students in 2022 that was fine. When enrolments jumped to **61 students in 2023**, spread across 14 ensembles in multiple workshop groups running several sessions per week, running the command manually stopped working. I automated it: a cron job ran the Lucy video pipeline for each class automatically as submissions arrived, so the crit reel was ready before anyone showed up. That's what kept the shared watching-together-at-the-start-of-class ritual possible at 60+ students across multiple weekly sessions.

## hci: 300 students, no pipeline needed

When I redesigned [COMP3900/6390 HCI]({% link _posts/2025-12-01-hci-course-redesign.md %}) in 2025, the video problem was different. Students weren't submitting a new screencast every week — just one five-minute final project video at the end of semester. With close to 300 enrolled, the challenge wasn't assembling reels. It was making sure submissions actually met the format requirements without anyone having to check them manually.

My solution was to use GitLab CI. Students were already using GitLab for their project work, so the final video just went into the repository. A CI check ran on every push and failed if the video exceeded five minutes. Students could self-check before the deadline; marking could start with confidence that every submission was the right length. The hard five-minute limit was actually hard — you couldn't add thirty seconds on the assumption nobody would look.

For recording, students used whatever they were comfortable with. PowerPoint's video recording feature (included in the ANU Microsoft 365 subscription) works well for anyone who already makes slides: narrate over your deck, camera in the corner, export to video. OBS is free and handles screencasts and webcam overlays cleanly. A few students used Zoom or Teams, which they already knew.

## why video works

A written report can be assembled without a coherent understanding of the whole. The right terminology covers a lot. A five-minute video is much harder to fake — students who don't understand their prototype struggle to demonstrate it, and students who haven't thought through their research question can't state it clearly when speaking. It surfaces understanding (or the lack of it) in a way that text doesn't.

There's also something you just don't get from written submissions: a face and a voice. By the end of a 300-student semester I know relatively few students personally. Watching 300 videos means putting a face and a voice to almost every name. Students explain their work in their own words, show enthusiasm or frustration, make jokes, demonstrate what they built. The submissions feel like people rather than documents, and that makes the marking experience something I actually enjoy.

On the practical side: five minutes times 300 is 25 hours of content. That sounds like a lot until you compare it to reading 300 fifteen-page reports. The marking time is bounded, there's much less padding, and the format makes it easy to allocate marking accurately across a team.

## the tools are there

None of this requires specialist equipment. PowerPoint, OBS, and Zoom are enough to record a clear, watchable five-minute video. The challenge for students isn't the recording — it's knowing their work well enough to explain it. Which is the challenge that the assessment is supposed to surface anyway.

I'll definitely keep the video format in HCI and I'm looking for more places to use it. If you're currently asking students for a technical report and want to see whether they actually understand their work, I'd try replacing it with five minutes of video. Enforce the time limit programmatically if you can. You'll probably enjoy marking it more than you expect.
