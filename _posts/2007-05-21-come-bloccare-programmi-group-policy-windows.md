---
title: Come bloccare i programmi con le Group Policy di Windows
author: Stefano Marzorati
layout: post
permalink: /come-bloccare-programmi-group-policy-windows/
categories:
  - Windows
tags:
  - bloccare
  - group
  - policy
  - programmi
  - Windows
---
![title](https://farm9.staticflickr.com/8790/16890882869_b931243b9d_o.jpg)  
![title](https://farm9.staticflickr.com/8779/16456946343_2fdbf9b604_o.jpg)  

**Procedimento**  
Per prima cosa, prendiamo gli .exe dei giochi di windows xp, prendendoli da un client qualunque.  
Questi file li copiamo in una cartella di rete con accesso limitato solo agli amministratori di dominio.

**Creazione regola**  
Apriamo GPMC &#8211; figura 1 &#8211; e creaiamo una nuova regola all&#8217;interno di una OU contenente i computer dell&#8217;azienda che chiameremo Software Restrictions.


![policy](https://farm8.staticflickr.com/7627/17075617882_67dd244738_o.jpg)
figura 1 &#8211; Group Policy Management Console

Fatto questo clicchiamo il tasto destro su **Software Restrictions Policies**, e scegliamo New Software Restriction Policies nel menù contestuale &#8211; figura 2; verranno creati un serie di oggetti &#8211; figura 3.

![policy](https://farm9.staticflickr.com/8741/16456946003_9a089abfe5_o.jpg)

![policy](https://farm8.staticflickr.com/7622/17051139426_3b803f4077_o.jpg)  
figura 3 &#8211; come creare una regola di Hash

A questo punto andiamo sulla categoria **Additional Rules** e scegliamo New Hash Rule, verrà visualizzata la finestra di configurazione &#8211; figura 4.

![policy](https://farm9.staticflickr.com/8707/16456945633_2c73f82e91_o.jpg)  
figura 4 &#8211; Regola di Hash

Premendo su Browse si aprirà la finestra per selezionare quale file andare a bloccare &#8211; figura 5

![policy](https://farm8.staticflickr.com/7636/16456945433_5f5d3903f3_o.jpg)  
figura 5 &#8211; selezioniamo che file andare a bloccare

Selezioniamo il file che ci interessa e premiamo su OK, come potete notare dalla figura 6, il file viene analizzato e &#8220;scomposto&#8221;; la stringa relativa al hash, serve per fare il confronto con tutti i file aperti dai computer interessati dalla policy, appena viene trovato il file con lo stesso hash della policy, scatta il blocco all&#8217;esecuzione.

![policy](https://farm8.staticflickr.com/7687/16889327208_60aa888fe8_o.jpg)  
figura 6 &#8211; analisi del file ed eventuale vostro commento

Premendo su OK, viene creato il blocco per il file.  
Si possono aggiungere altri file alla lista, sempre uno alla volta però.

Chiudiamo la finestra della policy e testiamo che la regola sia stata creata correttamente.  
Andiamo su un client XP e lanciamo un **gpupdate /force**, attendiamo un paio di secondi e proviamo a lanciare il file che abbiamo bloccato via GPO.

Se avete fatto tutto correttamente, dovrebbe apparire il messaggio di errore &#8211; come da figura 7  
![policy](https://farm8.staticflickr.com/7696/17075618482_5cbab0ae2d_o.jpg)   

Fatto!

Questo un modo per impedire di utilizzare file indesiderati, ci sono modi per bloccare l&#8217;esecuzione di intere cartelle o di estensioni di file&#8230;. ma magari lo vedremo la prossima volta.
