---
id: 1933
title: Importare o esportare un database mysql
author: Stefano Marzorati
layout: post
comments: true
guid: http://marzorati.co/?p=1933
permalink: /import-export-database-mysql/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-09-02 12:50:50";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-09-02 12:50:50";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2229648700
categories:
  - Linux
  - Windows
tags:
  - database
  - dump
  - esportazione
  - export
  - import
  - importazione
  - mysql
---
Esempio di esportazione:  
  `mysqldump -u utente --password=password nome_database > /tmp/nome_db.sql`

Esempio di importazione:  
  `mysql -u utente --password=password nome_database < /tmp/nome_db.sql`

Esportazione con compressione:   
  `mysqldump -u utente -p nome_database | gzip > /tmp/nome_db.sql.gz`

Importazione con compressione:   
  `gunzip < /tmp/nome_db.sql.gz | mysql -u utente -p nome_database`
