---
id: 1174
title: Convert video MTS to WMV
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1174
permalink: /convert-mts-to-wmv/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"194724054467485696";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"194724054467485696";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2162119827
categories:
  - Linux
  - Windows
tags:
  - convert
  - mts
  - wmv
---
`ffmpeg -i "/home/00064.MTS" -b 8500k -vcodec wmv2 -s 1024x576 -acodec wmav2 "/home/00064.wmv"`

<div id="dc_vk_code" style="display:none;">
</div>

oppure

`ffmpeg -i "/home/00064.MTS" -b 8500k -vcodec wmv1 -s 1024x576 -acodec wmav1 "/home/00064.wmv"`

<div id="dc_vk_code" style="display:none;">
</div>