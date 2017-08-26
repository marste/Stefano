---
id: 131
title: 'Firefox 4 &#8211; Ripristinare icone delle cartelle dei bookmarks'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/12/firefox-4-ripristinare-icone-delle-cartelle-dei-bookmarks
permalink: /firefox-4-ripristinare-icone-delle-cartelle-dei-bookmarks/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 5657786409668341790
  - 5657786409668341790
  - 5657786409668341790
dsq_thread_id:
  - 2147821147
categories:
  - Linux
tags:
  - cartelle
---
Tramite Ubuntu Tweak, basta semplice andare in Desktop -> Gnome Settings e spuntiamo &#8220;Show icons in menus&#8221;

oppure

`gconftool-2 --set /desktop/gnome/interface/menus_have_icons --type bool true`

e per tornare come prima

`gconftool-2 --set /desktop/gnome/interface/menus_have_icons --type bool false`