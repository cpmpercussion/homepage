---
layout: post
title: A day at the In2Change - 1
categories: []
tags:
- In2Change
- supercollider
status: publish
type: post
published: true
meta: {}
description: "mp3 - 12MB The concept behind this piece is to recreate the sounds of Belconnen bus interchange over a regular weekday. I used the daily timetable at the"
---

[mp3 - 12MB](http://files.me.com/cpmartin/hvucv1.mp3)

The concept behind this piece is to recreate the sounds of Belconnen bus interchange over a regular weekday. I used the daily timetable at the bus interchange as the "score" in this piece, recorded sounds of buses arriving and departing at the interchange are triggered with each scheduled bus in the timetable.

I used Supercollider to read a CSV file of the bus schedule, at each event in the schedule Supercollider plays one of the bus sounds that I recorded. The schedule is read at a tempo of 1.5 minutes per second so that the piece (first bus 0548, last bus 2411) takes about 12 minutes. Now that I have accomplished my main technical goal I can concentrate on refining the aesthetic outcome. 

One problem with the piece as it is that there is not enough variation over the 12 minutes to capture the idea of a day going past. The sounds are engaging, but there needs to be a constantly moving mood.

A second problem is that the shape of the schedule is not clear from the piece. There are most buses in the hours of 7-10 and 15-18 but because the tempo is fast (for a whole day) and the bus sounds blend into each other, this is not quite clear just from listening.

The solutions I have is to use many more bus samples and to discern between samples recorded during a quiet part of the day and those taken in a busy period.
