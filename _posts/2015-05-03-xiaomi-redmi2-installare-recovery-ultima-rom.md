---
title: Xiaomi RedMi2 - Installare recovery e ultima ROM MIUI
date: 2015-05-03 22:30:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /xiaomi-redmi2-installare-recovery-ultima-rom-miui/
categories:
  - Smartphone
tags:
  - xiaomi
  - redmi2
  - recovery
  - rom
  - miui
  - HM2014813
---
Se avete acquistato uno smartphone **Xiaomi RedMi2** (seconda edizione con 2GB di RAM e 16GB di ROM) da un rivenditore cinese, magari su [Aliexpress](http://www.aliexpress.com/) come il sottoscritto, ecco alcune informazioni che potranno esserti molto utili.   

Il telefono che mi è arrivato era il modello **HM2014813** (HM 2LTE-CU) che si differenzia dal modello HM2014811.   

  - HM2014813 (Chinese)
  - HM2014811 (International)
  
Il modello è riportato sotto la batteria.   

Questo telefono aveva preinstallata una ROM MIUI moddata, più precisamente la versione **MIUI 16.2.4.0 (KHJCNBK) Stable**, ovviamente non originale e non aggiornabile.   
Dopo poco che la usavo connesso ad internet, continuavano ad uscire pop-up pubblicitari di google.   
Qualsiasi app aprissi o si apriva una pubblicità a tutto schermo o solo in basso, ma da impedirti di usare la tastiera.   
Ho cominciato a dubitare fortemente di questa ROM.   
Dopo qualche ricerca sui forum ho avuto conferme da esperti che queste ROM sono piene di bloatware e non sono assolutamente consigliabili.   
Decido di installare l'app [Malwarebytes Anti-Malware](https://play.google.com/store/apps/details?id=org.malwarebytes.antimalware&hl=en) e scopro che erano presenti in due file .apk **due trojan**.   

  - <code>/system/app/twitter _qd_3025.apk</code>
  - <code>/system/app/miuivideo.apk</code>

Rimuovo questi due files, ma il problema dei pop-up rimane.   
Decido a questo punto di installare una nuova ROM e decido di mettere la multilingua ultimissimo aggiornamento.   

A questo punto, trovo della documentazione sul forum [http://en.miui.com](http://en.miui.com) che mi ha fatto perdere molto tempo e incappare in vari errori.   

**ATTENZIONE QUESTA PROCEDURA NON è FUNZIONANTE**   

  - Ho scaricato da Google Play l'app "Flashify" per poter installare la recovery
  - Ho scaricato la [Philz Touch Recovery](https://javteam.wordpress.com/download/xiaomi-redmi-2)
  - Ho tentato di installare questa [ROM](https://www.androidfilehost.com/?fid=24052804347822070)

L'installazione terminava con questo errore:   
**This package is for HM2014813 device; this is a HM2014811**

Ho cominciato ad avere dubbi su che modello avessi veramente, ma fortunatamente il modello era veramente quello riportato sulla batteria.   

**SOLUZIONE**   

Alla fine son riuscito a installare tutto seguendo questi passi:   

  - Ho scaricato da Google Play l'app "Flashify" per poter installare la recovery
  - Ho scaricato questa [CWM Recovery](http://marzorati.co/download/CWM_Recovery.zip)
  - Ho scaricato l'ultimissima ROM **MIUI 7** per questo modello dal sito [<del>http://htcfanboys.com/download/acid/?action=list&folder=75939</del>](http://htcfanboys.com/download/acid/?action=list&folder=75939) oppure [https://www.androidfilehost.com/?w=search&s=HM2014813](https://www.androidfilehost.com/?w=search&s=HM2014813) oppure [http://xiaomi.eu/community/threads/5-9-24.28459/](http://xiaomi.eu/community/threads/5-9-24.28459/)
  - Il telefono è partito con la nuova versione di MIUI 7
  - Sono rientrato in modalità recovery ufficiale MIUI dalle opzioni di System Update
  - Ho eseguito un wipe completo di cache e data
