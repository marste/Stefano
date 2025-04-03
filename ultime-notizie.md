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
</style>

<!-- Modern Menu Style -->
<style>
    .menu {
        text-align: center;
        padding: 10px;
        background: #333;
    }
    .menu a {
        color: white;
        text-decoration: none;
        padding: 10px 15px;
        font-size: 16px;
        display: inline-block;
    }
    .menu a:hover {
        background: #555;
        border-radius: 5px;
    }
</style>

<body>
<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>
<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">

<div class="menu">
    <a href="#Ultimissime">Ultim'ora</a>
    <a href="#Principali">Principali</a>
    <a href="#Italia">Italia</a>
    <a href="#Economia">Economia</a>
    <a href="#Mondo">Mondo</a>
    <a href="#Tecnologia">Tecnologia</a>
    <a href="#Salute">Salute</a>
</div>

<div id="rss-feeds"></div>

<script>
const feeds = [
    { id: "Ultimissime", title: "Ultim'ora", url: "https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml" },
    { id: "Principali", title: "Principali", url: "https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it" },
    { id: "Italia", title: "Italia", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it" },
    { id: "Economia", title: "Economia", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it" },
    { id: "Mondo", title: "Mondo", url: "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl=it&gl=IT&ceid=IT:it" },
    { id: "Tecnologia", title: "Tecnologia", url: "https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl=it&gl=IT&ceid=IT:it" },
    { id: "Salute", title: "Salute", url: "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl=it&gl=IT&ceid=IT:it" }
];

function loadRSS() {
    feeds.forEach(feed => {
        fetch(`https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(feed.url)}`)
            .then(response => response.json())
            .then(data => {
                let content = `<center><h1><a name="${feed.id}">${feed.title}</a></h1></center>`;
                content += '<div class="rss-container">';
                data.items.slice(0, 10).forEach(item => {
                    content += `<div class='item'><p class='itemTitle'><a href='${item.link}' target='_blank'>${item.title}</a></p>`;
                    content += `<p class='itemDate'>${new Date(item.pubDate).toLocaleDateString('it-IT')}</p></div>`;
                });
                content += '</div>';
                document.getElementById('rss-feeds').innerHTML += content;
            });
    });
}

document.addEventListener("DOMContentLoaded", loadRSS);
</script>

<script src='/js/jquery-3.6.0.min.js'></script>
<script>
$(window).scroll(function () {
  if ($(this).scrollTop() >= 50) {
    $('#return-to-top').fadeIn(200);
  } else {
    $('#return-to-top').fadeOut(200);
  }
});
$('#return-to-top').click(function () {
  $('body,html').animate({ scrollTop: 0 }, 500);
});
</script>
</body>
