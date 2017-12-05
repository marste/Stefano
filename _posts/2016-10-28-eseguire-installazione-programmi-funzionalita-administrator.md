---
title: Eseguire "Programmi e funzionalità" come Administrator
date: 2016-10-28 12:25:00 +0200
author: Stefano Marzorati
image: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
share-img: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
layout: post
permalink: /eseguire-installazione-programmi-funzionalita-administrator/
categories:
  - Windows
tags:
  - eseguire
  - installazione
  - applicazioni
  - administrator
  - appwiz.cpl
---
	runas /user:dominio\administrator "control appwiz.cpl"
	
	runas /username:siit\Administrator "rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl"