---
layout: page
title: Password Generator
permalink: /password-generator/
image: 'https://marzorati.co/img/google.png'
---

<div id="password-generator" style="font-family: Arial, sans-serif; max-width: 600px; margin: 2rem auto; padding: 2rem; background: #fff; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center;">

 

  <div style="margin-bottom: 1rem; font-size: 1.5rem;">
    <label>
      Lunghezza:
      <input type="number" id="length" value="16" min="4" max="128" style="width: 60px; padding: 0.3rem; margin-left: 0.5rem; font-size: 1.5rem;">
    </label>
  </div>

  <div style="margin-bottom: 1rem; font-size: 1.5rem; text-align: left; display: inline-block;">
    <label><input type="checkbox" id="uppercase" checked> Lettere Maiuscole</label><br>
    <label><input type="checkbox" id="lowercase" checked> Lettere Minuscole</label><br>
    <label><input type="checkbox" id="numbers" checked> Numeri</label><br>
    <label><input type="checkbox" id="symbols" checked> Simboli</label>
  </div>

  <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin: 1.5rem 0;">
    <div id="password" style="font-size: 1.8rem; font-weight: bold; word-break: break-all; background: #f0f0f0; padding: 0.6rem 1rem; border-radius: 5px; min-width: 300px;"></div>
    <button onclick="copyPassword()" style="padding: 0.5rem 1rem; font-size: 1.5rem; border: none; border-radius: 5px; background-color: #007bff; color: white; cursor: pointer;">Copia</button>
  </div>

  <button onclick="generatePassword()" style="padding: 0.6rem 1.2rem; font-size: 1.5rem; border: none; border-radius: 5px; background-color: #007bff; color: white; cursor: pointer;">Genera Password</button>

</div>

<script>
  function generatePassword() {
    const length = parseInt(document.getElementById('length').value);
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
    if (!passwordText || passwordText.includes("Seleziona")) return;
    navigator.clipboard.writeText(passwordText).then(() => {
      alert("Password copiata negli appunti!");
    }).catch(err => {
      alert("Errore nella copia: " + err);
    });
  }

  window.onload = generatePassword;
</script>