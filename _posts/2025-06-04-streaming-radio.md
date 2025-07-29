---
title: Streaming Radio
permalink: /radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
date: 2025-06-04 07:00:00 +0200
author: Stefano Marzorati
layout: page
bigimg: ['https://marzorati.co/img/post/music_1.jpeg', 'https://marzorati.co/img/post/music_4.png']
categories: [Music]
tags: [radio, web, streaming, mp3, m3u8, m2o, gabber, frenchcore, techno, jazz, pop]
---

<style>
:root {
  --accent: #4A90E2;
  --border: #000;
  --bg: #f9f9f9;
  --radius: .75em;
  --font: sans-serif;
}

.radio-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  font-family: var(--font);
  margin-bottom: 2em;
  width: 100%;
  padding: 0 1em;
}

label[for="radio-select"] {
  font: bold 2rem/1 var(--font);
  margin-bottom: .3em;
  display: block;
}

#radio-select {
  font-size: 1.5rem;
  padding: .75em 1.2em;
  border: 1px solid #ccc;
  border-radius: var(--radius);
  background: var(--bg) url("data:image/svg+xml,%3Csvg fill='gray' viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E") right .8em center / 1em no-repeat;
  appearance: none;
  min-width: 200px;
  max-width: 90vw;
  text-align: center;
  text-align-last: center;
  outline: none;
  transition: border .3s, box-shadow .3s;
}

#radio-select:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(74,144,226,.2);
}

.custom-player {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1em;
  padding: 1em;
  border: 3px solid var(--border);
  border-radius: var(--radius);
  box-shadow: 0 0 10px rgba(0,0,0,.1);
  margin-top: 1em;
  background: #fff;
  width: 100%;
  max-width: 1000px;
  box-sizing: border-box;
}

#play-pause {
  width: 2.5em;
  height: 2.5em;
  border: 3px solid var(--border);
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  transition: .3s;
  display: grid;
  place-items: center;
}

#play-pause:disabled {
  opacity: .5;
  cursor: not-allowed;
}

#play-pause:hover:enabled {
  background: #f0f0f0;
}

#progress {
  flex: 1;
  height: 8px;
  border-radius: 5px;
  accent-color: var(--border);
  background: #eee;
  cursor: pointer;
}

@media(max-width:600px) {
  #radio-select {
    font-size: 1.8rem;
    padding: .7em;
  }

  label[for="radio-select"] {
    font-size: 1.5rem;
  }
}
</style>

<div class="radio-wrapper">
  <label for="radio-select">Scegli una radio</label>
  <select id="radio-select">
    <option value="" disabled selected>Scegli…</option>
    <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2obck/radiom2obck/play1.m3u8">M2O</option>
    <option value="https://22333.live.streamtheworld.com/TLPSTR16.mp3?dist=538_web">538 Party Zone</option>
    <option value="https://stream.technolovers.fm/gabber">Gabber</option>
    <option value="https://listen5.myradio24.com/eugenijus">Eugenijus Radio</option>
    <option value="https://a8.asurahosting.com:7890/radio.mp3">Frenchcore24FM</option>
    <option value="https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420">90s 90s Techno</option>
    <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejaybck/radiodeejaybck/play1.m3u8">Radio Deejay</option>
    <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songsbck/radiodeejay30songsbck/play1.m3u8">30 Songs - Deejay</option>
    <option value="https://vdnvsxa1-4c4b867c89244861ac216426883d1ad0.msvdn.net/webradio/deejaytime/live.m3u8">Deejay Time</option>
    <option value="https://stream.discoradio.radio/audio/disco.stream_aac64/chunklist.m3u8">Disco Radio</option>
    <option value="https://nr15.newradio.it:9100/stream">R.I.N.</option>
    <option value="https://regiocast.streamabc.net/regc-80s80smweb2517500-mp3-192-1672667">80s 80s</option>
    <option value="https://nr8.newradio.it:19574/stream">70/80 Hits</option>
    <option value="https://smoothjazz.cdnstream1.com/2585_128.mp3">Smooth Jazz</option>
    <option value="https://ilsole24ore-radio.akamaized.net/hls/live/2035301/radio24/playlist-48000.m3u8">Il Sole 24 ore</option>
  </select>

  <div class="custom-player">
    <button id="play-pause" aria-label="Play / Pause" disabled>
      <svg class="icon play" viewBox="0 0 24 24" fill="currentColor"><polygon points="5,3 19,12 5,21"/></svg>
    </button>
    <input type="range" id="progress" min="0" max="100" value="0" aria-label="Progress bar">
  </div>

  <audio id="audio-player" preload="auto"></audio>
</div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
(() => {
  const player       = document.getElementById('audio-player');
  const selector     = document.getElementById('radio-select');
  const playBtn      = document.getElementById('play-pause');
  const progress     = document.getElementById('progress');
  const playIcon     = playBtn.querySelector('.icon');

  let hls = null;
  let isPlaying = false;

  const toggleBtn = () => {
    isPlaying = !player.paused;
    playBtn.classList.toggle('playing', isPlaying);
    playIcon.setAttribute('viewBox', isPlaying ? '0 0 24 24' : '0 0 24 24');
    playIcon.innerHTML = isPlaying
      ? '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>'
      : '<polygon points="5,3 19,12 5,21"/>';
  };

  const loadStream = url => {
    if (hls) { hls.destroy(); hls = null; }

    const play = () => player.play().then(() => { playBtn.disabled = false; toggleBtn(); });

    if (/\.m3u8$/i.test(url)) {
      if (Hls.isSupported()) {
        hls = new Hls({ enableWorker:true, liveSyncDuration:20, maxBufferLength:60 });
        hls.loadSource(url);
        hls.attachMedia(player);
        hls.once(Hls.Events.MANIFEST_PARSED, play);
        hls.on(Hls.Events.ERROR, (_, { fatal, type }) => {
          if (!fatal) return;
          type === Hls.ErrorTypes.NETWORK_ERROR ? hls.startLoad()
            : type === Hls.ErrorTypes.MEDIA_ERROR ? hls.recoverMediaError()
            : hls.destroy();
        });
      } else if (player.canPlayType('application/vnd.apple.mpegurl')) {
        player.src = url;
        player.addEventListener('loadedmetadata', play, { once:true });
      } else {
        alert('HLS non supportato dal browser.');
      }
    } else {
      player.src = url;
      play();
    }
  };

  selector.addEventListener('change', () => loadStream(selector.value));
  playBtn.addEventListener('click', () => {
    player.paused ? player.play() : player.pause();
  });
  player.addEventListener('play', toggleBtn);
  player.addEventListener('pause', toggleBtn);

  player.addEventListener('timeupdate', () => {
    if (!isNaN(player.duration)) progress.value = (player.currentTime / player.duration) * 100;
  });
  progress.addEventListener('input', () => {
    if (!isNaN(player.duration)) player.currentTime = (progress.value / 100) * player.duration;
  });

  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && player.src && !isPlaying) player.play();
  });
})();
</script>
