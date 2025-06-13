---
title: Streaming Radio
permalink: /radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
date: 2025-06-04 07:00:00 +0200
author: Stefano Marzorati
layout: page
bigimg: ['https://marzorati.co/img/post/music_2.jpg', 'https://marzorati.co/img/post/music_3.jpg']
categories: [Music]
tags: [radio, web, streaming, mp3, m3u8, m2o, gabber, frenchcore, techno, jazz, pop]
---

<style>
  .radio-wrapper {
    text-align: center;
    margin-bottom: 2em;
    font-family: sans-serif;
  }

  .radio-container {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
  }

  #radio-select {
    padding: 0.75em 1.2em;
    font-size: 1.5rem;
    border: 1px solid #ccc;
    border-radius: 0.75em;
    background-color: #f9f9f9;
    color: #333;
    outline: none;
    appearance: none;
    background-image: url("data:image/svg+xml;utf8,<svg fill='gray' height='20' viewBox='0 0 24 24' width='20' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/></svg>");
    background-repeat: no-repeat;
    background-position: right 0.8em center;
    background-size: 1em;
    transition: border 0.3s ease, box-shadow 0.3s ease;
    max-width: 300px;
    width: 100%;
    margin-top: 0.5em;
  }

  #radio-select:hover {
    border-color: #aaa;
  }

  #radio-select:focus {
    border-color: #4A90E2;
    box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.2);
  }

  label[for="radio-select"] {
    font-weight: bold;
    font-size: 2rem;
    margin-bottom: 0.3em;
    color: black;
  }

  .custom-player {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1em;
    background: #fff;
    padding: 1em;
    border-radius: 1em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border: 3px solid #000;
    margin-top: 1em;
  }

  #play-pause {
    background: #fff;
    color: #000;
    border: 3px solid #000;
    border-radius: 50%;
    width: 2.5em;
    height: 2.5em;
    cursor: pointer;
    transition: background 0.3s, color 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
  }

  #play-pause svg {
    width: 1.2em;
    height: 1.2em;
  }

  #play-pause:hover:enabled {
    background: #f0f0f0;
  }

  #play-pause:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  #progress {
    flex: 1;
    accent-color: #000;
    background-color: #eee;
    height: 8px;
    border-radius: 5px;
    cursor: pointer;
  }

  @media (max-width: 600px) {
    #radio-select {
      font-size: 2rem;
      padding: 1em;
    }

    label[for="radio-select"] {
      font-size: 1.5rem;
    }
  }
</style>

<div class="radio-wrapper">
  <div class="radio-container">
    
    <select id="radio-select">
      <option value="" disabled selected>------ Scegli ------</option>
      <option value="https://streamcdnr14-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">M2O</option>
      <option value="https://22663.live.streamtheworld.com/TLPSTR13.mp3?dist=538_web">538 TOP 50</option>
      <option value="https://stream.technolovers.fm/gabber">Gabber</option>
	  <option value="https://a8.asurahosting.com:7890/radio.mp3">Frenchcore24FM</option>
      <option value="https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420">90s 90s Techno</option>
	  <option value="https://best-of-techno.stream.laut.fm/best-of-techno?t302=2025-06-12_12-30-01&uuid=72708501-f14f-4e32-9043-cf4dc4f4d99a">Best of Techno</option>
      <option value="https://streamcdnm1-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay/radiodeejay/play1.m3u8">Radio Deejay</option>
      <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songs/radiodeejay30songs/play1.m3u8">30 Songs - Deejay</option>
	  <option value="https://stream.discoradio.radio/audio/disco.stream_aac64/chunklist.m3u8">Disco Radio</option>
	  <option value="https://nr15.newradio.it:9100/stream">R.I.N.</option>
      <option value="https://nr8.newradio.it:19574/stream">70/80 Hits</option>
	  <option value="https://smoothjazz.cdnstream1.com/2585_128.mp3">Smooth Jazz</option>
	  <option value="https://ilsole24ore-radio.akamaized.net/hls/live/2035301/radio24/playlist-48000.m3u8">Il Sole 24 ore</option>
    </select>
  </div>

  <div class="custom-player">
    <button id="play-pause" class="play" disabled>
      <svg id="play-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="5,3 19,12 5,21" />
      </svg>
    </button>
    <input type="range" id="progress" value="0" min="0" max="100" step="1">
  </div>

  <audio id="audio-player" preload="auto"></audio>
