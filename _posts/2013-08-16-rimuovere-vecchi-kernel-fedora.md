---
id: 1906
title: Rimuovere vecchi kernel da Fedora
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1906
permalink: /rimuovere-vecchi-kernel-fedora/
geo_public:
  - 0
  - 0
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2235783023
categories:
  - Linux
tags:
  - delete
  - fedora
  - kernel
  - old
  - remove
---
Quali versioni di kernel hai installate?  
`rpm -q kernel`

Installa questo pacchetto:  
`yum install yum-utils`

Rimuoviamo tutte le versioni del kernel tranne le ultime 2, per farlo basta digitare:  
`package-cleanup --oldkernels --count=2`

Se vogliamo impostare l&#8217;utilizzo automatico delle sole ultime 2 versioni del kernel:  
`nano /etc/yum.conf`

e modificare la riga:  
`installonly_limit=2`