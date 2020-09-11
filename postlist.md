---
layout: page
title: All Posts
---

{% for post in site.posts %}    
- _{{ post.date | date: "%Y %m %d" }}:_ [{{ post.title }}]({{ post.url | absolute_url }})
{% endfor %}
