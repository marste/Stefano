---
title: Page redirect con index.php
author: Stefano Marzorati
layout: post
permalink: /redirect-page-index-php/
categories:
  - Windows
  - Linux
tags:
  - page
  - redirect
  - index
  - php
  - apache
---

Se volete dirottare tutto il traffico del vostro sito internet verso un altro indirizzo, potete farlo con un file [index.html](http://marzorati.co/redirect-page-index/) oppure se il vostro server legge il codice php, con un file index.php   

All'interno della root del vostro sito, create un file index.php con questo contenuto:   

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #557799">&lt;?php</span>

header(<span style="background-color: #fff0f0">&quot;location: http://www.dominionuovo.com&quot;</span>);

<span style="color: #557799">?&gt;</span>
</pre></div>
