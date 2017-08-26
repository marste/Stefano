---
id: 2849
title: Esempio di aggiornamento impostazioni cluster pacemaker
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2849
permalink: /esempio-di-aggiornamento-impostazioni-cluster-pacemaker/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2667101720
categories:
  - Linux
tags:
  - apache
  - cluster
  - mysql
  - pacemaker
---
Se ad esempio voglio vedere tutte le risorse del mio cluster, dovrò digitare:

`pcs resource show`

Se poi voglio vedere i dettagli della risorsa ln_mysql, dovrò digitare:

`pcs resource show ln_mysql`

Se devo modificare il target della risorsa, dovrò digitare ad esempio:

`pcs resource update ln_mysql target=/mnt/autofs/nfs/netapp-vol3/cluster/var/lib/mysql`