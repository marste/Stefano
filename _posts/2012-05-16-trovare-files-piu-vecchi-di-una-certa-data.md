---
id: 1184
title: Trovare files più vecchi di una certa data
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1184
permalink: /trovare-files-piu-vecchi-di-una-certa-data/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"202767941337493504";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"202767941337493504";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1911258294
categories:
  - Linux
tags:
  - data
  - date
  - days
  - eliminare
  - files
  - older
  - trovare
  - vecchi
---
Trova tutti i files jpg nella directory cache più vecchi di 90 giorni:  
`find /var/www/html/cache/ -name "*.jpg" -type f -mtime +90 -exec ls -al {} ;`

Elimina tutti i files jpg nella directory cache più vecchi di 90 giorni:  
`find /var/www/html/cache/ -name "*.jpg" -type f -mtime +90 -exec rm -f {} ;`