---
title: 'Rimuovere PIN login in Windows Hello su Windows 10'
subtitle: Eliminare cartella Ngc
author: Stefano Marzorati
layout: post
date: 2023-03-15 07:25:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [pin, windows, hello, remove, rimuovere, impronta, digitale]
---
Ngc è la cartella che memorizza tutti i dati del PIN di Windows Hello sul PC.   
È possibile rimuovere il PIN disattivando ed eliminando questa cartella.   
L'eliminazione della cartella **Ngc** sarà una soluzione alla domanda su come rimuovere il PIN di accesso da Windows 10.   

- Apri **cmd** come amministratore
- Digita <code>takeown /f %windir%\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /R</code>
- Digita <code>icacls %windir%\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t</code>
- Vai nella cartella <code>C:\windows\ServiceProfiles\LocalService\AppData\Local\Microsoft</code>
- Elimina la cartella **NGC**