</div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
  const player = document.getElementById('audio-player');
  const selector = document.getElementById('radio-select');
  const playPauseBtn = document.getElementById('play-pause');
  let playIcon = document.getElementById('play-icon');
  const progress = document.getElementById('progress');

  let hlsInstance = null;
  let isPlaying = false;

  function setPlayIcon() {
    playPauseBtn.innerHTML = `
      <svg id="play-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="5,3 19,12 5,21" />
      </svg>
    `;
    playIcon = document.getElementById('play-icon');
  }

  function setPauseIcon() {
    playPauseBtn.innerHTML = `
      <svg id="play-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="6" y="4" width="4" height="16"></rect>
        <rect x="14" y="4" width="4" height="16"></rect>
      </svg>
    `;
    playIcon = document.getElementById('play-icon');
  }

  function playStream(url) {
    if (hlsInstance) {
      hlsInstance.destroy();
      hlsInstance = null;
    }

    if (url.includes('.m3u8')) {
      if (Hls.isSupported()) {
        hlsInstance = new Hls({
          maxBufferLength: 60,
          maxMaxBufferLength: 120,
          liveSyncDuration: 20,
          enableWorker: true,
        });

        hlsInstance.loadSource(url);
        hlsInstance.attachMedia(player);
        hlsInstance.on(Hls.Events.MANIFEST_PARSED, () => {
          player.play().then(() => {
            playPauseBtn.disabled = false;
            setPauseIcon();
            isPlaying = true;
          });
        });

        hlsInstance.on(Hls.Events.ERROR, function (event, data) {
          if (data.fatal) {
            switch (data.type) {
              case Hls.ErrorTypes.NETWORK_ERROR:
                hlsInstance.startLoad();
                break;
              case Hls.ErrorTypes.MEDIA_ERROR:
                hlsInstance.recoverMediaError();
                break;
              default:
                hlsInstance.destroy();
                player.src = '';
                break;
            }
          }
        });

      } else if (player.canPlayType('application/vnd.apple.mpegurl')) {
        player.src = url;
        player.addEventListener('loadedmetadata', () => {
          player.play().then(() => {
            playPauseBtn.disabled = false;
            setPauseIcon();
            isPlaying = true;
          });
        });
      } else {
        alert('Il tuo browser non supporta lo streaming HLS.');
      }
    } else {
      player.src = url;
      player.play().then(() => {
        playPauseBtn.disabled = false;
        setPauseIcon();
        isPlaying = true;
      });
    }
  }

  selector.addEventListener('change', () => {
    const url = selector.value;
    if (url) {
      playStream(url);
    }
  });

  playPauseBtn.addEventListener('click', () => {
    if (player.paused) {
      player.play().then(() => {
        setPauseIcon();
        isPlaying = true;
      });
    } else {
      player.pause();
      setPlayIcon();
      isPlaying = false;
    }
  });

  player.addEventListener('timeupdate', () => {
    if (!isNaN(player.duration)) {
      progress.value = (player.currentTime / player.duration) * 100;
    }
  });

  progress.addEventListener('input', () => {
    if (!isNaN(player.duration)) {
      player.currentTime = (progress.value / 100) * player.duration;
    }
  });

  document.addEventListener("visibilitychange", () => {
    if (!document.hidden && !isPlaying && player.src) {
      player.play().then(() => {
        setPauseIcon();
        isPlaying = true;
      });
    }
  });
</script>
