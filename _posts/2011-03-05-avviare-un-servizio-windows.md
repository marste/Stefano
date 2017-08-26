---
id: 62
title: Avviare un servizio Windows
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/avviare-un-servizio-windows
permalink: /avviare-un-servizio-windows/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 3332955656261345707
  - 3332955656261345707
  - 3332955656261345707
dsq_thread_id:
  - 1905168969
categories:
  - Linux
tags:
  - Windows
---
`net rpc service list -I 192.168.101.175 -U "xxx.domain.xxxadministrator"`

`net rpc service start "WinVNC4" -I 192.168.101.175 -U "xxx.domain.xxxadministrator"`