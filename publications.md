---
layout: page
title: Publications
permalink: /publications/
---

## Book Chapters

{% bibliography --query @*[keywords ~= book-chapter && keywords ~= refereed] %}

## Refereed Journal Articles

{% bibliography --query @*[keywords ~= journal-article && keywords ~= refereed] %}

## Refereed Conference Proceedings

{% bibliography --query @*[keywords ~= conference-paper && keywords ~= refereed] %}

## Other Publication Outputs

{% comment %}

### Articles Under Review

{% bibliography --query @*[keywords ^= under-review] %}

### Non-Refereed Conference Proceedings

{% bibliography --query @*[keywords ^= conference-paper && keywords ^= non-refereed] %}

{% endcomment %}

### Conference Presentations

{% bibliography --query @*[keywords ^= conference-presentation] %}

### Open-Source Code Projects

{% bibliography --query @*[keywords ^= open-source] %}

### Open Data Sets

{% bibliography --query @*[keywords ^= open-data] %}

### Selected Research-Led Artistic Performances

{% bibliography --query @*[keywords ^= artistic-performance] %}

### Selected Music Recordings

{% bibliography --query @*[keywords ^= music-recording] %}
