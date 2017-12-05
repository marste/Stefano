---
title: Uptime di un PC Windows Remoto
date: 2016-07-19 09:50:00 +0200
author: Stefano Marzorati
image: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
share-img: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
layout: post
permalink: /uptime-pc-remoto-windows/
categories:
  - Windows
tags:
  - systeminfo
  - uptime
  - remote
  - machine
  - commandline
  - avvio
  - sistema
  - windows
---
Il comando da digitare è il seguente:   

	systeminfo /s nome_pc_remoto | find "Tempo di avvio sistema"

Se fosse un PC con Windows in inglese:   

	systeminfo /s nome_pc_remoto | find "System Up Time"