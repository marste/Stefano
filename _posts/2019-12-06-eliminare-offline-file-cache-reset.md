---
title: Eliminare offline file cache e fare un reset del database CSC
date: 2019-12-06 16:11:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - Windows
tags:
  - csc-cache
  - offline
  - file
  - cache
  - regedit
  - database
  - reset
---
Apri regedit e vai al seguente percorso:   

	HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Csc\Parameters

Aggiungi una nuova **DWORD** chiamata **FormatDatabase** e dagli valore **1**

Riavvia il PC

Vedrai che i files offline non ci saranno più e la chiave di registro inserita sarà stata eliminata.   

A questo punto per far ripartire la **sincronizzazione** che rimarrà **in sospeso**, dovrete **riavviare il PC o disconnettersi almeno 3 volte**.   
