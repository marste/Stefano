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
    }

    .prezzo {
      float: right;
      font-weight: bold;
    }
  </style>

<body>

<h1>Ricerca prodotti</h1>

<input
  type="text"
  id="searchInput"
  placeholder="Cerca prodotto..."
>

<ul id="productList">
  <li data-nome="mela rubinia">
    Mela Rubinia <span class="prezzo">€ 2,99</span>
  </li>
  <li data-nome="banana">
    Banana <span class="prezzo">€ 1,79</span>
  </li>
  <li data-nome="arancia tarocco">
    Arancia Tarocco <span class="prezzo">€ 2,49</span>
  </li>
  <li data-nome="pera abate">
    Pera Abate <span class="prezzo">€ 3,10</span>
  </li>
</ul>

<script>
  const searchInput = document.getElementById('searchInput');
  const products = document.querySelectorAll('#productList li');

  searchInput.addEventListener('keyup', () => {
    const filter = searchInput.value.toLowerCase();

    products.forEach(product => {
      const nome = product.dataset.nome;
      product.style.display = nome.includes(filter) ? '' : 'none';
    });
  });
</script>

</body>

