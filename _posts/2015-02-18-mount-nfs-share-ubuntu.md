---
id: 3265
title: Mount NFS Share su Ubuntu
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3265
permalink: /mount-nfs-share-ubuntu/
authorsure_include_css:
  - 
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
dsq_thread_id:
  - 3526142991
categories:
  - Linux
tags:
  - client
  - export
  - mount
  - nfs
  - share
  - ubuntu
---
Installa questi pacchetti:  
`apt-get install nfs-common portmap`

Se vuoi vedere i volumi disponibili della tua NAS, digita il comando:  
`showmount -e 192.168.101.10` (indirizzo IP della NAS)

Crea una directory:  
`mkdir /mnt/nfs`

Poi monta il volume con il comando:  
`mount -o soft,intr,rsize=8192,wsize=8192 192.168.101.10:/vol/archiver /mnt/nfs`

Se vuoi rendere il mount persistente anche dopo un riavvio del server, modifica il file:  
`/etc/fstab`

e aggiungi:  
`192.168.101.10:/vol/archiver  /mnt/nfs  nfs   soft,intr,rsize=8192,wsize=8192`
