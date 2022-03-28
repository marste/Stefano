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
<!-- Style per bottone top -->
<!-- Style per RSS -->
<style>
    .itemTitle a{font-weight:bold; font-size:18px; color:#008AFF; text-decoration:none }
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:11px;color:#AAAAAA;}
</style>
<!-- Style per RSS -->

<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>

<body translate="no">

<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>

<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">



<center><a href="#Ultimissime">Ultim'ora</a> - <a href="#Principali">Principali</a> - <a href="#Italia">Italia</a> - <a href="#Economia">Economia</a> - <a href="#Mondo">Mondo</a> - <a href="#Tecnologia">Tecnologia</a> - <a href="#Salute">Salute</a> - <a href="https://www.money.it/Guerra-Ucraina-Russia-cosa-succede-oggi-ultime-notizie-diretta" target="_blank">Guerra in Ucraina</a></center>   

<a href="https://www.money.it/Guerra-Ucraina-Russia-cosa-succede-oggi-ultime-notizie-diretta" target="_blank">Guerra in Ucraina</a>

<center><h1><a name="Ultimissime"><font color="Black">Ultim'ora</font></a></h1></center>
<div id="divRssUltimissime"></div>
<script>
    $('#divRssUltimissime').FeedEk({
    FeedUrl : 'https://www.televideo.rai.it/televideo/pub/rss101.xml',
    MaxCount : 10,
	ShowPubDate:true,
    ShowDesc : true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Principali"><font color="Black">Principali</font></a></h1></center>
<div id="divRssPrincipali"></div>
<script>
    $('#divRssPrincipali').FeedEk({
    FeedUrl : 'https://news.google.com/rss?hl=it&gl=IT&ceid=IT:it',
    MaxCount : 10,
	ShowPubDate:true,
    ShowDesc : true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Italia"><font color="Black">Italia</font></a></h1></center>
<div id="divRssItalia"></div>
<script>
    $('#divRssItalia').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait3DIT%2526ceid%253DIT%25253Ait',
    MaxCount : 10,
	ShowPubDate:true,
    ShowDesc : true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Economia"><font color="Black">Economia</font></a></h1></center>
<div id="divRssEconomia"></div>
<script>
    $('#divRssEconomia').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtbDBHZ0pKVkNnQVAB?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Mondo"><font color="Black">Mondo</font></a></h1></center>
<div id="divRssMondo"></div>
<script>
    $('#divRssMondo').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtbDBHZ0pKVkNnQVAB?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Tecnologia"><font color="Black">Tecnologia</font></a></h1></center>
<div id="divRssTecnologia"></div>
<script>
    $('#divRssTecnologia').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnBkQm9DU1ZRb0FBUAE?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Salute"><font color="Black">Salute</font></a></h1></center>
<div id="divRssSalute"></div>
<script>
    $('#divRssSalute').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>




<!-- <script src="https://cpwebassets.codepen.io/assets/common/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js"></script> -->
<script src="/js/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js"></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
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