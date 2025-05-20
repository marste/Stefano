---
layout: page
title: Password Generator
permalink: /password-generator/
image: 'https://marzorati.co/img/google.png'
---
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    .container {
      background: #fff;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      text-align: center;
    }
    #password {
      font-size: 1.5rem;
      margin: 1rem 0;
      word-break: break-all;
    }
    button {
      padding: 0.7rem 1.2rem;
      font-size: 1rem;
      border: none;
      border-radius: 5px;
      background-color: #007bff;
      color: white;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>

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

