---
title: "Aggiungere il gruppo di Amministratori locali come owner di files e cartelle"
subtitle: "da Command Line"
date: 2022-03-07 07:53:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/microsoft.png'
share-img: 'https://marzorati.co/img/microsoft.png'
layout: post
categories: [Windows]
tags: [owner, proprietario, files, cartelle, administrator, locale, commandline]
---
Esempi:   

	takeown /F "D:\Shared Folders\Test\Prova\*.doc" /A

	takeown /F "D:\Shared Folders\Test\Prova\*.*" /A /R

**/A** Questo comando fa diventare proprietario il gruppo di amministratori locali invece dell'utente corrente   
**/R** Modifica ricorsivamente il proprietario di tutti i file e le cartelle nidificati nella directory specificata   
