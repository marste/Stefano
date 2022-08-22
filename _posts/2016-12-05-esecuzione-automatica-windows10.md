---
title: Esecuzione Automatica in Windows 10
date: 2016-12-05 09:42:00 +0200
author: Stefano Marzorati
layout: post
permalink: /esecuzione-automatica-windows10/
categories:
  - Windows
tags:
  - percorso
  - path
  - esecuzione
  - automatica
  - windows10
---
Percorso dei programmi da avviare in automatico **per tutti gli utenti** del PC:   
```
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```
oppure da **Esegui** digita:   
```
shell:common startup
```
---
Percorso dei programmi da avviare in automatico **per solo un utente**:   
```
C:\Users\profilo_utente\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
oppure da **Esegui**, digita:   
```
shell:startup
```