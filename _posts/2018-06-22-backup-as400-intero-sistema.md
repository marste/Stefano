---
title: Schedulare backup intero sistema su AS/400
date: 2018-07-09 09:45:00 +0200
published: true
image: https://marzorati.co/img/ibm.png
share-img: https://marzorati.co/img/ibm.png
categories:
  - AS/400
tags:
  - backup
  - go save
  - as400
  - nastro
  - tape
  - sistema
  - intero
---
Accedere alla Console di AS/400   

Digitare il comando <code>GO SAVE</code> opzione <code>21</code>   

![backup_as400](https://farm2.staticflickr.com/1788/41140944530_f3653a924a_o.png)   
<br>
![backup1_as400](https://farm2.staticflickr.com/1773/41140944630_1752d17423_o.png)   
<br>
![backup2_as400](https://farm2.staticflickr.com/1761/42540302084_77c0c2a6a3_o.png)   
<br>
Per verificare quanto tempo ci ha messo ad effettuare il backup, ti basterà premere F1 sul messaggio che vedrai in console sull'esito del backup.   
Oppure puoi vedere i log di sistema <code>DSPLOG PERIOD((010000 080718) (*AVAIL *END))</code> mettendo l'ora e la data iniziale dal quale partire.   

Per vedere il log del nastro, per capire cosa è stato salvato, digita:   
<code>DSPTAP DEV(TAP01) OUTPUT(*PRINT)</code>   
<code>WRKSPLF</code>   