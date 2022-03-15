---
title: "Impossibile conettersi la stampante"
subtitle: "Codice Errore 0x8007011b"
date: 2022-03-15 07:53:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories: [Windows]
tags: [printer, impossibile, collegare, stampante, server, spool, 0x8007011b]
---
Se da alcuni PC non riuscite a collegare la stampante al vostro **Printer Server** e avete il messaggio **Impossibile connettersi alla stampante** e nell' event viewer trovate il codice di errore **0x8007011b**, procedete così:   

Andate nel registro del vostro Printer Server:   

	HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Print\

Create una **DWORD**: **RpcAuthnLevelPrivacyEnabled=0**

Riavviate il servizio **Print Spooler"