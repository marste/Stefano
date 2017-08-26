---
id: 2406
title: Apache redirect dominio.it to www.dominio.it
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2406
permalink: /apache-redirect-dominio-it-to-www-dominio-it/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2467430626
categories:
  - Linux
  - Windows
tags:
  - apache
  - domain
  - dominio
  - redirect
---
Aggiungere al file .htaccess del sito, le seguenti righe di esempio:

`RewriteEngine On`  
`RewriteCond %{HTTP_HOST} ^marzorati\.co`  
`RewriteRule ^(.*)$ http://www.marzorati.co/$1 [R=permanent,L]`

Un altro esempio:

`RewriteEngine On`  
`RewriteCond %{HTTP_HOST} ^www\.miosito\.it`  
`RewriteRule ^(.*)$ http://www.tuosito.com/$1 [R=permanent,L]`