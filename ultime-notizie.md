---
layout: page
title: Ultime Notizie
permalink: /ultime-notizie/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<!-- Style per i pulsanti circolari -->
<style>
    .menu {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
    }
    .menu button {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: none;
        background-color: #007BFF;
        color: white;
        font-size: 20px;
        cursor: pointer;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        position: relative;
    }
    .menu button:hover {
        transform: translateY(-5px);
        box-shadow: 0px 8px 10px rgba(0, 0, 0, 0.3);
    }
    .tooltip {
        visibility: hidden;
        background-color: black;
        color: white;
        text-align: center;
        padding: 5px;
        border-radius: 5px;
        position: absolute;
        bottom: 60px;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
        white-space: nowrap;
    }
    .menu button:hover .tooltip {
        visibility: visible;
        opacity: 1;
    }
    .spinner {
        display: none;
        border: 4px solid rgba(0, 0, 0, 0.1);
        border-left-color: #007BFF;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
</style>

<body translate="no">

<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<!-- Menu con pulsanti circolari -->
<div class="menu">
    <button onclick="scrollToSection('Ultimissime')">
        <i class="fas fa-bolt"></i>
        <span class="tooltip">Ultim'ora</span>
    </button>
    <button onclick="scrollToSection('Principali')">
        <i class="fas fa-star"></i>
        <span class="tooltip">Principali</span>
    </button>
    <button onclick="scrollToSection('Italia')">
        <i class="fas fa-flag"></i>
        <span class="tooltip">Italia</span>
    </button>
    <button onclick="scrollToSection('Economia')">
        <i class="fas fa-chart-line"></i>
        <span class="tooltip">Economia</span>
    </button>
    <button onclick="scrollToSection('Mondo')">
        <i class="fas fa-globe"></i>
        <span class="tooltip">Mondo</span>
    </button>
    <button onclick="scrollToSection('Tecnologia')">
        <i class="fas fa-microchip"></i>
        <span class="tooltip">Tecnologia</span>
    </button>
    <button onclick="scrollToSection('Salute')">
        <i class="fas fa-heartbeat"></i>
        <span class="tooltip">Salute</span>
    </button>
</div>

<!-- Spinner di caricamento -->
<div class="spinner" id="spinner"></div>

<script>
    function scrollToSection(id) {
        document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
    }

    function loadFeeds() {
        $(".spinner").show();
        const feeds = [
            { id: "divRssUltimissime", url: "https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml" },
            { id: "divRssPrincipali", url: "https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it" },
            { id: "divRssItalia", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it" },
            { id: "divRssEconomia", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it" },
            { id: "divRssMondo", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it" },
            { id: "divRssTecnologia", url: "https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl=it&gl=IT&ceid=IT:it" },
            { id: "divRssSalute", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it" }
        ];

        let loaded = 0;
        feeds.forEach(feed => {
            $('#' + feed.id).load(feed.url, function () {
                loaded++;
                if (loaded === feeds.length) {
                    $(".spinner").hide();
                }
            });
        });
    }

    $(document).ready(function () {
        loadFeeds();
    });
</script>

<center><a name="Ultimissime"><font color="Black">Ultim'ora</font></a></center>
<div id="divRssUltimissime"></div>

<center><a name="Principali"><font color="Black">Principali</font></a></center>
<div id="divRssPrincipali"></div>

<center><a name="Italia"><font color="Black">Italia</font></a></center>
<div id="divRssItalia"></div>

<center><a name="Economia"><font color="Black">Economia</font></a></center>
<div id="divRssEconomia"></div>

<center><a name="Mondo"><font color="Black">Mondo</font></a></center>
<div id="divRssMondo"></div>

<center><a name="Tecnologia"><font color="Black">Tecnologia</font></a></center>
<div id="divRssTecnologia"></div>

<center><a name="Salute"><font color="Black">Salute</font></a></center>
<div id="divRssSalute"></div>

<script src="/js/jquery-3.6.0.min.js"></script>
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
</script>

</body>
