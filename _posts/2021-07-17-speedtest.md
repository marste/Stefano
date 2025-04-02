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


<!--speedtest start-->
<div style="font-family: 'Inter', -apple-system, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; text-align: center;">
  <!-- Pulsante Fast.com -->
  <a href="https://fast.com/it/" target="_blank" style="
    display: inline-block;
    background: linear-gradient(135deg, #E50914 0%, #B00610 100%);
    color: white;
    padding: 16px 32px;
    margin: 12px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(229, 9, 20, 0.1);
    border: none;
    cursor: pointer;
    width: 80%;
    max-width: 280px;
  " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 12px rgba(229, 9, 20, 0.15)'" 
  onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(229, 9, 20, 0.1)'">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;">
      <polyline points="23 4 23 10 17 10"></polyline>
      <polyline points="1 20 1 14 7 14"></polyline>
      <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
    </svg>
    Test di velocità con Fast
  </a>

  <!-- Pulsante Cloudflare -->
  <a href="https://speed.cloudflare.com/" target="_blank" style="
    display: inline-block;
    background: linear-gradient(135deg, #F38020 0%, #FC5F45 100%);
    color: white;
    padding: 16px 32px;
    margin: 12px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(243, 128, 32, 0.1);
    border: none;
    cursor: pointer;
    width: 80%;
    max-width: 280px;
  " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 12px rgba(243, 128, 32, 0.15)'" 
  onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 6px rgba(243, 128, 32, 0.1)'">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;">
      <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
    </svg>
    Test di velocità con Cloudflare
  </a>

  <!-- Stile responsive aggiuntivo -->
  <style>
    @media (max-width: 480px) {
      a {
        padding: 14px 24px;
        font-size: 15px;
      }
    }
  </style>
</div>
<!--speedtest end-->

Se vuoi eseguire uno speed test da command line su Windows, utilizza pure <a href="https://marzorati.co/download/speedtest.exe" target="_blank">questo eseguibile</a> rilasciato da Ookla.