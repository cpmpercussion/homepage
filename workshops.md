---
layout: page
title: Computer Music Workshops
---

Here's a list of workshops and talks that I give related to computer music, intelligent musical interfaces, and musical AI.

## Workshops

- [Creative Prediction with Deep Neural Networks](https://creativeprediction.xyz)

## Classes and Tutorials

{% assign posts = site.posts | where_exp: "item", "item.categories contains 'workshop'" %}

{% for post in posts %}    
- _{{ post.date | date: "%Y %m %d" }}:_ [{{ post.title }}]({{ post.url | absolute_url }})
{% endfor %}


