---
id: 995
title: Masterizzare un file ISO da command line
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=995
permalink: /burn-iso-command-line/
authorsure_include_css:
  - 
dsq_thread_id:
  - 1953198348
categories:
  - Linux
tags:
  - burn
  - command line
  - iso
  - masterizzare
  - terminal
---
`sudo apt-get install wodim`  
`wodim -devices` (x sapere il nome del masterizzatore)  
Esempio:  
`wodim dev=/dev/scd0 driveropts=burnfree fs=14M speed=10 -dao -eject -overburn -v fileiso.iso`