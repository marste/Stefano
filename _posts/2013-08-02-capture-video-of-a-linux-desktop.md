---
id: 1897
title: Capture video of a linux desktop
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
permalink: /capture-video-of-a-linux-desktop/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-08-02 07:36:57";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-08-02 07:36:57";}'
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - capture
  - desktop
  - ffmpeg
  - video
---
`ffmpeg -f x11grab -s wxga -r 25 -i :0.0 -sameq /tmp/out.mpg`