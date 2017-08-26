---
title: Flash Player Deploy
author: Stefano Marzorati
layout: post
permalink: /flash-player-deploy-remote-install/
categories:
  - Windows
tags:
  - deploy
  - flash
  - install
  - player
  - remote
---
<code>xcopy "\\Server\Software\Windows\Utility\Flash Player\install_flash_player_11_active_x.exe" "\\%1\C$\Temp" /r/i/c/h/k/e</code>   
<code>sleep 3</code>   
<code>pskill iexplore.exe \\%1</code>   
<code>psexec.exe \\%1 -s "C:\Temp\install_flash_player_11_active_x.exe" /install</code>   

<a href="http://www.adobe.com/products/flashplayer/distribution3.html" target="_blank">http://www.adobe.com/products/flashplayer/distribution3.html</a>