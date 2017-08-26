---
id: 660
title: Avere dettagli su molti files
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=660
permalink: /avere-dettagli-su-molti-files/
dsq_thread_id:
  - 2010467868
categories:
  - Linux
tags:
  - files
---
``for i in `ls`; do file $i ;done``

Esempio risultato:

&#8211; Come.Lo.Sai.CD1.avi: RIFF (little-endian) data, AVI, 720 x 384, 25.00 fps, video: XviD, audio: MPEG-1 Layer 3 (stereo, 44100 Hz)  
&#8211; cmdtime3.exe: PE32 executable for MS Windows (console) Intel 80386 32-bit  
&#8211; esempio.txt: ASCII English text, with CRLF line terminators  
&#8211; ghiera_verde.html: HTML document text  
&#8211; test.jpg: JPEG image data, JFIF standard 1.02  
&#8211; rolex-submariner.pdf: PDF document, version 1.3  
&#8211; Mac\_OS\_X_Cursors.zip: Zip archive data, at least v2.0 to extract  
&#8211; mp3ico.gif: GIF image data, version 89a, 347 x 346  
&#8211; Alice: directory