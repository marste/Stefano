---
id: 1492
title: Max connections on Mysql
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1492
permalink: /max-connections-mysql/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1983514438
categories:
  - Linux
  - Windows
---
Accedi a mysql:  
`mysql -u root -p`

Digita la query per sapere quante connessioni massime ha il tuo mysql:  
`select @@global.max_connections;`

Edita il file:  
`/etc/my.cnf`

Inserisci la riga con quante connessioni massime vuoi:  
`max_connections=250`

Riavvia MySQL  
`service mysqld restart`