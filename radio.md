---
layout: page
title: Web Radio
permalink: /web-radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
---
<center>
---
layout: default
title: Radio Streaming
---

<h1>Radio Streaming</h1>

<label for="radio-select">Scegli una radio:</label>
<select id="radio-select">
  <option value="https://streamcdnr14-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">Radio m2o</option>
  <option value="https://22663.live.streamtheworld.com/TLPSTR13.mp3?dist=538_web">Radio Test MP3 (StreamTheWorld)</option>
  <!-- Altre radio .mp3 o .m3u8 -->
</select>

<br><br>

<audio id="audio-player" controls style="width: 100%; max-width: 400px;"></audio>

<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
  const player = document.getElementById('audio-player');
  const selector = document.getElementById('radio-select');

  let hlsInstance = null;

  function playStream(url) {
    // Stop and detach any existing HLS stream
    if (hlsInstance) {
      hlsInstance.destroy();
      hlsInstance = null;
    }

    // Se è un flusso HLS (.m3u8)
    if (url.includes('.m3u8')) {
      if (Hls.isSupported()) {
        hlsInstance = new Hls();
        hlsInstance.loadSource(url);
        hlsInstance.attachMedia(player);
        hlsInstance.on(Hls.Events.MANIFEST_PARSED, function () {
          player.play();
        });
      } else if (player.canPlayType('application/vnd.apple.mpegurl')) {
        player.src = url;
        player.addEventListener('loadedmetadata', () => player.play());
      } else {
        alert('Il tuo browser non supporta lo streaming HLS.');
      }
    } else {
      // MP3 stream (o altro supportato nativamente)
      player.src = url;
      player.play();
    }
  }

  selector.addEventListener('change', () => playStream(selector.value));

  // Play default
  playStream(selector.value);
</script>

</center>