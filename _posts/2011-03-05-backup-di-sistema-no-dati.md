---
id: 87
title: Backup di sistema (no dati)
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/backup-di-sistema-no-dati
permalink: /backup-di-sistema-no-dati/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 346865220496635455
  - 346865220496635455
  - 346865220496635455
dsq_thread_id:
  - 1924263716
categories:
  - Linux
tags:
  - backup
  - system
---
<span style="font-size:130%;">Effettuare Backup:</span>

`tar cvpjf backup.tar.bz2 --exclude=/proc --exclude=/lost+found --exclude=/backup.tar.bz2 --exclude=/mnt --exclude=/sys / --exclude=/tmp --exclude=/home`

Ripristinare Backup:

`tar xvpfj backup.tar.bz2 -C /`

[via][1]

 [1]: http://www.edmondweblog.com/index.php/2010/06/21/backup-velocissimo-di-sistema/