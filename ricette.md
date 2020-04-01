---
layout: page
permalink: /ricette/
title: Ricette
---
{% for post in site.categories.ricette %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}