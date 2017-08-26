---
id: 1362
title: Numero di connessioni http contemporanee Apache
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1362
permalink: /numero-di-connessioni-http-contemporanee-apache/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1900458639
dsq_needs_sync:
  - 1
categories:
  - Linux
  - Windows
---
`netstat -atpun | grep ":80 " | grep ":ffff:" | awk '{print $4" "$5}' | sed -s 's/::ffff:/ /g' | awk -F":" '{print $1" "$2}' | wc -l`