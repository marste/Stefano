---
id: 1186
title: 'Netapp: WAFL inconsistent: bad user data block'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1186
permalink: /netapp-wafl-inconsistent-bad-user-data-block/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"204508625014767617";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"204508625014767617";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1962098912
categories:
  - Varie
tags:
  - check
  - file
  - netapp
  - rdfile
  - vol
  - wafl
---
Se avete un errore del genere sul Netapp:  
Sat May 19 21:07:07 CEST [wafl.raid.incons.userdata:error]: WAFL inconsistent: bad user data block 336474968 (vvbn:95647107 fbn:50 level:0) in inode (**fileid:3409596** snapid:0 file\_type:1 disk\_flags:0x2) **in volume vol2**.

Accedere via telnet a Netapp:  
poi digitare: **priv set diag**

Controllare qual è il file rovinato:  
**file check -vol vol2 -i 3409596 -s 0**

Leggere il log scritto:  
**rdfile /etc/log/file_check.vol2.0.3409596.20120520114228**

Vedere quanti snapshot si hanno:  
**snap list -n vol2**