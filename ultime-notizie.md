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

<!-- Style per RSS -->
<style>
    .itemTitle a{font-weight:bold; font-size:20px; color:#008AFF; text-decoration:none;}
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:11px;color:#AAAAAA;}
</style>
<!-- Style per RSS -->

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jFeed/0.0.1/jFeed.min.js"></script>

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

## <center><a name="Ultimissime">Ultim'ora</a></center>
<br>
<div id="divRssUltimissime"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://www.servizitelevideo.rai.it/televideo/pub/rss101.xml',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssUltimissime').html(html);
        }
    });
});
</script>

## <center><a name="Principali">Principali</a></center>
<br>
<div id="divRssPrincipali"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssPrincipali').html(html);
        }
    });
});
</script>

## <center><a name="Italia">Italia</a></center>
<br>
<div id="divRssItalia"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait3DIT%2526ceid%253DIT%25253Ait',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssItalia').html(html);
        }
    });
});
</script>

## <center><a name="Economia">Economia</a></center>
<br>
<div id="divRssEconomia"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssEconomia').html(html);
        }
    });
});
</script>

## <center><a name="Mondo">Mondo</a></center>
<br>
<div id="divRssMondo"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssMondo').html(html);
        }
    });
});
</script>

## <center><a name="Tecnologia">Tecnologia</a></center>
<br>
<div id="divRssTecnologia"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssTecnologia').html(html);
        }
    });
});
</script>

## <center><a name="Salute">Salute</a></center>
<br>
<div id="divRssSalute"></div>
<script>
$(document).ready(function() {
    $.getFeed({
        url: 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
        success: function(feed) {
            let html = '<ul>';
            for(let i=0; i<10 && i<feed.items.length; i++) {
                let item = feed.items[i];
                html += `
                    <li>
                        <div class="itemTitle">
                            <a href="${item.link}" target="_blank">${item.title}</a>
                        </div>
                        <div class="itemDate">${new Date(item.updated).toLocaleDateString('it-IT')}</div>
                        <div>${item.description}</div>
                    </li>
                    <br>
                `;
            }
            html += '</ul>';
            $('#divRssSalute').html(html);
        }
    });
});
</script>

<script>
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