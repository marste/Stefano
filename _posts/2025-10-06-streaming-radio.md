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
   /* border-top: 3px solid var(--border); <-- RIMOSSA */
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
  const audio    = document.getElementById('audio-player');
  const selector = document.getElementById('radio-select');
  const playBtn  = document.getElementById('play-pause');
  const prevBtn  = document.getElementById('prev');
  const nextBtn  = document.getElementById('next');
  const titleEl  = document.getElementById('station-title');
  const nowEl    = document.getElementById('now');
  const canvas   = document.getElementById('visualizer');
  const ctx      = canvas.getContext('2d', { alpha: false });

  // ---- Stations (salta la prima option placeholder) ----
  const stationOptions = Array.from(selector.options).slice(1);
  const stations = stationOptions.map(o => ({ url: o.value, name: o.text }));
  let currentIndex = -1;

  // ---- HLS / state ----
  let hls = null;
  let usingHls = false;
  let wantedPlaying = false;     // l’intento dell’utente (play/pause)
  let reconnectTimer = null;
  let lastUrl = "";

  // ---- Visualizer (lazy, e stop quando in pausa) ----
  let audioCtx = null;
  let analyser = null;
  let source = null;
  let dataArray = null;
  let rafId = null;

  function resizeCanvas() {
    const dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
    const w = Math.floor(canvas.clientWidth * dpr);
    const h = Math.floor(canvas.clientHeight * dpr);
    if (canvas.width !== w) canvas.width = w;
    if (canvas.height !== h) canvas.height = h;
    ctx.setTransform(1,0,0,1,0,0);
  }
  window.addEventListener('resize', resizeCanvas, { passive: true });
  resizeCanvas();

  function setPlayIcon(playing) {
    playBtn.innerHTML = playing
      ? '<svg class="icon" viewBox="0 0 48 48"><rect x="12" y="8" width="8" height="32"/><rect x="28" y="8" width="8" height="32"/></svg>'
      : '<svg class="icon" viewBox="0 0 48 48"><polygon points="14,10 34,24 14,38"/></svg>';
  }

  function setStatus(text) { nowEl.textContent = text; }

  function ensureAudioContext() {
    if (audioCtx) return;
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    source = audioCtx.createMediaElementSource(audio);
    analyser = audioCtx.createAnalyser();
    analyser.fftSize = 256;
    dataArray = new Uint8Array(analyser.frequencyBinCount);
    source.connect(analyser);
    analyser.connect(audioCtx.destination);
  }

  function startVisualizer() {
    ensureAudioContext();
    if (rafId) return;
    const draw = () => {
      rafId = requestAnimationFrame(draw);
      if (!analyser) return;
      analyser.getByteFrequencyData(dataArray);

      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const len = dataArray.length;
      const barW = Math.max(1, (canvas.width / len) * 1.6);
      let x = 0;
      ctx.fillStyle = '#000';
      for (let i = 0; i < len; i++) {
        const v = dataArray[i] / 255;
        const barH = Math.floor(v * canvas.height);
        ctx.fillRect(x, canvas.height - barH, barW, barH);
        x += barW + 1;
        if (x > canvas.width) break;
      }
    };
    draw();
  }

  function stopVisualizer() {
    if (!rafId) return;
    cancelAnimationFrame(rafId);
    rafId = null;
  }

  // ---- Helpers: safe play with mobile constraints ----
  async function safePlay() {
    try {
      if (audioCtx && audioCtx.state === 'suspended') {
        // Su iOS/Chrome mobile spesso serve riprendere il contesto su gesture
        await audioCtx.resume().catch(() => {});
      }
      await audio.play();
      return true;
    } catch (e) {
      // Autoplay/gesture restrictions oppure stream non pronto
      console.log('safePlay error:', e);
      return false;
    }
  }

  function clearReconnect() {
    if (reconnectTimer) clearTimeout(reconnectTimer);
    reconnectTimer = null;
  }

  function scheduleReconnect(delayMs = 1500) {
    clearReconnect();
    reconnectTimer = setTimeout(() => {
      if (currentIndex >= 0 && wantedPlaying) {
        // reload controllato dello stesso stream
        loadStream(currentIndex, { keepWanted: true, forceReload: true });
      }
    }, delayMs);
  }

  function destroyHls() {
    if (!hls) return;
    try { hls.destroy(); } catch (_) {}
    hls = null;
    usingHls = false;
  }

  function attachStream(url) {
    usingHls = /\.m3u8($|\?)/i.test(url) && window.Hls && Hls.isSupported();

    // Se url uguale e HLS già attaccato, non rifare tutto.
    if (usingHls && hls && lastUrl === url) return;

    // Cambio stream: reset pulito
    destroyHls();
    audio.pause();
    audio.removeAttribute('src');
    audio.load(); // reset pipeline

    if (usingHls) {
      hls = new Hls({
        // Buffer più “mobile safe”
        maxBufferLength: 20,
        backBufferLength: 10,
        maxLiveSyncPlaybackRate: 1.0,
        enableWorker: true,
        lowLatencyMode: false,
      });

      hls.attachMedia(audio);
      hls.on(Hls.Events.MEDIA_ATTACHED, () => {
        hls.loadSource(url);
      });

      hls.on(Hls.Events.ERROR, (evt, data) => {
        console.log('HLS error:', data);
        if (!data || !data.fatal) return;

        // Se l’utente ha messo in pausa, non impazzire.
        if (!wantedPlaying) return;

        switch (data.type) {
          case Hls.ErrorTypes.NETWORK_ERROR:
            // retry load
            try { hls.startLoad(); } catch (_) {}
            scheduleReconnect(1200);
            break;
          case Hls.ErrorTypes.MEDIA_ERROR:
            try { hls.recoverMediaError(); } catch (_) { scheduleReconnect(1200); }
            break;
          default:
            scheduleReconnect(1200);
            break;
        }
      });

    } else {
      audio.src = url;
      // audio.load() non sempre necessario, ma su mobile aiuta nei cambi rapidi
      audio.load();
    }

    lastUrl = url;
  }

  // ---- Core: load stream ----
  async function loadStream(index, opts = {}) {
    const { keepWanted = false, forceReload = false } = opts;
    if (index < 0 || index >= stations.length) return;

    clearReconnect();

    currentIndex = index;
    selector.selectedIndex = index + 1; // +1 perché abbiamo placeholder
    const { url, name } = stations[index];

    titleEl.textContent = name;
    playBtn.disabled = true;
    setPlayIcon(false);

    if (!keepWanted) wantedPlaying = true;

    setStatus('Connessione…');

    // Se stesso URL e non forzo reload: basta ripartire
    if (!forceReload && lastUrl === url && audio.src) {
      if (usingHls && hls) {
        try { hls.startLoad(); } catch (_) {}
      }
      const ok = await safePlay();
      if (!ok) setStatus('Tocca Play per riprendere');
      return;
    }

    attachStream(url);

    // Attendo che ci sia qualcosa da suonare (specie su mp3)
    const ok = await safePlay();
    playBtn.disabled = false;

    if (ok) {
      setPlayIcon(true);
      setStatus('In riproduzione');
      startVisualizer();
    } else {
      setPlayIcon(false);
      setStatus('Tocca Play per riprendere');
    }
  }

  // ---- Play/Pause behavior (no refresh) ----
  async function doPlay() {
    if (currentIndex < 0) return;
    wantedPlaying = true;

    if (usingHls && hls) {
      // Riprendi download segmenti
      try { hls.startLoad(); } catch (_) {}
    }

    // Se pipeline “fredda” (dopo pausa lunga / background), ricarico soft
    if (audio.readyState < 2 && lastUrl && !usingHls) {
      audio.load();
    }

    const ok = await safePlay();
    if (!ok) {
      setStatus('Tocca Play per riprendere');
      setPlayIcon(false);
      return;
    }

    playBtn.disabled = false;
    setPlayIcon(true);
    setStatus('In riproduzione');
    startVisualizer();
  }

  function doPause() {
    wantedPlaying = false;
    clearReconnect();

    // Pausa immediata
    try { audio.pause(); } catch (_) {}

    // Stop buffer/download su HLS ma NON distruggere
    if (usingHls && hls) {
      try { hls.stopLoad(); } catch (_) {}
    }

    setPlayIcon(false);
    setStatus('In pausa');
    stopVisualizer();
  }

  // ---- UI events ----
  selector.addEventListener('change', () => {
    const i = selector.selectedIndex - 1; // -1 placeholder
    if (i >= 0) loadStream(i);
  });

  playBtn.addEventListener('click', async () => {
    if (currentIndex < 0) return;

    // IMPORTANTE: su mobile, questo click è la "user gesture" utile anche per AudioContext
    if (audio.paused) await doPlay();
    else doPause();
  });

  prevBtn.addEventListener('click', () => {
    if (stations.length === 0) return;
    const nextI = currentIndex <= 0 ? 0 : currentIndex - 1;
    loadStream(nextI);
  });

  nextBtn.addEventListener('click', () => {
    if (stations.length === 0) return;
    const nextI = currentIndex >= stations.length - 1 ? stations.length - 1 : currentIndex + 1;
    loadStream(nextI);
  });

  // ---- Audio lifecycle / resilience ----
  audio.addEventListener('playing', () => {
    playBtn.disabled = false;
    setPlayIcon(true);
    if (wantedPlaying) setStatus('In riproduzione');
    startVisualizer();
  });

  audio.addEventListener('pause', () => {
    // Se la pausa non è voluta (es. background), non forzo play (iOS può bloccare)
    if (!wantedPlaying) {
      setPlayIcon(false);
      setStatus('In pausa');
      stopVisualizer();
    }
  });

  audio.addEventListener('error', () => {
    console.log('audio error');
    if (!wantedPlaying) return;
    setStatus('Errore, riconnessione…');
    scheduleReconnect(1200);
  });

  window.addEventListener('online', () => {
    if (wantedPlaying && currentIndex >= 0) {
      setStatus('Riconnessione…');
      scheduleReconnect(300);
    }
  }, { passive: true });

  window.addEventListener('offline', () => {
    setStatus('Offline');
  }, { passive: true });

  // Quando torni visibile: se l’utente voleva play, prova a riprendere (ma fallback su tap)
  document.addEventListener('visibilitychange', async () => {
    if (document.visibilityState !== 'visible') return;
    if (wantedPlaying && currentIndex >= 0) {
      // riprova soft
      await doPlay();
    }
  });

  // Stato iniziale
  setPlayIcon(false);
  setStatus('In pausa');
})();
</script>