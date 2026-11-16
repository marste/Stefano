---
layout: page
title: "Strong & Random Password Generator"
permalink: /strong-random-password-generator/
date: 2025-06-03 10:00:00 +0200
description: "Genera password complesse e sicure in un click. Nessun dato inviato al server."
image: "https://marzorati.co/img/password.png"
share-img: "https://marzorati.co/img/password.png"
tags: [password, generator, strong, random]
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">

<style>
  /* --- RESET & UTILITIES --- */
  input[type=number]::-webkit-inner-spin-button,
  input[type=number]::-webkit-outer-spin-button {-webkit-appearance:none;margin:0;}
  input[type=number]{-moz-appearance:textfield;}

  /* --- GENERATOR STYLES --- */
  .generator-wrapper{
    font-family:'Open Sans',sans-serif;
    max-width:600px;margin:2rem auto;padding:2rem;background:#fff;
    border-radius:10px;box-shadow:0 4px 10px rgba(0,0,0,.1);text-align:center;
  }

  .length-slider-wrapper{display:flex;flex-direction:column;align-items:center;margin-bottom:1.5rem;}
  .length-slider-wrapper label{margin-bottom:.5rem;font-size:1.7rem;}
  .length-slider{width:220px;max-width:100%;}

  /* Lista opzioni senza bordo e senza legend */
  .checkboxes{
    margin:1rem auto;
    text-align:left;
    max-width:260px;
  }
  .checkboxes label{display:block;margin:.35rem 0;font-size:1.7rem;}

  #password-output{
    font-size:1.8rem;font-weight:600;word-break:break-all;
    background:#f0f0f0;padding:.6rem 1rem;border-radius:5px;min-width:300px;
  }

  /* Pulsante Copia moderno */
  .copy-btn{
    display:inline-flex;align-items:center;gap:.4rem;
    padding:.55rem .9rem;
    font-size:1rem;
    border:none;
    border-radius:6px;
    background:#007bff;
    color:#fff;
    cursor:pointer;
    transition:background .25s,transform .1s;
    box-shadow:0 2px 4px rgba(0,0,0,.15);
  }
  .copy-btn:hover{background:#0069d9;}
  .copy-btn:focus-visible{outline:2px solid #0053b3;outline-offset:2px;}
  .copy-btn:active{transform:scale(.96);}
  /* Effetto ripple */
  .copy-btn{position:relative;overflow:hidden;}
  .copy-btn::after{
    content:'';
    position:absolute;
    border-radius:50%;
    transform:scale(0);
    background:rgba(255,255,255,.4);
    transition:transform .4s,opacity .4s;
    opacity:1;
  }
  .copy-btn:active::after{transform:scale(4);opacity:0;}

  .btn{padding:.6rem 1.2rem;font-size:1.5rem;border:none;border-radius:5px;background:#007bff;color:#fff;cursor:pointer;}
  .copy-feedback{font-size:1rem;color:#28a745;margin-top:1rem;display:none;}
</style>

<main class="generator-wrapper">
 

  <div class="length-slider-wrapper">
    <label for="lengthRange">Lunghezza: <strong id="lengthValue">16</strong></label>
    <input type="range" id="lengthRange" min="4" max="64" value="16" class="length-slider">
  </div>

  <div class="checkboxes">
    <label><input type="checkbox" id="passphrase"> Passphrase in italiano</label>
  </div>
  <p id="passphrase-help" hidden>Parole italiane separate da “-” e un numero di quattro cifre alla fine.
    La lunghezza selezionata è il limite massimo: le parole restano intere.</p>

  <!-- Opzioni senza fieldset/legend né bordo -->
  <div class="checkboxes" id="character-options">
    <label><input type="checkbox" id="uppercase" checked> Lettere maiuscole</label>
    <label><input type="checkbox" id="lowercase" checked> Lettere minuscole</label>
    <label><input type="checkbox" id="numbers" checked> Numeri</label>
    <label><input type="checkbox" id="symbols" checked> Simboli</label>
    <label><input type="checkbox" id="excludeAmbiguous"> Escludi caratteri ambigui</label>
  </div>

  <div style="display:flex;justify-content:center;align-items:center;gap:.5rem;margin:1.5rem 0;">
    <output id="password-output" aria-live="polite" aria-atomic="true"></output>
    <button id="copyBtn" class="copy-btn" aria-label="Copia negli appunti">
      <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24">
        <path d="M16 1H4a2 2 0 0 0-2 2v14h2V3h12V1zm3 4H8a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm0 18H8V7h11v16z"/>
      </svg>
     
    </button>
  </div>

  <button id="generateBtn" class="btn">Genera password</button>
  <p id="copy-feedback" class="copy-feedback" aria-live="assertive">Password copiata negli appunti!</p>
</main>

<script>
(() => {
  const $ = sel => document.querySelector(sel);
  const lengthRange = $('#lengthRange');
  const lengthValue = $('#lengthValue');
  const outputEl = $('#password-output');
  const feedbackEl = $('#copy-feedback');

  const charset = {
    uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    lowercase: 'abcdefghijklmnopqrstuvwxyz',
    numbers: '0123456789',
    symbols: '!@#$%^&*()-_=+[]{};:,.<>?'
  };
  const ambiguous = /[0O1lI]/g;
  const passphraseEl = $('#passphrase');
  const lengthLabel = document.querySelector('label[for="lengthRange"]');
  let passwordLength = lengthRange.value;

  // Dizionario locale: nessuna richiesta di rete per generare le passphrase.
  const italianWords = (`
    abete aceto acqua agave alato albero album alce alga alibi amaca amico
    amore anatra ancora anello angolo anima ape arco arena argine aroma arpa
    asino astro atomo attimo aula aurora auto avorio azione azzurro bacio
    baffo bagno baita balena ballo banana barca barile base basilico bastone
    becco benda benzina betulla bianco bibita bimbo birillo biscotto bosco
    borsa botte braccio branco brezza brina brodo bruco buccia budino bufalo
    buio burro busta cabina cacao cactus caduta caffe calcio calice calore
    cambio camicia camino campo canale canapa canestro cane canoa canto
    capanna capello capra carota carro carta casa cascata casco castoro
    catena cavallo cedro celeste cena cenere centro cera cerchio cervo cesta
    cetra chiave chiodo cima cigno ciliegia cinema cintura ciotola cipolla
    citta ciuffo cocco codice collina colore colomba cometa conchiglia coniglio
    coperta corallo corda cornice corno corona corsa corte costa cotone cresta
    crine cristallo cubo cucina culla cuore cupola curva cuscino dado daino
    danza dattero decoro delfino dente deserto diario difesa diga dipinto dito
    divano dolce dono dorato dorso drago duomo ebano eco edera elica elmo
    emblema energia erba erede erica esame estate estro ettaro evento falco
    falena farina faro fata favola febbre felce felino ferro festa fetta fiamma
    fiato fico fieno fiera figlio fila filo filtro fiocco fiore firma fiume
    flauto foglia folaga fondo fonte forma forno forte fossa foto fragola
    frana freccia freddo fresco fronda fronte frutto fuga fulmine fumo fungo
    fuoco furgone gabbia gallo gamba gara garofano garza gatto gazza gelato
    gemma genio gesto getto ghianda ghiro ghisa gioco giostra giglio giraffa
    giubba globo gnomo goccia golfo gomma gonna grano grappolo grillo grotta
    gufo guscio hotel idea idolo igloo indice indaco insetto invito iris isola
    lago lampada lampo lana lancia lanterna lapis larice lastra latte lava
    lavoro leccio legno lente lenza leone lepre lettera leva liana libro
    lieve lima limone lino lista liuto lode loto luce lucido luglio lumaca
    lume luna lupo macchia madia maglia mago malva manico mano mappa mare
    marmo marrone marzo matita mattino medusa mela melone menta merlo mese
    metro miele miglio mimosa miniera mirtillo modello molo moneta mondo monte
    mora morso mosaico mostra motto mulino muro muschio museo musica naso
    nastro nave nebbia nettare neve nicchia nido noce nodo nome nonno nota
    notte nuca numero nuvola oblio occhio ocra odore olio oliva olmo ombra
    onda onice opera orata orbita orca ordine organo orma oro ortica orto
    orzo otre ovale pacco paese pagina palazzo palco palma palla palo panda
    pane panno papavero papera parco parete parola passo pasta patata pausa
    pavone pazienza pecora pedale pegno pelle penna pepe pera perla pesce
    peso petalo pettine pezzo piano pianta piatto pigna pila pilota pineta
    pino pinza pioggia piuma pizza poeta polenta polipo polline polpo pomo
    ponte popolo porta posto prato premio presa prova prugna punto quadro
    quaglia quarzo quercia quota radio radice ramo rana rapa razzo regalo
    remo renna resina rete ricamo riccio ricetta riga rima riparo riso rito
    riva roccia rondine rosa rosso rotta rovere rubino ruota rupe ruspa
    sabbia sacco saggio sale salice salmone salto saluto sandalo sasso scala
    scalo scarpa scatola scena scia scimmia scoglio scopa scorza scudo sedia
    sedano segno sella selva seme sentiero seppia sera seta siepe sigillo
    silenzio sirena slitta smeraldo sorriso sogno soglia sole sonno sonda
    sorso spada spago spalla spazio specchio spiga spillo spina spugna stadio
    stella stelo storia strada stufa succo sughero suolo suono tacco taglio
    talpa tamburo tana tappeto targa tasso tazza tela tempo tenda terra testa
    tetto tiglio tigre timone tino tipo titolo tonno topo torre torta trave
    treno trifoglio triglia tronco tufo tulipano tuono turno ulivo umore unione
    uovo uva vacca vagone valle vapore vaso vela vello vento verde vernice
    vetro viale viaggio vicolo villa viola viso vista vite voce volpe volta
    voto zaino zampa zanna zebra zefiro zolla zona zucca zucchero
  `).trim().split(/\s+/).filter(word => word.length >= 4 && word.length <= 8);

  // Rejection sampling per evitare distorsioni nella selezione casuale.
  function randomIndex(size) {
    const limit = Math.floor(0x100000000 / size) * size;
    const random = new Uint32Array(1);
    do { crypto.getRandomValues(random); } while (random[0] >= limit);
    return random[0] % size;
  }

  function generatePassphrase(maxLength) {
    const wordCount = Math.max(2, Math.floor((maxLength - 4) / 9));
    const words = [];
    // Riserva quattro cifre e un trattino per ogni parola.
    let remaining = maxLength - 4 - wordCount;
    for (let i = 0; i < wordCount; i++) {
      const maxWordLength = remaining - (wordCount - i - 1) * 4;
      const candidates = italianWords.filter(word => word.length <= maxWordLength);
      const word = candidates[randomIndex(candidates.length)];
      words.push(word);
      remaining -= word.length;
    }
    return words.join('-') + '-' + (1000 + randomIndex(9000));
  }

  function getCharset() {
    let chars = '';
    if ($('#uppercase').checked) chars += charset.uppercase;
    if ($('#lowercase').checked) chars += charset.lowercase;
    if ($('#numbers').checked) chars += charset.numbers;
    if ($('#symbols').checked) chars += charset.symbols;
    if ($('#excludeAmbiguous').checked) chars = chars.replace(ambiguous, '');
    return chars;
  }

  function generatePassword() {
    feedbackEl.style.display = 'none';
    const length = Math.min(64, Math.max(+lengthRange.min, +lengthRange.value));
    if (passphraseEl.checked) {
      outputEl.textContent = generatePassphrase(length);
      outputEl.style.color = 'black';
      return;
    }
    const chars = getCharset();
    if (!chars) {
      outputEl.textContent = 'Seleziona almeno un tipo di carattere.';
      outputEl.style.color = 'red';
      return;
    }
    let pwd = '';
    for (let i = 0; i < length; i++) pwd += chars[randomIndex(chars.length)];
    outputEl.textContent = pwd;
    outputEl.style.color = 'black';
  }

  async function copyPassword() {
    const txt = outputEl.textContent;
    if (!txt || txt.includes('Seleziona')) return;
    try {
      await navigator.clipboard.writeText(txt);
      feedbackEl.style.display = 'block';
      setTimeout(() => feedbackEl.style.display = 'none', 2000);
    } catch (err) {
      console.error(err);
    }
  }

  lengthRange.addEventListener('input', () => {
    lengthValue.textContent = lengthRange.value;
    generatePassword();
  });
  passphraseEl.addEventListener('change', () => {
    const enabled = passphraseEl.checked;
    if (enabled) passwordLength = lengthRange.value;
    lengthRange.min = enabled ? '16' : '4';
    lengthRange.value = enabled ? '48' : passwordLength;
    lengthLabel.firstChild.textContent = enabled ? 'Lunghezza massima: ' : 'Lunghezza: ';
    lengthValue.textContent = lengthRange.value;
    $('#passphrase-help').hidden = !enabled;
    $('#character-options').hidden = enabled;
    document.querySelectorAll('#character-options input').forEach(input => {
      input.disabled = enabled;
    });
    generatePassword();
  });
  $('#generateBtn').addEventListener('click', generatePassword);
  $('#copyBtn').addEventListener('click', copyPassword);
  document.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'g') {
      e.preventDefault();
      generatePassword();
    }
  });

  generatePassword();
})();
</script>