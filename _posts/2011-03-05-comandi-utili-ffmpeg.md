---
id: 90
title: Comandi utili ffmpeg
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/comandi-utili-ffmpeg
permalink: /comandi-utili-ffmpeg/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 6776324971515121136
  - 6776324971515121136
  - 6776324971515121136
dsq_thread_id:
  - 2596224410
categories:
  - Linux
tags:
  - ffmpeg
---
**Base:**

> <span style="color:#0000ff;"><code>ffmpeg -formats</code></span>

> <span style="color:#0000ff;"><code>ffmpeg -codecs</code></span>

**Video:**

per ottenere info su un video:

> <span style="color:#0000ff;"><code>ffmpeg -i video.avi</code></span>

convertire da .avi a .mpg e viceversa:

> <span style="color:#0000ff;"><code>ffmpeg -i input.avi output.mpg</code></span>

convertire da .avi a .flv:

> <span style="color:#0000ff;"><code>ffmpeg -i input.avi -sameq -ar 44100 output.flv</code></span>

convertire da .flv a .mpg:

> <span style="color:#0000ff;"><code>ffmpeg -i input.flv -sameq -ab 56k -ar 22050 -b 500 -s 640x480 output.mpg</code></span>

convertire da .avi a .mpeg per lettori dvd:

> <span style="color:#0000ff;"><code>ffmpeg -i input.avi -target pal-dvd -ps 2000000000 -aspect 16:9 output.mpeg</code></span>

tagliare una sequenza video, dove **-ss** rappresenta il tempo d&#8217;inizio e **t** la fine:

> <span style="color:#0000ff;"><code>ffmpeg -vcodec copy -acodec copy -i input.avi -ss 00:00:30 -t 0:0:15 output.avi</code></span>

convertire video per ipod/iphone:

> <span style="color:#0000ff;"><code>ffmpeg -i input.flv -acodec libfaac -ab 96k -ac 2 -vcodec libx264 -vpre hq -vpre ipod320 -threads 0 -crf 22 output.mp4</code></span>

**Audio:**

estrarre suono da un video e convertirlo in mp3:

> <span style="color:#0000ff;"><code>ffmpeg -i input.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 output.mp3</code></span>

cancellare suono da un video:

> <span style="color:#0000ff;"><code>ffmpeg -i input.avi -an -b 1200 output.avi</code></span>

aggiungere suono ad un video:

> <span style="color:#0000ff;"><code>ffmpeg -i input.wav -i input.avi output.mpg</code></span>

convertire da wav a mp3:

> <span style="color:#0000ff;"><code>ffmpeg -i input.wav -ab 128 output.mp3</code></span>

**Immagini:**

convertire un video in una sequenza di immagini:

> <span style="color:#0000ff;"><code>ffmpeg -i input.flv -an -r 1 -y -s 320x240 video%d.jpg</code></span>

estrarre immagine da una sequenza prestabilita:

> <span style="color:#0000ff;"><code>ffmpeg -i input.flv -an -ss 00:00:25 -t 00:00:01 -r 1 -y video%d.jpg</code></span>

**Screencast:**

> <span style="color:#0000ff;"><code>ffmpeg -f x11grab -s 1280x1024 -r 30 -i :0.0 /tmp/screencast.mpg</code></span>

oppure:

> <span style="color:#0000ff;"><code>ffmpeg -y -t 60 -r 25 -s 1280x1024 -f x11grab -i :0.0 screencast.avi</code></span>

screencast utilizzando un **microfono** + oss:

> <span style="color:#0000ff;"><code>ffmpeg -s 1280x1024 -r 25 -f x11grab -i :0.0 -f oss -i /dev/dsp screen.avi</code></span>

screencast utilizzando un **microfono** + arecord:

> <span style="color:#0000ff;"><code>arecord -D default -t raw  -c 1 -f S16_LE -r 48000 - | ffmpeg -f s16le -ab 128k -ar 48000 -ac 1 -i  --acodec mp2 -f x11grab -r 2 -s 1280x1024 -i :0.0 -vcodec mpeg4  screen.avi</code></span>

screencast prendendo il suono direttamente da un file **mp3**:

> <span style="color:#0000ff;"><code>ffmpeg -f x11grab -s 1280x1024 -r 30 -i :0.0 -i percorso_del_file.mp3 -ar 22050 -ac 1 -acodec mp2 -ab 128k screen.avi</code></span>
> 
> <span style="color:#0000ff;"></span>
> 
> <span style="color:#0000ff;"><code>&lt;a href="http://www.edmondweblog.com/index.php/2010/01/05/top-20-comandi-per-ffmpeg/">via&lt;/a>&lt;br />
</code></span>