---
title: Come eliminare partizioni da una chiavetta USB in Windows con diskpart
date: 2018-12-18 16:15:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/usb.png'
share-img: 'https://marzorati.co/img/usb.png'
categories:
  - Windows
tags:
  - eliminare
  - partizioni
  - chiavetta
  - usb
  - diskpart
---
<code>diskpart</code>   
<code>list disk</code>   
<code>select disk X</code>   
<code>clean</code>(cancellerà la partizione presente)   
<code>create partition primary</code>(creerà una nuova partizione)   
<code>format fs=fat32 quick</code>(formattazine rapida in "fat32")   
<code>active</code>(renderà la partizione attiva e le permetterà di essere nuovamente bootable)   
<code>assign</code>(per attribuire una lettera alla propria USB)   
<code>exit</code>   
<BR>