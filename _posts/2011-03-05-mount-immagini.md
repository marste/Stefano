---
id: 92
title: Mount immagini
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/mount-immagini
permalink: /mount-immagini/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 4005853294777284204
  - 4005853294777284204
  - 4005853294777284204
categories:
  - Linux
tags:
  - immagini
  - iso
---
<span style="font-weight:bold;">Immagine ISO:</span>

> mount -t iso9660 -o loop archivio.iso /directory/di/montaggio

#### 

#### Immagine BIN e Cue

Per poter montare questo tipo di immagine prima bisogna convertirla in ISO.

> apt-get install bchunk
> 
> bchunk archivio.bin archivio.cue nuovoarchivio.iso

Una volta trasformato in ISO:

> mount -t iso9660 -o loop archivio.iso /directory/di/montaggio

#### 

#### Immagine NRG

Non c’è bisogno di convertirla in ISO

> mount -t iso9660 -o loop,offset=307200 immagine.nrg /directory/di/montaggio

Se si volesse convertire:

> apt-get install nrg2iso
> 
> nrg2iso archivo.nrg nuovoarchivio.iso

#### 

#### Immagine MDFe MDS

Anche qua bisogna prima convertire in Iso

> apt-get install mdf2iso
> 
> mdf2iso archivio.mdf nuovaimmagine.iso

#### 

#### Immagine IMG

Convertiamo in ISO

> apt-get install ccd2iso
> 
> ccd2iso immagine.img immagine.iso

#### 

#### Immagine DAA

Il formato DAA è quello che utilizza Poweriso. Anche in questo caso bisogna prima convertirlo in ISO.

> wget http://poweriso.com/poweriso.tar.gz
> 
> tar -zxvf poweriso.tar.gz

convertiamo in ISO con:

> ./poweriso convert immagine.daa -o nuovaimmagine.iso

Tutti i formati di immagine convertiti in ISO, si montano con:

> mount -t iso9660 -o loop archivio.iso /directory/di/montaggio
> 
> [via][1]

 [1]: http://www.edmondweblog.com/index.php/2008/11/16/montare-immagini-isobincuenrgmdfimgccddaa-in-debian/