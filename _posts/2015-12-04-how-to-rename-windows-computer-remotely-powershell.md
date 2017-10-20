---
title: How to rename a Windows Computer remotely with PowerShell
date: 2015-12-04 15:42:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /how-to-rename-windows-computer-remotely-powershell/
image: 'http://ramblingcookiemonster.github.io/images/why-powershell/logo.png'
share-img: 'http://ramblingcookiemonster.github.io/images/why-powershell/logo.png'
categories:
  - Windows
tags:
  - commandline
  - rename
  - remotely
  - powershell
  - name
  - computer
  - script
---
Questo comando richiede almeno la versione 3.0 di PowerShell   

	Rename-Computer -NewName NuovoNome -ComputerName VecchioNome -DomainCredential Dominio\Administrator