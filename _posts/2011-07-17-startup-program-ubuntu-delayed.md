---
id: 928
title: Startup program ubuntu delayed
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=928
permalink: /startup-program-ubuntu-delayed/
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - delayed
  - pidgin
  - program
  - startup
  - startup application
  - ubuntu
---
Lancia  
`gnome-session-properties`  
per poter avere la lista dei programmi da caricare all&#8217;avvio (startup application)  
Poi aggiungi:  
`sh -c "sleep 10 && pidgin &"`