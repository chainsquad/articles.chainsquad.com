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
 <span class="time">[{{post.date | date: "%-d %B %Y"}}]</span>
 <a class="overview-link" href="{{ post.url }}">{{ post.title }}</a>
 <span class="excerpt">{{ post.excerpt }}</span>
</div>
{% endfor %}
