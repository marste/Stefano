---
title: 'Trova il Product Key di Windows 10 da commandline'
author: Stefano Marzorati
layout: post
date: 2021-04-12 07:59:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [find, trova, product, key, windows, wmic]
---

Da command line, basta digitare:   

~~~batch
wmic path SoftwareLicensingService get OA3xOriginalProductKey
~~~
