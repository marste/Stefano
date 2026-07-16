---
layout: page
title: Ultime Notizie
permalink: /news/
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
  { containerId: "divRssUltimissime", url: "https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml", max: 20 }
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

    container.innerHTML = items.map(item => {
      let dateDisplay = item.date || "";
      let title = item.title || "";
      let description = item.description || "";
      
      // Estrai data dal titolo
      const dateMatch = title.match(/^(\d{1,2}[\/\.]\d{1,2}[\/\.]\d{2,4})\s*/);
      if (dateMatch) {
        dateDisplay = dateMatch[1];
        title = title.substring(dateMatch[0].length).trim();
      }
      
      // Estrai ora dal titolo
      const timeMatch = title.match(/^(\d{1,2}[\.:]\d{2})\s*/);
      if (timeMatch) {
        dateDisplay = dateDisplay ? `${dateDisplay} - ${timeMatch[1]}` : timeMatch[1];
        title = title.substring(timeMatch[0].length).trim();
      }
      
      return `
        <div class="feed-item">
          <div class="itemDate">${escapeHtml(dateDisplay)}</div>
          <div class="itemTitle"><a href="${escapeHtml(item.link)}" target="_blank" rel="noopener">${escapeHtml(title)}</a></div>
          ${description ? `<div class="itemDesc">${escapeHtml(description)}</div>` : ""}
        </div>
      `;
    }).join("");
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
