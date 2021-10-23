---
title: I files eliminati dal desktop riappaiono
date: 2021-10-23 07:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories: [Windows]
tags: [cestino, recylce, files, corrotto, danneggiato, reset, riapparire, folder redirect]
---
Se eliminate dei files dal vostro desktop e vi accorgete che dopo qualche secondo il file riappare, molto probabilmente il cestino di Windows si è corrotto.   

Per resettare e ripristinare il cestino, occorre digitare questo comando che lo eliminerà:   

	rd /s /q C:\$Recycle.bin

Questo comando eliminerà il cestino del disco **C:\**, ma se avete più dischi dovrete eliminare il cestino dell'altro disco cambiando la lettera.   

Se avete abilitato il folder redirect, dovrete eliminare il cestino presente sul server, ad esempio:   

	rd /s /q "D:\Shared Folders\Utenti\<nome_utente>\Desktop\$RECYCLE.BIN"