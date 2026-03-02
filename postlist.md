---
layout: page
title: All Posts
description: "Complete archive of all blog posts by Charles Martin on music, technology, research, and performance."
tags: [blog, posts, archive]
---

{% for post in site.posts %}    
- _{{ post.date | date: "%Y %m %d" }}:_ [{{ post.title }}]({{ post.url | absolute_url }})
{% endfor %}
