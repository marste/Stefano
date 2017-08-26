---
title: Responsive YouTube and Vimeo Videos
author: Stefano Marzorati
layout: post
permalink: /responsive-youtube-vimeo-videos/
comments: true
categories:
  - Varie
tags:
  - responsive
  - youtube
  - vimeo
  - videos
  - css
---
Inserisci nel tuo file .css questo codice:

```
.video-responsive{
    overflow:hidden;
    padding-bottom:56.25%;
    position:relative;
    height:0;
}
.video-responsive iframe{
    left:0;
    top:0;
    height:100%;
    width:100%;
    position:absolute;
}
```

Quando vorrai postare un video, non dovrai far altro che aggiungere la classe `video-responsive` in questo modo:

```
<div class="video-responsive">
    <iframe width="420" height="315" src="//www.youtube.com/embed/2GxWs54v2d0" frameborder="0" allowfullscreen></iframe>
</div>
```
