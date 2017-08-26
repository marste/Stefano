---
id: 984
title: Effetti 3D senza compiz, ma solo con Metacity
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=984
permalink: /effetti-3d-senza-compiz-ma-solo-con-metacity/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2167978944
categories:
  - Linux
tags:
  - 3d
  - compiz
  - compositing
  - metacity
---
Alt+F2  
gconf-editor  
Andare in: /apps/metacity/general/compositing_manager e mettere la spunta

oppure scrivere nel terminal:  
`gconftool-2 -s '/apps/metacity/general/compositing_manager' --type bool true`