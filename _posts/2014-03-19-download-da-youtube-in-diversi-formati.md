---
title: Download da youtube in diversi formati
date: 2019-09-02 09:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/video.jpg'
share-img: 'https://marzorati.co/img/video.jpg'
categories:
  - Linux
  - Windows
tags:
  - format
  - tag
  - youtube
  - youtube-dl
---
Esempio:

	youtube-dl https://www.youtube.com/watch?v=vk5Jg-mAeVY --list-formats

Il risultato sarà:   

	[info] Available formats for vk5Jg-mAeVY:
	format code  extension  resolution note
	249          webm       audio only DASH audio   50k , opus @ 50k, 2.78MiB
	250          webm       audio only DASH audio   60k , opus @ 70k, 3.46MiB
	251          webm       audio only DASH audio  107k , opus @160k, 6.17MiB
	140          m4a        audio only DASH audio  128k , m4a_dash container, mp4a.40.2@128k, 7.56MiB
	160          mp4        192x144    144p   66k , avc1.4d400b, 25fps, video only, 2.56MiB
	278          webm       192x144    144p   72k , webm container, vp9, 25fps, video only, 4.21MiB
	133          mp4        320x240    240p  114k , avc1.4d400d, 25fps, video only, 4.41MiB
	242          webm       320x240    240p  138k , vp9, 25fps, video only, 6.12MiB
	18           mp4        384x288    small  358k , avc1.42001E, mp4a.40.2@ 96k (44100Hz), 21.33MiB
	43           webm       640x360    medium , vp8.0, vorbis@128k, 19.27MiB (best)

Puoi scaricare il miglior video per qualità audio e video digitando:   

	youtube-dl https://www.youtube.com/watch?v=vk5Jg-mAeVY -f best
	
Oppure selezionare quello che si preferisce dalla lista qua sopra:   

	youtube-dl https://www.youtube.com/watch?v=vk5Jg-mAeVY -f 18