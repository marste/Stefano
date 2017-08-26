---
id: 892
title: Rimuovere residui di configurazione e files orfani
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=892
permalink: /purge-applications-residual-config-orphans/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2141089891
categories:
  - Linux
tags:
  - config
  - dpkg
  - orphan
  - purge
  - remove
---
`sudo dpkg -l | sed '/^rc/!d;s/^[^ ]* [^ ]* ([^ ]*).*/1/' | xargs -r sudo apt-get -y purge`