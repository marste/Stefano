---
title: "Errore NTFS FILE SYSTEM su Windows 10"
author: Stefano Marzorati
date: 2020-11-03 09:31:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - windows
tags:
  - error
  - ntfs
  - file
  - system
  - bsod
  - windows10
---
Se visualizzi la schermata blu **NTFS_FILE_SYSTEM** e non hai idea di cosa fare, non sei solo.   
Anche molti utenti di Windows 10 segnalano questo problema. Ecco una risoluzione che nel mio caso ha funzionato.   

- Quando tenta di avviarsi il PC e non ci riesce, si vedrà la schermata **Preparing Automatic Repair**.   
Quando Windows non si avvia correttamente, viene visualizzata questa schermata e Windows tenta di risolvere il problema da solo.

- Partirà la schermata **Diagnosing you PC**

- Poi apparirà la schermata **Startup Repair** con due opzioni: **Shut Down** oppure **Advanced Options**
- Poi click su **Troubleshoot** - **Advanced option** - **CommandPrompt**

Digitare: <code>chkdsk /f c:</code> e alla fine <code>exit</code>

Spegnere il PC e riaccenderlo.