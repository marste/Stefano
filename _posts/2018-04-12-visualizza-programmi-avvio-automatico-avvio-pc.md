---
title: Visualizza programmi che si avviano automaticamente all'avvio del PC
date: 2018-04-12 15:00:00 +0200
image: 'http://ramblingcookiemonster.github.io/images/why-powershell/logo.png'
share-img: 'http://ramblingcookiemonster.github.io/images/why-powershell/logo.png'
author: Stefano Marzorati
layout: post
categories:
  - Windows
tags:
  - Windows
  - version
  - OS
  - command
  - cmd
  - remote
  - wmic
  - programmi
  - avvio
  - automatico
  - startup
---
Local PC:
	
	wmic startup get command
	
Remote PC:   
	
	wmic /node:NOME_PC startup get command