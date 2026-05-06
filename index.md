---
layout: default
ref: home
lang: en
permalink: /
priority: 0
---

<div class="mb-10">
  <p class="text-xs text-primary font-bold uppercase tracking-[0.15em] mb-3">// articles</p>
  <p class="text-muted-foreground text-sm leading-relaxed">{{ site.vision }}</p>
</div>

<ul class="flex flex-col gap-4">
{% for post in site.posts %}
  <li class="flex flex-col gap-2 border-l-2 border-gray-200 pl-5">
    <div class="flex items-center justify-between gap-4">
      <div class="flex gap-1.5 flex-wrap">
        {% for tag in post.tags limit:3 %}
        <span class="text-xs font-medium uppercase tracking-wider text-gray-400 border border-gray-200 rounded px-1.5 py-0.5">{{ tag }}</span>
        {% endfor %}
      </div>
      <time class="text-xs text-gray-400 whitespace-nowrap">{{ post.date | date: "%b %-d, %Y" }}</time>
    </div>
    <a href="{{ post.url }}" class="text-base font-semibold text-gray-900 hover:text-gray-600 leading-snug">{{ post.title }}</a>
    <p class="text-sm text-gray-500 leading-relaxed">{{ post.excerpt | strip_html | truncate: 200 }}</p>
  </li>
{% endfor %}
</ul>
