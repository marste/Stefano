---
layout: page
title: Ultime Notizie
permalink: /new-news/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
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
    .itemTitle a{font-weight:bold; font-size:20px; color:#008AFF; text-decoration:none;}
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:11px;color:#AAAAAA;}
    .feed-item{margin-bottom:16px;}
    .feed-error{font-size:13px;color:#AA3333;}
</style>

<body translate="no">

<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<center><a href="#Ultimissime">Ultim'ora</a> - <a href="#Principali">Principali</a> - <a href="#Italia">Italia</a> - <a href="#Economia">Economia</a> - <a href="#Mondo">Mondo</a> - <a href="#Tecnologia">Tecnologia</a> - <a href="#Salute">Salute</a></center>
<br>

<center><h1><a name="Ultimissime"><font color="Black">Ultim'ora</font></a></h1></center>
<br>
<div id="divRssUltimissime" class="feed-container">Caricamento...</div>

<center><h1><a name="Principali"><font color="Black">Principali</font></a></h1></center>
<br>
<div id="divRssPrincipali" class="feed-container">Caricamento...</div>

<center><h1><a name="Italia"><font color="Black">Italia</font></a></h1></center>
<br>
<div id="divRssItalia" class="feed-container">Caricamento...</div>

<center><h1><a name="Economia"><font color="Black">Economia</font></a></h1></center>
<br>
<div id="divRssEconomia" class="feed-container">Caricamento...</div>

<center><h1><a name="Mondo"><font color="Black">Mondo</font></a></h1></center>
<br>
<div id="divRssMondo" class="feed-container">Caricamento...</div>

<center><h1><a name="Tecnologia"><font color="Black">Tecnologia</font></a></h1></center>
<br>
<div id="divRssTecnologia" class="feed-container">Caricamento...</div>

<center><h1><a name="Salute"><font color="Black">Salute</font></a></h1></center>
<br>
<div id="divRssSalute" class="feed-container">Caricamento...</div>

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
  { containerId: "divRssUltimissime", url: "https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml", max: 20 },
  { containerId: "divRssPrincipali", url: "https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it", max: 10 },
  { containerId: "divRssItalia", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it", max: 10 },
  { containerId: "divRssEconomia", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it", max: 10 },
  { containerId: "divRssMondo", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it", max: 10 },
  { containerId: "divRssTecnologia", url: "https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl=it&gl=IT&ceid=IT:it", max: 10 },
  { containerId: "divRssSalute", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it", max: 10 },
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
    }

    container.innerHTML = items.map(item => `
      <div class="feed-item">
        <p class="itemTitle"><a href="${escapeHtml(item.link)}" target="_blank" rel="noopener">${escapeHtml(item.title)}</a></p>
        ${item.date ? `<p class="itemDate">${escapeHtml(item.date)}</p>` : ""}
        ${item.description ? `<p class="itemDesc">${escapeHtml(item.description)}</p>` : ""}
      </div>
    `).join("");
  } catch (err) {
    container.innerHTML = `<p class="feed-error">Feed non disponibile al momento.</p>`;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  FEEDS.forEach(loadFeed);
});

// ===== Scroll to Top ====
$(window).scroll(function () {
  if ($(this).scrollTop() >= 50) {
    $('#return-to-top').fadeIn(200);
  } else {
    $('#return-to-top').fadeOut(200);
  }
});
$('#return-to-top').click(function () {
  $('body,html').animate({
    scrollTop: 0
  }, 500);
});
</script>
