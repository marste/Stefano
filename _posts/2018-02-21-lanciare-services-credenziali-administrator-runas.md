---
layout: post
title: Lanciare services.msc con credenziali di Administrator usando runas
date: '2018-02-21 10:00:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories:
  - Windows
tags:
  - esegui
  - programmi
  - windows
  - run
  - services.msc
  - command line
published: true
---
**Elevate Permission to Stop/Restart Services**   

	runas /user:Domain\Administrator "mmc.exe \"services.msc\""

**Shutdown a PC from the Command Prompt**   

	runas /user:Domain\Administrator "shutdown -s -t 0"

**Restart a PC from the Command Prompt**   

	runas /user:Domain\Administrator "shutdown -r -t 0"

**Elevate Permissions to Edit the Registry**   

	runas /user:Domain\Administrator "regedit.exe"

**Elevate Permissions to run CMD commands**   

	runas /user:Domain\Administrator "cmd.exe"

**Elevate Permissions to Modify Local Policy**   

	runas /user:Domain\Administrator "mmc.exe \"gpmc.msc\""

**Elevate Permissions to View Security Events**   

	runas /user:Domain\Administrator "eventvwr.exe"

**Elevate Permissions to Manage Network Computers**   

	runas /user:domain\Domain\Administrator "mmc.exe \"compmgmt.msc\""
