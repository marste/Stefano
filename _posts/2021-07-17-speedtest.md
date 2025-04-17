---
title: Speed Test
author: Stefano Marzorati
layout: post
date: 2021-07-17 11:05:00 +0200
image: 'https://marzorati.co/img/speedtest.png'
share-img: 'https://marzorati.co/img/speedtest.png'
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
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: white;
    color: black;
    padding: 16px 32px;
    margin: 12px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    border: 1px solid #e0e0e0;
    cursor: pointer;
    width: 80%;
    max-width: 280px;
    gap: 10px;
  " 
  onmouseover="this.style.background='#E50914'; this.style.color='white'; this.style.borderColor='#E50914'; this.querySelector('svg').style.filter='brightness(0) invert(1)'" 
  onmouseout="this.style.background='white'; this.style.color='black'; this.style.borderColor='#e0e0e0'; this.querySelector('svg').style.filter='none'">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="transition: all 0.3s ease;">
      <path d="M4 17V7H8L12 3V21L8 17H4Z" fill="currentColor"/>
      <path d="M14 7H18V17H14L10 21V3L14 7Z" fill="currentColor"/>
    </svg>
    Fast.com
  </a>

  <!-- Pulsante Cloudflare -->
  <a href="https://speed.cloudflare.com/" target="_blank" style="
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: white;
    color: black;
    padding: 16px 32px;
    margin: 12px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    border: 1px solid #e0e0e0;
    cursor: pointer;
    width: 80%;
    max-width: 280px;
    gap: 10px;
  " 
  onmouseover="this.style.background='#F38020'; this.style.color='white'; this.style.borderColor='#F38020'; this.querySelector('svg').style.filter='brightness(0) invert(1)'" 
  onmouseout="this.style.background='white'; this.style.color='black'; this.style.borderColor='#e0e0e0'; this.querySelector('svg').style.filter='none'">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="transition: all 0.3s ease;">
      <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" fill="currentColor"/>
    </svg>
    Cloudflare
  </a>
  
</div>
<!--speedtest end-->

Se vuoi eseguire uno speed test da command line su Windows, utilizza pure <a href="https://marzorati.co/download/speedtest.exe" target="_blank">questo eseguibile</a> rilasciato da Ookla.