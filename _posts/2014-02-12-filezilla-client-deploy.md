---
id: 2730
title: Deploy FileZilla Client
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2730
permalink: /filezilla-client-deploy/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2255484288
categories:
  - Windows
tags:
  - batch
  - client
  - deploy
  - filezilla
---
Crea un file .cmd con le seguenti istruzioni:

	xcopy "\\Server\FileZilla\*" "\\%1\C$\Temp\FileZilla\*.*" /r/i/c/h/k/e   
	sleep 3   
	psexec.exe \\%1 -s "C:\Temp\FileZilla\FileZilla_3.7.4.1_win32-setup.exe" /S