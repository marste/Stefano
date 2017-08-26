---
id: 1478
title: Convert jpg to avi with ffmpeg
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1478
permalink: /convert-jpg-to-avi-with-ffmpeg/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1937766028
categories:
  - Linux
  - Windows
---
This will create a video slideshow (using video codec libx264) from series of jpg images, named image001.jpg, image002.jpg, image003.jpg, &#8230; and each image will have a duration of 2 seconds.  
`ffmpeg -r 1/2 -i image%3d.jpg -vcodec libx264 out.avi`