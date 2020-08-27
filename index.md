---
layout: default
ref: home
lang: en
permalink: /
priority: 0
---

# <strong>🖇 Articles</strong><br />

{{ site.vision }}

<hr />
{% for post in site.posts %}
<div>
 <div class="overview-link">
  <a href="{{ post.url }}">{{ post.title }}</a>
  <div class="time">[{{post.date | date: "%-d %B %Y"}}]</div>
 </div>
 <span class="excerpt">{{ post.excerpt }}</span>
</div>
{% endfor %}
