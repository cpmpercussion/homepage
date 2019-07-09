---
layout: page
title: Publications
permalink: /publications/
---

<!-- <style>
// Bibliography boxes
*, ::after, ::before {
    box-sizing: border-box;
}
.collapse {
  display: block;
  max-height: 0px;
  overflow: hidden;
  /*transition: max-height .5s cubic-bezier(0, 1, 0, 1);*/
&.show {
    max-height: 99em;
    /*transition: max-height .5s ease-in-out;*/
  }
}
</style> -->

{% bibliography %}

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