---
id: 1380
title: Darkstat on CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1380
permalink: /darkstat-on-centos/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1922509598
categories:
  - Linux
---
Installa: `yum install darkstat`  
Uso di base: `darkstat -i eth0`

Test via browser: http://ip-address:667

Esempio:

`darkstat -i eth0 -l 172.16.1.0/255.255.255.0 -f "port 80" --chroot /var/log/darkstat`

Per stoppare l&#8217;analisi: `pkill darkstat`

<div id="dc_vk_code" style="display:none;">
</div>