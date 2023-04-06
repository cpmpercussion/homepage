---
layout: page
title: "SMCCLAB: Sound, Music and Creative Computing Lab"
permalink: /lab/
hidden: true
---

The Sound, Music and Creative Computing Lab is part of the  [School of Computing](https://comp.anu.edu.au) at the Australian National University.

The goal of the lab is to create **new kinds of musical instruments** that **sense** and **understand** music. These instruments will actively respond during performances to assist musicians.

![Performing on touchscreens and percussion]({{site.baseurl}}/assets/images/performing/metatone-hands-header.jpg)

We envision that musical instruments of the future will do more than react to musicians. They will **predict their human player’s intentions** and **sense the current artistic context**. Intelligent instruments will use this information to shape their sonic output. They might seamlessly add expression to sounds, update controller mappings, or even generate notes that the performer hasn’t played (yet!).

The idea here is not to put musicians out of work. We want to create tools that allow **musicians** to reach the highest levels of **artistic expression**, and that assist **novice users** in experiencing the **excitement and flow of performance**. Imagine an expert musician recording themselves on different instruments in their studio, and then performing a track with a live AI-generated ensemble, trained in their style. Think of a music student who can join their teachers in a jazz combo, learning how to follow the form of the song without worrying about playing wrong notes in their solo.

We think that combining music technology with AI and machine learning can lead to a plethora of new musical instruments. **Our mission is to develop new intelligent instruments, perform with them, and bring them to a broad audience of musicians and performers**. Along the way, we want to find out what intelligent instruments mean to musicians, to their music-making process, and what new music these tools can create!

Our work combines three cutting edge fields of research:

- **Expressive Musical Sensing**: Understanding how music is played and what performers are doing. This involves hardware prototyping, creating new hyper-instruments, and applying cutting-edge sensors.
- **Musical Machine Learning**: Creating and training predictive models of musical notes, sounds, and gestures. This includes applying techniques symbolic music generation, to understand scores and MIDI data,  and music information retrieval to "hear" music in audio data.
- **Musical Human-Computer Interaction**: Finding new ways for predictive models to work with musicians, and to analyse the musical experience that emerges.

## Current Lab Members

{% for person in site.data.lab-members %}
- [{{ person.name }}]({{ person.url }}) ({{ person.title }})
{% endfor %}

([list of lab alumni and former students]({% link _lab/02-alumni.md %}))

## Lab Pages

{% assign labposts = site.posts | where: "type", "lab" %} 
{% assign labpages = site.lab | concat: labposts %}

<section class="row">
{% for entry in labpages %}
{% unless entry.hidden %}
<div class="col-sm-4 p-3">
<div class="card">
{% if entry.image %}
<img class="card-img-top" src="{{ entry.image }}" alt="{{ entry.image_alt }}">
{% endif %}
<div class="card-body">
<h5 class="card-title"><a href="{{ entry.url | relative_url }}">{{ entry.title }}</a></h5>
{{ entry.summary }}
<a class="card-link" href="{{ entry.url | relative_url }}">read more</a>
</div>
</div>
</div>
{% endunless %}
{% endfor %}
</section>

## SMCClab Projects

Projects from Charles and other members of the lab.

{% assign labprojects = site.data.lab-projects %}

<section class="row">
{% for entry in labprojects %}
{% unless entry.hidden %}
<div class="col-sm-6 p-3">
<div class="card">
{% if entry.image %}
<img class="card-img-top" src="{% link {{entry.image}} %}" alt="{{ entry.image_alt }}" style="object-fit: cover; width: 100%; height: 30vh;">
{% endif %}
<div class="card-body">
<h5 class="card-title">{{ entry.title }}</h5>
{{ entry.summary }}
{% if entry.youtube %}
<a href="https://youtu.be/{{ entry.youtube }}">video</a>
{% endif %}
</div>
</div>
</div>
{% endunless %}
{% endfor %}
</section>


{% comment %}
style="object-fit: cover; width: 100%; height: 40vh;"
<!-- <a href="{{ entry.url | relative_url }}"> -->


Summer project goals:
Team project: Create an AI-enhanced band.
Need ML-interactions for each performer in a small band (e.g., Jazz combo: bass, drums, piano, and sound engineer).
Sound engineer: Apply techniques of Intelligent Music Production to assist a sound engineer in making a live or recorded mix of a band. This could include mic-placement, volume, EQ, panning, and application of audio effects.
Piano: Need to use a cutting model such as Music Transformer to alternate between playing a song's melody, comping, and soloing. We will need to study data of each type of performance.
Drums: We need to study drummer's playing styles to apply expression to stable drumset loops and introduce variations, fills, and stylistic changes.
Bass: We need to develop 

Individual Projects:
- Enhance aspects of IMPS (Intelligent Music Prediction System)
- Develop new MIR metrics for application in future collaborations. How do we know that generated signals are good?

{% endcomment %}
