---
id: 1165
title: Non aggiornare un pacchetto specifico
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1165
permalink: /non-aggiornare-un-pacchetto-specifico/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"193345243188436993";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"193345243188436993";}}}'
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - aggiornare
  - lock
  - packages
  - ubuntu
---
Ad esempio, se non voglio che venga più aggiornato flash, basta scrivere:  
`echo flashplugin-installer hold | sudo dpkg --set-selections`  
Se poi decido di rimantenerlo aggiornato:  
`echo flashplugin-installer install | sudo dpkg --set-selections`