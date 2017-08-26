---
id: 53
title: Backup con rsync
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/backup-con-rsync
permalink: /backup-con-rsync/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 413232360335717170
  - 413232360335717170
  - 413232360335717170
dsq_thread_id:
  - 2066525498
categories:
  - Linux
tags:
  - backup
  - rsync
---
<span style="font-size:130%;">Backup (controlla i cambiamenti tra sorgente e destinazione e cancella dalla destinazione i file che sono stati cancellati nella sorgente)</span>

Esempio backup locale/locale:

`rsync -av --delete --progress /home/utente/ /home/utente/Desktop/backup`

Se invece non voglio mai cancellare dalla destinazione, togli &#8211;delete

Esempio backup locale/remoto:

`rsync -avz --progress --exclude /cache/ /var/www/html/prova/ root@172.16.1.1:/var/www/html/prova/`