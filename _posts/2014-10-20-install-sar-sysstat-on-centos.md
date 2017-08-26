---
id: 3130
title: Install sar (sysstat) on CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3130
permalink: /install-sar-sysstat-on-centos/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3135836525
categories:
  - Linux
tags:
  - centos
  - configure
  - install
  - ksar
  - log
  - sar
  - sysstat
---
**Install:**  
`yum install sysstat`

**Avvialo al boot e fallo partire:**  
`chkconfig sysstat on &#038;&#038; service sysstat start`

**Schedulazione:**  
`cat /etc/cron.d/sysstat`

Di default ci sono questi processi schedulati:   

<code># Run system activity accounting tool every 10 minutes</code>   
<code>*/10 * * * * root /usr/lib64/sa/sa1 1 1</code>   
<code># 0 * * * * root /usr/lib64/sa/sa1 600 6 &</code>   
<code># Generate a daily summary of process accounting at 23:53</code>   
<code>53 23 * * * root /usr/lib64/sa/sa2 -A</code>   

**Di default i logs saranno salvati in:**  
`/var/log/sa/`

**Esempi:**

View disk i/o and transfer rate stats:  
`sar -b 3 10`

View memory and swap space stats:  
`sar -r 3 10`

View swapping stats:  
`sar -W 3 10`

View network stats:  
`sar -n DEV 3 10`

View CPU stats:  
`sar -P ALL 3 10`

Se vuoi visualizzare in modalità grafica i dati raccolti, puoi usare <a href="http://sourceforge.net/projects/ksar/files/latest/download" title="ksar" target="_blank">ksar</a>

Prima di usarlo, ti servirà esportare in un file i dati.  
Per esportare tutto, basterà digitare:

`LC_ALL=C sar -A > /tmp/sar.data.txt`

Se vuoi estrarre ad esempio tutti i dati del giorno 20, dovrò digitare:

`LC_ALL=C sar -A -f /var/log/sa/sa20 > /tmp/sar.data20.txt`

Poi aprire ksar e importare il file di testo da &#8220;data&#8221; &#8211; &#8220;Load from text file&#8230;&#8221;

L&#8217;applicazione ksar è in java e può essere comodamente usata anche in Windows.
