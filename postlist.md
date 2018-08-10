---
layout: page
title: Post List
categories: []
tags: []
status: publish
type: page
published: true
meta: {}
---

A list of all posts:

{% for post in site.posts %}    
- {{ post.date | date: "%Y %m %d" }} - [{{ post.title }}]({{ post.url | absolute_url }})
{% endfor %}