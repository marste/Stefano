---
id: 2830
title: 'Accelerare o rallentare l&#8217;audio di un video'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2830
permalink: /accelerare-o-rallentare-laudio-di-un-video/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2613247067
categories:
  - Linux
  - Windows
tags:
  - audio
  - rallentare
  - velocizzare
---
Esempio:

`ffmpeg -i c:\input.mkv -filter:a "atempo=2.0" -vn c:\output.mkv`

Puoi usare valori tra 0.5 e 2.0

Ovviamente questo comando permette di accelerare o rallentare anche file .wav o .mp3 senza perdere di qualità e senza avere voci stridule alla Chipmunks.