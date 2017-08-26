---
id: 34
title: Installare Orta Theme
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/installare-orta-theme
permalink: /installare-orta-theme/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 3202667970540910907
  - 3202667970540910907
  - 3202667970540910907
categories:
  - Linux
tags:
  - theme
---
`sudo add-apt-repository ppa:nikount/orta-desktop`  
`sudo apt-get update`  
`sudo apt-get install orta-theme`

`sudo add-apt-repository ppa:tiheum/equinox`

`sudo apt-get update && sudo apt-get install faenza-icon-theme`

Cambiare dimensione delle icone:

You can change it yourself, if you installed the theme manually goto  
`~/.themes/Orta/gtk-2.0/`  
and if you have installed it via ppa goto  
`/usr/share/themes/Orta/gtk-2.0/`  
and open the gtkrc file you will find there. At line 13 you will find this :  
`gtk-icon-sizes = "panel-menu=22,22:gtk-button=16,16"`  
change it to this :  
`gtk-icon-sizes = "panel-menu=16,16:gtk-button=16,16"`  
save the file and reload the theme.