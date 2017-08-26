---
id: 1815
title: Installare Acrobat Reader su Debian
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1815
permalink: /installare-acrobat-reader-debian/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1948037853
categories:
  - Linux
tags:
  - acrobat
  - deb
  - debian
  - multimedia
  - reader
  - repository
---
Aggiungi in: /etc/apt/sources.list   

`deb http://www.deb-multimedia.org sid main non-free`   
`deb-src http://www.deb-multimedia.org sid main`

`sudo apt-get install deb-multimedia-keyring`   
`sudo apt-get install acroread mozilla-acroread`