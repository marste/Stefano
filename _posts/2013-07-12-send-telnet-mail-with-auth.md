---
id: 1840
title: Send Telnet mail with AUTH
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1840
permalink: /send-telnet-mail-with-auth/
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1901557894
categories:
  - Linux
  - Windows
tags:
  - auth
  - smtp
  - telnet
---
Esempio:

`telnet smtp.marzorati.co 587`  
`EHLO`  
`auth login`  
incollare la username in formato base64  
`ZWRpc3BvcnRAdmgkZW8tbWFnYXppbmUuaXQ=`  
[http://www.motobit.com/util/base64-decoder-encoder.asp](http://www.motobit.com/util/base64-decoder-encoder.asp)   
incollare la password sempre in formato base64  
`ZWRpc4BvcnQ=`  
`mail from: `  
`rcpt to: `  
`data`  
`From: sender@example.com`  
`To: recipient@example.com`  
`Subject: Test message`  
`This is a test message.`  
`.`  
`QUIT`  
Se volete una GUI per Windows, potete usare <a href="http://telnet25.codeplex.com/releases/view/48205" title="telnet25" target="_blank">TELNET25.exe</a>
