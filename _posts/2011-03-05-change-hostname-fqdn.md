---
id: 36
title: Cambiare hostname e fqdn
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/rinominare-hostname-pc
permalink: /change-hostname-fqdn/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 3583658649705446490
  - 3583658649705446490
  - 3583658649705446490
geo_public:
  - 0
  - 0
  - 0
dsq_thread_id:
  - 1904290098
categories:
  - Linux
tags:
  - rename
---
Editare questi due files:

`/etc/hostname`  
`/etc/hosts`

Per apportare le modifiche:  
`/etc/init.d/hostname.sh`

Per verificare che le modifiche siano state prese, digita:  
`hostname`  
`hostname -fqdn`