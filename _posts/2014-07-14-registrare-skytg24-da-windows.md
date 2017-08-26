---
id: 2905
title: Registrare SkyTG24 da Windows
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2905
permalink: /registrare-skytg24-da-windows/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2842536907
categories:
  - Windows
tags:
  - dump
  - mplayer
  - registrare
  - salvare
  - skytg24
---
Usando <a href="http://sourceforge.net/projects/mplayerwin/" title="mplayer" target="_blank">mplayer</a> per Windows puoi salvare su file SkyTG24 lanciando il seguente comando:

`mplayer -dumpstream -dumpfile c:\skytg24.avi rtmp://212.243.210.71:1935/live?_fcs_vhost=cp49989.live.edgefcs.net/streamRM1@2564`