---
id: 1168
title: Device or resource busy
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1168
permalink: /device-or-resource-busy/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"194717155055517697";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"194717155055517697";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1910405653
categories:
  - Linux
tags:
  - busy
  - device
  - lsof
  - resource
---
Se mentre stai cancellando un file, ti appare questo errore: device or resource busy , con un comando puoi vedere quale servizio sta utilizzando quel file:  
`lsof +D /path`