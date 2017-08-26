---
title: Eliminare file più vecchi di n giorni sotto Windows
date: 2017-02-28 09:15:00 +0200
author: Stefano Marzorati
layout: post
permalink: /eliminare-file-piu-vecchi-n-giorni-windows/
categories:
  - Windows
tags:
  - eliminare
  - files
  - vecchi
  - giorni
  - forfiles
---
Esempio:   

<code>Forfiles /p C:\MG12Backup /s /m *.bak /d -15 /c "cmd /c del /q @path"</code>   

Il comando lanciato, controllerà la directory e sottodirectory di MG12Backup e controllerà se ci sono files con estensione .bak più vecchi di 15 giorni.   
In tal caso andrà ad eliminare i files più vecchi di 15 giorni.   

Se volete provare lo script senza far cancellazioni di files, potete digitare il seguente comando:   

<code>Forfiles /p C:\MG12Backup /s /m *.bak /d -5 /c "Cmd /C Echo 0x22@Path\@File0x22"</code>

Con alcuni comandi esplicati:   
**p** = path   
**s** = cerca anche nelle subdirectory del path principale   
**m** = file con criteri (mark) specificati   
**d** = ultima modifica più vecchia di (giorni)   
**c** = esegui il comando   
<BR>