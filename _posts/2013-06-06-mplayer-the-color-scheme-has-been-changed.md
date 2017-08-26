---
id: 1577
title: 'mplayer &#8211; The color scheme has been changed'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1577
permalink: /mplayer-the-color-scheme-has-been-changed/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1981610136
categories:
  - Windows
---
Se usate **mplayer.exe** su Windows 7, magari preso da <a href="http://sourceforge.net/projects/mplayerwin/files/latest/download?utm_campaign=updater&#038;utm_medium=email&#038;utm_source=subscribers" target="_blank">http://sourceforge.net/projects/mplayerwin/files/latest/download?utm_campaign=updater&#038;utm_medium=email&#038;utm_source=subscribers</a> e all&#8217;avvio di un filmato avete uno sfarfallio del video con il messaggio &#8220;**The color scheme has been changed**&#8220;, nessun problema, ecco la soluzione:

Aggiungi la seguente riga al file &#8220;**config**&#8221; all&#8217;interno della directory &#8220;**mplayer**&#8221; (use Notepad or another text editor):

`vo=direct3d`

MPlayer uses the directx video driver by default which causes that and needs to be changed to direct3d or gl. Prefer direct3d over gl.