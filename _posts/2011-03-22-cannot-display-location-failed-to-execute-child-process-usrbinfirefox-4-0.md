---
id: 457
title: Cannot display location failed to execute child process usr/bin/firefox-4.0
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=457
permalink: /cannot-display-location-failed-to-execute-child-process-usrbinfirefox-4-0/
dsq_thread_id:
  - 2188120846
categories:
  - Linux
tags:
  - ftp
---
Quando cerchi di collegarti da Places -> Connect to Server -> FTP ad un sito ftp

e hai un errore simile a questo:

**cannot display location failed to execute child process usr/bin/firefox-4.0**

Fai così:

alt+f2

gconf-editor

/desktop/gnome/url-handlers/ftp/command   rimettere il valore di default **nautilus %s**

&nbsp;