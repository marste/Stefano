---
layout: page
title: Password Generator
permalink: /password-generator/
image: 'https://marzorati.co/img/google.png'
---
<body>
  <div class="container">
    <h2>Password Generata</h2>
    <div id="password"></div>
    <button onclick="generatePassword()">Genera Nuova Password</button>
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

    // Genera una password automaticamente al caricamento
    window.onload = generatePassword;
  </script>
</body>

