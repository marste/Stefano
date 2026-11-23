---
layout: page
title: Ultime Notizie
permalink: /news/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---

<style>
    #return-to-top {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        display: none;
        width: 50px;
        height: 50px;
        padding: 0;
        border: none;
        border-radius: 35px;
        background: rgba(0, 0, 0, 0.7);
        color: #fff;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    #return-to-top:hover {
        background: rgba(0, 0, 0, 0.9);
    }

    #return-to-top i {
        display: inline-block;
        font-size: 19px;
        transition: transform 0.3s ease;
    }

    #return-to-top:hover i {
        transform: translateY(-5px);
    }

    .feed-item {
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 1px solid #e0e0e0;
    }

    .feed-item:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

<<<<<<< HEAD
    .itemTitle a {
        font-weight: bold;
        font-size: 20px;
        color: #008AFF;
        text-decoration: none;
=======
<body translate="no">

<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">


<div id="divRssUltimissime" class="feed-container">Caricamento...</div>

<script>
  window.console = window.console || function(t) {};
</script>
<script src='/js/jquery-3.6.0.min.js'></script>
<script>
// URL del tuo Cloudflare Worker - da sostituire con quello reale
// dopo il deploy (es. https://news-proxy.tuosubdominio.workers.dev
// oppure un dominio custom tipo https://newsproxy.marzorati.co)
const WORKER_URL = "https://rss-proxy.stefano-marzorati.workers.dev/";

const FEEDS = [
  { containerId: "divRssUltimissime", url: "https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml", max: 500 }
  ];

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str || "";
  return div.innerHTML;
}

async function loadFeed(feed) {
  const container = document.getElementById(feed.containerId);
  try {
    const endpoint = `${WORKER_URL}/?url=${encodeURIComponent(feed.url)}&max=${feed.max}`;
    const res = await fetch(endpoint);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const items = await res.json();

    if (!Array.isArray(items) || items.length === 0) {
      container.innerHTML = "<p><em>Nessuna notizia disponibile al momento.</em></p>";
      return;
>>>>>>> 9e5614a26b36590f53e7b2b359a888b6a47446b4
    }

    .itemTitle a:hover {
        text-decoration: underline;
    }

    .itemDate {
        font-size: 12px;
        color: #404040;
        margin: 0 0 2px 0;
        padding: 0;
        line-height: 1.4;
    }

    .itemDesc {
        white-space: pre-line;
        overflow-wrap: anywhere;
    }

    .feed-error {
        font-size: 13px;
        color: #AA3333;
    }

    .section-title {
        margin: 30px 0 15px 0;
    }
</style>

<link
    href="https://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css"
    rel="stylesheet"
>

<div translate="no">
    <button
        type="button"
        id="return-to-top"
        aria-label="Torna all'inizio della pagina"
        title="Torna all'inizio"
    >
        <i class="icon-chevron-up" aria-hidden="true"></i>
    </button>

    <h2 class="section-title">ANSA — Ultime notizie</h2>
    <div id="divRssUltimissime" class="feed-container">
        Caricamento...
    </div>

    <h2 class="section-title">ANSA — Economia</h2>
    <div id="divRssEconomia" class="feed-container">
        Caricamento...
    </div>
</div>

<script>
(() => {
    "use strict";

    const WORKER_URL =
        "https://rss-proxy.stefano-marzorati.workers.dev/";

    // Senza max vengono richieste tutte le notizie archiviate di oggi.
    const FEEDS = [
        {
            containerId: "divRssUltimissime",
            url: "https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml"
        },
        {
            containerId: "divRssEconomia",
            url: "https://www.ansa.it/sito/notizie/economia/economia_rss.xml"
        }
    ];

    function safeLink(value) {
        try {
            const url = new URL(value);

            if (url.protocol === "https:" || url.protocol === "http:") {
                return url.href;
            }
        } catch {
            // Un link non valido viene mostrato come semplice testo.
        }

        return "";
    }

    function showMessage(container, message, isError = false) {
        const paragraph = document.createElement("p");
        paragraph.textContent = message;

        if (isError) {
            paragraph.className = "feed-error";
        } else {
            paragraph.style.fontStyle = "italic";
        }

        container.replaceChildren(paragraph);
    }

    function createFeedItem(item) {
        let dateDisplay = item.date || "";
        let title = item.title || "";
        const description = item.description || "";

        // Mantiene la gestione di eventuali date inserite nel titolo.
        const dateMatch = title.match(
            /^(\d{1,2}[\/.]\d{1,2}[\/.]\d{2,4})\s*/
        );

        if (dateMatch) {
            dateDisplay = dateMatch[1];
            title = title.substring(dateMatch[0].length).trim();
        }

        const timeMatch = title.match(/^(\d{1,2}[.:]\d{2})\s*/);

        if (timeMatch) {
            dateDisplay = dateDisplay
                ? `${dateDisplay} - ${timeMatch[1]}`
                : timeMatch[1];

            title = title.substring(timeMatch[0].length).trim();
        }

        const article = document.createElement("div");
        article.className = "feed-item";

        const dateElement = document.createElement("div");
        dateElement.className = "itemDate";
        dateElement.textContent = dateDisplay;
        article.appendChild(dateElement);

        const titleElement = document.createElement("div");
        titleElement.className = "itemTitle";

        const link = safeLink(item.link);

        if (link) {
            const anchor = document.createElement("a");
            anchor.href = link;
            anchor.target = "_blank";
            anchor.rel = "noopener noreferrer";
            anchor.textContent = title;
            titleElement.appendChild(anchor);
        } else {
            titleElement.textContent = title;
        }

        article.appendChild(titleElement);

        if (description) {
            const descriptionElement = document.createElement("div");
            descriptionElement.className = "itemDesc";
            descriptionElement.textContent = description;
            article.appendChild(descriptionElement);
        }

        return article;
    }

    async function loadFeed(feed) {
        const container = document.getElementById(feed.containerId);

        if (!container) {
            return;
        }

        try {
            const endpoint = new URL(WORKER_URL);
            endpoint.searchParams.set("url", feed.url);

            if (Number.isInteger(feed.max) && feed.max > 0) {
                endpoint.searchParams.set("max", String(feed.max));
            }

            const response = await fetch(endpoint);

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const items = await response.json();

            if (!Array.isArray(items)) {
                throw new Error("Formato della risposta non valido");
            }

            if (items.length === 0) {
                showMessage(
                    container,
                    "Nessuna notizia archiviata per la giornata di oggi."
                );
                return;
            }

            const fragment = document.createDocumentFragment();

            items.forEach(item => {
                fragment.appendChild(createFeedItem(item));
            });

            container.replaceChildren(fragment);
        } catch (error) {
            console.error("Errore caricamento feed:", feed.url, error);

            showMessage(
                container,
                "Notizie non disponibili al momento. Riprova più tardi.",
                true
            );
        }
    }

    function initializePage() {
        FEEDS.forEach(loadFeed);

        const returnToTop = document.getElementById("return-to-top");

        if (!returnToTop) {
            return;
        }

        function updateReturnToTop() {
            returnToTop.style.display =
                window.scrollY >= 50 ? "block" : "none";
        }

        window.addEventListener("scroll", updateReturnToTop, {
            passive: true
        });

        updateReturnToTop();

        returnToTop.addEventListener("click", () => {
            const reducedMotion = window.matchMedia(
                "(prefers-reduced-motion: reduce)"
            ).matches;

            window.scrollTo({
                top: 0,
                behavior: reducedMotion ? "auto" : "smooth"
            });
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initializePage);
    } else {
        initializePage();
    }
})();
</script>