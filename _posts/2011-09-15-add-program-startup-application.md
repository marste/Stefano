---
id: 982
title: Aggiungere un programma nelle startup application
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=982
permalink: /add-program-startup-application/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2173030681
categories:
  - Linux
tags:
  - add
  - aggiungere
  - application
  - automatico
  - avvio
  - programma
  - startup
---
Prendiamo l&#8217;esempio di voler aggiungere Empathy nella lista delle &#8220;Startup Applications&#8221;  
`sudo cp /usr/share/applications/empathy.desktop /etc/xdg/autostart</span>   
<span style="font-family:monospace;">sudo chmod a+r /etc/xdg/autostart/empathy.desktop`