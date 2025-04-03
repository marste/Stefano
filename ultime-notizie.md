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

/* Stile per menu tondo */
.round-menu {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 15px;
    margin: 20px 0;
    padding: 15px 0;
}

.round-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #008AFF;
    color: white;
    text-decoration: none;
    font-size: 24px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    position: relative;
}

.round-btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    background: #0066cc;
}

.round-btn .tooltip {
    position: absolute;
    bottom: -35px;
    left: 50%;
    transform: translateX(-50%);
    background: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 12px;
    opacity: 0;
    transition: opacity 0.3s;
    white-space: nowrap;
    pointer-events: none;
}

.round-btn:hover .tooltip {
    opacity: 1;
}

/* Style per RSS (invariato) */
.itemTitle a{font-weight:bold; font-size:20px; color:#008AFF; text-decoration:none;}
.itemTitle a:hover{ text-decoration:underline }
.itemDate{font-size:11px;color:#AAAAAA;}

/* Loading spinner */
.loading-spinner {
    border: 4px solid #f3f3f3;
    border-top: 4px solid #008AFF;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
    margin: 20px auto;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.error-message {
    color: #d9534f;
    text-align: center;
    padding: 20px;
}
</style>

<body translate="no">

<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<!-- Menu tondo -->
<div class="round-menu">
    <a href="#Ultimissime" class="round-btn" title="Ultim'ora">
        <i class="icon-bolt"></i>
        <span class="tooltip">Ultim'ora</span>
    </a>
    <a href="#Principali" class="round-btn" title="Principali">
        <i class="icon-star"></i>
        <span class="tooltip">Principali</span>
    </a>
    <a href="#Italia" class="round-btn" title="Italia">
        <i class="icon-flag"></i>
        <span class="tooltip">Italia</span>
    </a>
    <a href="#Economia" class="round-btn" title="Economia">
        <i class="icon-euro"></i>
        <span class="tooltip">Economia</span>
    </a>
    <a href="#Mondo" class="round-btn" title="Mondo">
        <i class="icon-globe"></i>
        <span class="tooltip">Mondo</span>
    </a>
    <a href="#Tecnologia" class="round-btn" title="Tecnologia">
        <i class="icon-laptop"></i>
        <span class="tooltip">Tecnologia</span>
    </a>
    <a href="#Salute" class="round-btn" title="Salute">
        <i class="icon-heart"></i>
        <span class="tooltip">Salute</span>
    </a>
</div>

<!-- Sezioni feed -->
<center><h1><a name="Ultimissime"><font color="Black">Ultim'ora</font></a></h1></center>
<div id="divRssUltimissime">
    <div class="loading-spinner"></div>
</div>

<center><h1><a name="Principali"><font color="Black">Principali</font></a></h1></center>
<div id="divRssPrincipali">
    <div class="loading-spinner"></div>
</div>

<center><h1><a name="Italia"><font color="Black">Italia</font></a></h1></center>
<div id="divRssItalia">
    <div class="loading-spinner"></div>
</div>

<center><h1><a name="Economia"><font color="Black">Economia</font></a></h1></center>
<div id="divRssEconomia">
    <div class="loading-spinner"></div>
</div>

<center><h1><a name="Mondo"><font color="Black">Mondo</font></a></h1></center>
<div id="divRssMondo">
    <div class="loading-spinner"></div>
</div>

<center><h1><a name="Tecnologia"><font color="Black">Tecnologia</font></a></h1></center>
<div id="divRssTecnologia">
    <div class="loading-spinner"></div>
</div>

<center><h1><a name="Salute"><font color="Black">Salute</font></a></h1></center>
<div id="divRssSalute">
    <div class="loading-spinner"></div>
</div>

<script src='/js/jquery-3.6.0.min.js'></script>
<script>
// Configurazione dei feed
const feeds = [
    { 
        id: 'divRssUltimissime',
        url: 'https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml',
        icon: 'icon-bolt'
    },
    { 
        id: 'divRssPrincipali',
        url: 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it',
        icon: 'icon-star'
    },
    { 
        id: 'divRssItalia',
        url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREYwYldRU0FtbHZMaWdBUAE?hl=it&gl=IT&ceid=IT%3Ait',
        icon: 'icon-flag'
    },
    { 
        id: 'divRssEconomia',
        url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbHZMaWdBUAE?hl=it&gl=IT&ceid=IT%3Ait',
        icon: 'icon-euro'
    },
    { 
        id: 'divRssMondo',
        url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbHZMaWdBUAE?hl=it&gl=IT&ceid=IT%3Ait',
        icon: 'icon-globe'
    },
    { 
        id: 'divRssTecnologia',
        url: 'https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSmxiaElDWlc0b0FBUAE?hl=it&gl=IT&ceid=IT%3Ait',
        icon: 'icon-laptop'
    },
    { 
        id: 'divRssSalute',
        url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbHZMaWdBUAE?hl=it&gl=IT&ceid=IT%3Ait',
        icon: 'icon-heart'
    }
];

// Funzione per caricare un feed RSS
async function loadFeed(feedConfig) {
    const container = document.getElementById(feedConfig.id);
    
    try {
        // Usiamo un proxy CORS per evitare problemi
        const proxyUrl = `https://api.allorigins.win/get?url=${encodeURIComponent(feedConfig.url)}`;
        const response = await fetch(proxyUrl);
        
        if (!response.ok) {
            throw new Error('Errore nel caricamento del feed');
        }
        
        const data = await response.json();
        
        if (data.contents) {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(data.contents, "text/xml");
            const items = xmlDoc.querySelectorAll("item");
            
            let htmlContent = '';
            const maxItems = 10;
            
            items.forEach((item, index) => {
                if (index >= maxItems) return;
                
                const title = item.querySelector("title")?.textContent || "Nessun titolo";
                const link = item.querySelector("link")?.textContent || "#";
                const pubDate = item.querySelector("pubDate") ? 
                    new Date(item.querySelector("pubDate").textContent).toLocaleDateString('it-IT') : '';
                const description = item.querySelector("description")?.textContent || '';
                
                htmlContent += `
                    <div class="rss-item">
                        <div class="itemTitle"><a href="${link}" target="_blank">${title}</a></div>
                        ${pubDate ? `<div class="itemDate">${pubDate}</div>` : ''}
                        ${description ? `<div class="itemDescription">${description}</div>` : ''}
                    </div>
                `;
            });
            
            container.innerHTML = htmlContent || '<div class="error-message">Nessuna notizia disponibile</div>';
        } else {
            throw new Error('Dati del feed non validi');
        }
    } catch (error) {
        console.error(`Errore nel caricamento del feed ${feedConfig.id}:`, error);
        container.innerHTML = `
            <div class="error-message">
                Errore nel caricamento delle notizie. 
                <a href="${feedConfig.url}" target="_blank">Prova ad aprire il feed direttamente</a>.
            </div>
        `;
    }
}

// Carica tutti i feed quando la pagina è pronta
document.addEventListener("DOMContentLoaded", function() {
    // Carica ogni feed
    feeds.forEach(feed => {
        loadFeed(feed);
    });
    
    // Smooth scroll per i pulsanti
    document.querySelectorAll('.round-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
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