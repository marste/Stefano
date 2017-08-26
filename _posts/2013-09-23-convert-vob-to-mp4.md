---
id: 2006
title: Convert VOB to mp4
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2006
permalink: /convert-vob-to-mp4/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2605846385
categories:
  - Linux
  - Windows
tags:
  - convert
  - ffmpeg
  - mp4
  - vob
---
`ffmpeg -i D:\VIDEO_TSVTS_01_0.VOB -acodec copy -aq 100 -ac 5 -vcodec libx264 -threads 0 c:\output.mp4`