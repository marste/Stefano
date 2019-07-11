---
title: Utilizzo della CPU e della Memoria di un PC remoto
date: 2017-08-30 09:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
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
  - pslist
---
Per visualizzare la <span style="background-color:yellow">percentuale di processore</span> utilizzata di un PC remoto, digita:   

	psexec \\nome_pc wmic cpu get loadpercentage   
	
oppure potete digitare:   

	pslist \\nome_pc -s

oppure, se volete monitorare un singolo processo (PID)   

	pslist \\nome_pc <pid> -s

Per visualizzare la <span style="background-color:yellow">percentuale di memoria utilizzata</span> di un PC remoto, digita:   

	psexec \\nome_pc wmic OS get FreePhysicalMemory

Il valore ottenuto sarà espresso in **Kilobyte**, per cui basterà dividerlo per **1.048.576** per ottenere il valore in **Gigabyte**   

In alternativa potete installare <a href="https://lizardsystems.com/downloads/index.php#remote-process-explorer" target="_blank">Remote Process Explorer</a> per poter gestire i processi dei PC remoti in tempo reale.   
