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
</style>
<!-- Style per bottone top -->


<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aggregatore di Notizie</title>
    <style>
        :root {
            --primary-color: #000000; /* Nero invece del rosso Rai */
            --text-color: #333;
            --light-gray: #f5f5f5;
            --medium-gray: #e0e0e0;
            --dark-gray: #757575;
            --font-main: 'Segoe UI', Roboto, -apple-system, sans-serif;
        }
        
        body {
            font-family: var(--font-main);
            line-height: 1.6;
            color: var(--text-color);
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 1px solid var(--medium-gray);
            padding-bottom: 20px;
        }
        
        h1 {
            color: var(--primary-color);
            font-weight: 300;
            font-size: 2.2rem;
            margin-bottom: 5px;
        }
        
        .subtitle {
            color: var(--dark-gray);
            font-size: 0.9rem;
        }
        
        .nav-menu {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--medium-gray);
        }
        
        .nav-button {
            padding: 8px 15px;
            background-color: white;
            border: 1px solid var(--medium-gray);
            border-radius: 20px;
            color: var(--text-color);
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }
        
        .nav-button:hover, .nav-button.active {
            background-color: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }
        
        .news-container {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }
        
        .news-item {
            border-bottom: 1px solid var(--medium-gray);
            padding-bottom: 20px;
            transition: transform 0.2s ease;
        }
        
        .news-item:hover {
            transform: translateX(5px);
        }
        
        .news-title {
            font-size: 1.1rem;
            margin-bottom: 8px;
            color: var(--primary-color);
        }
        
        .news-date {
            font-size: 0.8rem;
            color: var(--dark-gray);
            margin-bottom: 10px;
            display: block;
        }
        
        .news-description {
            font-size: 0.95rem;
            margin-bottom: 10px;
        }
        
        .news-link {
            display: inline-block;
            font-size: 0.85rem;
            color: var(--primary-color);
            text-decoration: none;
            border: 1px solid var(--primary-color);
            padding: 5px 10px;
            border-radius: 3px;
            transition: all 0.2s ease;
        }
        
        .news-link:hover {
            background-color: var(--primary-color);
            color: white;
        }
        
        .source-title {
            margin-top: 40px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--primary-color);
            color: var(--primary-color);
            font-weight: 500;
        }
        
        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid var(--medium-gray);
            font-size: 0.8rem;
            color: var(--dark-gray);
        }
        
        .loading {
            text-align: center;
            padding: 20px;
            color: var(--dark-gray);
        }
        
        @media (max-width: 600px) {
            body {
                padding: 15px;
            }
            
            h1 {
                font-size: 1.8rem;
            }
            
            .nav-menu {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Aggregatore di Notizie</h1>
        <p class="subtitle">Tutte le ultime notizie in un unico posto</p>
    </header>
    
    <div class="nav-menu" id="nav-menu">
        <!-- I pulsanti di navigazione verranno generati qui -->
    </div>
    
    <div id="content-container">
        <!-- Il contenuto dei feed verrà caricato qui -->
        <div class="loading">Seleziona una fonte dal menu in alto</div>
    </div>
    
    <footer>
        Aggregatore di notizie - Contenuti aggiornati automaticamente da varie fonti
    </footer>

    <script>
        // Configurazione dei feed RSS
        const feeds = [
            {
                id: 'rai-televideo',
                title: 'Rai Televideo',
                url: 'https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml'
            },
            {
                id: 'google-news-italia',
                title: 'Google News Italia',
                url: 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it'
            },
            {
                id: 'google-top-news',
                title: 'Google Top News',
                url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait3DIT%2526ceid%253DIT%25253Ait'
            },
            {
                id: 'google-politica',
                title: 'Google Politica',
                url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait'
            },
            {
                id: 'google-economia',
                title: 'Google Economia',
                url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait'
            },
            {
                id: 'google-tecnologia',
                title: 'Google Tecnologia',
                url: 'https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait'
            },
            {
                id: 'google-sport',
                title: 'Google Sport',
                url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait'
            }
        ];

        document.addEventListener('DOMContentLoaded', function() {
            const navMenu = document.getElementById('nav-menu');
            const contentContainer = document.getElementById('content-container');
            
            // Genera i pulsanti di navigazione
            feeds.forEach(feed => {
                const button = document.createElement('button');
                button.className = 'nav-button';
                button.textContent = feed.title;
                button.dataset.feedId = feed.id;
                
                button.addEventListener('click', () => {
                    // Rimuovi la classe active da tutti i pulsanti
                    document.querySelectorAll('.nav-button').forEach(btn => {
                        btn.classList.remove('active');
                    });
                    
                    // Aggiungi la classe active al pulsante cliccato
                    button.classList.add('active');
                    
                    // Carica il feed selezionato
                    loadFeed(feed);
                });
                
                navMenu.appendChild(button);
            });
            
            // Carica il primo feed per default
            if (feeds.length > 0) {
                document.querySelector('.nav-button').click();
            }
        });
        
        function loadFeed(feed) {
            const contentContainer = document.getElementById('content-container');
            contentContainer.innerHTML = `<div class="loading">Caricamento in corso...</div>`;
            
            // Usiamo un proxy CORS per evitare problemi di same-origin policy
            const proxyUrl = 'https://api.allorigins.win/get?url=' + encodeURIComponent(feed.url);
            
            fetch(proxyUrl)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Errore nel caricamento dei dati');
                    }
                    return response.json();
                })
                .then(data => {
                    const parser = new DOMParser();
                    const xmlDoc = parser.parseFromString(data.contents, "text/xml");
                    
                    const items = xmlDoc.querySelectorAll('item');
                    if (items.length === 0) {
                        contentContainer.innerHTML = `<p>Nessuna notizia disponibile al momento per ${feed.title}.</p>`;
                        return;
                    }
                    
                    let htmlContent = `<h2 class="source-title">${feed.title}</h2>`;
                    htmlContent += `<div class="news-container" id="news-container">`;
                    
                    items.forEach(item => {
                        const title = item.querySelector('title')?.textContent || 'Nessun titolo';
                        const description = item.querySelector('description')?.textContent || '';
                        const link = item.querySelector('link')?.textContent || '#';
                        const pubDate = item.querySelector('pubDate')?.textContent || '';
                        
                        const dateObj = new Date(pubDate);
                        const formattedDate = dateObj.toLocaleDateString('it-IT', {
                            day: '2-digit',
                            month: '2-digit',
                            year: 'numeric',
                            hour: '2-digit',
                            minute: '2-digit'
                        });
                        
                        htmlContent += `
                            <div class="news-item">
                                <h3 class="news-title">${title}</h3>
                                <span class="news-date">${formattedDate}</span>
                                <p class="news-description">${description}</p>
                                <a href="${link}" class="news-link" target="_blank" rel="noopener">Leggi di più</a>
                            </div>
                        `;
                    });
                    
                    htmlContent += `</div>`;
                    contentContainer.innerHTML = htmlContent;
                })
                .catch(error => {
                    console.error('Errore:', error);
                    contentContainer.innerHTML = `<p>Impossibile caricare le notizie da ${feed.title}. Si prega di riprovare più tardi.</p>`;
                });
        }
    </script>
</body>
</html>


<!-- <script src="https://cpwebassets.codepen.io/assets/common/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js"></script> -->
<script src="/js/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js"></script>
<script src='/js/jquery-3.6.0.min.js'></script>
<script id="rendered-js">
// ===== Scroll to Top ==== 
$(window).scroll(function () {
  if ($(this).scrollTop() >= 50) {// If page is scrolled more than 50px
    $('#return-to-top').fadeIn(200); // Fade in the arrow
  } else {
    $('#return-to-top').fadeOut(200); // Else fade out the arrow
  }
});
$('#return-to-top').click(function () {// When arrow is clicked
  $('body,html').animate({
    scrollTop: 0 // Scroll to top of body
  }, 500);
});
//# sourceURL=pen.js
    </script>