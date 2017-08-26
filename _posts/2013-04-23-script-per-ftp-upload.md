---
id: 1538
title: Script per FTP upload
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1538
permalink: /script-per-ftp-upload/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:29;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:29;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1919572222
categories:
  - Linux
---
`   
#!/bin/sh   
USERNAME="tmp"   
PASSWORD="tmp"   
SERVER="192.168.101.8"</p>
<p># local directory to pickup *.tar.gz file   
LOCALDIR="/var/backups/snapshots"</p>
<p># remote server directory to upload backup   
BACKUPDIR="/prova"</p>
<p># login to remote server   
ftp -n -i $SERVER <<EOF   
user $USERNAME $PASSWORD   
cd $BACKUPDIR   
lcd $LOCALDIR   
mput *.tar.gz   
quit   
EOF   
`