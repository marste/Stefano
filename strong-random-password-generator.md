---
layout: page
title: "Strong & Random Password Generator"
permalink: /strong-random-password-generator/
date: 2025-06-03 10:00:00 +0200
description: "Genera password complesse e sicure in un click. Nessun dato inviato al server: tutto avviene localmente nel tuo browser."
image: "https://marzorati.co/img/password.png"
share-img: "https://marzorati.co/img/password.png"
tags: [password, generator, strong, random]
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">

<style>
  /* Reset spinners */
  input[type=number]::-webkit-inner-spin-button,
  input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  input[type=number] { -moz-appearance: textfield; }

  .generator-wrapper {
    font-family: 'Open Sans', sans-serif;
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,.1);
    text-align: center;
  }

  .length-slider {
    width: 100%;
    max-width: 220px;
  }

  .checkboxes {
    margin: 1rem 0;
    font-size: 1.2rem;
    text-align: left;
    display: inline-block;
  }

  .checkboxes label { display: block; margin: .4rem 0; }

  #password-output {
    font-size: 1.8rem;
    font-weight: 600;
    word-break: break-all;
    background: #f0f0f0;
    padding: .6rem 1rem;
    border-radius: 5px;
    min-width: 300px;
  }

  .btn {
    padding: .6rem 1.2rem;
    font-size: 1.5rem;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
  }

  .copy-feedback {
    font-size: 1rem;
    color: #28a745;
    margin-top: 1rem;
    display: none;
  }
</style>

<main class="generator-wrapper">
  

  <label for="lengthRange">
    Lunghezza: <strong id="lengthValue">16</strong>
  </label>
  <br>
  <input type="range" id="lengthRange" min="4" max="128" value="16" class="length-slider">

  <fieldset class="checkboxes">
    <legend>Opzioni caratteri</legend>
    <label><input type="checkbox" id="uppercase" checked> Lettere maiuscole</label>
    <label><input type="checkbox" id="lowercase" checked> Lettere minuscole</label>
    <label><input type="checkbox" id="numbers" checked> Numeri</label>
    <label><input type="checkbox" id="symbols" checked> Simboli</label>
    <label><input type="checkbox" id="excludeAmbiguous"> Escludi caratteri ambigui</label>
  </fieldset>

  <div style="display:flex;justify-content:center;align-items:center;gap:.5rem;margin:1.5rem 0;">
    <output id="password-output" aria-live="polite" aria-atomic="true"></output>
    <button id="copyBtn" class="btn" aria-label="Copia negli appunti" style="background:#6c757d;">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
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
    const length = +lengthRange.value;
    const chars = getCharset();
    if (!chars) {
      outputEl.textContent = 'Seleziona almeno un tipo di carattere.';
      outputEl.style.color = 'red';
      return;
    }
    let pwd = '';
    const random = new Uint32Array(length);
    crypto.getRandomValues(random);
    for (let i = 0; i < length; i++) pwd += chars[random[i] % chars.length];
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

  // Init
  lengthRange.addEventListener('input', () => {
    lengthValue.textContent = lengthRange.value;
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