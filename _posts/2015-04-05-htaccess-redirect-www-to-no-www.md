---
title: .htaccess redirect www to non-www
author: Stefano Marzorati
layout: post
permalink: /htaccess-redirect-www-to-non-www/
categories:
  - Linux
  - Windows
tags:
  - htaccess
  - redirect
  - www
  - no-www
  - apache
---
Se volete dirottare tutte le chiamate al vostro sito www.domain.com al sito domain.com, basta che aggiungiate un file .htaccess nella root del vostro sito con il codice seguente:

<pre><code>RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ http://%1/$1 [R=301,L]</code></pre>
