---
title: Schedulare backup intero sistema su AS/400
subtitle: Full Backup
date: 2018-07-09 09:45:00 +0200
published: true
image: https://marzorati.co/img/ibm.png
share-img: https://marzorati.co/img/ibm.png
categories: [AS400]
tags: [backup, go save, nastro, as400. tape, full, sistema, intero]
---
Prima di tutto occorre inizializzare il nastro secondo <a href="https://marzorati.co/inizializzare-tape-nastro-as400/" target="_blank">questa procedura</a>.   

Poi togli la schedulazione di spegnimento e avvio di domenica secondo <a href="https://marzorati.co/schedulazione-spegnimento-accensione-as400/" target="_blank">questa procedura</a>, utilizzando la scelta 2.   

Poi digita <code>WRKJOBSCDE</code> cerca il processo <code>SI5BACKUP</code>, modificalo, vai alla seconda pagina, premi F10 e ometti la data del backup di sabato notte per non far scrivere sulla cassetta del FULL il backup del sabato.   

![backup3_as400](https://marzorati.co/img/post/backup_as400_4.png)   

Accedere alla Console di AS/400   

Digitare il comando <code>GO SAVE</code> opzione <code>21</code>   

![backup_as400](https://marzorati.co/img/post/backup_as400_1.png)   
<br>
![backup1_as400](https://marzorati.co/img/post/backup_as400_2.png)   
<br>
![backup2_as400](https://marzorati.co/img/post/backup_as400_3.png)   
<br>

Per verificare quanto tempo ci ha messo ad effettuare il backup, ti basterà premere F1 sul messaggio che vedrai in console sull'esito del backup.   
Oppure puoi vedere i log di sistema <code>DSPLOG PERIOD((010000 080718) (*AVAIL *END))</code> mettendo l'ora e la data iniziale dal quale partire.   

Per vedere il log del nastro, per capire cosa è stato salvato, digita:   
<code>DSPTAP DEV(TAP01) OUTPUT(*PRINT)</code>   
<code>WRKSPLF</code>   

Ma può bastare:   
<code>DSPTAP DEV(TAP01)</code>
