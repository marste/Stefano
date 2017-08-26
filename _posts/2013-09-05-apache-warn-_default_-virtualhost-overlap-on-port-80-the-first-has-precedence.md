---
id: 1961
title: 'Apache: [warn] _default_ VirtualHost overlap on port 80, the first has precedence'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1961
permalink: /apache-warn-_default_-virtualhost-overlap-on-port-80-the-first-has-precedence/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1927505959
categories:
  - Linux
tags:
  - apache
  - overlap
  - virtualhost
  - warn
---
Molto probabilmente ti sei dimenticato di togliere un commento dal file di configurazione di Apache.

Edita il file:  
`nano /etc/httpd/conf/httpd.conf`

Togli il commento dalla riga:

Da così:  
`#NameVirtualHost *:80`  
A così:  
`NameVirtualHost *:80`

Riavvia Apache:  
`service httpd restart`