---
id: 1101
title: Caught signal 15 shutting down
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1101
permalink: /caught-signal-15-shutting-down/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"168973768272773121";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"168973768272773121";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1911603494
categories:
  - Linux
tags:
  - modem-manager
---
`sudo mv /etc/rc6.d/S35networking /etc/rc6.d/S15networking`  
`sudo mv /etc/rc0.d/S35networking /etc/rc0.d/S15networking`