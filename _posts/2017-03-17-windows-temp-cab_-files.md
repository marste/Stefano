---
title: Windows Temp is full of cab_xxxx files
date: 2017-03-17 15:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /windows-temp-cab_-files/
categories:
  - Windows
tags:
  - windows
  - temp
  - cab
  - files
  - pieno
  - enormi
  - giganti
---
Se vi trovate un PC con il disco pieno e avete scoperto che son stati creati migliaia di files giganti in <code>C:\Windows\Temp</code>, fai così:   

- Stoppa il servizio di **Windows Update**   

Se è un PC remoto, digita il seguente comando:   
<code>psexec -s -d \\Nome_PC net stop "Windows Update"</code>   

- Elimina i files contenuti nella directory <code>C:\Windows\Temp</code>   

- Rinomina la directory **SoftwareDistribution**   

- Avvia il servizio di **Windows Update**   

Se è un PC remoto, digita il seguente comando:   
<code>psexec -s -d \\Nome_PC net start "Windows Update"</code>   

- Elimina la vecchia directory **SoftwareDistribution**   

- Stoppa il servizio **TrustedInstaller**   

Se è un PC remoto, digita il seguente comando:   
<code>psexec -s -d \\Nome_PC net stop "TrustedInstaller"</code>   

- Elimina i files CAB dalla directory <code>C:\Windows\Logs\CBS</code>   

- Avvia il servizio **TrustedInstaller**   

Se è un PC remoto, digita il seguente comando:   
<code>psexec -s -d \\Nome_PC net start "TrustedInstaller"</code>   
