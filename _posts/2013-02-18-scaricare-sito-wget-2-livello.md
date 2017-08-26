---
id: 1415
title: Scaricare un sito fino al 2° livello
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1415
permalink: /scaricare-sito-wget-2-livello/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 3063119143
categories:
  - Linux
  - Windows
---
`wget -rkpNl2 http://marzorati.co`

-r — Retrieve recursively

-k — Convert the links in the document to make them suitable for local viewing

-p — Download everything (inlined images, sounds, and referenced stylesheets)

-N — Turn on time-stamping

-l2 — Specify recursion maximum depth level 2