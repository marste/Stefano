---
layout: page
title: Ultime Notizie
permalink: /news/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
published: true
---
<!-- Style per bottone top -->
<style>
#return-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: rgb(0, 0, 0);
    background: rgba(0, 0, 0, 0.7);
    width: 50px;
    height: 50px;
    display: block;
    text-decoration: none;
    -webkit-border-radius: 35px;
    -moz-border-radius: 35px;
    border-radius: 35px;
    display: none;
    -webkit-transition: all 0.3s linear;
    -moz-transition: all 0.3s ease;
    -ms-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#return-to-top i {
    color: #fff;
    margin: 0;
    position: relative;
    left: 16px;
    top: 13px;
    font-size: 19px;
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -ms-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#return-to-top:hover {
    background: rgba(0, 0, 0, 0.9);
}
#return-to-top:hover i {
    color: #fff;
    top: 5px;
}
</style>

<!-- Style RSS: stesse classi di prima -->
<style>
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
    .itemTitle a{font-weight:bold; font-size:20px; color:#008AFF; text-decoration:none;}
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:12px;color:#404040; margin:0 0 2px 0; padding:0; line-height:1.4;}
    .feed-error{font-size:13px;color:#AA3333;}
    .section-title{margin:15px 0 10px 0;}
</style>

<div translate="no">

<a href="#" id="return-to-top" aria-label="Torna all'inizio">
    <i class="icon-chevron-up" aria-hidden="true"></i>
</a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<div id="divRssUltimissime" class="feed-container">Caricamento...</div>

</div>

<script src="/js/jquery-3.6.0.min.js"></script>

<script>
(() => {
    "use strict";

    const WORKER_URL =
        "https://rss-proxy.stefano-marzorati.workers.dev/";

    const FEEDS = [
        "https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml",
        "https://www.ansa.it/sito/notizie/economia/economia_rss.xml"
    ];

    function escapeHtml(str) {
        const div = document.createElement("div");
        div.textContent = str == null ? "" : String(str);
        return div.innerHTML;
    }

    function safeLink(value) {
        try {
            const url = new URL(value);

            if (url.protocol === "https:" || url.protocol === "http:") {
                url.hash = "";
                return url.href;
            }
        } catch {}

        return "";
    }

    function timestamp(item) {
        const value = Date.parse(item.published_at || "");
        return Number.isNaN(value) ? 0 : value;
    }

    async function fetchFeed(feedUrl) {
        const endpoint = new URL(WORKER_URL);
        endpoint.searchParams.set("url", feedUrl);

        // Nessun parametro max: richiede tutta la giornata.
        const response = await fetch(endpoint);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const items = await response.json();

        if (!Array.isArray(items)) {
            throw new Error("Formato della risposta non valido");
        }

        return items;
    }

    function renderItem(item) {
        let dateDisplay = item.date || "";
        let title = item.title || "";
        const description = item.description || "";
        const link = safeLink(item.link);

        // Estrai data dal titolo.
        const dateMatch = title.match(
            /^(\d{1,2}[\/\.]\d{1,2}[\/\.]\d{2,4})\s*/
        );

        if (dateMatch) {
            dateDisplay = dateMatch[1];
            title = title.substring(dateMatch[0].length).trim();
        }

        // Estrai ora dal titolo.
        const timeMatch = title.match(/^(\d{1,2}[\.:]\d{2})\s*/);

        if (timeMatch) {
            dateDisplay = dateDisplay
                ? `${dateDisplay} - ${timeMatch[1]}`
                : timeMatch[1];

            title = title.substring(timeMatch[0].length).trim();
        }

        const titleHtml = link
            ? `<a href="${escapeHtml(link)}"
                  target="_blank"
                  rel="noopener noreferrer">${escapeHtml(title)}</a>`
            : escapeHtml(title);

        return `
            <div class="feed-item">
                <div class="itemDate">${escapeHtml(dateDisplay)}</div>
                <div class="itemTitle">${titleHtml}</div>
                ${
                    description
                        ? `<div class="itemDesc">${escapeHtml(description)}</div>`
                        : ""
                }
            </div>
        `;
    }

    async function loadNews() {
        const container = document.getElementById("divRssUltimissime");

        if (!container) {
            return;
        }

        // Se un feed non risponde, mostra comunque l'altro.
        const results = await Promise.allSettled(
            FEEDS.map(fetchFeed)
        );

        const successful = results.filter(
            result => result.status === "fulfilled"
        );

        const failedCount = results.length - successful.length;

        if (successful.length === 0) {
            container.innerHTML =
                '<p class="feed-error">Notizie non disponibili al momento.</p>';
            return;
        }

        // Unisce i due feed ed elimina i duplicati per link.
        const uniqueItems = new Map();

        successful.forEach(result => {
            result.value.forEach(item => {
                if (!item || typeof item !== "object") {
                    return;
                }

                const link = safeLink(item.link);

                if (!link) {
                    return;
                }

                const existing = uniqueItems.get(link);

                // Per lo stesso link preferisce la versione più recente.
                if (
                    !existing ||
                    timestamp(item) > timestamp(existing)
                ) {
                    uniqueItems.set(link, item);
                }
            });
        });

        // Ordinamento cronologico decrescente sulla data ISO del Worker.
        const items = Array.from(uniqueItems.values()).sort(
            (a, b) =>
                timestamp(b) - timestamp(a) ||
                String(a.title || "").localeCompare(
                    String(b.title || ""),
                    "it"
                )
        );

        const warning = failedCount > 0
            ? '<p class="feed-error">Una delle fonti non è disponibile: l’elenco potrebbe essere incompleto.</p>'
            : "";

        if (items.length === 0) {
            container.innerHTML =
                warning +
                "<p><em>Nessuna notizia archiviata per la giornata di oggi.</em></p>";
            return;
        }

        container.innerHTML =
            warning + items.map(renderItem).join("");
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", loadNews);
    } else {
        loadNews();
    }

    // ===== Scroll to Top ====
    $(window).scroll(function () {
        if ($(this).scrollTop() >= 50) {
            $("#return-to-top").fadeIn(200);
        } else {
            $("#return-to-top").fadeOut(200);
        }
    });

    $("#return-to-top").click(function (event) {
        event.preventDefault();

        $("body,html").animate({
            scrollTop: 0
        }, 500);
    });
})();
</script>