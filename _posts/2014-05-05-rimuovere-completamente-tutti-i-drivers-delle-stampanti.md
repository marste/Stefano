---
id: 2843
title: Rimuovere completamente tutti i drivers delle stampanti
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2843
permalink: /rimuovere-completamente-tutti-i-drivers-delle-stampanti/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2662464515
categories:
  - Windows
tags:
  - driver
  - printer
  - rimuovere
  - stampante
---
- Riavvia il pc in **modalità provvisoria**

&#8211; Rimuovi il contenuto della seguente directory:

(su 32 bit(x86) computers)  
`C:\Windows\System32\spool\drivers\W32X86`  
(su 64 bit(x64) computers)  
`C:\Windows\System32\spool\drivers\x64`

&#8211; Apri **regedit** e rimuovi tutte le sottodirectory:

(su 32 bit(x86) computers)  
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows NT x86\Drivers\Version-3`  
(su 64 bit(x64) computers)  
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Drivers\Version-3`

&#8211; **Riavvia il pc**