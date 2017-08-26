---
id: 3166
title: 'Protezione contro gli attacchi BEAST &#8211; CRIME &#8211; BREACH &#8211; POODLE'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3166
permalink: /protezione-contro-gli-attacchi-beast-crime-breach-poodle/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3258504930
categories:
  - Linux
  - Windows
tags:
  - apache
  - attacks
  - BEAST
  - BREACH
  - CRIME
  - virtualhost
---
La configurazione ideale per Apache è:   
<code>
SSLEngine			On   
  SSLProxyEngine		On   
  SSLProtocol			All -SSLv2 -SSLv3   
  SSLCipherSuite		ECDHE-RSA-AES128-SHA256:AES128-GCM-SHA256:RC4:HIGH:!MD5:!aNULL:!EDH   
  SSLCompression Off   
  SSLCertificateFile 	/etc/httpd/ssl/publickey_2014.crt   
  SSLCertificateKeyFile 	/etc/httpd/ssl/privatekey_2014.key   
  SSLCertificateChainFile	/etc/httpd/ssl/intermediate_2014.crt
</code>  