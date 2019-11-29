---
title: Cambiare hostname e fqdn in linux
author: Stefano Marzorati
date: 2019-11-29 17:30:00 +0200
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
layout: post
permalink: /change-hostname-fqdn/
categories:
  - Linux
tags:
  - rename
  - hostname
  - fqdn
---
Editare questi due files:

`/etc/hostname`  
`/etc/hosts`

Per apportare le modifiche:  
`/etc/init.d/hostname.sh`

Per verificare che le modifiche siano state prese, digita:  
`hostname`  
`hostname -fqdn`