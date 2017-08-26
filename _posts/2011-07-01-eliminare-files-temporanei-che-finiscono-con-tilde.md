---
id: 912
title: Eliminare files temporanei che finiscono con ~
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=912
permalink: /eliminare-files-temporanei-che-finiscono-con-tilde/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2179016921
categories:
  - Linux
tags:
  - files
  - temporanei
  - tilde
---
Prima controlla se c&#8217;è qualche files:  
`find $HOME -type f -name "*~" -print`  
Poi lo cancelli:  
`find $HOME -type f -name "*~" -print -exec rm {} ;`