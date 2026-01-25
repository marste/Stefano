---
layout: page
title: "Ricerca Prezzi Prodotti"
permalink: /prezzi-prodotti/
date: 2025-06-03 10:00:00 +0200
description: "Genera password complesse e sicure in un click. Nessun dato inviato al server."
image: "https://marzorati.co/img/password.png"
share-img: "https://marzorati.co/img/password.png"
tags: [password, generator, strong, random]
---


  <style>
    body {
      font-family: Arial, sans-serif;
    }

    textarea {
      width: 100%;
      height: 160px;
      padding: 10px;
      font-size: 15px;
      margin-bottom: 15px;
    }

    input {
      width: 100%;
      padding: 12px;
      font-size: 16px;
      margin-bottom: 15px;
    }

    ul {
      list-style: none;
      padding: 0;
    }

    li {
      padding: 10px;
      border-bottom: 1px solid #ddd;
      display: flex;
      justify-content: space-between;
    }

    .prezzo {
      font-weight: bold;
      white-space: nowrap;
    }
  </style>
  
<body>

<h1>Ricerca prodotti</h1>

<p><strong>Lista prodotti</strong> (una riga per prodotto)</p>

<textarea id="productSource">
Pere Abate;2,59 €/Kg
Banane;1,79 €/Kg
Mele Rubinia;2,99 €/Kg
Arance Tarocco;2,49 €/Kg
</textarea>

<input
  type="text"
  id="searchInput"
  placeholder="Cerca prodotto..."
>

<ul id="productList"></ul>

<script>
  const textarea = document.getElementById('productSource');
  const list = document.getElementById('productList');
  const searchInput = document.getElementById('searchInput');

  function renderList() {
    list.innerHTML = '';

    const lines = textarea.value.split('\n');

    lines.forEach(line => {
      if (!line.includes(';')) return;

      const [nome, prezzo] = line.split(';');

      const li = document.createElement('li');
      li.dataset.nome = nome.toLowerCase();
      li.innerHTML = `
        <span>${nome.trim()}</span>
        <span class="prezzo">${prezzo.trim()}</span>
      `;

      list.appendChild(li);
    });
  }

  textarea.addEventListener('input', renderList);

  searchInput.addEventListener('keyup', () => {
    const filter = searchInput.value.toLowerCase();
    document.querySelectorAll('#productList li').forEach(li => {
      li.style.display = li.dataset.nome.includes(filter) ? '' : 'none';
    });
  });

  // inizializzazione
  renderList();
</script>

</body>
</html>
