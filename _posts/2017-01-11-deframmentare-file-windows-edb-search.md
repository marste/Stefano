---
title: Deframmentare il file Windows.edb di Windows Search
date: 2017-01-05 18:42:00 +0200
author: Stefano Marzorati
layout: post
permalink: /deframmentare-file-windows-edb-search/
categories:
  - Windows
tags:
  - deframmentare
  - windows
  - windows.edb
  - search
  - dimensioni
  - indice
  - outlook
  - wsearch
---
Se il file **Windows.edb** ha raggiunto dimensioni eccessive è possibile deframmentarlo.   

**Chiudi Outlook**   
Modificare il servizio Windows Search in modo che non venga automaticamente avviato:   

<code>sc config wsearch start=disabled</code>

Eseguire il comando seguente per arrestare il servizio Windows Search:   

<code>net stop wsearch</code>

Eseguire il comando seguente per eseguire la compressione non in linea del file Windows.edb:   

<code>esentutl.exe /d %AllUsersProfile%\Microsoft\Search\Data\Applications\Windows\Windows.edb</code>

Eseguire il comando seguente per eseguire la compressione non in linea del file Windows.edb:   

<code>sc config wsearch start=delayed-auto</code>

Eseguire il comando seguente per avviare il servizio:   

<code>net start wsearch</code>

Stoppando il servizio Windows Search è anche possibile eliminare il file e alla ripartenza il file verrà ricreato.