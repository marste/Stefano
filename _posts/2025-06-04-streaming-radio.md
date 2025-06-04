---
title: Streaming Radio
permalink: /radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
date: 2025-06-04 07:00:00 +0200
author: Stefano Marzorati
layout: post
bigimg: ['https://marzorati.co/img/post/music_2.jpg', 'https://marzorati.co/img/post/music_3.jpg']
categories: [Music]
tags: [radio, web, streaming, mp3, m3u8]
---

<style>
  .radio-wrapper {
    text-align: center;
    margin-bottom: 2em;
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
    max-width: 200px;
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
  }

  audio {
    display: block;
    margin: 1.5em auto 0;
    width: 100%;
    max-width: 600px;
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
    <label for="radio-select">🎧 Scegli una radio:</label>
    <select id="radio-select">
      <option value="https://streamcdnr14-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">Radio M2O</option>
      <option value="https://22663.live.streamtheworld.com/TLPSTR13.mp3?dist=538_web">538 TOP 50</option>
      <option value="https://stream.technolovers.fm/gabber">Gabber</option>
      <option value="https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420">90s 90s Techno</option>
      <option value="http://technoszene.stream.laut.fm/technoszene">Technoszene</option>
      <option value="https://streamcdnm1-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay/radiodeejay/play1.m3u8">Radio DEEJAY</option>
      <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songs/radiodeejay30songs/play1.m3u8">30 Songs</option>
      <option value="https://smoothjazz.cdnstream1.com/2585_128.mp3">Smooth Jazz</option>
      <option value="https://nr8.newradio.it:19574/stream">70/80 Hits</option>
    </select>
  </div>

  <audio id="audio-player" controls></audio>
</div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
  const player = document.getElementById('audio-player');
  const selector = document.getElementById('radio-select');

  let hlsInstance = null;

  function playStream(url) {
    if (hlsInstance) {
      hlsInstance.destroy();
      hlsInstance = null;
    }

    if (url.includes('.m3u8')) {
      if (Hls.isSupported()) {
        hlsInstance = new Hls();
        hlsInstance.loadSource(url);
        hlsInstance.attachMedia(player);
        hlsInstance.on(Hls.Events.MANIFEST_PARSED, () => player.play());
      } else if (player.canPlayType('application/vnd.apple.mpegurl')) {
        player.src = url;
        player.addEventListener('loadedmetadata', () => player.play());
      } else {
        alert('Il tuo browser non supporta lo streaming HLS.');
      }
    } else {
      player.src = url;
      player.play();
    }
  }

  selector.addEventListener('change', () => playStream(selector.value));
  playStream(selector.value);
</script>
