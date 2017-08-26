---
id: 1517
title: Inviare una mail via cURL
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1517
permalink: /inviare-una-mail-via-curl/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1926977058
categories:
  - Linux
---
Esempio:  
`curl smtp://mailserver.acme.it -v --mail-from "rossi@gmail.com" --mail-rcpt "verdi@gmail.com" -T "c:test.txt"`