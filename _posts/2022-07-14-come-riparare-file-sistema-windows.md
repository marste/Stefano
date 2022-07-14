---
title: "Come riparare i file di sistema di Windows"
subtitle: "Usando CHKDSK, SFC e DISM"
author: Stefano Marzorati
date: 2022-07-14 08:30:00 +0200
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [riparare, file, sistema, windows, disco, chkdsk, sfc, dism]
---
- Digiti **cmd** nella barra di ricerca di Windows
- Clicca con il pulsante destro su **Prompt dei comandi**
- Seleziona **Esegui come amministratore**

Da quì potete lanciare diversi tools.   

**CHKDSK (Check Disk)**   
Esegue la scansione dell'unità per trovare settori danneggiati e tenta di correggere gli errori nel file system.

	chkdsk /F /R C:

**SFC (Controllo file di sistema)**   
SFC verifica la presenza di file importanti mancanti del tuo sistema operativo Windows e li ripristina dalla cache.

	sfc /scannow

**DISM (Manutenzione e gestione delle immagini di distribuzione)**   
DISM si occupa direttamente delle immagini Windows difettose e le ripara scaricando i file sostitutivi effettivi dai server online di Windows.

	DISM /Online /Cleanup-Image /CheckHealth
	DISM /Online /Cleanup-Image /ScanHealth
	DISM /Online /Cleanup-Image /RestoreHealth
	
