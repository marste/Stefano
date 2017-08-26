---
id: 2766
title: Mount volumi e share su CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2766
permalink: /mount-volumi-e-share-su-centos/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2456723923
dsq_needs_sync:
  - 1
categories:
  - Linux
tags:
  - centos
  - montare
  - mount
  - share
  - volume
---
Se voglio montare dei volumi nfs su CentOS, occorre editare il file:

`/etc/auto.nfs`

E ad esempio aggiungere queste righe per montare dei volumi di Netapp:

`netapp-vol2           -fstype=nfs,rw,bg,soft,nolock                   netapp:/vol/vol2`  
`netapp-vol3           -fstype=nfs,rw,bg,soft,nolock                   netapp:/vol/vol3`

Se invece vuoi montare delle share Windows, occorre editare il file:

`/etc/auto.cifs`

E ad esempio aggiungere queste righe per montare delle share:

`storageserver           -fstype=cifs,file_mode=0644,dir_mode=0755,username=administrator,password=password ://storageserver/BackupMysql`  
`webserver               -fstype=cifs,ro,file_mode=0644,dir_mode=0755,username=administrator,password=password ://webserver/c\$   
`  
`servizi_pdf             -fstype=cifs,username=arcserve,password=password,iocharset=utf8,file_mode=0777,dir_mode=0777 ://netapp/Servizi_PDF`

`service autofs restart`

Per verificare che funzioni:  
`ls -al /mnt/autofs/nfs/netapp-vol...`