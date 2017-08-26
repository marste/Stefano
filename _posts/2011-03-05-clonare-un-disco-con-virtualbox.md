---
id: 2028
title: Clonare un disco con VirtualBox
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/clonare-un-disco-con-virtualbox
permalink: /clonare-un-disco-con-virtualbox/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 2663578423003024452
  - 2663578423003024452
  - 2663578423003024452
dsq_thread_id:
  - 2683027101
categories:
  - Linux
tags:
  - virtualbox
---
`VBoxManage clonehd "C:Usersutente.VirtualBoxHardDisksWindows XP.vdi" "E:XP.vdi"`

(su Ubuntu e Windows è la stessa cosa)

Se una macchina ubuntu non vede più la scheda di rete eth0 dopo aver copiato un disco:

`rm -f /etc/udev/rules.d/70-persistent-net.rules`