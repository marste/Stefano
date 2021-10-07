---
title: "Verificare se un sito ha la compressione GZip abilitata"
date: 2021-10-07 13:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/web.png'
share-img: 'https://marzorati.co/img/web.png'
categories: [web]
tags: [gzip, compression, website, test, online, tool, github, pages]
---
Se volete vedere se un sito ha la componente di compressione GZip abilitata, potete andare su <a href="https://www.giftofspeed.com/gzip-test/" target="_blank">questo sito</a> per verificarlo:   

Il risultato sarà come questo:   

<center><img src="https://marzorati.co/img/post/gzip-test.png" alt="gzip-test"></center>

Se volete abilitarlo sul vostro sito in hosting su <a href="https://pages.github.com/" target="_blank">GitHub Pages</a>, sarà sufficiente editare il file **_config.yml** ed aggiungere nella sezione plugins: **jekyll-gzip**
