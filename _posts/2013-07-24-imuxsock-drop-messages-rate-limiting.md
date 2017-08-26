---
id: 1862
title: imuxsock begins to drop messages due to rate-limiting
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1862
permalink: /imuxsock-drop-messages-rate-limiting/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1947848132
categories:
  - Linux
tags:
  - debian
  - imuxsock
  - rate-limiting
  - rsyslog
---
Se nel messages log trovate un errore del genere:  
`rsyslogd-2177: imuxsock begins to drop messages from pid 12050 due to rate-limiting`

per disabilitare il limite edita il file **/etc/rsyslog.conf** e nella sezione &#8220;modules&#8221;, aggiungi:  
`$SystemLogRateLimitInterval 0`  
`$SystemLogRateLimitBurst 0`

Se non lo vuoi disabilitare, potresti mettere come valori:  
`$SystemLogRateLimitInterval 2`  
`$SystemLogRateLimitBurst 5000`

`/etc/init.d/rsyslog restart`