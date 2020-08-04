---
title: Trovare tutte le password WiFi salvate sul PC da commandline
author: Stefano Marzorati
layout: post
date: 2020-08-04 21:43:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [WiFi]
tags: [find, trovare, password, wifi, cmd, netsh]
published: true
---
~~~batch
netsh wlan export profile folder=C:\ key=clear
~~~
