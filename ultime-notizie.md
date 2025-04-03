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

/* Style per RSS */
.rss-feed {
    margin: 20px auto;
    max-width: 800px;
}
.rss-item {
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #eee;
}
.itemTitle a {
    font-weight: bold; 
    font-size: 20px; 
    color: #008AFF; 
    text-decoration: none;
}
.itemTitle a:hover { 
    text-decoration: underline;
}
.itemDate {
    font-size: 11px;
    color: #AAAAAA;
    margin-top: 5px;
}
.itemDescription {
    margin-top: 10px;
    font-size: 14px;
    line-height: 1.5;
}
.loading {
    text-align: center;
    padding: 20px;
    font-style: italic;
    color: #888;
}
.error {
    color: #d9534f;
    text-align: center;
    padding: 20px;
}
</style>

<body translate="no">

<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<center>
    <a href="#Ultimissime">Ultim'ora</a> - 
    <a href="#Principali">Principali</a> - 
    <a href="#Italia">Italia</a> - 
    <a href="#Economia">Economia</a> - 
    <a href="#Mondo">Mondo</a> - 
    <a href="#Tecnologia">Tecnologia</a> - 
    <a href="#Salute">Salute</a>
</center>   
<br>

<center><h1><a name="Ultimissime"><font color="Black">Ultim'ora</font></a></h1></center>
<br>
<div id="divRssUltimissime" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<center><h1><a name="Principali"><font color="Black">Principali</font></a></h1></center>
<br>
<div id="divRssPrincipali" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<center><h1><a name="Italia"><font color="Black">Italia</font></a></h1></center>
<br>
<div id="divRssItalia" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<center><h1><a name="Economia"><font color="Black">Economia</font></a></h1></center>
<br>
<div id="divRssEconomia" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<center><h1><a name="Mondo"><font color="Black">Mondo</font></a></h1></center>
<br>
<div id="divRssMondo" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<center><h1><a name="Tecnologia"><font color="Black">Tecnologia</font></a></h1></center>
<br>
<div id="divRssTecnologia" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<center><h1><a name="Salute"><font color="Black">Salute</font></a></h1></center>
<br>
<div id="divRssSalute" class="rss-feed">
    <div class="loading">Caricamento notizie in corso...</div>
</div>

<script src='/js/jquery-3.6.0.min.js'></script>
<script>
// Funzione per ottenere e visualizzare il feed RSS
function loadRSS(feedUrl, targetDivId, maxCount = 10) {
    const targetDiv = document.getElementById(targetDivId);
    
    // Usa un proxy CORS per evitare problemi di same-origin policy
    const proxyUrl = 'https://api.allorigins.win/get?url=' + encodeURIComponent(feedUrl);
    
    fetch(proxyUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Errore nel caricamento del feed');
            }
            return response.json();
        })
        .then(data => {
            if (data.contents) {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(data.contents, "text/xml");
                
                // Estrai gli item dal feed
                const items = xmlDoc.querySelectorAll("item");
                let htmlContent = '';
                
                // Limita il numero di elementi mostrati
                const itemCount = Math.min(items.length, maxCount);
                
                if (itemCount === 0) {
                    htmlContent = '<div class="error">Nessuna notizia disponibile</div>';
                } else {
                    for (let i = 0; i < itemCount; i++) {
                        const item = items[i];
                        const title = item.querySelector("title").textContent;
                        const link = item.querySelector("link").textContent;
                        const pubDate = item.querySelector("pubDate") ? new Date(item.querySelector("pubDate").textContent).toLocaleDateString('it-IT') : '';
                        const description = item.querySelector("description") ? item.querySelector("description").textContent : '';
                        
                        htmlContent += `
                            <div class="rss-item">
                                <div class="itemTitle"><a href="${link}" target="_blank">${title}</a></div>
                                ${pubDate ? `<div class="itemDate">${pubDate}</div>` : ''}
                                ${description ? `<div class="itemDescription">${description}</div>` : ''}
                            </div>
                        `;
                    }
                }
                
                targetDiv.innerHTML = htmlContent;
            } else {
                targetDiv.innerHTML = '<div class="error">Impossibile caricare il feed RSS</div>';
            }
        })
        .catch(error => {
            console.error('Errore:', error);
            targetDiv.innerHTML = `<div class="error">Errore nel caricamento del feed: ${error.message}</div>`;
        });
}

// Carica tutti i feed quando la pagina è pronta
document.addEventListener("DOMContentLoaded", function() {
    // Definizione dei feed
    const feeds = [
        { id: 'divRssUltimissime', url: 'https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml' },
        { id: 'divRssPrincipali', url: 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it' },
        { id: 'divRssItalia', url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it' },
        { id: 'divRssEconomia', url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it' },
        { id: 'divRssMondo', url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it' },
        { id: 'divRssTecnologia', url: 'https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl=it&gl=IT&ceid=IT:it' },
        { id: 'divRssSalute', url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it' }
    ];
    
    // Carica ogni feed
    feeds.forEach(feed => {
        loadRSS(feed.url, feed.id);
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
});
</script>