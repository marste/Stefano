---
id: 1065
title: Modificare i fonts di Fedora come in Ubuntu
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1065
permalink: /fonts-fedora-like-ubuntu/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"151780099706990592";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"151780099706990592";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1923202421
categories:
  - Linux
tags:
  - fedora
  - fonts
  - like
  - ubuntu
---
`yum install freetype-freeworld`  
`gsettings set org.gnome.settings-daemon.plugins.xsettings hinting slight`  
`gsettings set org.gnome.settings-daemon.plugins.xsettings antialiasing rgba`  
`echo "Xft.lcdfilter: lcddefault" > ~/.Xresources`  
riavvia e poi scrivi:  
`xrdb -query`  
deve uscire questo  
` Xft.antialias: 1 Xft.dpi: 96 Xft.hinting: 1 Xft.hintstyle: hintslight Xft.lcdfilter: lcddefault Xft.rgba: rgb `  
Ora installa i fonts di Ubuntu, vedi [questo][1].

 [1]: http://ubbunti.wordpress.com/2011/08/14/installare-i-fonts-di-ubuntu-anche-su-altre-distribuzioni-linux/