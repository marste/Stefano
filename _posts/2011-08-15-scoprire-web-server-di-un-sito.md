---
id: 949
title: Scoprire web server di un sito
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=949
permalink: /scoprire-web-server-di-un-sito/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2093929738
categories:
  - Linux
  - Windows
tags:
  - apache
  - find
  - iis
  - web server
---
`curl -Is http://www.google.com | grep -E "^Server"`