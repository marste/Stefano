---
title: How to deploy TightVNC remotely
date: 2015-07-06 10:15:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /how-to-deploy-tightvnc-remotely/
categories:
  - software
tags:
  - deploy
  - vnc
  - remotely
  - script
  - tightvnc
  - psexec
  - batch
---
Ecco lo script che ho fatto per installare TightVNC in remoto, in modalità silent sui vari PC dell'azienda.
Copiare il contenuto in un file .cmd:   

	xcopy "\\server\Applicazioni\Tightvnc\tightvnc-2.7.10-setup-64bit.msi" "\\%1\C$\temp\*.*" /r/i/c/h/k/e
	xcopy "\\server\Applicazioni\Tightvnc\tvnc.txt" "\\%1\C$\temp\*.*" /r/i/c/h/k/e
	
	psexec \\%1 -s -d msiexec /i "C:\temp\tightvnc-2.7.10-setup-64bit.msi" ADDLOCAL="Server" SET_RUNCONTROLINTERFACE=1 VALUE_OF_RUNCONTROLINTERFACE=0 SET_PASSWORD=1 VALUE_OF_PASSWORD=password SET_USECONTROLAUTHENTICATION=1 VALUE_OF_USECONTROLAUTHENTICATION=1 SET_CONTROLPASSWORD=1 VALUE_OF_CONTROLPASSWORD=password SET_REMOVEWALLPAPER=1 VALUE_OF_REMOVEWALLPAPER=0 /quiet /norestart /l* log.txt
	
	sleep 15
	
	psexec \\%1 -s -d c:\WINDOWS\regedit.exe /s "C:\temp\tvnc.txt"
	
	tvnviewer.exe %1


Questo è il contenuto del file tvnc.txt:   

	Windows Registry Editor Version 5.00
	
	[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\tvnserver]
	"Type"=dword:00000010
	"Start"=dword:00000003
	"ErrorControl"=dword:00000001
	"ImagePath"=hex(2):22,00,43,00,3a,00,5c,00,50,00,72,00,6f,00,67,00,72,00,61,00,\
	6d,00,20,00,46,00,69,00,6c,00,65,00,73,00,5c,00,54,00,69,00,67,00,68,00,74,\
	00,56,00,4e,00,43,00,5c,00,74,00,76,00,6e,00,73,00,65,00,72,00,76,00,65,00,\
	72,00,2e,00,65,00,78,00,65,00,22,00,20,00,2d,00,73,00,65,00,72,00,76,00,69,\
	00,63,00,65,00,00,00
	"DisplayName"="TightVNC Server"
	"ObjectName"="LocalSystem"
	"FailureActions"=hex:00,00,00,00,00,00,00,00,00,00,00,00,01,00,00,00,14,00,00,\
	00,01,00,00,00,88,13,00,00
	"DelayedAutostart"=dword:00000001

La chiave **"Start"=dword:00000003** sta ad indicare che il servizio verrà messo in modalità manuale, di modo che verrà avviato da me solo a richiesta.   
Se volete lasciarlo in automatico, come è di default, potete evitare di importare il registro tvnc.txt, oppure modificare il valore a 2.
