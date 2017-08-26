---
id: 1252
title: Restore a single table from a full mysql mysqldump file
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1252
permalink: /restore-a-single-table-from-a-full-mysql-mysqldump-file-2/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1982490079
categories:
  - Linux
  - Windows
---
``grep "^INSERT INTO `nometabella`" /tmp/restore/backup-030002.sql | mysql -u root -p nomedb``