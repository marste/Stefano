---
layout: page
title: Web Radio
permalink: /web-radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
---
<center>

<label for="radio-select">Scegli una radio:</label>
<select id="radio-select">
  <option value="https://streamcdnr14-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">m2o</option>
  <option value="https://22663.live.streamtheworld.com/TLPSTR13.mp3?dist=538_web">538 TOP 50</option>
  <option value="http://213.141.131.10:8002/gabber">Gabber</option>
  <option value="https://stream.technolovers.fm/gabber">Gabber2</option>
  <option value="https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420">90s 90s Techno</option>
  <option value="http://technoszene.stream.laut.fm/technoszene">Technoszene</option>
  <option value="https://streamcdnm1-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay/radiodeejay/play1.m3u8">Radio DEEJAY</option>
  <option value="https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songs/radiodeejay30songs/play1.m3u8">30 Songs</option>
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