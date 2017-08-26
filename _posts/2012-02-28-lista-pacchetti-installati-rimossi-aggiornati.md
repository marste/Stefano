---
id: 1120
title: Lista pacchetti installati rimossi e aggiornati
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1120
permalink: /lista-pacchetti-installati-rimossi-aggiornati/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"174580157829488641";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"174580157829488641";}}}'
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - install
  - list
  - packages
  - remove
  - upgrade
---
`awk '$3 ~ /install|remove|upgrade/ {print $1 " "$3 ": "$4}' /var/log/dpkg.log > $HOME/Desktop/elenco.txt`