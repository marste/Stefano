---
layout: page
title: Streaming Radio
permalink: /radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
---

<center>
  <label for="radio-select">Scegli una radio:</label>
  <select id="radio-select">
    <option value="https://streamcdnr14-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">Radio m2o</option>
    <option value="https://22663.live.streamtheworld.com/TLPSTR13.mp3?dist=538_web">538 TOP 50</option>
    <option value="https://stream.technolovers.fm/gabber">Gabber</option>
    <option value="https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420">90s 90s Techno</option>
    <option value="http://technoszene.stream.laut.fm/technoszene">Technoszene</option>
    <option value="https://streamcdnm1-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay/radiodeejay/play1.m3u8">Radio DEEJAY</option>
    <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songs/radiodeejay30songs/play1.m3u8">30 Songs</option>
    <option value="https://smoothjazz.cdnstream1.com/2585_128.mp3">Smooth Jazz</option>
    <option value="https://nr8.newradio.it:19574/stream">70/80 Hits</option>
  </select>

  <br><br>

  <audio id="audio-player" controls style="width: 100%; max-width: 600px;"></audio>

  <div id="now-playing" style="margin-top: 1em; font-weight: bold;">
    🎵 In attesa di metadati...
  </div>

  <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
  <script>
    const player = document.getElementById('audio-player');
    const selector = document.getElementById('radio-select');
    const nowPlaying = document.getElementById('now-playing');
    let hlsInstance = null;
    let metadataInterval = null;

    function playStream(url) {
      // Ferma eventuali fetch di metadati precedenti
      if (metadataInterval) clearInterval(metadataInterval);

      // Stop e reset HLS
      if (hlsInstance) {
        hlsInstance.destroy();
        hlsInstance = null;
      }

      nowPlaying.textContent = '🎵 Caricamento stream...';

      // HLS
      if (url.includes('.m3u8')) {
        if (Hls.isSupported()) {
          hlsInstance = new Hls();
          hlsInstance.loadSource(url);
          hlsInstance.attachMedia(player);
          hlsInstance.on(Hls.Events.MANIFEST_PARSED, () => {
            player.play();
            nowPlaying.textContent = '🎵 Streaming avviato';
          });
        } else if (player.canPlayType('application/vnd.apple.mpegurl')) {
          player.src = url;
          player.addEventListener('loadedmetadata', () => {
            player.play();
            nowPlaying.textContent = '🎵 Streaming avviato';
          });
        } else {
          alert('Il tuo browser non supporta lo streaming HLS.');
        }
      } else {
        // Stream MP3
        player.src = url;
        player.play();
        nowPlaying.textContent = '🎵 Connessione al flusso...';

        // Se è un MP3 compatibile, tenta di leggere i metadati ogni 30 secondi
        metadataInterval = setInterval(() => fetchMetadata(url), 30000);
        fetchMetadata(url); // subito
      }
    }

    async function fetchMetadata(streamUrl) {
      const proxy = 'https://corsproxy.io/?'; // Gratis e utile per demo
      const proxiedUrl = proxy + encodeURIComponent(streamUrl);

      try {
        const response = await fetch(proxiedUrl, {
          method: 'GET',
          headers: { 'Icy-MetaData': '1' }
        });

        const reader = response.body.getReader();
        const { value } = await reader.read();
        const str = new TextDecoder('utf-8').decode(value);
        const match = str.match(/StreamTitle='([^']+)'/);

        if (match && match[1]) {
          nowPlaying.textContent = '🎵 ' + match[1];
        } else {
          nowPlaying.textContent = '🎵 Nessuna informazione disponibile';
        }
      } catch (err) {
        nowPlaying.textContent = '🎵 Info non disponibili';
        console.warn('Errore metadati:', err);
      }
    }

    selector.addEventListener('change', () => playStream(selector.value));
    playStream(selector.value); // al primo caricamento
  </script>
</center>
