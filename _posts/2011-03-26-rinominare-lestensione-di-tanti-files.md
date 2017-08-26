---
id: 662
title: 'Rinominare l&#8217;estensione di tanti files'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=662
permalink: /rinominare-lestensione-di-tanti-files/
dsq_thread_id:
  - 2625793163
categories:
  - Linux
tags:
  - files
  - rename
---
Se volessi rinominare molti files .html in .pdf presenti in una directory:  
``for i in `ls *.html`; do mv ${i} `basename ${i} '.html'`.pdf; done``