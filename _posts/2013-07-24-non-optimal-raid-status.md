---
id: 1865
title: Non-optimal RAID Status
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1865
permalink: /non-optimal-raid-status/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
geo_public:
  - 0
  - 0
authorsure_include_css:
  - 
dsq_thread_id:
  - 2115985031
categories:
  - Linux
tags:
  - debian
  - non-optimal
  - raid
  - status
  - vmware
---
Se avete installato Debian su una macchina virtuale VMware, potreste avere l&#8217;errore in oggetto.

Stoppate il servizio:  
`/etc/init.d/mpt-statusd stop`

e poi lo disabilitare dall&#8217;avvio automatico:  
`update-rc.d -f mpt-statusd remove`