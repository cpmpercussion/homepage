---
layout: post
title: A note on tutorials with Teams
date: 2020-07-16
---

This is part 2 of my series of posts on online teaching in 2020; this time I'm going to write about how we set up _tutorials_ for COMP2300 in Microsoft Teams. 

The previous post was about [online lectures](/blog/2020/07/08/streaming-lectures).

## Why Microsoft Teams?

Teams is Microsoft's workplace chat and collaboration platform. It [comes with Office 365](https://en.wikipedia.org/wiki/Microsoft_Teams) so it's immediately available for all of our ANU students (they can just log into it with their university ID).

It has a pretty good web client, native clients for Windows, MacOS and Linux, and nice mobile clients as well.

So here's the tl;dr of why I use it for teaching:

- A virtual classroom that is **available 24/7** for students to collaborate or ask questions.
- **Chat-first interaction** is handy for keeping track of questions and triaging calls for help.
- Ability for video/audio meetings to occur **spontaneously** between students and teachers.
- Ability to be **in more than one call** at once (this is a bit of a game changer).
- Works with students on **campus**, at **home**, on their **phone**, in **China**, _wherever they are they can engage with the course_.
- Supports gifs in chat, so **high meme productivity**. 

Compared to running classes in Zoom, teams gives you the ability to run meetings and share screens, but also gives persistent asynchronous collaboration through chat which I really prefer for engaging students regularly.

Teams seems to be changing rapidly (makes sense!) There's already heaps more documentation available (e.g., this nice [Education Guide](https://edudownloads.azureedge.net/msdownloads/MicrosoftTeamsforEducation_QuickGuide_EN-US.pdf)) since I started using it in February, so feel free to let me know about new features or workflows!

## Set up a class team

![The COMP2300 Team]({% link assets/blog/2020/3-choose-group.jpg %})

There's a couple of options when creating a new team, I make mine private (invite only for students), and use the ["Class" type](https://support.microsoft.com/en-us/office/choose-a-team-type-to-collaborate-in-microsoft-teams-0a971053-d640-4555-9fd7-f785c2b99e67) for my classes.

I've also used the "other" type for my research lab and other collaborations, but the class type seems to be set up with some limitations for members (students) and extra capabilities for owners (instructors). It comes with some annoying tabs ("assignments", "grades", etc) which can't be deleted -- not sure which Team type is really best for tertiary courses.

## Add channels

![A meeting of tutors and lecturer in Teams]({% link assets/blog/2020/4-lab-channel.jpg %})

Your team starts with a "general" channel, and I like to keep this one for normal announcements and discussions during lectures.

I've added an "instructors" channel for my classes, and made this private. I add all my tutors to this channel so we can have meetings, chat and back-channel discussions.

For COMP2300, we started out with a different private channel for each tutorial group so students **only** belonged to their group. A few weeks into remote learning, we shifted to just having one massive public "labs" channel for all our groups.

We found that many students didn't show up to their tutorials, and some that did wanted to attend more than one. This made sense for the structure of COMP2300, but might not work for classes with, e.g., specific project groups.

For my big class of 400 students, my tutors were a team of their own, so we actually used **another** collaboration tool (Mattermost) for all of our other workplace tasks (e.g., marking, moderation, rosters, tracking issues on Piazza, timesheets). In future, I might just make a separate team for tutors to handle these tasks.

## Meetings

![A meeting of tutors and lecturer in Teams]({% link assets/blog/2020/teams-meeting.png %})

In any channel, anybody can chat, or spontaneously start a meeting by [clicking the little camera icon](https://support.microsoft.com/en-us/office/start-an-instant-meeting-in-teams-ff95e53f-8231-4739-87fa-00b9723f4ef5) below the chat box. Once a meeting has started anybody in the channel can join in.

As you start the meeting, you can give it a name. There might be multiple meetings simultaneously happening in one channel, so good names might become important.

Once a meeting has started, you can record it ([here's the recording instructions](https://support.microsoft.com/en-us/office/record-a-meeting-in-teams-34dfbe7f-b07d-4a27-b4c6-de62f1348c24)). Once it's recorded it stays in the chat so that students can play it back later.

If you want to have a private meeting with a small group, you could invite them to a scheduled meeting (e.g., start from Outlook and schedule a ["New Teams Meeting"](https://support.microsoft.com/en-us/office/schedule-a-teams-meeting-from-outlook-883cc15c-580f-441a-92ea-0992c00a9b0f)), or start an instant meeting in a private channel (this is how I have tutor meetings). You can also just call an individual in Teams from the "calls" pane.

You can add a whiteboard to a meeting, share screens, and even remote control someone else's computer (sortof scary!).

## Running Tutorials

So here's how we actually run tutorials (labs) in Teams (finally!) Our labs are designed to be self-directed programming challenges with opportunities to get help from tutors (e.g., check out our lab on [making a DIY operating system](https://cs.anu.edu.au/courses/comp2300/labs/11-diy-operating-system/)).

![Labs in Teams]({% link assets/blog/2020/teams-labs.png %})

Each lab would work like this:

1. The tutors **start a meeting** in the labs channel to explain the tasks for the lab. They record this meeting so that students arriving late can catch up.
2. The students get to work on the lab exercises and **put any questions or issues in the chat**.
3. If a student asks a question, tutors can either **answer it quickly as a chat** or go into a **call with the student**.
4. We prefer to do **public calls** in the channel to answer questions so that other students can join in and hear what's going on or contribute some ideas as well.
5. Some of my tutors like to go into mini-lectures during labs, so they might **hit record** so the students can catch up on them later.
6. If a student has a question that's _private_ for some reason (e.g., about an individual assignment), the tutor can call them directly through Teams to help.

To catch up with students who don't ask questions during labs, we have a policy that tutors send a **direct chat to each student** in their lab at least once each hour, just to check in. They catch a few extra questions this way.

During the whole lab, the tutors _also_ have a meeting running in their instructors-only channel (you can be in two meetings simultaneously in Teams - although only one is active at a time.)

In future, I think I'd like to encourage students to have independent **group calls** for longer periods of time, even if I'm not running group projects. Hopefully this could just encourage a bit of social connection between them and to help them develop their expectations and ambitions a bit more for submitted work.

## Getting students/tutors into your team

I make my class teams _private_ so students and tutors have to be added or ask permission to join. 

In the little "three dots" menu in the Teams pane you can hit "manage team" and add members directly. All your tutors/co-lecturers should be added as owners. Students should merely be members.

You can also copy a link to the team ("Get link to team" in the "three dots" menu) and put this on Wattle or elsewhere for students to click, then you can add them manually from the "Pending Requests" tab.

The above is ok for small classes, but for lots of students we've used a **PowerShell** script to add users automatically from a CSV (see [this post for instructions](https://medium.com/@joaquin.guerrero/adding-bulk-users-from-a-csv-file-to-a-microsoft-teams-team-374414b9d8c9)).

NB: we're working on a new script for my S2 class, I'll post a link here soon.

## Hosting lectures and videos

All of our lectures for COMP2300 were streamed through Microsoft Stream ([see my post on lectures!](/blog/2020/07/08/streaming-lectures)). You can add a Microsoft Stream channel as a tab in Teams. I did this in COMP2300's general channel. This means that whenever I was lecturing, the students can chat in teams, ask questions, and I can answer them on the spot. Neat!

![Streams in Teams]({% link assets/blog/2020/teams-lectures.png %})

## Does all this it work?

Sure it works--we got through semester 1 with it! I really like how flexible and open Teams is, although the downside is that the interface can be a bit confusing. It's much easier to start a spontaneous meeting in Teams than Zoom, and we know that there are many students who prefer chat to video, particularly for asking questions. Lots of our students also just like to lurk for a while until they build up their confidence (which is fine too!)

A rough look at our analytics for the second half Semester 1 shows that we had roughly 100 students engaging with our Team every weekday during the semester-not too shabby!

![Analytics for teams usage!]({% link assets/blog/2020/teams-sem1-analytics.png %})

I've also got some [instructions for students](https://cs.anu.edu.au/courses/comp2300/resources/online-labs/) for getting started in Teams and online labs.

## Some other features I'd like to try

- **Tags**: You can create tags for groups of users (e.g., "group-1") and then make announcements to a tagged group at once (e.g., "@group-1 - come meet in the general channel!").

## Fun facts

- Our _longest_ Teams meeting was 15 hours during a marking marathon in the exam period. Good times! (marking? good? what is wrong with me?!)

