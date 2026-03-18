---
title: Streaming Radio
permalink: /radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
date: 2025-06-04 07:00:00 +0200
author: Stefano Marzorati
layout: page
categories: [Music]
tags: [radio, web, streaming, mp3, m3u8, m2o, gabber, frenchcore, techno, jazz, pop]
published: false
---
<style>
:root {
  --border: #000;
  --bg: #fff;
  --font: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}
.radio-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--font);
  gap: 1rem;
  margin-bottom: 2rem;
  padding: 0 1rem;
}
label[for="radio-select"] {
  font: 700 2rem/1.1 var(--font);
  margin-top: .25rem;
  text-align: center;
}
#radio-select {
  font-size: 2rem;
  padding: .75em 1.2em;
  border: 2px solid #000;
  border-radius: .75em;
  background: var(--bg);
  min-width: 260px;
  max-width: min(90vw, 740px);
  text-align: center;
  outline: none;
}
.player-card {
  width: 100%;
  max-width: 1100px;
  border: 3px solid var(--border);
  border-radius: 1rem;
  background: #fff;
  box-shadow: 0 10px 30px rgba(0,0,0,.08);
  overflow: clip;
}
.player-top {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding: 2rem 1rem 1rem 1rem;
}
#play-pause {
  width: 10rem;
  height: 10rem;
  border: 5px solid var(--border);
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  transition: .2s;
  display: flex;
  justify-content: center;
  align-items: center;
}
#play-pause:hover:enabled { background: #f3f3f3; transform: translateY(-2px); }
#play-pause:active:enabled { transform: translateY(0); }
#play-pause .icon { width: 5rem; height: 5rem; }
.control-btn {
  width: 7rem;
  height: 7rem;
  border: 3px solid #000;
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: .2s;
}
.control-btn:hover { background: #f3f3f3; transform: translateY(-1px); }
.control-btn .icon { width: 4rem; height: 4rem; }
.meta {
  text-align: center;
  margin-top: 3rem;
}
.meta .title {
  font-weight: 700;
  font-size: 2rem;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.vis-wrap {
  width: 100%;
  background: #fff;
  border-bottom: 3px solid var(--border);
  position: relative;
}
#visualizer {
  width: 100%;
  display: block;
  height: clamp(160px, 33vw, 180px);
}
.vis-overlay {
  position: absolute; inset: 0;
  pointer-events: none;
}
.footer-row {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}
.now {
  font-size: .9rem;
  color: #000;
}
</style>
<div class="radio-wrapper">
  <label for="radio-select">Scegli una radio</label>
  <select id="radio-select">
    <option value="" disabled selected>🔊 Select and make it louder! 👊</option>
    <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">M2O</option>
    <option value="https://stream.technolovers.fm/gabber">Gabber</option>
	<option value="https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420">90s 90s Techno</option>
	<option value="https://techno-revival.stream.laut.fm/techno-revival?ref=web-app&start_time=1759669832984">Techno Revival</option>
	<option value="https://listen5.myradio24.com/eugenijus">Truckers Rave Radio</option>
	<option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejaybck/radiodeejaybck/play1.m3u8">Radio Deejay</option>
	<option value="https://vdnvsxa1-4c4b867c89244861ac216426883d1ad0.msvdn.net/webradio/deejaytime/live.m3u8">Deejay Time</option>
	<option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songs/radiodeejay30songs/play1.m3u8">30 Songs - Deejay</option>
	<option value="https://22713.live.streamtheworld.com/TLPSTR01.mp3?dist=538_web">538 Dance Department</option>
	<option value="https://n32a-eu.rcs.revma.com/prbak410t13vv?rj-ttl=5&rj-tok=AAABm7aZVdkAXZEe-G3o3PLkeQ">ON Club</option>
	<option value="https://stream.discoradio.radio/audio/disco.stream_aac64/chunklist.m3u8">Disco Radio</option>
	<option value="https://regiocast.streamabc.net/regc-80s80smweb2517500-mp3-192-1672667">80s 80s</option>
    <option value="https://altair.streamerr.co:8124/stream">Deep House FM</option>
	<option value="https://sh.onweb.gr:7115/;">Venus Radio</option>
    <option value="https://smoothjazz.cdnstream1.com/2585_128.mp3">Smooth Jazz</option>
    <option value="https://ilsole24ore-radio.akamaized.net/hls/live/2035301/radio24/playlist-48000.m3u8">Il Sole 24 ore</option>
  </select>
  <div class="player-card" id="player-card">
    <div class="player-top">
      <button id="prev" class="control-btn" aria-label="Previous">
        <svg class="icon" viewBox="0 0 48 48" fill="currentColor">
          <polygon points="32,10 16,24 32,38"/>
        </svg>
      </button>
      <button id="play-pause" aria-label="Play / Pause" disabled>
        <svg class="icon" viewBox="0 0 48 48" fill="currentColor">
          <polygon points="14,10 34,24 14,38"/>
        </svg>
      </button>
      <button id="next" class="control-btn" aria-label="Next">
        <svg class="icon" viewBox="0 0 48 48" fill="currentColor">
          <polygon points="16,10 32,24 16,38"/>
        </svg>
      </button>
    </div>
    <div class="meta">
      <div class="title" id="station-title">Nessuna radio selezionata</div>
    </div>
    <div class="vis-wrap">
      <canvas id="visualizer"></canvas>
      <div class="vis-overlay"></div>
    </div>
    <div class="footer-row">
      <span class="now" id="now">In pausa</span>
    </div>
  </div>
  <audio id="audio-player" preload="auto" crossorigin="anonymous"></audio>
</div>
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>

<script>
(() => {
  const audio = document.getElementById('audio-player');
  const selector = document.getElementById('radio-select');
  const playBtn = document.getElementById('play-pause');
  const prevBtn = document.getElementById('prev');
  const nextBtn = document.getElementById('next');
  const titleEl = document.getElementById('station-title');
  const nowEl = document.getElementById('now');
  const canvas = document.getElementById('visualizer');
  const ctx = canvas.getContext('2d');
  let hls = null;
  let audioCtx = null;
  let analyser, source, dataArray;
  let isPlaying = false;
  let wasPlayingBeforeHide = false;
  let hideTime = 0;
  
  const stations = Array.from(selector.options).map(o => ({url: o.value, name: o.text}));
  let currentIndex = -1;
  
  function resizeCanvas() { canvas.width = canvas.clientWidth; canvas.height = canvas.clientHeight; }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();
  
  function setPlayIcon(playing) {
    playBtn.innerHTML = playing
      ? '<svg class="icon" viewBox="0 0 48 48"><rect x="12" y="8" width="8" height="32"/><rect x="28" y="8" width="8" height="32"/></svg>'
      : '<svg class="icon" viewBox="0 0 48 48"><polygon points="14,10 34,24 14,38"/></svg>';
  }
  
  function setupVisualizer() {
    if (audioCtx) return;
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    source = audioCtx.createMediaElementSource(audio);
    analyser = audioCtx.createAnalyser();
    source.connect(analyser);
    analyser.connect(audioCtx.destination);
    analyser.fftSize = 256;
    dataArray = new Uint8Array(analyser.frequencyBinCount);
    draw();
  }
  
  function draw() {
    requestAnimationFrame(draw);
    if (!analyser) return;
    analyser.getByteFrequencyData(dataArray);
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    const barWidth = (canvas.width / dataArray.length) * 2.5;
    let x = 0;
    for (let i = 0; i < dataArray.length; i++) {
      const barHeight = dataArray[i] / 2;
      ctx.fillStyle = '#000';
      ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
      x += barWidth + 1;
    }
  }

  function loadStream(index, forceReload = false) {
    if (index < 0 || index >= stations.length) return;
    
    // Se è lo stesso stream e non forziamo reload, non fare nulla se già attivo
    if (currentIndex === index && !forceReload && (audio.src || hls)) {
      return;
    }
    
    currentIndex = index;
    const {url, name} = stations[index];
    
    // Pulisci HLS precedente
    if (hls) { hls.destroy(); hls = null; }
    
    // Ferma e resetta audio
    audio.pause(); 
    audio.src = '';
    setPlayIcon(false); 
    playBtn.disabled = true;
    nowEl.textContent = 'Connessione…';
    titleEl.textContent = name;

    const play = () => {
      audio.play().then(() => {
        playBtn.disabled = false; 
        setPlayIcon(true); 
        isPlaying = true;
        nowEl.textContent = 'In riproduzione'; 
        setupVisualizer();
      }).catch((err) => {
        console.log('Errore durante la riproduzione:', err);
        nowEl.textContent = 'Errore, ritento...';
        setTimeout(() => loadStream(currentIndex, true), 2000);
      });
    };

    if (/\.m3u8($|\?)/i.test(url) && window.Hls && Hls.isSupported()) {
      hls = new Hls({
        maxBufferLength: 60,
        maxMaxBufferLength: 120,
        maxBufferSize: 60 * 1000 * 1000,
        liveSyncDurationCount: 3,
        liveMaxLatencyDurationCount: 10
      });
      hls.loadSource(url);
      hls.attachMedia(audio);
      hls.on(Hls.Events.MANIFEST_PARSED, play);
      hls.on(Hls.Events.ERROR, (event, data) => {
        if (data.fatal) {
          switch (data.type) {
            case Hls.ErrorTypes.NETWORK_ERROR:
              console.log('Errore di rete, tentativo di riconnessione...');
              hls.startLoad();
              break;
            case Hls.ErrorTypes.MEDIA_ERROR:
              console.log('Errore media, tentativo di recupero...');
              hls.recoverMediaError();
              break;
            default:
              console.log('Errore non recuperabile:', data);
              hls.destroy();
              loadStream(currentIndex, true);
              break;
          }
        }
      });
    } else {
      audio.src = url;
      play();
    }
  }
  
  selector.addEventListener('change', () => { 
    const i = selector.selectedIndex; 
    if (i > 0) loadStream(i); 
  });
  
  playBtn.addEventListener('click', () => {
    if (!audio.src && currentIndex > 0) {
      loadStream(currentIndex, true);
      return;
    }
    
    if (audio.paused) { 
      audio.play().catch(err => console.error('Error on manual play:', err)); 
    } else { 
      audio.pause(); 
    }
  });
  
  audio.addEventListener('pause', () => { 
    setPlayIcon(false); 
    nowEl.textContent = 'In pausa'; 
    isPlaying = false; 
  });
  
  audio.addEventListener('playing', () => { 
    setPlayIcon(true); 
    nowEl.textContent = 'In riproduzione'; 
    isPlaying = true; 
  });
  
  audio.addEventListener('error', () => {
    console.log('Errore audio, tentativo di riconnessione...');
    nowEl.textContent = 'Errore, riconnessione...';
    setTimeout(() => loadStream(currentIndex, true), 2000);
  });
  
  // GESTIONE VISIBILITY CHANGE - La chiave per le telefonate
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') {
      // Pagina nascosta (telefonata in arrivo o app in background)
      wasPlayingBeforeHide = !audio.paused;
      hideTime = Date.now();
      console.log('Pagina nascosta, wasPlaying:', wasPlayingBeforeHide);
    } else {
      // Pagina visibile di nuovo
      const hiddenDuration = Date.now() - hideTime;
      console.log('Pagina visibile, durata nascosta:', hiddenDuration, 'ms');
      
      // Se era in riproduzione ed è passato più di 2 secondi (probabilmente telefonata)
      if (wasPlayingBeforeHide && hiddenDuration > 2000) {
        console.log('Rilevata interruzione lunga, ricarico stream...');
        nowEl.textContent = 'Sincronizzazione...';
        // Ricarica lo stesso stream per tornare al tempo reale
        loadStream(currentIndex, true);
      } else if (wasPlayingBeforeHide && audio.paused) {
        // Se era solo brevemente in pausa, riprendi normalmente
        audio.play().catch(err => {
          console.log('Errore ripresa:', err);
          loadStream(currentIndex, true);
        });
      }
      
      // Resume AudioContext
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }
  });
  
  // Gestione online/offline
  window.addEventListener('online', () => {
    if (currentIndex >= 0) {
      nowEl.textContent = 'Riconnessione...';
      loadStream(currentIndex, true);
    }
  });
  
  window.addEventListener('offline', () => {
    nowEl.textContent = 'Offline, in attesa di connessione...';
  });
  
  prevBtn.addEventListener('click', () => { 
    if (currentIndex > 1) loadStream(currentIndex - 1); 
  });
  
  nextBtn.addEventListener('click', () => { 
    if (currentIndex < stations.length - 1) loadStream(currentIndex + 1); 
  });
})();
</script>