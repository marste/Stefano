---
title: 'Ridurre la grandezza di un video MP4 con FFMPEG'
author: Stefano Marzorati
layout: post
date: 2021-03-11 13:20:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [size, video, mp4, ffmpeg, dimensioni, ridurre]
---
Ecco un esempio di video di dimensioni 1920x1080 che voglio far diventare 640x352:   

~~~batch
ffmpeg -i C:\TMP\VID_20210310_111304.mp4 -vf scale=640:352 "C:\TMP\output_640.mp4"
~~~

oppure

~~~batch
ffmpeg -i input.avi -vf scale="640:-1" output.avi
~~~