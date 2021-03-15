---
title: 'Installare Disk Cleanup su Windows Server 2008 R2 (64 bit) in italiano'
author: Stefano Marzorati
layout: post
date: 2021-03-15 08:20:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [installare, disk, cleanup, pulizia, windows, italiano]
---
Su Windows Server 2008 R2 (64-bit) basterà copiare due files nei percorsi corretti con questi comandi:   

~~~batch
copy C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr_31bf3856ad364e35_6.1.7600.16385_none_c9392808773cd7da\cleanmgr.exe C:\Windows\System32\
copy C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr.resources_31bf3856ad364e35_6.1.7600.16385_it-it_46762abe7c82b9e8\cleanmgr.exe.mui C:\Windows\System32\it-IT
~~~
