---
id: 1997
title: Tagliare video con mplayer e mencoder
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1997
permalink: /tagliare-video-con-mplayer-e-mencoder/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-09-16 10:53:49";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-09-16 10:53:49";}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1935750159
categories:
  - Linux
  - Windows
tags:
  - cut
  - editor
  - mencoder
  - mplayer
  - tagliare
  - video
---
`mplayer -edlout lista.edl video.avi`

Il file lista.edl e&#8217; un file vuoto che diciamo di creare all&#8217;edl per metterci i tempi di inizio e fine degli spezzoni che gli indicheremo.  
Ora guardiamo il video, premiamo il tasto **i** della nostra tastiera quando inizia la scena da tagliare e ripremiamo sempre il tasto **i** quando finisce la scena da tagliare.

Per salvare il video con le scene tagliate:  
`mencoder -oac pcm -ovc copy -edl lista.edl video.avi -o videout.avi`

Invece se vogliamo solo vederlo:  
`mplayer -edl lista.edl video.avi`

Tip:  
Nel file lista.edl ci sono i tempi.  
Per partire da inizio filmato, mettere valore: 0.000000  
Per dirgli, &#8220;taglialo fino alla fine&#8221;, mettere un valore anche più alto di quello con cui termina il video.