---
title: Utilizzo della CPU e della Memoria di un PC remoto
date: 2017-08-30 09:00:00 +0200
author: Stefano Marzorati
layout: post
categories:
  - Windows
tags:
  - cpu
  - memory
  - memoria
  - remote
  - commandline
  - wmic
---
Per visualizzare la percentuale di processore utilizzata di un PC remoto, digita:   
<code>wmic /node:NOME_PC cpu get loadpercentage</code>   

Per visualizzare la percentuale di memoria utilizzata di un PC remoto, digita:   
<code>wmic /node:NOME_PC OS get FreePhysicalMemory</code>   

Il valore ottenuto sarà espresso in **Kilobyte**, per cui basterà dividerlo per **1.048.576** per ottenere il valore in **Gigabyte**   

In alternativa potete installare <a href="https://lizardsystems.com/downloads/index.php#remote-process-explorer" target="_blank">Remote Process Explorer</a> per poter gestire i processi dei PC remoti in tempo reale.   

| bit | byte | Kilobyte | Megabyte | Gigabyte |
| :--- |:--- | :--- | :--- | :--- |
| bit 1 | byte 1 |  |
| byte 8 | Kilobyte 1.024 | Kilobyte 1 |
| Kilobyte 8.192 | Megabyte  1.048.576 | Megabyte 1.024 |
| Megabyte  8.388.608 | Gigabyte  1.073.741.824 | Gigabyte  1.048.576 |