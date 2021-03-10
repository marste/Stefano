---
title: Qual è il modello del mio processore?
subtitle: Comando linux
author: Stefano Marzorati
layout: post
date: 2021-03-01 08:20:00 +0200
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
categories: [Linux]
tags: [cpu, model, modello, processore, processor]
---
~~~batch
cat /proc/cpuinfo | grep "model name"
~~~