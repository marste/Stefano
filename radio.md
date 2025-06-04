---
layout: page
title: Web Radio
permalink: /web-radio/
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
---

<label for="radio-select">Scegli una radio:</label>
<select id="radio-select">
  <option value="https://streamcdnr14-4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8">m2o</option>
  <option value="https://22663.live.streamtheworld.com/TLPSTR13.mp3?dist=538_web&ttag=talpa_consent:1&gdpr=1&gdpr_consent=CQEDvvAQEDvvAAcABBNLBDFwAP_gAEPgAChQGgQGQAKgAXABAADIAIkATABOADEAG4APwAgABGADjAHeAQgAi0BHAEdAJKAS4AnYBWQDOAIpAXmAvYBoAGCQBQALgEIAI4AlUBggAoSASABUAEAAMgAiABMAD8AO8AkoC8x0AwACoAIAAZABEACYAGIAPwA7wCLAEdAJKAvMhACADEAO8lAFACIAEwAMQA7wF5lIBgAFQAQAAyACIAEwAMQAfgB3gEWAI6ASUBeY.f_wACHwAAAAA">538 Top 50</option>
  <!-- Aggiungi altre stazioni qui -->
</select>

<br><br>

<video id="audio-player" controls style="width: 100%; max-width: 400px;"></video>

<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
  const player = document.getElementById('audio-player');
  const selector = document.getElementById('radio-select');

  function playStream(url) {
    if (Hls.isSupported()) {
      const hls = new Hls();
      hls.loadSource(url);
      hls.attachMedia(player);
      hls.on(Hls.Events.MANIFEST_PARSED, function () {
        player.play();
      });
    } else if (player.canPlayType('application/vnd.apple.mpegurl')) {
      player.src = url;
      player.addEventListener('loadedmetadata', function () {
        player.play();
      });
    } else {
      alert('Il tuo browser non supporta lo streaming HLS.');
    }
  }

  selector.addEventListener('change', function () {
    playStream(this.value);
  });

  // Play default
  playStream(selector.value);
</script>
