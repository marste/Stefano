---
title: "Speed Test"
author: Stefano Marzorati
layout: post
date: 2021-07-17 11:05:00 +0200
image: 'https://marzorati.co/img/speed.webp'
share-img: 'https://marzorati.co/img/speed.webp'
categories: [Networking]
tags: [speed, test, velocità, connessione, fibra, broadband, bandwidth, speedtest, speed test, bandwidth speed test, internet speed test, broadband speed test, internet, network, broadband, latency, ping, throughput, download, upload, connection, dsl, adsl, cable, t1, isp, voip, ip, p address, tcp, mioip, whatismyip]
---
<center> <div id="ip-widget">
        <strong>Il tuo IP:</strong> <span id="ip"></span><br>
        <strong>Località:</strong> <span id="location"></span>
    </div>
    
    <script>
        fetch('https://ipapi.co/json/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('ip').textContent = data.ip;
                document.getElementById('location').textContent = `${data.city}, ${data.country_name}`;
            })
            .catch(error => console.error('Errore nel recupero dei dati IP:', error));
    </script></center>


<!--OST Widget code start--><div style="text-align:right;"><div style="min-height:360px;"><div style="width:100%;height:0;padding-bottom:50%;position:relative;"><iframe style="border:none;position:absolute;top:0;left:0;width:100%;height:100%;min-height:360px;border:none;overflow:hidden !important;" src="//openspeedtest.com/speedtest"></iframe></div></div></div>
<!-- OST Widget code end -->

Se vuoi eseguire uno speed test da command line su Windows, utilizza pure <a href="https://marzorati.co/download/speedtest.exe" target="_blank">questo eseguibile</a> rilasciato da Ookla.