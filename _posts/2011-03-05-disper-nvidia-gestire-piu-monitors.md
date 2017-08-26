---
id: 27
title: Disper Nvidia (gestire più monitors)
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/disper-nvidia-gestire-piu-monitors
permalink: /disper-nvidia-gestire-piu-monitors/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8926687646883543453
  - 8926687646883543453
  - 8926687646883543453
categories:
  - Linux
tags:
  - nvidia
---
`sudo add-apt-repository ppa:disper-dev/ppa`  
`sudo apt-get update`  
`sudo apt-get install disper`

Esempio:

`#!/bin/bash   
disper -S -r 1360x768`

<http://maketecheasier.com/change-linux-displays-on-the-fly-with-disper/2010/12/22>