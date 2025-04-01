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
        <strong>Località:</strong> <span id="location"></span><br>
        <strong>Paese:</strong> <span id="country"></span>
    </div>
    
    <script>
        fetch('https://ipapi.co/json/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('ip').textContent = data.ip;
                document.getElementById('location').textContent = `${data.city}, ${data.region}`;
                document.getElementById('country').textContent = data.country_name;
            })
            .catch(error => console.error('Errore nel recupero dei dati IP:', error));
    </script></center>


<!--OST Widget code start-->
<div style="text-align: center; margin: 30px 0;">
  <a 
    href="https://speed.cloudflare.com" 
    target="_blank"
    style="
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #F38020 0%, #FC5F45 100%);
      color: white;
      font-family: 'Segoe UI', Roboto, sans-serif;
      font-size: 18px;
      font-weight: 600;
      text-decoration: none;
      padding: 16px 32px;
      border-radius: 50px;
      box-shadow: 0 4px 15px rgba(252, 95, 69, 0.3);
      transition: all 0.3s ease;
      border: none;
      cursor: pointer;
      position: relative;
      overflow: hidden;
    "
    onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 7px 20px rgba(252, 95, 69, 0.4)'"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(252, 95, 69, 0.3)'"
  >
    <svg 
      xmlns="http://www.w3.org/2000/svg" 
      width="24" 
      height="24" 
      viewBox="0 0 24 24" 
      fill="none" 
      stroke="currentColor" 
      stroke-width="2" 
      stroke-linecap="round" 
      stroke-linejoin="round"
      style="margin-right: 10px;"
    >
      <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
    </svg>
    Testa la tua velocità con Cloudflare
  </a>
  <p style="margin-top: 12px; color: #666; font-size: 14px;">
    Misurazione precisa di download, upload e ping
  </p>
</div>
<!-- OST Widget code end -->

Se vuoi eseguire uno speed test da command line su Windows, utilizza pure <a href="https://marzorati.co/download/speedtest.exe" target="_blank">questo eseguibile</a> rilasciato da Ookla.