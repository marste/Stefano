---
title: "Windows 11 non esce ignora, sostituisci o confronta files durante una copia"
author: Stefano Marzorati
date: 2022-10-23 10:30:00 +0200
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [microsoft, windows 11, copia, files, sostituisci, confronta, ignora, replace]
---
- Premi il tasto Windows logo + R per aprire la finestra **Esegui**
- Digita **regedit** e premi **Invio**.
- Vai in:
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
```
- Crea un valore DWORD (32-bit) e chiamalo **HideMergeConflicts** con valore a **0**
- Riavvia il PC.