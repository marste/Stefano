---
id: 876
title: Crontab
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=876
permalink: /crontab-debian-centos/
geo_public:
  - 0
  - 0
authorsure_include_css:
  - 
dsq_thread_id:
  - 2101014498
categories:
  - Linux
tags:
  - centos
  - cron
  - crontab
  - debian
---
Avviare servizio cron su Debian:  
 
	/etc/init.d/cron start
oppure   

	service cron start

Avviare servizio cron su CentOS:   

	/etc/init.d/crond start

Avviare cron al boot su CentOS:   

	chkconfig crond on

Avviare cron al boot su Debian:   

	update-rc.d cron defaults

Oppure installi rcconf (gui da terminal):   

	apt-get install rcconf

Per creare un nuovo task:   

	crontab -e

Esempio:   
Elimina le mail in coda con errore mailer-daemon ogni 2 minuti   

	*/2 * * * * /bin/pulisci.sh
