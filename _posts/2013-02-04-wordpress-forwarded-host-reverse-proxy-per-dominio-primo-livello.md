---
id: 1250
title: WordPress FORWARDED_HOST per dominio primo livello
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1250
permalink: /wordpress-forwarded-host-reverse-proxy-per-dominio-primo-livello/
categories:
  - Linux
  - Windows
tags:
  - htaccess
---
Questa è la soluzione per quando si installa WordPress sotto un Reverse Proxy di Apache.

Aggiungere queste righe nel file **wp-config.php**

Esempio:

	$_SERVER['HTTP_HOST'] = $_SERVER['HTTP_X_FORWARDED_HOST'];   
	define('WP_HOME', 'http://marzorati.co');   
	define('WP_SITEURL', 'http://marzorati.co');   
	$_SERVER['REQUEST_URI'] = str_replace("/marzorati", "", $_SERVER['REQUEST_URI']);

**Modifica .htaccess per non aver problemi con i permalink**

	# BEGIN WordPress   
	<IfModule mod_rewrite.c>   
	RewriteEngine On   
	RewriteBase /marzorati/   
	RewriteRule ^index\.php$ - [L]
	RewriteCond %{REQUEST_FILENAME} !-f   
	RewriteCond %{REQUEST_FILENAME} !-d   
	RewriteRule . /marzorati/index.php [L]
	</IfModule>   
	# END WordPress