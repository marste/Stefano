---
id: 2684
title: Cambiare password di MySQL in Windows
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2684
permalink: /cambiare-password-di-mysql-in-windows/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2102030379
categories:
  - Windows
tags:
  - cambiare
  - change
  - mysql
  - password
---
Accedi come amministratore sul server dove gira MySQL.

Stoppare MySQL

Scrivi un file di testo con Notepad o altro con queste istruzioni:

`UPDATE mysql.user SET Password=PASSWORD(”NuovaPassword”) WHERE User='root';`   
`FLUSH PRIVILEGES;`   


Ovviamente “NuovaPassword” è la nuova password scelta per MySQL.  
Salviamo il file come mysql.txt

Apriamo una riga di comando (Start->Esegui->cmd) e scriviamo:

`C:\mysql\bin\mysqld-nt –init-file=C:\mysql.txt`

La password è stata cambiata e il server MySQL può essere riavviato.