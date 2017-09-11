---
layout: page
title: Tags
subtitle: Browse this blog by tag.
---

<div class="home">
	<h1 class="page-heading">All tags</h1>

	<p class="post-meta" style="text-align: justify;">
	{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
	{% assign tags = site_tags | split:',' | sort %}
	{% include tagcloud.html %}
	</p>
</div>

<hr>
