---
title: Enable Windows Update to force Windows 10 upgrade via regedit
date: 2016-04-15 11:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /enable-windows-update-to-force-windows-10-upgrade/
categories:
  - Windows
tags:
  - Windows10
  - upgrade
  - regedit
  - update
  - AllowOSUpgrade
---
Apri regedit e vai in questo percorso:

	HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\OSUpgrade

Troverai la voce **AllowOSUpgrade** impostala a **1**   

Rilancia il Windows Update o dal prompt il comando:   

	wuauclt /detectnow
	
Verrà notificato l'aggiornamento a Windows 10 con il successivo download (circa 3GB) e la successiva richiesta di installazione pianificata.
