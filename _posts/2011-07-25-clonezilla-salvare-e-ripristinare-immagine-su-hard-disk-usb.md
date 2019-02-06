---
title: Clonezilla salvare e ripristinare immagine su hard disk usb
author: Stefano Marzorati
date: 2019-02-06 16:00:00 +0200
layout: post
permalink: /clonezilla-salvare-e-ripristinare-immagine-su-hard-disk-usb/
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
categories:
  - Linux
  - Windows
tags:
  - clonezilla
  - hdd
  - immagine
  - restore
  - ripristinare
  - salvare
  - save
  - sda
  - sdb
  - usb
---
***Fai partire il cd di boot e seleziona quanto segue:***   

1. it_IT.UTF-8 Italian
2. Non modificare la mappatura della tastiera
3. Start_Clonezilla Avvio di Clonezilla
4. device-image disco partizione su/da immagine
5. local_dev
6. (attacca il disco usb esterno)
7. Seleziona il disco usb esterno (sdbx)
8. lascia la / se vuoi salvare l'immagine nella root del disco usb
9. Beginner
10. Savedisk
11. Seleziona il disco di origine (sdax)   
_______________

***Per ripristino immagine:***   

1. it_IT.UTF-8 Italian
2. Non modificare la mappatura della tastiera
3. Start_Clonezilla Avvio di Clonezilla
4. device-image disco partizione su/da immagine
5. local_dev
6. (attacca il disco usb esterno)
7. Seleziona il disco usb esterno (sdbx o sddx)
8. lascia la / se vuoi leggere l'immagine nella root del disco usb
9. Beginner
10. Restoredisk
11. Seleziona il disco di origine (sdax)