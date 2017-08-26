---
id: 3114
title: Installa e configura un certificato SSL su CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3114
permalink: /installa-e-configura-un-certificato-ssl-su-centos/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3065040158
categories:
  - Linux
tags:
  - centos
  - certificate
  - install
  - ssl
---
Genera una **private key**:  
`openssl genrsa -out privatekey.key 2048`

Genera un **Certificate Request** file:  
`openssl req -new -key privatekey.key -out request.csr`

Incolla la request.csr presso il tuo venditore di certificati SSL (ex. <a href="http://www.rapidssl.com/" title="http://www.rapidssl.com/" target="_blank">http://www.rapidssl.com/</a> )

Ti invieranno un **Web Server Certificate** (copia il certificato in un file che chiameremo **publickey.crt**)  
e ti invieranno un **Intermediate Certificate** (copia il certificato in un file che chiameremo **intermediate.crt**)

Ora configuriamo il nostro server Apache.

Copiamo i 3 files:  
&#8211; **publickey.crt**  
&#8211; **intermediate.crt**  
&#8211; **privatekey.key**

in **/etc/httpd/ssl**

Poi configuriamo il nostro VirtualHost aggiungendo le 3 righe che richiamano i nostri certificati, ad esempio:

<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%"><span style="font-weight: bold">&lt;VirtualHost</span> <span style="border: 1px solid #FF0000">123.456.78.9:443</span> <span style="border: 1px solid #FF0000">172.16.1.101:443</span> <span style="border: 1px solid #FF0000">*:80</span><span style="font-weight: bold">&gt;</span>

  ServerName			stefano.marzorati.it 

  SSLEngine			On
  SSLProxyEngine		On
  SSLCertificateFile 		/etc/httpd/ssl/publickey_2014.crt
  SSLCertificateKeyFile 	/etc/httpd/ssl/privatekey_2014.key
  SSLCertificateChainFile	/etc/httpd/ssl/intermediate_2014.crt
    
  ProxyRequests         	Off
  ProxyPreserveHost     	On
   
  ProxyPass             	/ http://12.34.56.78/test/
  ProxyPassReverse      	/ http://12.34.56.78/test/

  ErrorLog              	/var/log/httpd/test.it-error.log
  CustomLog		   	/var/log/httpd/test.it-combined.log combined

<span style="font-weight: bold">&lt;/VirtualHost&gt;</span>
</pre>
</div>

Per testare che il certificato sia installato correttamente:

<a href="https://sslguru.it/ssl-tools/check-ssl-certificate.html" target="_blank">https://sslguru.it/ssl-tools/check-ssl-certificate.html</a>