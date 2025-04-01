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


<!--cloudflare code start-->
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
    Test di velocità con Cloudflare
  </a>
  <p style="margin-top: 12px; color: #666; font-size: 14px;">
    Misurazione precisa di download, upload e ping
  </p>
</div>
<!-- cloudflare code end -->
<center>Oppure utilizza</center>

<!--fast code start-->
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Netflix+Sans:wght@700;900&display=swap" rel="stylesheet">
    <style>
        .fast-btn-container {
            text-align: center;
            margin: 40px 0;
            font-family: 'Netflix Sans', 'Helvetica Neue', Arial, sans-serif;
        }
        
        .fast-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #E50914 0%, #B00710 100%);
            color: white;
            font-size: 20px;
            font-weight: 700;
            text-decoration: none;
            padding: 18px 36px;
            border-radius: 8px;
            box-shadow: 0 6px 18px rgba(229, 9, 20, 0.3);
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transform: translateY(0);
            letter-spacing: 0.5px;
        }
        
        .fast-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(229, 9, 20, 0.4);
        }
        
        .fast-btn:active {
            transform: translateY(1px);
            box-shadow: 0 4px 12px rgba(229, 9, 20, 0.4);
        }
        
        .fast-btn::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0));
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .fast-btn:hover::after {
            opacity: 1;
        }
        
        .fast-btn svg {
            margin-right: 12px;
            transition: transform 0.3s ease;
        }
        
        .fast-btn:hover svg {
            transform: scale(1.1);
        }
        
        .fast-subtext {
            margin-top: 16px;
            color: #777;
            font-size: 15px;
            line-height: 1.5;
        }
        
        /* Effetto luce dinamica */
        .fast-btn::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);
            transform: translate(var(--mouse-x), var(--mouse-y));
            opacity: 0;
            transition: opacity 0.5s;
            pointer-events: none;
        }
        
        .fast-btn:hover::before {
            opacity: 0.6;
        }
    </style>
</head>
<body>
    <div class="fast-btn-container">
        <a href="https://fast.com/it/" target="_blank" class="fast-btn" id="fastButton">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
            </svg>
            Test di velocità con FAST.COM
        </a>
        <p class="fast-subtext">
            Servizio ufficiale Netflix • Misurazione precisa in 30 secondi
        </p>
    </div>

    <script>
        // Effetto luce che segue il mouse
        const btn = document.getElementById('fastButton');
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            btn.style.setProperty('--mouse-x', `${x - rect.width/2}px`);
            btn.style.setProperty('--mouse-y', `${y - rect.height/2}px`);
        });
        
        // Effetto click più pronunciato
        btn.addEventListener('mousedown', () => {
            btn.style.transform = 'translateY(2px)';
            btn.style.boxShadow = '0 3px 9px rgba(229, 9, 20, 0.4)';
        });
        
        btn.addEventListener('mouseup', () => {
            btn.style.transform = 'translateY(-4px)';
            btn.style.boxShadow = '0 12px 24px rgba(229, 9, 20, 0.4)';
        });
    </script>
</body>


<!--fast code start-->

Se vuoi eseguire uno speed test da command line su Windows, utilizza pure <a href="https://marzorati.co/download/speedtest.exe" target="_blank">questo eseguibile</a> rilasciato da Ookla.