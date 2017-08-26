---
id: 1547
title: Cambiare indirizzo IP su CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1547
permalink: /cambiare-indirizzo-ip-su-centos/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1934031114
categories:
  - Linux
---
Andare in:

`/etc/sysconfig/network-scripts`

editare il file inerente alla scheda di rete da modificare, esempio: ifcfg-eth2 (modifichi l&#8217;ip della scheda di rete eth2)

Esempio di file:

<pre><code>DEVICE=eth2   
BOOTPROTO=static   
HWADDR=00:14:5E:4B:57:E0   
ONBOOT=yes   
TYPE=Ethernet   
IPADDR=192.168.101.104   
NETMASK=255.255.252.0   
GATEWAY=192.168.101.101</code></pre>
