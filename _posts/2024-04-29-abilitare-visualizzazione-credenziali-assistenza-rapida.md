---
title: "Assistenza Rapida: abilitare la visualizzazione della finestra delle credenziali"
subtitle: "Per poter eseguire un programma come amministratore"
date: 2024-04-29 17:35:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories: [Windows]
tags: [assistenza, rapida, quick, assist, credenziali, uac, pausa, schermata, nera,]
---
- Apri cmd.exe (come utente normale) sul computer remoto.   
- Esegui: **runas /user:Administrator cmd**   
- Incolla la seguente riga che modificherà un valore in una chiave di registro.   

~~~regedit
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v PromptOnSecureDesktop /t REG_DWORD /d 0x0 /f
~~~

In Windows 10 è sufficiente lasciare la group policy di default per avere impostato l'UAC (Controllo Account Utente), mentre per Windows 11 occorre modificare quella chiave di registro oppure appoggiarsi all'MDM InTune di Office 365 per impostarlo in automatico su tutti i PC.   

Vedi anche:   

<a href="https://www.resolve-consulenza.it/ispirazioni/come-risolvere-il-problema-della-schermata-nera-su-quickassist-o-teamviewer-grazie-ad-intune/" target="_blank">https://www.resolve-consulenza.it/ispirazioni/come-risolvere-il-problema-della-schermata-nera-su-quickassist-o-teamviewer-grazie-ad-intune/</a>
