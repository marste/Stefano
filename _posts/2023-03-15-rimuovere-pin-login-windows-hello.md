---
title: 'Rimuovere PIN login in Windows Hello su Windows 10'
subtitle: Eliminare cartella NGC
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
L'eliminazione della cartella **NGC** sarà una soluzione alla domanda su come rimuovere il PIN di accesso da Windows 10.   

- Apri **cmd** come amministratore   
- Digita   
<pre>takeown /f %windir%\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /R</pre>
Digita
<pre>icacls %windir%\ServiceProfiles\LocalService\AppData\Local\Microsoft\NGC /grant administrators:F /t</pre>
- Vai nella cartella
<pre>C:\windows\ServiceProfiles\LocalService\AppData\Local\Microsoft</pre>
- Elimina la cartella **NGC**

- prova1
- prova2 <pre>provaaaa</pre>
- prova3
