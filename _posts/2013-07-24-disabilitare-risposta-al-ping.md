---
id: 1857
title: Disabilitare risposta al ping
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1857
permalink: /disabilitare-risposta-al-ping/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1996192168
categories:
  - Linux
tags:
  - disable
  - echo
  - icmp
  - ping
---
Per disabilitare la risposta al ping eseguire il seguente comando:  
`echo 1 >/proc/sys/net/ipv4/icmp_echo_ignore_all`

Per riabilitare la risposta al ping eseguire il seguente comando:  
`echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_all`

Per disabilitare la risposta al ping in modo permanente editare il file /etc/sysctl.conf aggiungendo la seguente riga:  
`net.ipv4.conf.icmp_echo_ignore_all = 1`

Per eseguire immediatamente le modifiche apportate eseguire il seguente comando:  
`sysctl -p`