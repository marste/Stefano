---
title: "Impossibile avviare Windows, file windows danneggiato o mancante"
author: Stefano Marzorati
layout: post
categories:
  - Windows
tags:
  - danneggiato
  - mancante
  - Windows
---
Solitamente c&#8217;è qualche settore danneggiato sull&#8217;hard disk.

Ma vediamo come far ripartire Windows

**Fai partire il PC dal CD di Windows XP** come se si volesse eseguire una nuova installazione.

Selezioniamo **R per avviare la console di ripristino**.

Ci verrà chiesto quale installazione ripristinare. Normalmente su disco è presente una sola installazione in &#8220;C:\WINDOWS&#8221;, selezioniamo quindi il numero corrispondente e premiamo invio.

Spostiamoci nella directory:  
**C:\Windows\system32\config**

Rinominiamo il file danneggiato:  
**ren system system.bad**

Ripristiniamo il file di backup di windows digitando il comando:

**copy c:\windows\repair\system**

Questo metodo può essere applicato per i seguenti files:

&#8211; system  
&#8211; software  
&#8211; SECURITY  
&#8211; SAM  
&#8211; ntuser.dat  
&#8211; default  
&#8211; config.nt  
&#8211; autoexec.nt

Una volta ripristinati tutti i file in errore possiamo chiudere la console di ripristino digitando il comando &#8220;exit&#8221; ed estraendo il cd di installazione.

Al riavvio del pc, occorrerà probabilmente reinstallare alcuni drivers di Windows.
