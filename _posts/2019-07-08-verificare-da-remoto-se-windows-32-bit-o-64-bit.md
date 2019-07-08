---
title: Verificare da remoto se Windows è a 32 bit o 64 bit
date: 2019-07-08 17:40:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories:
  - Windows
tags:
  - Windows
  - version
  - wmic
  - command
  - cmd
  - remote
  - os
  - 32bit
  - 64bit
  - architecture
---
Local PC:
	
	wmic wmic OS get OSArchitecture
	
Remote PC:   
	
	psexec \\nome_pc wmic OS get OSArchitecture
