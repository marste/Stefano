---
layout: page
title: "Ricerca Prezzi Prodotti"
permalink: /prezzi-prodotti/
date: 2025-06-03 10:00:00 +0200
description: "Ricerca veloce dei prezzi dei prodotti"
image: "https://marzorati.co/img/salvadanaio.jpg"
share-img: "https://marzorati.co/img/salvadanaio.jpg"
tags: [prezzi, prodotti, spesa, esselunga, supermercati, conad, aldi]
---

<style>
  .content-wrapper {
    max-width: 720px;
    margin: 0 auto;
    padding: 0 16px;
    box-sizing: border-box;
  }

  input[type="text"] {
    width: 100%;
    padding: 14px 16px;
    font-size: 17px;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
    margin: 1.5rem 0 1.2rem 0;
  }

  input[type="text"]:focus {
    outline: none;
    border-color: #0066cc;
    box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.12);
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
    color: #111;
  }

  .prezzo {
    font-weight: 600;
    color: #c62828;
    white-space: nowrap;
    min-width: 90px;
    text-align: right;
  }

  li.no-results {
    display: block;
    text-align: center;
    color: #666;
    font-style: italic;
    padding: 30px 20px;
    font-size: 15px;
  }
</style>

<div class="content-wrapper">

  <input
    type="text"
    id="searchInput"
    placeholder="Cerca un prodotto (es. gorgonzola, pollo, tovaglioli…)"
    aria-label="Cerca un prodotto"
    autofocus
    autocomplete="off"
  />

  <ul id="productList"></ul>

  <textarea id="productSource" hidden>
Tovaglioli monovelo Esselunga 350;2,65 €
Sovracoscia pollo;5,69 €/kg
Pollo a fette;11,30 €/kg
Gorgonzola;16 €/kg
Bagno doccia Esselunga;1,70 €/l
Carta igienica 4 rotoli;3 €
Wafer Esselunga;4,46 €/kg
Pasta Esselunga;1,30 €/kg
Lenticchie in scatola;3,05 €/kg
Ceci in scatola;2,69 €/kg
Exquisa;8,30 €/kg
Galbanino Esselunga;7,39 €/kg
Riso Carnaroli Gallo;2,58 €/kg
Tortellini;7,78 €/kg
Grana Padano 16 mesi;12 €/kg
Parmigiano Reggiano 24 mesi;17 €/kg
Caffè Solubile Aldi;29,95 €/kg
Cacao amaro;2,07 €/kg
Brioschi;10,91 €/kg
Testine OralB;2,33 cad.
Caffè Lavazza Dek;15,98 €/kg
Gorgonzola Santi;18 €/kg
Detersivo Felce Azzurra;2,16 €/l
Detersivo lavatrice;1,85 €/l
Shampoo Johnson;3,84 €/l
Pancetta affumicata;22 €/kg
Farina 0 Esselunga 13 gr;1,19 €/kg
Scottona Iperal;20 €/kg
Farina Caputo Oro 14 gr Conad;1,49 €/kg
Sapone liquido Dove;2,58 €/l
Prosciutto Crudo;45 €/kg
Prosciutto Cotto;17 €/kg
Coppa;30 €/kg
Salamino;14 €/kg
Bresaola;31 €/kg
Pancetta;18 €/kg
Mortadella Bologna;12 €/kg
Speck;28 €/kg
  </textarea>

</div>

<script>
  const searchInput   = document.getElementById("searchInput");
  const productList   = document.getElementById("productList");
  const productSource = document.getElementById("productSource");

  const products = productSource.value
    .split("\n")
    .map(l => l.trim())
    .filter(l => l && l.includes(";"))
    .map(l => {
      const [name, price] = l.split(";");
      return {
        name: name.trim(),
        price: price.trim()
      };
    });

  function renderList() {
    const filter = searchInput.value.toLowerCase().trim();
    productList.innerHTML = "";

    const matches = filter
      ? products.filter(p => p.name.toLowerCase().includes(filter))
      : products;

    if (!matches.length) {
      const li = document.createElement("li");
      li.className = "no-results";
      li.textContent = "Nessun prodotto trovato";
      productList.appendChild(li);
      return;
    }

    const fragment = document.createDocumentFragment();

    matches.forEach(p => {
      const li = document.createElement("li");

      li.innerHTML = `
        <span class="product-name">${p.name}</span>
        <span class="prezzo">${p.price}</span>
      `;

      fragment.appendChild(li);
    });

    productList.appendChild(fragment);
  }

  renderList();
  searchInput.addEventListener("input", renderList);
</script>
