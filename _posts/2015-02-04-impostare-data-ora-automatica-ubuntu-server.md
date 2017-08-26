---
title: Impostare data e ora automatica su Ubuntu Server
author: Stefano Marzorati
layout: post
permalink: /impostare-data-ora-automatica-ubuntu-server/
comments: true
categories:
  - Linux
tags:
  - ntp
  - ubuntu
  - orario
  - time
  - esatta
---
Se vuoi sincronizzare <span style="text-decoration: underline;">solo una volta</span> l'orario, basta digitare:   
<code>sudo ntpdate pool.ntp.org</code>

Se invece vogliamo mantenere l'<span style="text-decoration: underline;">orario sempre aggiornato</span>, dobbiamo seguire questa procedura:   
<code>sudo apt-get install ntp</code>

Edita il seguente file:   
<code>sudo nano /etc/ntp.conf</code>

Assicurasi di aver all'interno del file i servers dal quale prendere l'ora esatta.


<pre><code>server 0.ubuntu.pool.ntp.org
server 1.ubuntu.pool.ntp.org
server 2.ubuntu.pool.ntp.org
server 3.ubuntu.pool.ntp.org</code></pre>

Riavvia il servizio:   
<code>sudo service ntp restart</code>
