---
id: 2409
title: 'WordPress Themes: display post excerpts o full'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2409
permalink: /wordpress-themes-display-post-excerpts-full/
authorsure_include_css:
  - 
dsq_thread_id:
  - 1900633899
layout_key:
  - 
post_slider_check_key:
  - 0
categories:
  - Linux
  - Windows
tags:
  - completo
  - estratto
  - excerpt
  - full
  - theme
  - wordpress
---
Cercare all&#8217;interno dei files del tema che stai utilizzando, la funzione:

`<?php the_content(); ?>` se attualmente vedi il post completo

oppure

`<?php the_excerpt(); ?>` se attualmente vedi un estratto del post.

Ti consiglio di guardare nei possibili files:  
content.php, index.php, archive.php, category.php.. etc.. etc..

Se utilizzate il theme <a href="http://wordpress.org/themes/customizr" target="_blank">Customizr</a> il file da modificare è il seguente:

`/themes/customizr/parts/class-content-post_list.php`