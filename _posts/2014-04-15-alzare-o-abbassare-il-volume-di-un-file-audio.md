---
id: 2827
title: Alzare o abbassare il volume di un file audio
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2827
permalink: /alzare-o-abbassare-il-volume-di-un-file-audio/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2613085141
categories:
  - Linux
  - Windows
tags:
  - abbassare
  - alzare
  - audio
  - mp3
  - volume
  - wav
---
Esempio:

`ffmpeg -i c:\input.wav -af 'volume=0.5' c:\output.wav`