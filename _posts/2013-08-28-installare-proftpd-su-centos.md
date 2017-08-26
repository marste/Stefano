---
id: 1925
title: Installare ProFTPD su CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1925
permalink: /installare-proftpd-su-centos/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1906726234
categories:
  - Linux
tags:
  - centos
  - ftp
  - proftpd
  - server
---
`yum install proftpd`

Per farlo avviare al reboot:  
`chkconfig --level 3 proftpd on`

Avvia il servizio:  
`service proftpd start`

Modifica il file di configurazione:  
`nano /etc/proftpd.conf`  
`ServerName                      "example.com"`

Aggiungi un utente:  
`useradd -d /var/www/html/ -s /sbin/nologin marzorati`

Assegno la password all&#8217;utente  
`passwd marzorati`