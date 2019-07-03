---
title: 'Samsung Data Migration error cloning failed'
author: Stefano Marzorati
date: 2019-07-03 07:33:00 +0200
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - clonare
  - PC
  - ssd
  - hdd
  - samsung
  - migration
  - error
  - failed
  - ffffffff
---
Volendo sostituire i vecchi HDD meccanici con dei dischi SSD, di solito utilizzavo il software proprietario di Samsung **Data Migration**.   
Purtroppo ultimamente la clonazione arriva al 99% terminando con un errore: **cloning failed -00001[ffffffff]**   
Anche seguendo le decine di consigli trovati nelle FAQ (HDD defragment, disable page files, disable hibernation mode, disable system restore point files), non sono riuscito a portarte a termine la clonazione.   
Ho provato anche delle alternative consigliate, come AOMEI Backupper o  EaseUS Todo Backup Free, ma nulla... Anche se andavano a buon fine le clonazioni, il sistema operativo non si avviava mai.   

Alla fine ho deciso di provare il buon vecchio **CloneZilla** avviato da chiavetta USB e oltre ad essere stato molto più rapido, ha clonato perfettamente il disco.   

Ecco i passaggi corretti per effettuare la clonazione di un HDD su un SSD:   

 - **device-device**	work directly from a disk or partition to a disk or partition
 - **Beginner**	Beginner mode: Accept the default options
 - **disk_to_local_disk**	local_disk_to_local_disk_clone
 - scegli il disco **origine**
 - scegli disco **destinazione**
 - Skip checking/repairing source file system
