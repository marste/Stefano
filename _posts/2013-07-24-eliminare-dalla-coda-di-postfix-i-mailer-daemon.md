---
id: 1868
title: Eliminare dalla coda di postfix i MAILER-DAEMON
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1868
permalink: /eliminare-dalla-coda-di-postfix-i-mailer-daemon/
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
  - 1913846132
categories:
  - Linux
tags:
  - delete
  - mailer-daemon
  - postfix
---
`mailq | grep MAILER-DAEMON | awk '{print $1}' | postsuper -d -`