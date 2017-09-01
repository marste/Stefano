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

<code>sudo apt-get install atftpd atftp</code>   

<code>sudo nano /etc/default/atftpd</code>   

Cambia da: <code>USE_INETD=true</code> a <code>USE_INETD=false</code>   

Di default i files verranno salvati in **/srv/tftp**, ma se vuoi cambiare percorso, basta che modifichi sempre questo file, sostituendo il percorso /srv/tftp in quello che vuoi.

Nel mio caso ho creato la directory **/var/cisco_config** in questo modo:   

<code>sudo mkdir /var/cisco_config</code>   
<code>sudo chmod -R 777 /var/cisco_config</code>   
<code>sudo chown -R nobody /var/cisco_config</code>   

Salva ed esci

<code>sudo invoke-rc.d atftpd start</code>

<code>sudo /etc/init.d/atftpd restart</code>

Come client usate **atftp**

Example:   
<code>atftp 127.0.0.1</code>   
<code>put test.txt</code>   
<code>get test.txt</code>   
