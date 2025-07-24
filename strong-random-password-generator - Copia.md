---
layout: page
title: "Strong & Random Passwords Generator"
permalink: /strong-random-password-generator/
date: 2025-06-03 10:00:00 +0200
description: "Generare una password complessa e sicura. Stai al sicuro online creando una password forte e sicura con il nostro strumento di generazione. Una password complessa è il primo passo per rafforzare la sicurezza dei vostri dati prevenendo le violazioni."
image: 'https://marzorati.co/img/password.png'
share-img: 'https://marzorati.co/img/password.png'
tags: [password, generator, strong, random]
published: false
---

<style>
  input[type=number]::-webkit-inner-spin-button,
  input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  input[type=number] {
    -moz-appearance: textfield;
  }

  .length-input {
    width: 50px;
    padding: 0.4rem 0.6rem;
    font-size: 1.5rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    text-align: center;
    transition: border-color 0.3s ease;
  }

  .length-input:focus {
    outline: none;
    border-color: #007bff;
  }

  .copy-feedback {
    font-size: 1rem;
    color: green;
    margin-top: 1rem;
    display: none;
  }
</style>

<div id="password-generator" style="font-family: Open Sans, sans-serif; max-width: 600px; margin: 2rem auto; padding: 2rem; background: #fff; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center;">

  <div style="margin-bottom: 1rem; font-size: 1.5rem;">
    <label style="font-weight: normal;">
      Lunghezza:
      <input
        type="number"
        id="length"
        value="16"
        min="1"
        max="999"
        class="length-input"
        oninput="enforceMaxLength(this)"
      >
    </label>
  </div>

  <div style="margin-bottom: 1rem; font-size: 1.5rem; text-align: left; display: inline-block;">
    <label style="font-weight: normal;"><input type="checkbox" id="uppercase" checked> Lettere Maiuscole</label><br>
    <label style="font-weight: normal;"><input type="checkbox" id="lowercase" checked> Lettere Minuscole</label><br>
    <label style="font-weight: normal;"><input type="checkbox" id="numbers" checked> Numeri</label><br>
    <label style="font-weight: normal;"><input type="checkbox" id="symbols" checked> Simboli</label>
  </div>

  <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin: 1.5rem 0;">
    <div id="password" style="font-size: 1.8rem; font-weight: bold; word-break: break-all; background: #f0f0f0; padding: 0.6rem 1rem; border-radius: 5px; min-width: 300px;"></div>
    <button onclick="copyPassword()" style="background: none; border: none; cursor: pointer; padding: 0;">
      <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="#007bff" viewBox="0 0 28 28">
        <path d="M16 1H4a2 2 0 0 0-2 2v14h2V3h12V1zm3 4H8a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm0 18H8V7h11v16z"/>
      </svg>
    </button>
  </div>

  <button onclick="generatePassword()" style="padding: 0.6rem 1.2rem; font-size: 1.5rem; border: none; border-radius: 5px; background-color: #007bff; color: white; cursor: pointer;">Genera Password</button>

  <div id="copy-feedback" class="copy-feedback">✅ Password copiata!</div>

</div>

<script>
  function enforceMaxLength(el) {
    if (el.value.length > 3) {
      el.value = el.value.slice(0, 3);
    }
  }

  function generatePassword() {
    let length = parseInt(document.getElementById('length').value);
    if (isNaN(length) || length < 1) length = 1;
    if (length > 999) length = 999;

    const useUpper = document.getElementById('uppercase').checked;
    const useLower = document.getElementById('lowercase').checked;
    const useNumbers = document.getElementById('numbers').checked;
    const useSymbols = document.getElementById('symbols').checked;

    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lower = "abcdefghijklmnopqrstuvwxyz";
    const numbers = "0123456789";
    const symbols = "!@#$%^&*()-_=+[]{};:,.<>?";

    let charset = "";
    if (useUpper) charset += upper;
    if (useLower) charset += lower;
    if (useNumbers) charset += numbers;
    if (useSymbols) charset += symbols;

    const output = document.getElementById("password");
    const feedback = document.getElementById("copy-feedback");
    feedback.style.display = "none";

    if (charset.length === 0) {
      output.textContent = "Seleziona almeno un tipo di carattere!";
      output.style.fontWeight = "normal";
      output.style.color = "red";
      return;
    }

    let password = "";
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * charset.length);
      password += charset[randomIndex];
    }

    output.textContent = password;
    output.style.fontWeight = "bold";
    output.style.color = "black";
  }

  function copyPassword() {
    const passwordText = document.getElementById("password").textContent;
    const feedback = document.getElementById("copy-feedback");

    if (!passwordText || passwordText.includes("Seleziona")) return;

    navigator.clipboard.writeText(passwordText).then(() => {
      feedback.style.display = "block";
      setTimeout(() => {
        feedback.style.display = "none";
      }, 2000);
    }).catch(err => {
      console.error("Errore nella copia: ", err);
    });
  }

  window.onload = generatePassword;
</script>
