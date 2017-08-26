---
id: 1945
title: Installare e configurare rsnapshot
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1945
permalink: /installare-configurare-rsnapshot/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1910814522
categories:
  - Linux
tags:
  - backup
  - centos
  - rsnapshot
  - snapshot
---
Installare su CentOS con:  
`yum install rsnapshot`

Editare il file di configurazione **/etc/rsnapshot.conf** modificando le seguenti righe

Percorso dove salvare i backup:  
`snapshot_root /home/backup/snapshots/`

Quanti giorni mantenere:  
`interval daily 14`

Se dovete escludere qualche directory dai backup:  
`exclude /home/var/www/html/sito/cache/`

Che cosa backuppare:  
`backup /home/var/www/html/ localhost/`  
`backup /etc/ localhost/`  
`backup /usr/local/ localhost/`

Schedulare il backup con cron:  
`0 1 * * * /usr/bin/rsnapshot daily`

Se volete vedere quanto spazio occupano gli snapshots, basta digitare:  
`rsnapshot du`