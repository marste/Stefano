---
title: Clonezilla salvare e ripristinare immagine su hard disk usb
author: Stefano Marzorati
layout: post
permalink: /clonezilla-salvare-e-ripristinare-immagine-su-hard-disk-usb/
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

1. Tutto uguale a prima fino al punto 10
2. Selezionare restoredisk
3. Scegli l'immagine che vuoi ripristinare
4. Scegli la destinazione