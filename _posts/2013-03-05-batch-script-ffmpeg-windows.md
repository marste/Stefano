---
id: 1453
title: Batch script ffmpeg windows
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1453
permalink: /batch-script-ffmpeg-windows/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1963402881
categories:
  - Windows
tags:
  - batch
  - ffmpeg
  - script
  - Windows
---
Salvare in un file .cmd il seguente script di esempio (mov to wmv):  
(con questi parametri avrai un .wmv compatibile con Windows Movie Maker per Windows XP)

`for %%a in ("*.mov") do ffmpeg -i %%a -b 8500k -vcodec wmv1 -acodec wmav1 %%~na.wmv`

`for %%a in ("*.mp4") do ffmpeg -i %%a -b 8500k -vcodec wmv1 -acodec pcm_s32le %%~na.wmv`

Oppure (wmv to avi)

`for %%a in ("*.wmv") do ffmpeg -i %%a -b 8500k -vcodec libx264 -acodec libfaac %%~na.avi`