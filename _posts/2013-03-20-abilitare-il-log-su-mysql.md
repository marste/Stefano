---
id: 1468
title: Abilitare il log su mysql
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1468
permalink: /abilitare-il-log-su-mysql/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1962627150
categories:
  - Linux
  - Windows
---
Editare il file: `/etc/my.cnf`

Aggiungere la riga: `log=/var/log/mysql/mysql.log`

Riavviare il servizio: `/etc/init.d/mysqld restart`