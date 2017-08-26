---
id: 1340
title: Squid autenticazione tramite Active Directory
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1340
permalink: /squid-autenticazione-tramite-active-directory/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1913972937
categories:
  - Linux
  - Windows
---
editare il file `/etc/squid/squid.conf`

`http_access allow LAN AD`      (attiva l&#8217;autenticazione all&#8217;Active Directory)

o uno o l&#8217;altro

`http_access allow LAN`        (disabilitata l&#8217;autenticazione all&#8217;Active Directory)