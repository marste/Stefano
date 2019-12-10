---
title: Abilitare e schedulare le Shadow Copy in Windows 10
date: 2019-12-10 15:58:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - Windows
tags:
  - shadow
  - copy
  - abilitare
  - schedulare
  - swprv
  - eliminare
  - reset
---
Eseguire come amministratore il comando **cmd** ed avviare due servizi, il primo è "Provider di copie shadow software Microsoft:   

	net start swprv

e l'altro è "Copia shadow del volume"

	net start vss

Se questi due servizi erano in "**Manuale**", consiglio di metterli in "**Automatico (avvio ritardato)**"   

Poi creare una shadowcopy, eseguire il seguente comando:   

	wmic shadowcopy call create Volume=c:\

Se volete farlo in automatico, sarà sufficiente schedularlo con il **Task Scheduler** di Windows.   

Lo spazio che potranno occupare al massimo le shadow copy è quello impostato in "Protezione Sistema"

	Pannello di controllo\Sistema\Protezione Sistema
