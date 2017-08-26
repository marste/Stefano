---
title: Visualizzare l'indice di prestazioni di un PC con Windows 10
date: 2017-02-10 17:15:00 +0200
author: Stefano Marzorati
layout: post
permalink: /indice-prestazioni-windows-10-powershell/
categories:
  - Windows
tags:
  - windows10
  - indice
  - prestazioni
  - powershell
---
Il comando da digitare in PowerShell come amministratore, è il seguente:   
<code>Get-WmiObject -Class Win32_WinSAT</code>   

L'indice di prestazioni Windows valuta i componenti chiave del sistema, in base ad una **scala da 1,0 a 7,9**   

* CPUScore - Prestazioni del processore
* D3DScore - Prestazioni scheda video per Grafica e giochi
* DiscScore - Prestazioni del disco rigido principale
* GraphicsScore - Prestazioni scheda video Desktop Graphics
* MemoryScore - Prestazioni della memoria RAM
* WinSPRLevel - Punteggio base
