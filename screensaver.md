---
layout: default
title: Risparmio energetico
permalink: /screensaver/
---

<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
    background: #000;
    transition: background 20s linear;
  }

  /* Contenuto normale del sito */
  #content {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background: #f8f8f8;
    color: #333;
    transition: opacity 1.8s ease;
    text-align: center;
    padding: 2rem;
    box-sizing: border-box;
  }

  /* Modalità screensaver attivo */
  body.saver {
    background: #000;
    animation: slowColor 120s linear infinite;
    cursor: none;
  }

  body.saver #content {
    opacity: 0;
    pointer-events: none;
  }

  body.saver #lamp {
    opacity: 1 !important;
  }

  /* Lampadina sempre visibile */
  #lamp {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 180px;
    height: 180px;
    pointer-events: none;
    opacity: 0;
    transition: opacity 2s ease;
    z-index: 9999;
  }

  /* Animazione lenta dello sfondo per evitare burn-in */
  @keyframes slowColor {
    0%    { background: #000000; }
    20%   { background: #0a001f; }
    40%   { background: #1a0033; }
    60%   { background: #1f0a2e; }
    80%   { background: #0f0a1f; }
    100%  { background: #000000; }
  }

  .info {
    max-width: 600px;
    font-size: 1.1rem;
    opacity: 0.8;
    margin-top: 2rem;
  }
</style>

<div id="content">
  <h1>Lampadina Screensaver</h1>
  <p>Questa pagina è pensata per essere lasciata aperta quando non usi il computer.</p>
  <p>Dopo 20 secondi di inattività lo schermo diventa quasi si spegne, lasciando solo una piccola lampadina accesa.</p>
  <p class="info">Ideale per monitor OLED (nero = pixel spenti = consumo quasi zero)<br>
  Lo sfondo cambia lentamente colore per proteggere anche i monitor LCD dal burn-in</p>
  <p><strong>Clicca o tocca lo schermo per riattivare subito</strong></p>
</div>

<!-- La lampadina (immagine SVG inline = zero richieste extra) -->
<div id="lamp" aria-hidden="true">
  <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="70" fill="#111" stroke="#333" stroke-width="8"/>
    <circle cx="100" cy="100" r="50" fill="#333"/>
    <path d="M80 140 Q100 170 120 140" fill="none" stroke="#555" stroke-width="12" stroke-linecap="round"/>
    <circle cx="100" cy="85" r="30" fill="#444"/>
    <circle cx="100" cy="80" r="20" fill="#ffdd00" opacity="0.9">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="r" values="18;22;18" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="100" cy="80" r="12" fill="#ffffaa">
      <animate attributeName="opacity" values="0.9;1;0.9" dur="2s" repeatCount="indefinite"/>
    </circle>
  </svg>
</div>

<script>
  let timer;

  const activate = () => {
    document.body.classList.add('saver');
  };

  const deactivate = () => {
    document.body.classList.remove('saver');
    resetTimer();
  };

  const resetTimer = () => {
    clearTimeout(timer);
    timer = setTimeout(activate, 20000); // 20 secondi di inattività
  };

  // Tutti gli eventi che svegliano lo schermo
  ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart', 'click', 'keydown'].forEach(e => {
    document.addEventListener(e, deactivate, { passive: true });
  });

  // Avvia il timer quando la pagina viene caricata
  resetTimer();
</script>