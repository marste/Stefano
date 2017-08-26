---
id: 3289
title: Create .tar file with exclude
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3289
permalink: /create-tar-file-with-exclude/
authorsure_include_css:
  - 
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
categories:
  - Linux
tags:
  - create
  - exclude
  - tar
  - zip
---
Esempio:

`tar -pczf /tmp/site.tar.gz /var/www/html/site --exclude=/var/www/html/site/cache --exclude=/var/www/html/site/logs --exclude=/var/www/html/site/moduli/attachments`
