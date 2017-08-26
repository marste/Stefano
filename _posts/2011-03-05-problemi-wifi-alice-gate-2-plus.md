---
id: 94
title: Problemi wifi ALICE GATE 2 Plus
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/problemi-wifi-alice-gate-2-plus
permalink: /problemi-wifi-alice-gate-2-plus/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 5897032199811224947
  - 5897032199811224947
  - 5897032199811224947
dsq_thread_id:
  - 2384185719
categories:
  - Linux
---
ALICE GATE 2 Plus Wi-Fi (bianco, bordatura nera, smart card sulla sinistra)  
Funziona con MAC e con Windows ma con Linux si blocca la ricezione dei  
pacchetti dopo pochi kappa&#8230;dopo molti smadonnamenti ho trovato questo:

In pratica basta eseguire uno script al boot (per es. il /etc/rc.local)

echo 1 > /proc/sys/net/ipv4/tcp_syncookies  
echo 0 > /proc/sys/net/ipv4/tcp\_window\_scaling  
echo 0 > /proc/sys/net/ipv4/tcp_ecn

oppure basta aggiungere nel file /etc/sysctl.conf le righe seguenti:

net.ipv4.tcp_syncookies = 1  
net.ipv4.tcp\_window\_scaling = 0  
net.ipv4.tcp_ecn = 0