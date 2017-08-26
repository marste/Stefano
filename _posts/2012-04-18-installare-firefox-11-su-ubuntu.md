---
id: 1163
title: Installare Firefox 11 su Ubuntu
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1163
permalink: /installare-firefox-11-su-ubuntu/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"192613878302121984";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"192613878302121984";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 3063545946
categories:
  - Linux
tags:
  - firefox
  - installare
  - manual
  - ubuntu
---
`wget http://dm-download02.mozilla.org/pub/mozilla.org/firefox/releases/11.0/linux-i686/it/firefox-11.0.tar.bz2`  
`tar xvjf firefox-11.0.tar.bz2`  
`sudo mv firefox /opt/firefox`  
`sudo mv /usr/bin/firefox /usr/bin/firefox-old`  
`sudo ln -s /opt/firefox/firefox /usr/bin/firefox`  
`sudo rm firefox-11.0.tar.bz2`  
`killall firefox`