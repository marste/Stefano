---
id: 3298
title: 'Connect: Network is unreachable'
author: Stefano Marzorati
layout: post
guid: http://php-marzorati.rhcloud.com/?p=3298
permalink: /connect-network-is-unreachable/
authorsure_include_css:
  - 
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
dsq_needs_sync:
  - 1
categories:
  - Linux
tags:
  - gateway
  - Linux
  - network
  - route
  - unreachable
---
Se sulla vostra macchina Linux non riuscite a pingare una rete che dovreste poter raggiungere, probabilmente non avete impostato un gateway sulla scheda di rete.

Digitate:  
`route -n`

Se avete un risultato simile a questo, in cui non c&#8217;è il gateway:

    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 wlan0

Per aggiungerlo, basta digitare, ad esempio:

`route add default gw 192.168.1.1`
