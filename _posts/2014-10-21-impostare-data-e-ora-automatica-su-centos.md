---
id: 3135
title: Impostare data e ora automatica su CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3135
permalink: /impostare-data-e-ora-automatica-su-centos/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3139838255
categories:
  - Linux
tags:
  - centos
  - data
  - impostare
  - ntp
  - ora
  - setup
---
Installa il servizio ntp:  
<code>yum install ntp</code>

Edita il file:  
<code>/etc/ntp/step-tickers</code>

Aggiungendo i servers ntp che vuoi, ad esempio:

<code>
0.pool.ntp.org   
1.pool.ntp.org   
2.pool.ntp.org
</code>

Fai in modo che il servizio si avvii automaticamente al boot:   

<code>chkconfig ntpd on</code>

Avvia il servizio:  
<code>service ntpd start</code>   

Controlla la data e l&#8217;ora:  
<code>date</code>