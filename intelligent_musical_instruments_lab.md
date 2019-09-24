---
layout: page
title: Intelligent Musical Instruments Lab
permalink: /imilab/
---

## Research Goals

![Performing on touchscreens and percussion]({{site.baseurl}}/assets/images/performing/metatone-hands-header.jpg)

The goal of the intelligent musical instruments lab is to create new kinds of musical instruments that sense and understand music. These instruments will actively respond during performances to assist musicians.

We envision that musical instruments of the future will do more than react to musicians. They will predict their human player’s intentions and sense the current artistic context. Intelligent instruments will use this information to shape their sonic output. They might seamlessly add expression to sounds, update controller mappings, or even generate notes that the performer hasn’t played (yet!).

The idea here is not to put musicians out of work. We want to create tools that allow them to reach ever-higher levels of artistic expression, and that assist novice users in experiencing the excitement and flow of performance. Imagine an expert musician recording themselves on different instruments in their studio, and then performing a track with a live AI-generated ensemble, trained in their style. Think of a music student who can join their teachers in a jazz combo, learning how to follow the form of the song without worrying about playing wrong notes in their solo.

We think that combining music technology with AI and machine learning can lead to a plethora of new musical instruments. Our mission is to develop new intelligent instruments, perform with them, and bring them to a broad audience of musicians and performers. Along the way, we want to find out what intelligent instruments mean to musicians, to their music-making process, and what new music these tools can create!

Our work combines three cutting edge fields of research:

- **Expressive Musical Sensing**: Understanding how music is played and what performers are doing. This involves hardware prototyping, creating new hyper-instruments, and applying cutting-edge sensors.
- **Musical Machine Learning**: Creating and training predictive models of musical notes, sounds, and gestures. This includes applying techniques symbolic music generation, to understand scores and MIDI data,  and music information retrieval to "hear" music in audio data.
- **Musical Human-Computer Interaction**: Finding new ways for predictive models to work with musicians, and to analyse the musical experience that emerges.

## Projects

### Intelligent Musical Prediction System (IMPS)

The [Intelligent Musical Prediction System (IMPS)]({{site.baseurl}}/imps/) is a system for connecting musicians and interface developers with deep neural networks. IMPS connects with any musical interface or software using open sound control (OSC) and helps users to record a dataset, train a neural network and interact with it in real-time performance. See it in action in demo video below:

{% include youtubePlayer.html id="Kdmhrp2dfHw" %}

<!-- https://youtu.be/Kdmhrp2dfHw -->

### Physical Musical RNN

This project was to develop a physically encapsulated musical neural network. The box contains a Raspberry running a melody-generating recurrent neural network that continually composes music. You can adjust the sound, tempo, the ML-model used, and the "randomness" of the chosen samples to guide the music making process.

<!-- <div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/TKRIuWAYyrhkxZxzEp" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>
 -->
{% include youtubePlayer.html id="2RDVyOTRAj4" %}

<!-- https://youtu.be/2RDVyOTRAj4 -->

### PhaseRings for ML-connected touchscreen ensemble

PhaseRings is a touchscreen instrument that works with an ML-connected ensemble. A server tracks the four performer's improvisations and adjusts their user interface during the performance to give them access to different notes and sounds on their screens.

![Musicians performing on ML-enhanced touchscreen instruments]({{site.baseurl}}/assets/images/teaching/ipad-ensemble.jpg)

{% include youtubePlayer.html id="aDEQMLwd8ok" %}

<!-- https://youtu.be/aDEQMLwd8ok -->

### Self-playing, sensor-driven guitars

This installation of six, self-playing sensor-driven guitars was developed as part of collaborations at the University of Oslo's RITMO Centre for Interdisciplinary Studies in Rhythm, Time and Motion. Each guitar uses a [Bela](https://bela.io) embedded computer to generate sounds from a speaker driver attached to the guitar body. A distance sensor track the movement of listeners in the environment and the guitars use a firefly synchronisation algorithm to phase in and out of time. 

![Self-playing sensor-driven guitars]({{site.baseurl}}/assets/images/performing/bela-guitars2.jpg)

<!--

Summer project goals:
Team project: Create an AI-enhanced band.
Need ML-interactions for each performer in a small band (e.g., Jazz combo: bass, drums, piano, and sound engineer).
Sound engineer: Apply techniques of Intelligent Music Production to assist a sound engineer in making a live or recorded mix of a band. This could include mic-placement, volume, EQ, panning, and application of audio effects.
Piano: Need to use a cutting model such as Music Transformer to alternate between playing a song's melody, comping, and soloing. We will need to study data of each type of performance.
Drums: We need to study drummer's playing styles to apply expression to stable drumset loops and introduce variations, fills, and stylistic changes.
Bass: We need to develop 

-->
