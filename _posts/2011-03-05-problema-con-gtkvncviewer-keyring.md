---
id: 70
title: Problema con gtkvncviewer keyring
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/problema-con-gtkvncviewer-keyring
permalink: /problema-con-gtkvncviewer-keyring/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 1961739413039569530
  - 1961739413039569530
  - 1961739413039569530
dsq_thread_id:
  - 2182002704
categories:
  - Linux
tags:
  - vnc
---
`sudo sed -i -e '130 s/gnomekeyring.DeniedError/(gnomekeyring.DeniedError, gnomekeyring.BadArgumentsError,gnomekeyring.IOError)/' /usr/share/gtkvncviewer/gtkvncviewer.py`