---
id: 1034
title: Rimuovere Overlay Scrollbars in Ubuntu 11.10
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1034
permalink: /remove-overlay-scrollbar-11-10/
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - overlay
  - remove
  - rimuovere
  - scrollbar
---
`sudo apt-get remove overlay-scrollbar`  
`sudo su`  
`echo "export LIBOVERLAY_SCROLLBAR=0" > /etc/X11/Xsession.d/80overlayscrollbars`