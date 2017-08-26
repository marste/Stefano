---
id: 1347
title: 'Apache: non far navigare all&#8217;interno delle directory dei siti'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1347
permalink: /apache-non-far-navigare-allinterno-delle-directory-dei-siti/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2124990997
categories:
  - Linux
  - Windows
---
Andare in /etc/httpd/conf/httpd.conf

Andare alla riga:   Options Indexes FollowSymLinks  
e cancellare Indexes

in modo da lasciare:   Options FollowSymLinks

riavviare l&#8217;httpd

/etc/init.d/httpd restart

<div id="dc_vk_code" style="display:none;">
</div>