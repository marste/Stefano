---
id: 1529
title: Auto mount Volume on CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1529
permalink: /auto-mount-volume-on-centos/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:29;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:29;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1992790289
categories:
  - Linux
---
Edit:  
`/etc/auto.master`

`/mnt/autofs/cifs /etc/auto.cifs --timeout=300`  
`/mnt/autofs/nfs  /etc/auto.nfs  --timeout=300`

Edit:  
`/etc/auto.nfs`

`netapp-vol4		-fstype=nfs,rw,bg,soft,nolock                   172.16.1.16:/vol/vol4`

Edit:  
`/etc/auto.cifs`

`Test             -fstype=cifs,username=utente,password=password,iocharset=utf8,file_mode=0555,dir_mode=0555 ://192.168.1.16/Test`

`service autofs restart`

Per verificare che funzioni:  
`ls -al /mnt/autofs/nfs/netapp-vol4`