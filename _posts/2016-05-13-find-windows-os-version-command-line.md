---
title: Find windows OS version from command line
date: 2016-05-13 15:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'http://ramblingcookiemonster.github.io/images/why-powershell/logo.png'
share-img: 'http://ramblingcookiemonster.github.io/images/why-powershell/logo.png'
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