---
id: 1297
title: Reverse Proxy pagina 404
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1297
permalink: /reverse-proxy-pagina-404/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1956448323
categories:
  - Linux
---
Vanno aggiunte le righe in grassetto:

<VirtualHost *:80>

ServerName servername  
DocumentRoot /somepath/  
**ProxyPass /errors !**  
ProxyPass / http://localhost:8080/someapp/  
ProxyPassReverse / http://localhost:8080/someapp/  
**ProxyErrorOverride On**  
**  ErrorDocument 404 /errors/error.html**

</VirtualHost>

<div id="dc_vk_code" style="display:none;">
</div>