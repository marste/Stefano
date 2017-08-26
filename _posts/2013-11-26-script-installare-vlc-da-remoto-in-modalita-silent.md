---
id: 2521
title: 'Script: installare VLC da remoto in modalità Silent'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2521
permalink: /script-installare-vlc-da-remoto-in-modalita-silent/
authorsure_include_css:
  - 
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 2000629263
categories:
  - Windows
tags:
  - deploy
  - remote
  - silent
  - vlc
---
`xcopy "\\Server\VLC\vlc-2.1.1-win32.exe" "\\%1\C$\Temp\*.*" /r/i/c/h/k/e`   
`psexec \\%1 -s -d "C:\Temp\vlc-2.1.1-win32.exe" /L=1033 /S`