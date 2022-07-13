---
title: "Chiavetta USB dimensione errata"
subtitle: "Come risolvere il problema"
author: Stefano Marzorati
date: 2022-07-13 08:30:00 +0200
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [chiavetta, usb, dimensione, sbagliata, errata, diskpart, disco]
---
- Apri il **Prompt dei comandi**
- Digita **diskpart**
- Seleziona la chiavetta USB, es. **sel disk 1**
- Digita **clean** per eliminare tutte le partizioni presenti nel supporto USB
- Digita **create partition primary** per creare un'unica partizione primaria

A questo punto sarà sufficiente formattarla.