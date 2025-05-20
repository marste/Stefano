---
layout: page
title: Password Generator
permalink: /password-generator/
image: 'https://marzorati.co/img/google.png'
---
<div id="password-generator" style="font-family: Arial, sans-serif; max-width: 1000px; margin: 4rem auto; padding: 4rem; background: #fff; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); text-align: center;">
  
  <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin: 1rem 0;">
    <div id="password" style="font-size: 2.6rem; word-break: break-all; background: #f0f0f0; padding: 1rem 2rem; border-radius: 10px; min-width: 5000px;"></div>
    <button onclick="copyPassword()" style="padding: 1rem 2rem; font-size: 2rem; border: none; border-radius: 10px; background-color: #007bff; color: white; cursor: pointer;">Copia</button>
  </div>
  <button onclick="generatePassword()" style="padding: 1.2rem 2.4rem; font-size: 2rem; border: none; border-radius: 10px; background-color: #007bff; color: white; cursor: pointer;">Genera Nuova Password</button>
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