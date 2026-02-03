---
title: "News"
permalink: /news/
author_profile: true
---

# News & Updates

<div class="news-list">
{% for item in site.news reversed %}
  <div class="news-item">
    <span class="news-date">
      {{ item.date | date: "%Y · %b" }}
    </span>
    <p class="news-text">
      <strong>{{ item.title }}</strong><br>
      {{ item.content | strip_html | truncate: 160 }}
    </p>
  </div>
{% endfor %}
</div>
