---
id: 2018
title: Quanta memoria è usata da un singolo processo
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2018
permalink: /quanta-memoria-usata-singolo-processo/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1900324840
categories:
  - Linux
tags:
  - memoria
  - memory
  - process
  - processo
  - ram
---
Esempio per l&#8217;httpd:

`ps -o rss -C httpd | tail -n +2 | (sed 's/^/x+=/'; echo x) | bc`

Esempio per mysqld:

`ps -o rss -C httpd | tail -n +2 | (sed 's/^/x+=/'; echo x) | bc`

I valori sono in kilobytes, per cui se lo vuoi sapere in **megabytes** dovrai fare &#8220;**diviso 1024**&#8221;

Se lo vuoi sapere in **gigabytes** dovrai fare &#8220;**diviso 1048576**&#8221;

<div id="dc_vk_code" style="display: none;">
</div>