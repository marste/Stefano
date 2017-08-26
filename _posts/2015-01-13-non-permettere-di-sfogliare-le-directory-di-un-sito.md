---
title: Non permettere di sfogliare le directory di un sito
author: Stefano Marzorati
layout: post
permalink: /non-permettere-di-sfogliare-le-directory-di-un-sito/
comments: true
categories:
  - Windows
  - Linux
tags:
  - directory
  - folder
  - permission
  - sfogliare
  - browse
---

Occorre modificare il file httpd.conf
All'interno della sezione Directory, basta aggiungere:

  `Options -Indexes FollowSymLinks`

Ecco un esempio:

  <pre><code>
  <Directory "/var/www/html">
  Options -Indexes FollowSymLinks
  AllowOverride All
  Order allow,deny
  Allow from all
  </Directory>
  </code></pre>
  
