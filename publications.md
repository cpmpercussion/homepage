---
layout: page
title: Publications
permalink: /publications/
---

# Book Chapters

{% bibliography --query @*[keywords ~= book-chapter && keywords ~= refereed] %}

# Refereed Journal Articles

{% bibliography --query @*[keywords ~= journal-article && keywords ~= refereed] %}

# Refereed Conference Proceedings

{% bibliography --query @*[keywords ~= conference-paper && keywords ~= refereed] %}

# Other Publication Outputs

## Articles Under Review

{% bibliography --query @*[keywords ^= under-review] %}

## Non-Refereed Conference Proceedings

{% bibliography --query @*[keywords ^= conference-paper && keywords ^= non-refereed] %}

## Non-Refereed Conference Presentations

{% bibliography --query @*[keywords ^= conference-presentation] %}

## Open-Source Code Projects

{% bibliography --query @*[keywords ^= open-source] %}

## Open Data Sets

{% bibliography --query @*[keywords ^= open-data] %}

## Selected Research-Led Artistic Performances

{% bibliography --query @*[keywords ^= artistic-performance] %}

## Selected Music Recordings

{% bibliography --query @*[keywords ^= music-recording] %}

<script>
// map our commands to the classList methods
const fnmap = {
  'toggle': 'toggle',
    'show': 'add',
    'hide': 'remove'
};
const collapse = (selector, cmd) => {
  const targets = Array.from(document.querySelectorAll(selector));
  targets.forEach(target => {
    target.classList[fnmap[cmd]]('show');
  });
}

// Grab all the trigger elements on the page
const triggers = Array.from(document.querySelectorAll('[data-toggle="collapse"]'));
// Listen for click events, but only on our triggers
window.addEventListener('click', (ev) => {
  const elm = ev.target;
  if (triggers.includes(elm)) {
    const selector = elm.getAttribute('data-target');
    collapse(selector, 'toggle');
  }
}, false);
</script>
