---
id: 3101
title: Changing default storage engine in MySQL from InnoDB to MyISAM
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3101
permalink: /changing-default-storage-engine-in-mysql-from-innodb-to-myisam/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3001872465
categories:
  - Linux
  - Windows
tags:
  - cambiare
  - change
  - engine
  - motore
  - mysql
---
Da terminale, basta semplicemente digitare questo comando:

`set global storage_engine=MYISAM;`

<span style="text-decoration: underline;">Non è necessario riavviare</span> il servizio di MySQL.

Se poi volete modificare anche la struttura delle tabelle da InnoDB a MyISAM, potete fare in due modi.  
Da riga comando, la query SQL da digitare è:

``ALTER TABLE `nome_tabella` ENGINE = MYISAM``

In alternativa, se avete PhpMyAdmin, potete andare sulla tabella, operazioni e cambiare da lì l&#8217;engine.