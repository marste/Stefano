---
id: 2696
title: Mettere sotto autenticazione un sito web con Apache
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2696
permalink: /mettere-sotto-autenticazione-un-sito-web-con-apache/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2121076924
categories:
  - Linux
tags:
  - apache
  - autenticazione
  - autorizzazione
  - htaccess
  - password
---
Per prima cosa digitare da terminal il seguente comando che creerà la password per l&#8217;utente di test:

`htpasswd -c /www/html/website/.htpasswd test`

Verrà chiesta due volte la password che si vuole dare all&#8217;utente e avrete il seguente risultato:

	New password:   
	Re-type new password:   
	Adding password for user test   


Poi editate il file .htaccess del vostro sito e all&#8217;inizio del file scrivete queste quattro righe:

	AuthUserFile /www/html/website/.htpasswd   
	AuthType Basic   
	AuthName "Sito Demo"   
	Require valid-user

Ora il vostro sito è protetto da password.