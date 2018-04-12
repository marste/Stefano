---
title: Find windows OS version from command line
date: 2016-05-13 15:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
permalink: /find-windows-os-version-command-line/
categories:
  - Windows
tags:
  - Windows
  - version
  - OS
  - command
  - cmd
  - remote
---
Local PC:
	
	wmic os get Caption,CSDVersion /value
	
Remote PC:   
	
	wmic /node:NOME_PC os get Caption,CSDVersion /value