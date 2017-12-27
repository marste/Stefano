---
title: Disinstallare completamente e reinstallare Symantec Endpoint Protection Small Business Edition
date: 2017-12-27 09:25:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://tigerware.lsu.edu/image/e7275ace-8ee7-4baf-9fe7-df2f62e76682.png'
share-img: 'https://tigerware.lsu.edu/image/e7275ace-8ee7-4baf-9fe7-df2f62e76682.png'
permalink: /disinstallare-completamente-reinstallare-symantec-endpoint-protection-small-business-edition/
categories:
  - Software
tags:
  - download
  - removal
  - uninstall
  - symantec
  - antivirus
  - norton
  - tool
---
Procedere con seguenti passaggi per garantire che nulla delle installazioni precedenti possa causare il fallimento della nuova installazione.   

Esegui Norton Removal Tool (Desktop OS) o CleanWipe (Server OS) e riavvia.   

1.	Per i **Desktops** <a href="ftp://ftp.symantec.com/public/english_us_canada/removal_tools/Norton_Removal_Tool.exe" target="_blank">Norton Removal Tool</a>   
	Per i **Servers**, collegamento diretto all'ultima versione disponibile di CleanWipe la trovi nella parte inferiore di questo articolo: <a href="http://www.symantec.com/docs/HOWTO124983" target="_blank">http://www.symantec.com/docs/HOWTO124983</a>   
2.	Esegui **CEDAR Tool** (può essere richiesto il riavvio) <a href="https://ins.spn.com/CEDAR.exe" target="_blank">CEDAR</a>   
3.	Rimuovere il client dalla console di hostendpoint (<a href="https://hostedendpoint.spn.com" target="_blank">https://hostedendpoint.spn.com</a>).   
4.	Esegui **Symantec Removal Tool Extractor v2** <a href="https://symantec.app.box.com/SymantecRemovalToolExtractorV2" target="_blank">Symantec Removal Tool Extractor v2</a>   
5.	Riavvia la macchina   
6.	Se ancora presenti, elimina:   

	C:\ProgramData\Norton   
	C:\ProgramData\NortonInstaller   
	C:\ProgramData\Symantec   
	C:\ProgramData\Symantec Cloud   
 
7.	[Opzionale] Se ancora presente, eliminare le seguenti chiavi del Registro di sistema (eseguire sempre il backup del registro prima di eliminare qualsiasi chiave):   

	HKEY_LOCAL_MACHINE\SOFTWARE\Norton
	HKEY_LOCAL_MACHINE\SOFTWARE\Symantec
	HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Norton
	HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Symantec
 
8.	Log on to <a href="https://hostedendpoint.spn.com" target="_blank">https://hostedendpoint.spn.com</a> > Computers > Add Computers > download a fresh new package.
