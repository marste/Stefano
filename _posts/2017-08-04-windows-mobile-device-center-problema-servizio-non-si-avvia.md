---
title: (Solved) Windows 10, Windows Mobile Device Center non si avvia
date: 2017-08-04 08:50:00 +0200
author: Stefano Marzorati
layout: post
permalink: /windows-mobile-device-center-problema-servizio-non-si-avvia/
categories:
  - Windows
tags:
  - windows
  - mobile
  - device
  - center
  - servizio
  - WcesComm
  - CreateSemaphore
---
Se collegando un dispositivo Mobile (esempio: Datalogic Falcon X3+) con Windows CE, non si avvia il programma **Centro Gestione Dispositivi Windows Mobile** e nell'event viewer trovate un errore come il seguente:   

**Event ID 2 - WcesComm**   
*Impossibile avviare il servizio di connettività per dispositivi Windows Mobile 2003 a causa dell'errore CreateSemaphore(0x80070005) (vedere il codice di errore nei dati)*   

Molto probabilmente il servizio di Windows chiamato **Connettività dispositivi Windows Mobile 2003** che dovrebbe essere in avvio automatico, lo troverete non avviato.

Basterà andare in **Proprietà** - **Connessione** e scegliere **Account di sistema locale**, fatto ciò il servizio si avvierà correttamente.

Altre chiavi di ricerca:   

WcesComm CreateSemaphore(0x80070005)   
The Windows 10 Creator update changed some internal Windows services which causes the Windows Mobile Device Center to not work anymore.   
Windows 10 Creators Update: Windows Mobile Device Center message "This app isn't working correctly" or hangs at splash screen   