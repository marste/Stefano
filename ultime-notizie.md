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

<!-- Sezioni RSS -->
<div id="rss-feeds">
    <h1 id="Ultimissime">Ultim'ora</h1>
    <div id="divRssUltimissime"></div>

    <h1 id="Principali">Principali</h1>
    <div id="divRssPrincipali"></div>

    <h1 id="Italia">Italia</h1>
    <div id="divRssItalia"></div>

    <h1 id="Economia">Economia</h1>
    <div id="divRssEconomia"></div>

    <h1 id="Mondo">Mondo</h1>
    <div id="divRssMondo"></div>

    <h1 id="Tecnologia">Tecnologia</h1>
    <div id="divRssTecnologia"></div>

    <h1 id="Salute">Salute</h1>
    <div id="divRssSalute"></div>
</div>

<script>
// Scorrimento fluido alla sezione
function scrollToSection(id) {
    const section = document.getElementById(id);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Gestione pulsante "Torna su"
window.addEventListener('scroll', function () {
    const button = document.getElementById('return-to-top');
    if (window.scrollY >= 50) {
        button.style.display = 'block';
    } else {
        button.style.display = 'none';
    }
});
document.getElementById('return-to-top').addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Funzione per caricare i feed RSS
async function loadRSS(feedUrl, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    document.getElementById('loading-spinner').style.display = 'block';

    try {
        const response = await fetch(`https://api.rss2json.com/v1/api.json?rss_url=${feedUrl}`);
        const data = await response.json();

        let html = '';
        data.items.forEach(item => {
            html += `
                <div class="rss-item">
                    <div class="itemTitle"><a href="${item.link}" target="_blank">${item.title}</a></div>
                    <div class="itemDate">${new Date(item.pubDate).toLocaleDateString('it-IT')}</div>
                    <div class="itemContent">${item.content}</div>
                </div>
            `;
        });

        container.innerHTML = html;
    } catch (error) {
        container.innerHTML = '<p>Errore nel caricamento del feed.</p>';
    } finally {
        document.getElementById('loading-spinner').style.display = 'none';
    }
}

// Caricamento parallelo dei feed
const feeds = {
    divRssUltimissime: 'https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml',
    divRssPrincipali: 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it',
    divRssItalia: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it',
    divRssEconomia: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it'
};

Object.entries(feeds).forEach(([containerId, feedUrl]) => loadRSS(feedUrl, containerId));
</script>
</body>
