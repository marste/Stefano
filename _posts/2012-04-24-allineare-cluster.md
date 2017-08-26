---
id: 1170
title: Allineare Cluster
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1170
permalink: /allineare-cluster/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"194718351736586241";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"194718351736586241";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2031261561
categories:
  - Linux
tags:
  - allineare
  - cluster
  - csync2
---
Per verificare se i nodi di un cluster sono allineati:  
`csync2 -xv`

Se non fossero allineati e vorresti forzare l&#8217;allineamento dobbiamo decidere chi ha il file nuovo e buono e con il comando `csync2 -f /path/nomefile.xml` lanciato sul nodo in cui vogliamo tenere il file.