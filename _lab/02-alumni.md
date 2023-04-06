---
layout: page
title: Lab alumni and graduated students
permalink: /lab/grads/
summary: Links to research from lab alumni.
---

Here's some links to research produced by my PhD, Master and Honours students.

If you'd like to work on something like this, check out the details [here]({% link _lab/01-join.md %}).

{% for person in site.data.lab-alumni %}
#### [{{ person.name }}]({{ person.url }}) ({{ person.title }} {{ person.dates }}) 

{{ person.project-title }} {% if person.thesis-url %}[(thesis)]({{ person.thesis-url }}){% endif %}

{{ person.note }}

{% endfor %}


{% comment %}
{% endcomment %}
