---
layout: page
title: Ultime Notizie
permalink: /ultime-notizie/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---

<!-- Style per bottone top -->
<style>
#return-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: rgba(0, 0, 0, 0.7);
    width: 50px;
    height: 50px;
    border-radius: 35px;
    display: none;
    transition: all 0.3s ease;
}
#return-to-top i {
    color: #fff;
    position: relative;
    left: 16px;
    top: 13px;
    font-size: 19px;
    transition: all 0.3s ease;
}
#return-to-top:hover {
    background: rgba(0, 0, 0, 0.9);
}
#return-to-top:hover i {
    top: 5px;
}
</style>

<!-- Style per RSS -->
<style>
    .itemTitle a { font-weight: bold; font-size: 20px; color: #008AFF; text-decoration: none; }
    .itemTitle a:hover { text-decoration: underline; }
    .itemDate { font-size: 11px; color: #AAAAAA; }
    .rss-container { max-width: 800px; margin: auto; padding: 10px; }
    .itemDesc { font-size: 14px; color: #333; margin-top: 5px; }
</style>

<!-- Style per pulsanti circolari -->
<style>
    .buttons-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        padding: 20px;
    }
    .circle-btn {
        width: 60px;
        height: 60px;
        background: #333;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        cursor: pointer;
    }
    .circle-btn i {
        color: white;
        font-size: 24px;
    }
    .circle-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .circle-btn:hover::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: -30px;
        background: black;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 12px;
        white-space: nowrap;
    }
</style>

<body>
<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>
<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<div class="buttons-container">
    <div class="circle-btn" data-tooltip="Ultim'ora" onclick="scrollToSection('Ultimissime')"><i class="icon-bolt"></i></div>
    <div class="circle-btn" data-tooltip="Principali" onclick="scrollToSection('Principali')"><i class="icon-globe"></i></div>
    <div class="circle-btn" data-tooltip="Italia" onclick="scrollToSection('Italia')"><i class="icon-flag"></i></div>
    <div class="circle-btn" data-tooltip="Economia" onclick="scrollToSection('Economia')"><i class="icon-money"></i></div>
    <div class="circle-btn" data-tooltip="Mondo" onclick="scrollToSection('Mondo')"><i class="icon-globe"></i></div>
    <div class="circle-btn" data-tooltip="Tecnologia" onclick="scrollToSection('Tecnologia')"><i class="icon-cogs"></i></div>
    <div class="circle-btn" data-tooltip="Salute" onclick="scrollToSection('Salute')"><i class="icon-heart"></i></div>
</div>

<div id="loading-spinner" style="text-align: center; padding: 20px; font-size: 20px; display: none;">
    <i class="icon-spinner icon-spin"></i> Caricamento...
</div>

<div id="rss-feeds"></div>

<script>
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

const feeds = [
    { id: "Ultimissime", title: "Ultim'ora", url: "https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml" },
    { id: "Principali", title: "Principali", url: "https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it" },
    { id: "Italia", title: "Italia", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it" },
    { id: "Economia", title: "Economia", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it" },
    { id: "Mondo", title: "Mondo", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it" },
    { id: "Tecnologia", title: "Tecnologia", url: "https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl=it&gl=IT&ceid=IT:it" },
    { id: "Salute", title: "Salute", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it" }
];

async function loadRSS() {
    document.getElementById('loading-spinner').style.display = 'block';
    await Promise.all(feeds.map(async (feed) => {
        const response = await fetch(`https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(feed.url)}`);
        const data = await response.json();
        let content = `<center><h1><a name="${feed.id}">${feed.title}</a></h1></center><div class='rss-container'>`;
        data.items.slice(0, 10).forEach(item => {
            content += `<div class='item'><p class='itemTitle'><a href='${item.link}' target='_blank'>${item.title}</a></p>`;
            content += `<p class='itemDate'>${new Date(item.pubDate).toLocaleDateString('it-IT')}</p>`;
            content += `<p class='itemDesc'>${item.description}</p></div>`;
        });
        content += '</div>';
        document.getElementById('rss-feeds').innerHTML += content;
    }));
    document.getElementById('loading-spinner').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", loadRSS);
</script>
</body>
