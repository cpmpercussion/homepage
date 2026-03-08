---
layout: page
title: Computer Music Workshops
permalink: /workshops/
description: "Workshops and tutorials on computer music, intelligent musical interfaces, and musical AI by Charles Martin."
tags: [workshops, computer music, machine learning, music technology, tutorials]
---

Here's a list of workshops and talks that I give related to computer music, intelligent musical interfaces, and musical AI.

## Workshops

- [Creative Prediction with Deep Neural Networks](https://cpmpercussion.github.io/creative-prediction)

## Classes and Tutorials

{% assign posts = site.posts | where_exp: "item", "item.categories contains 'workshop'" %}

{% for post in posts %}
- _{{ post.date | date: "%Y %m %d" }}:_ [{{ post.title }}]({{ post.url | absolute_url }})
{% endfor %}
