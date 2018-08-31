---
id: 2016
title: Percentuale di memoria libera su Linux
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
permalink: /percentuale-di-memoria-libera-su-linux/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1916039790
categories:
  - Linux
tags:
  - command
  - free
  - libera
  - mem
  - memoria
  - memory
  - percentage
---
`free | grep Mem | awk '{ printf("free: %.4f %n", $4/$2 * 100.0) }'`