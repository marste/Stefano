---
id: 1571
title: wget download all files from ftp
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1571
permalink: /wget-download-all-files-from-ftp/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1978212471
categories:
  - Linux
  - Windows
---
`wget -r -c -nc ftp://username:password@ftp.example.com/`

-r = recursive  
-c = resume  
-nc = &#8211;no-clobber (skip downloads that would download to existing files)