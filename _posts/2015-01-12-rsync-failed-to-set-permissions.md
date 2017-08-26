---
title: rsync failed to set permissions
author: Stefano Marzorati
layout: post
permalink: /rsync-failed-to-set-permissions/
comments: true
categories:
  - Linux
tags:
  - rsync
  - failed
  - permission
---

Se avete un messaggio di errore simile al seguente:

	rsync: failed to set permissions on "/gluster/content/AVH01/document-root/.": Operation not permitted (1) ./

	rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1039) [sender=3.0.6]

Risolvete aggiungendo i seguenti parametri per la vostra copia tramite rsync:

	rsync -avz --no-perms --no-o --no-g --progress PATH_DA_TRASFERIRE/ root@5.6.7.8:/gluster/content/AVH01/document-root/ -O
