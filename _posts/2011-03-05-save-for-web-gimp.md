---
id: 72
title: 'Save for Web &#8211; Gimp'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/save-for-web-gimp
permalink: /save-for-web-gimp/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 1770976981001352153
  - 1770976981001352153
  - 1770976981001352153
dsq_thread_id:
  - 2120493746
categories:
  - Linux
  - Windows
tags:
  - gimp
  - save
  - web
---
Scarica <a href="http://registry.gimp.org/files/gimp-save-for-web-0.29.0.tar.bz2" target="_blank">http://registry.gimp.org/files/gimp-save-for-web-0.29.0.tar.bz2</a>  
`sudo apt-get install libgimp2.0-dev intltool`  
e poi:

cd ~/.gimp-2.6/plug-ins/gimp-save-for-web-0.29.0/

./configure

make

sudo make install