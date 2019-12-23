---
layout: post
title: Christmas Carillon at the Canberra Centre
date: 2019-12-23
categories:
- news
tags:
- research
- carillon
- music
- canberra
---

This week I've been talking about our [Christmas carillon installation at the Canberra Centre](https://cecs.anu.edu.au/news/christmas-bells-ring-canberra-thanks-musical-ai).

![Christmas Carillon Clavier at the Canberra Centre]({{site.baseurl}}/assets/blog/2019/20191223-carillon1.jpg)

The National Capital Authority has been upgrading the National Carillon and replaced the clavier, they asked me to help create electronic sensors and sounds for the old clavier as part of a Christmas installation.

The carillonists, including Thomas Laue from the ANU School of Music had recorded a couple of Christmas Carols and some new bell samples for us to use. I worked with Terry McGee to make some modifications to the keyboard that would hold the batons up with springs and Alistair Riddell who built a sensor system using magnetic field sensors.

![A test rig with one carillon baton and the Bela]({{site.baseurl}}/assets/blog/2019/20191223-carillon3.jpg)

I coded up the electronic sounds and connections to the sensor board using the [Bela](https://bela.io) platform, this was great because the installation needed to work continuously in the Canberra Centre for the whole of December (and it has!). We used magnetic field sensors to trigger the sounds so that we wouldn't have any parts that could wear out in the clavier. Terry build a little test baton for us to make sure it would work.

![One octave of sensors installed on the carillon]({{site.baseurl}}/assets/blog/2019/20191223-carillon4.jpg)

After we settled on parts in our test rig, Terry made some aluminium fingers to hold magnets in the clavier. This way, the sensors could be securely attached to a board and visible in case we need to make adjustments. We installed the sensors and Bela and put the finishing touches on the software so that it would sound the way we wanted.

It's always great to hear the first "real sound" out of a new musical instrument and it was especially so with this carillon. It's pretty uncommon to actually be able to "test out" a carillon keyboard without annoying a whole city, so we had a bit of fun in Thomas' office getting this to work before sending it off to be installed. The final configuration had 16 "working" batons, 13 played carillon samples (C to C) and the remaining three triggered one Christmas carol each.

![A close up of the carillon clavier's batons]({{site.baseurl}}/assets/blog/2019/20191223-carillon2.jpg)

And here it is in the Canberra centre! It's been up and running for about four weeks now, slowly counting down the days to Christmas! Sitting and watching it for a while, I noticed that it's (of course) popular with kids who jump in to see what does, but also adults can help but reach out to ring a bell as they walk by. Certainly fun, but hopefully this gives a bit of insight into how our carillon actually works and what the musicians do who play it! It should be up and running all through Christmas until the 3rd of January 2020.
