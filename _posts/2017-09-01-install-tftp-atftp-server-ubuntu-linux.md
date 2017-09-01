---
title: Come installare un TFTP Server su Ubuntu
date: 2017-09-01 14:00:00 +0200
author: Stefano Marzorati
layout: post
categories:
  - Linux
tags:
  - tftp
  - server
  - cisco
  - ubuntu
  - linux
---
*Innanzitutto non consiglio di installare xinetd*

Invece ti consiglio di installare **ATFTP**

`sudo apt-get install atftpd atftp`

`sudo nano /etc/default/atftpd`

Cambia da: `USE_INETD=true` a `USE_INETD=false`

Di default i files verranno salvati in **/srv/tftp**, ma se vuoi cambiare percorso, basta che modifichi sempre questo file, sostituendo il percorso /srv/tftp in quello che vuoi.

Nel mio caso ho creato la directory **/var/cisco_config** in questo modo:   

`sudo mkdir /var/cisco_config`
`sudo chmod -R 777 /var/cisco_config`
`sudo chown -R nobody /var/cisco_config`

Salva ed esci

`sudo invoke-rc.d atftpd start`
`sudo /etc/init.d/atftpd restart`

Come client usate **atftp**

Example:   

`atftp 127.0.0.1`
`put test.txt`
`get test.txt`
