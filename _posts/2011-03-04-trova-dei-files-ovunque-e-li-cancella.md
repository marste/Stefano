---
id: 7
title: Trova dei files ovunque e li cancella
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/04/trova-dei-files-ovunque-e-li-cancella
permalink: /trova-dei-files-ovunque-e-li-cancella/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 645485731987010142
  - 645485731987010142
  - 645485731987010142
dsq_thread_id:
  - 2030356612
categories:
  - Linux
tags:
  - delete
  - files
  - find
---
Esempio:

Trova tutti i file .cache in dir e nelle sottodirectory e li cancella

`find . -name "*.cache" -exec rm -rf {} ;`