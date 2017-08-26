---
id: 1317
title: Convert video for Mobile
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1317
permalink: /convert-video-for-mobile/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
categories:
  - Linux
  - Windows
---
Formato File: MP4  
Formato Video: H.264  
Frame Size: 640&#215;320  
Bitrate: 500kb  
Frame rate: 24  
Formato audio: AAC  
Date rate: 128 kpbs  
Output sample: 44.100 KHz

ffmpeg -i c:input.mp4 -acodec libfaac -ab 128kb -ac 2 -vcodec libx264 -b 500kb -r 24 -ar 44100 -s 640&#215;320 c:output.mp4

<div id="dc_vk_code" style="display:none;">
</div>