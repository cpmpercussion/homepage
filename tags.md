---
layout: page
title: Tags
description: "Browse all blog posts by topic tag."
permalink: /tags/
---

<div id="active-filter" class="mb-3 d-none">
  <span class="text-secondary">Filtered by tag:</span>
  <strong id="active-tag-name"></strong>
  <a href="/tags/" class="btn btn-sm btn-outline-secondary ms-2">Clear</a>
  <button class="btn btn-sm btn-outline-secondary ms-2" id="show-all-tags-btn">Browse all tags</button>
</div>

<div id="tag-cloud" class="d-flex flex-wrap gap-2 mb-4">
{% assign tag_names = "" | split: "" %}
{% for tag in site.tags %}
  {% assign tag_names = tag_names | push: tag[0] %}
{% endfor %}
{% assign tag_names = tag_names | sort_natural %}
{% for tag_name in tag_names %}
  {% assign tag_posts = site.tags[tag_name] %}
  <a href="/tags/?tag={{ tag_name | url_encode }}"
     class="btn btn-sm btn-outline-secondary rounded-pill tag-filter-btn"
     data-tag="{{ tag_name | downcase }}">
    {{ tag_name }} <span class="ms-1 opacity-75">{{ tag_posts.size }}</span>
  </a>
{% endfor %}
</div>

<div id="post-list">
{% for post in site.posts %}
<div class="post-item border-bottom py-2" data-tags="{{ post.tags | join: '|' | downcase }}">
  <small class="text-secondary me-2">{{ post.date | date: "%d %b %Y" }}</small>
  <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
  {% if post.tags.size > 0 %}
  <span class="ms-2">
    {% for tag in post.tags %}<a href="/tags/?tag={{ tag | url_encode }}"
       class="badge rounded-pill text-decoration-none me-1"
       style="font-size:0.7rem;"
       data-tag="{{ tag | downcase }}">{{ tag }}</a>{% endfor %}
  </span>
  {% endif %}
</div>
{% endfor %}
</div>

<script>
(function () {
  var params = new URLSearchParams(window.location.search);
  var activeTag = (params.get('tag') || '').toLowerCase().trim();

  if (!activeTag) return;

  document.getElementById('active-filter').classList.remove('d-none');
  document.getElementById('active-tag-name').textContent = params.get('tag');
  document.getElementById('tag-cloud').classList.add('d-none');

  var showBtn = document.getElementById('show-all-tags-btn');
  showBtn.addEventListener('click', function () {
    document.getElementById('tag-cloud').classList.toggle('d-none');
    showBtn.textContent = document.getElementById('tag-cloud').classList.contains('d-none') ? 'Browse all tags' : 'Hide tags';
  });

  document.querySelectorAll('.post-item').forEach(function (el) {
    var tags = el.dataset.tags ? el.dataset.tags.split('|') : [];
    el.style.display = tags.includes(activeTag) ? '' : 'none';
  });

  document.querySelectorAll('.tag-filter-btn').forEach(function (el) {
    if (el.dataset.tag === activeTag) {
      el.classList.remove('btn-outline-secondary');
      el.classList.add('btn-secondary');
    }
  });
})();
</script>
