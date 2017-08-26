---
title: Spostare i dati del WSUS in un percorso differente
date: 2015-05-12 15:15:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /spostare-dati-WSUS-percorso-differente/
categories:
  - Software
tags:
  - wsus
  - move
  - data
  - microsoft
  - update
  - services
---
  - Aprire la console mmc di **Windows Server Update Services** - **Opzioni** - **Pulizia guidata server**   

Facendo ciò verranno rimossi dal server i files degli aggiornamenti più vecchi e non più utilizzati.   

  - Creare la cartella sul nuovo disco o sul nuovo percorso in cui verrano "spostati" i files del WSUS.   

Finita la pulizia, andare da prompt dei comandi al percorso:   

`C:\Program Files\Update Services\Tools`   

e lanciare il seguente comando di esempio:   

`wsusutil.exe movecontent D:\Wsus\ D:\move.log`   

dove *D:\Wsus* sarà il nuovo percorso e *D:\move.log* il percorso dove salvare il log dello spostamento.   

Una volta terminata la copia avrete nel log le operazioni fatte:   

	2015-05-12T12:12:20 Successfully stopped WsusService.
	2015-05-12T12:12:20 Beginning content file location change to D:\WsusContent\
	2015-05-12T12:33:10 Successfully copied content files.
	2015-05-12T12:33:10 Successfully copied application files.
	2015-05-12T12:33:10 Successfully changed WUS configuration.
	2015-05-12T12:33:11 Successfully changed IIS virtual directory path.
	2015-05-12T12:33:11 Successfully removed existing local content network shares.
	2015-05-12T12:33:11 Successfully created local content network shares.
	2015-05-12T12:33:11 Successfully changed registry value for content store directory.
	2015-05-12T12:33:11 Successfully changed content file location.
	2015-05-12T12:33:14 Successfully started WsusService.
	2015-05-12T12:33:14 Content integrity check and repair...
	2015-05-12T12:33:14 Initiated content integrity check and repair.

A questo punto al prossimo aggiornamento di update di WSUS verranno condivise come prima le directory WsusContent e UpdateServicesPackages

I files vecchi potranno essere poi rimossi manualmente.
