---
id: 1419
title: Inviare files con rsync verso un FTP
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1419
permalink: /rsync-ftp-server-lftp/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1903071795
categories:
  - Linux
tags:
  - ftp
  - lftp
  - rsync
---
Installa lftp:  
`yum install lftp`

Accedi al server ftp:  
`lftp ftp.marzorati.co`  
`lftp ftp.marzorati.co:~> user stefano`  
`Password:   
lftp stefano@ftp.marzorati.co:~>`

Invia files da locale a remoto:  
`lftp ftp.marzorati.co:~> mirror -R /home/stefano/projects/website/version10 /var/www/html`