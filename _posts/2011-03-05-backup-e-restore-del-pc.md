---
id: 124
title: Backup e Restore del pc su Ubuntu
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/backup-e-restore-del-pc
permalink: /backup-e-restore-del-pc-ubuntu/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8710752210464683859
  - 8710752210464683859
  - 8710752210464683859
categories:
  - Linux
tags:
  - backup
  - restore
  - ubuntu
---
  - Copiamo la lista dei pacchetti installati sul nostro sistema:

	`mkdir ~/backup`  
	`dpkg --get-selections > ~/backup/lista_pacchetti`  

  - Copiamo i repository del nostro sistema:   

	`cat /etc/apt/sources.list /etc/apt/sources.list.d/* > ~/backup/sources.list`   

  - Copiamo la cartella backup (presente nella nostra home) da qualche parte (anche una chiavetta USB andrà benissimo) oppure, opzionalmente, copiamo tutta la nostra home directory (se abbiamo bisogno di copiare anche i nostri dati).

###Restore   

  - Installiamo il sistema operativo (chiaramente della stessa versione di quello sorgente) sul nostro pc di destinazione e, cosa fondamentale, colleghiamolo a internet.   

  - Copiamo la cartella backup, che avevamo salvato prima, dentro la nostra nuova home directory; oppure, se avevamo deciso di copiare tutta la home, copiamo (ed eventualmente sovrascriviamo) i files presenti nella home vecchia all’interno della nuova home.   

  - Copiamo il nostro nuovo file sources.list (quello creato in precedenza) nel posto in cui deve essere sul nuovo sistema, creiamo un backup (non si sa mai) di quello vecchio e aggiorniamo la lista pacchetti, ossia:   
  
	`sudo mv /etc/apt/sources.list /etc/apt/sources.list.old`   
	`sudo cp ~/backup/sources.list /etc/apt/sources.list`   
	`sudo apt-get update`   

A questo punto non ci resta che ripristinare tutti i pacchetti che avevamo installato sulla nostra macchina, utilizzando il file lista_pacchetti creato in precedenza. Anche questa è un’operazione pressochè immediata, in quanto abbiamo bisogno di un solo comando da terminale, cioè:   

	`dpkg --set-selections ~/backup/lista_pacchetti`   
	`sudo apt-get dselect-upgrade`   

Aspettiamo il completamento dell’operazione ed avremo terminato! Ecco qui un bel sistema operativo clonato… con meno di un’ora di lavoro (di cui circa 40 minuti servono per installare il nuovo sistema operativo)