---
layout: page
title: "Ricerca Prezzi Prodotti"
permalink: /prezzi-prodotti/
date: 2025-06-03 10:00:00 +0200
description: "Ricerca rapida dei prezzi dei prodotti. Nessun dato inviato al server."
image: "https://marzorati.co/img/password.png"
share-img: "https://marzorati.co/img/password.png"
tags: [prezzi, prodotti, ricerca]
---

<style>
  textarea {
    display: none;
  }

  input {
    width: 100%;
    padding: 14px;
    font-size: 17px;
    margin-bottom: 20px;
  }

  ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  li {
    padding: 12px 10px;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: space-between;
    font-size: 16px;
  }

  .prezzo {
    font-weight: bold;
    white-space: nowrap;
  }
</style>

<input
  type="text"
  id="searchInput"
  placeholder="Cerca un prodotto..."
  autofocus
>

<!-- SORGENTE DATI NASCOSTA -->
<textarea id="productSource">
Tovaglioli monovelo Esselunga 350;2,65 €
Sovracoscia pollo;5,69 €/kg
Pollo a fette;11,30 €/kg
Gorgonzola;16 €/kg
Bagno doccia Esselunga;1,70 €/L
</textarea>

<ul id="productList"></ul>

<script>
  const textarea = document.getElementById('productSource');
  const list = document.getElementById('productList');
  const searchInput = document.getElementById('searchInput');

  function renderList() {
    list.innerHTML = '';

    const filter = searchInput.value.toLowerCase();
    const lines = textarea.value.split('\n');

    lines.forEach(line => {
      if (!line.includes(';')) return;

      const [nome, prezzo] = line.split(';');
      const nomeClean = nome.trim();

      if (!nomeClean.toLowerCase().includes(filter)) return;

      const li = document.createElement('li');
      li.innerHTML = `
        <span>${nomeClean}</span>
        <span class="prezzo">${prezzo.trim()}</span>
      `;

      list.appendChild(li);
    });
  }

  searchInput.addEventListener('keyup', renderList);

  // inizializzazione (lista vuota finché non cerchi)
  list.innerHTML = '';
</script>
