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
  /* Reset minimo e contenitore centrale */
  font-family:'Montserrat', sans-serif;
  .content-wrapper {
    max-width: 720px;           /* o 800px, 640px... scegli tu in base a quanto vuoi largo */
    margin: 0 auto;             /* ← questo centra orizzontalmente */
    padding: 0 16px;            /* respira un po' sui lati nei telefoni */
    box-sizing: border-box;
  }

  /* Input di ricerca */
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

  /* Lista prodotti */
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
    color: #c62828;             /* rosso scuro per i prezzi – più leggibile */
    white-space: nowrap;
    min-width: 90px;
    text-align: right;
  }

  .no-results {
    color: #666;
    font-style: italic;
    padding: 30px 20px;
    text-align: center;
    font-size: 15px;
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
Gorgonzola;16 €/kg
Bagno doccia Esselunga;1,70 €/L
Carta igienica 4 rotoli;3 €
Wafer Esselunga;4,46 €/kg
Pasta Esselunga;1,30 €/kg
Lenticchie in scatola;3,05 €/kg
Ceci in scatola;2,69 €/kg
Exquisa;8,30 €/kg
Galbanino Esselunga;7,39 €/kg
Riso Carnaroli Gallo;2,58 €/kg
Tortellini;7,78€/kg
Grana Padano 16 mesi; 12€/kg
Parmigiano Reggiano 24 mesi;17 €/kg
Caffè Solubile Aldi;29,95 €/kg
Cacao amaro;2,07 €/kg
Brioschi;10,91 €/kg
Testine OralB; 2,33 cad.
Caffè Lavazza Dek;15,98 €/kg
Gorgonzola Santi;18 €/Kg
Detersivo Felce Azzurra;2,16 €/L
Detersivo lavatrice;1,85 €/L
Shampoo Johnson;3,84 €/L
Pancetta affumicata;22 €/kg
Farina 0 Esselunga 13gr;1,19 €/kg
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