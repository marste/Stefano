---
layout: page
title: Password Generator
permalink: /password-generator/
image: 'https://marzorati.co/img/google.png'
---
<div id="password-generator" style="font-family: Arial, sans-serif; max-width: 500px; margin: 2rem auto; padding: 2rem; background: #fff; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center;">
  <h2 style="margin-top: 0;">Password Generata</h2>
  <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin: 1rem 0;">
    <div id="password" style="font-size: 1.3rem; word-break: break-all; background: #f0f0f0; padding: 0.5rem 1rem; border-radius: 5px; min-width: 250px;"></div>
    <button onclick="copyPassword()" style="padding: 0.5rem 1rem; font-size: 1rem; border: none; border-radius: 5px; background-color: #007bff; color: white; cursor: pointer;">Copia</button>
  </div>
  <button onclick="generatePassword()" style="padding: 0.6rem 1.2rem; font-size: 1rem; border: none; border-radius: 5px; background-color: #007bff; color: white; cursor: pointer;">Genera Nuova Password</button>
</div>

<script>
  function generatePassword() {
    const length = 16;
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:,.<>?";
    let password = "";
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * charset.length);
      password += charset[randomIndex];
    }
    document.getElementById("password").textContent = password;
  }

  function copyPassword() {
    const passwordText = document.getElementById("password").textContent;
    if (!passwordText) return;
    navigator.clipboard.writeText(passwordText).then(() => {
      alert("Password copiata negli appunti!");
    }).catch(err => {
      alert("Errore nella copia: " + err);
    });
  }

  window.onload = generatePassword;
</script>