---
title: .htaccess redirect https to http
author: Stefano Marzorati
layout: post
permalink: /htaccess-redirect-https-to-http/
categories:
  - Linux
  - Windows
tags:
  - htaccess
  - redirect
  - https
  - http
  - apache
---
Se volete dirottare tutte le chiamate al vostro sito **https**://www.domain.com al sito **http**://www.domain.com, basta che aggiungiate un file .htaccess nella root del vostro sito con il codice seguente:

<pre><code>RewriteEngine On   
RewriteBase /   
RewriteCond %{SERVER_PORT} ^443$ [OR]   
RewriteCond %{HTTPS} =on   
RewriteRule ^(.*)$ http://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]</code></pre>
