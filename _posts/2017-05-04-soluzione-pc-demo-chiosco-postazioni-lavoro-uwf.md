---
title: Unified Write Filter (UWF) - Soluzione per PC Demo o chioschi
date: 2017-05-04 11:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /soluzione-pc-demo-chiosco-postazioni-lavoro-uwf/
categories:
  - Windows
tags:
  - windows
  - uwf
  - soluzione
  - chiosco
  - PC
  - postazione
  - demo
---
Il filtro Unified Write Filter (UWF), consente di ridirigere in memoria tutte le scritture fatte su disco, rendendo perciò disponibili le modifiche fatte in una sessione di utilizzo, solo fino allo spegnimento del sistema.   
Questa caratteristica può essere usata per preparare macchine dimostrative, postazioni didattiche, chioschi per il pubblico, postazioni di lavoro, ecc...   
Un riavvio sarà sufficiente per avere una macchina alla pari di una "nuova", sempre pronta per il prossimo utente.   
Tutte le operazioni di configurazione, verranno effettuate tramite il prompt dei comandi, come amministratore, usando il comando **uwfmgr.exe**.   
L’abilitazione del filtro, si occuperà di configurare il sistema in modo da evitare inutili scritture su disco. Memoria virtuale, punti di ripristino, deframmentazione ed indicizzazione dei file devono essere disattivati.   

**Per proteggere il disco C:\ di sistema:**   

<code>uwfmgr.exe volume protect c:</code>   

**Il sistema UWF permette anche di escludere file, cartelle e chiavi di registri dalla protezione.**   

Per esempio, se vogliamo evitare che ad ogni avvio, Windows Defender si riscarichi tutte le firme dei virus, possiamo aggiungere le seguenti esclusioni:   

<code>uwfmgr file add-exclusion "c:\Program Files\Windows Defender"</code>   
<code>uwfmgr file add-exclusion "c:\Windows\WindowsUpdate.log"</code>   
<code>uwfmgr file add-exclusion "c:\Windows\Temp\MpCmdRun.log"</code>   
<code>uwfmgr file add-exclusion "c:\ProgramData\Microsoft\Windows Defender"</code>   
<code>uwfmgr registry add-exclusion "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender"</code>   

Per far sì che il sistema si ricordi del cambio di orario, si dovranno aggiungere le seguenti esclusioni nel registro:   

<code>uwfmgr registry add-exclusion "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones"</code>   
<code>uwfmgr registry add-exclusion "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation"</code>   

Dopo aver finito di configurare il sistema, si deve attivare il filtro con il comando:   

<code>uwfmgr.exe filter enable</code>   

Dopo il riavvio, il disco c e lo stato del sistema verranno ripristinati sempre a questo punto.   
Per eseguire delle modifiche al sistema sarà necessario disattivare il filtro con il seguente comando:   

<code>uwfmgr.exe filter disable</code>   

**N.B.**   
Non c’è alcun modo di mantenere gli aggiornamenti Microsoft mentre la protezione è attiva. È possibile tramite policy locali disattivare i download e far sì che l’utente amministratore venga avvertito quando ci sono aggiornamenti disponibili.   

Quando ci saranno aggiornamenti disponibili potranno essere installati tramite il comando: <code>uwfmgr.exe servicing enable</code>   
Riavviare il sistema per iniziare l’installazione degli aggiornamenti. Arrivati alla schermata di login, vedrete la presenza dell’utente UWF-Servicing.   
Attendete che abbia finito.
