---
layout: post
title: 'Review: Distributed Network Data by Alasdair Allan and Kipp Bradford; O''Reilly
  Media'
categories:
- review
tags:
- review
- arduino
- data
- book
status: publish
type: post
published: true
description: "Capture sensor data! Send it over a network! But then what? Great guide to building a wireless Arduino sensor node, not much on interpretation."
---

![Capture sensor data! Send it over a network! But then what?]({{ site.baseurl }}/assets/squarespace_images/2013-06-25-DistributedNetworkData.jpg) 

Capture sensor data! Send it over a network! But then what? 

## Great guide to building a wireless Arduino sensor node, not much on interpretation.

"Distributed Network Data" is a beginner's guide to building a swarm of wirelessly-connected Arduino-powered "motes" or sensor nodes.

This book takes the reader step by step through the process of creating an Arduino based sensor node equipped with a combined temperature and humidity sensor, a motion sensor, and a microphone. This sensor "mote" is connected to a receiving computer via an XBee wireless module. On the receiving side, we connect a master XBee directly to a computer to receive data from one or more "motes", log it all to a text file and graph it with Processing or LabVIEW.

The authors nailed the two chapters dedicated to setting up the XBee wireless modules - a tricky topic! They cut through the subtle variations of XBees available and carefully explain the surprisingly low-level setup (think typing arcane commands into a serial terminal). Another great section demonstrates how to avoid soldering a messy circuit by using the Arduino's digital IO pins to supply power and ground to the simple components. This cool trick saves space as well as battery power by allowing you to switch sensors off in between samples.

After such thorough chapters on wiring up all of these gizmos, I missed the detail in the section on visualising the data which was limited to graphing readings from a single temperature and humidity sensor. Once you've got a couple of motion detectors, noise level recorders and climate sensors set up, how do you make connections between the data from different sensor nodes and how do you visualise it all together? The authors make no attempts to answer this hard question even though the back cover suggests that we would be “performing real-time analysis on data captured by a deployed multi-sensor network”. I felt a bit let down that we missed out on this final crucial step.

Overall - grab this (inexpensive!) book for the great Arduino walkthroughs but don't expect a lot of help in understanding the output.

(PS, I reviewed this book as part of the O'Reilly Blogger Review Program!)
