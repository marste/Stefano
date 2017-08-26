---
id: 1159
title: 'Cron &#8211; Esempio di eliminazione files o directory'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1159
permalink: /cron-delete-file-direcory/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"187479829019500544";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"187479829019500544";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2039529448
categories:
  - Linux
tags:
  - cron
  - directory
  - elimina
  - eliminazione
  - files
---
Spostarsi nelle directory:  
`/var/spool/cron/`  
ed editare il file &#8220;**root**&#8221;

Esempio:

`# elimina i files di cache di mysql ogni 8 ore   
00 */8 * * * find /mnt/cluster/var/www/html/cms-*/cache/mysql -type f -name "*.cache" -exec rm -f {} ;`

`# elimina le directory con estensione .dir ogni 8 ore   
00 */8 * * * find /mnt/cluster/var/www/html/cms-*/cache/mysql -type d -name "*.dir" -exec rm -rf {} ;`