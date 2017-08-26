---
id: 3103
title: 'Install mytop on CentOS &#8211; display MySQL server performance'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3103
permalink: /install-mytop-on-centos-display-mysql-server-performance/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3004529322
categories:
  - Linux
tags:
  - centos
  - mysql
  - mytop
---
`yum install mytop`

**Utilizzo:**  
`mytop -u admin -p 123456 -d database`

**Leggere i valori:**

La prima riga identifica il nome host del server (localhost) e la versione di MySQL che è in esecuzione. Sul lato destro si vede il tempo di attività del processo server MySQL in giorni + ore: minuti: secondi e l&#8217;ora corrente.

Sulla seconda riga si visualizza il numero totale di query che il server ha elaborato, il numero medio di query al secondo, il numero di query lente, e la percentuale di SELECT, INSERT, UPDATE e DELETE.

Sulla terza riga ci sono i valori in tempo reale. Il primo è il numero di query al secondo, poi il numero di query lente, seguito dalla percentuale di query (come nella riga precedente).

E nella quarta riga si visualizza la chiave di efficienza (ciò che viene letto dal buffer anziché dal disco) e il numero di byte che MySQL ha inviato e ricevuto.