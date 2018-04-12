---
title: Visualizza programmi che si avviano automaticamente all'avvio del PC
date: 2018-04-12 15:00:00 +0200
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
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