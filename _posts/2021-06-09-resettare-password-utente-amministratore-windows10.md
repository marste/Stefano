---
title: "Resettare la password utente o dell'amministratore di Windows 10"
author: Stefano Marzorati
layout: post
redirect_url: https://www.youtube.com/watch?v=TDuXjHDaqeY
date: 2021-06-09 11:05:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [reset, ripristino, password, windows, utilman, wpeutil, net, user]
---
* Avviare dal boot una chiavetta USB o un DVD con Windows 10
* Premere **Avanti** e successivamente **Ripristina il computer**
* **Risoluzione dei problemi** e poi **Prompt dei comandi**
* Digitiamo **diskpart** per vedere su che disco è installato Windows e poi **list volume**
* Andare in **C:\Windows\System32** o se fosse su un altro disco D:\, E:\, etc...
* Digitiamo **move utilman.exe utilman1.exe**
* Digitiamo **copy cmd.exe utilman.exe**
* Riavviamo digitando **wpeutil reboot**
* Al riavvio clicchiamo sull'icona dell'**accessibilità** in modo che parta il prompt dei comandi
* Digitiamo **net user** per vedere i nomi degli utenti locali
* Digitiamo <code>net user administrator *</code> o al posto di administrator il nome dell'utente di cui vogliamo resettare la password
* Diamo **due volte invio** in modo da non mettere nessuna password
* Digitare **exit** e riavviare il PC e come per magia il vostro utente di cui non ricordavate la password accederà senza problemi

Ora rimettiamo a posto i files che abbiamo modificato

* Avviare nuovamente dal boot Windows 10 da USB o DVD
* Premere **Avanti** e successivamente **Ripristina il computer**
* **Risoluzione dei problemi** e poi **Prompt dei comandi**
* Andare in **C:\Windows\System32** o se fosse su un altro disco D:\, E:\, etc...
* Digitiamo **move utilman1.exe utilman.exe** e sovrascrivere il files
* Riavviamo digitando **wpeutil reboot**

<div class="video">
    <iframe src="//www.youtube.com/embed/TDuXjHDaqeY" frameborder="0" allowfullscreen></iframe>
</div>