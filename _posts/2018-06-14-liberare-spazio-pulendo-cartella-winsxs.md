---
title: Liberare spazio pulendo la cartella WinSXS
subtitle: In Windows 10
date: 2022-06-10 10:28:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [cleanup, folder, windows, winsxs, liberare, spazio, pulire]
---
Per verificare quanto spazio occupa effettivamente la cartella WinSxS, digita:   

	dism /Online /Cleanup-Image /AnalyzeComponentStore

Nella parte inferiore del report si leggerà **Pulizia archivio componenti consigliata**.   
Se ci sarà come risposta un **sì**, procedere con il seguente comando per rimuovere gli elementi non più utilizzati da Windows:   

	dism /online /Cleanup-Image /StartComponentCleanup
