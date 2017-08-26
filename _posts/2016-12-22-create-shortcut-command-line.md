---
title: Create shortcut from command line
date: 2016-12-22 14:42:00 +0200
author: Stefano Marzorati
layout: post
permalink: /create-shortcut-command-line/
categories:
  - Windows
tags:
  - create
  - shortcut
  - windows
  - mklink
  - commandline
  - secpol
---
Ecco il comando che ti servirà per creare un collegamento ad un file:   

<code>mklink nome_da_dare_al_link file_di_destinazione</code>

Se ti esce il seguente messaggio, vorrà dire che non sei abilitato a lanciare il comando **mklink**, per cui o lo lanci come administrator oppure dai gli accessi a chi vuoi per poterlo eseguire:   

> Non si dispone di privilegi sufficienti per eseguire questa operazione.   

Per dare gli accessi ad eseguire questo comando:   

Esegui: **secpol.msc**   
Apri: **Security Settings → Local Policies → User Rights Assignment**   
Nella lista trova **Create symbolic links**   
Doppio click sulla voce e aggiungi l'utente o il gruppo desiderato   
