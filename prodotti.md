---
layout: page
title: "Ricerca Prezzi Prodotti"
permalink: /prezzi-prodotti/
date: 2025-06-03 10:00:00 +0200
description: "Ricerca veloce dei prezzi dei prodotti. Tutto in locale, nessun dato inviato al server."
image: "https://marzorati.co/img/price-tag.png"      # ← immagine più appropriata?
share-img: "https://marzorati.co/img/price-tag.png"
tags: [prezzi, prodotti, spesa, esselunga]
---
<style>
  body {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  input[type="text"] {
    width: 100%;
    padding: 14px 16px;
    font-size: 17px;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
    margin-bottom: 1.2rem;
  }

  input[type="text"]:focus {
    outline: none;
    border-color: #0066cc;
    box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.15);
  }

  ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  li {
    padding: 14px 12px;
    border-bottom: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 16px;
    gap: 16px;
  }

  li:last-child {
    border-bottom: none;
  }

  .product-name {
    flex: 1;
    color: #222;
  }

  .prezzo {
    font-weight: 600;
    color: #d32f2f;
    white-space: nowrap;
    min-width: 80px;
    text-align: right;
  }

  .no-results {
    color: #777;
    font-style: italic;
    padding: 20px;
    text-align: center;
  }
</style>

<input
  type="text"
  id="searchInput"
  placeholder="Cerca un prodotto (es. gorgonzola, pollo, tovaglioli…)"
  autofocus
  autocomplete="off"
/>

<ul id="productList"></ul>

<textarea id="productSource" hidden>
Tovaglioli monovelo Esselunga 350;2,65 €
Sovracoscia pollo;5,69 €/kg
Pollo a fette;11,30 €/kg
Gorgonzola;16,00 €/kg
Bagno doccia Esselunga;1,70 €/L
Fazzoletti 10 pacchi;2,19 €
Latte parzialmente scremato 1L;1,55 €
Pasta di semola 500g;0,89 €
Pomodori pelati 400g;0,79 €
Olio extravergine 1L;7,90 €
</textarea>

<script>
  const searchInput  = document.getElementById("searchInput");
  const productList  = document.getElementById("productList");
  const productSource = document.getElementById("productSource");

  // Prepariamo i dati una volta sola (più performante)
  const products = productSource.value
    .split("\n")
    .map(line => line.trim())
    .filter(line => line && line.includes(";"))
    .map(line => {
      const [name, price] = line.split(";");
      return {
        name: name.trim(),
        price: price.trim()
      };
    });

  function renderList() {
    const filter = searchInput.value.trim().toLowerCase();
    productList.innerHTML = "";

    const matches = filter
      ? products.filter(p => p.name.toLowerCase().includes(filter))
      : products;

    if (matches.length === 0) {
      const li = document.createElement("li");
      li.className = "no-results";
      li.textContent = filter ? "Nessun prodotto trovato" : "Nessun prodotto in lista";
      productList.appendChild(li);
      return;
    }

    const fragment = document.createDocumentFragment();

    matches.forEach(item => {
      const li = document.createElement("li");

      const nameSpan = document.createElement("span");
      nameSpan.className = "product-name";
      nameSpan.textContent = item.name;

      const priceSpan = document.createElement("span");
      priceSpan.className = "prezzo";
      priceSpan.textContent = item.price;

      li.appendChild(nameSpan);
      li.appendChild(priceSpan);
      fragment.appendChild(li);
    });

    productList.appendChild(fragment);
  }

  // Mostra tutti i prodotti all'apertura
  renderList();

  // Ricerca live
  searchInput.addEventListener("input", renderList);
  // Anche "keyup" va bene, ma "input" cattura anche copia/incolla
</script>