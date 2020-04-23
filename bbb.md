---
layout: page
title: Ultime Notizie
permalink: /bbb/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<style>
    .itemTitle a{font-weight:bold; font-size:18px; color:#008AFF; text-decoration:none }
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:11px;color:#AAAAAA;}
</style>

<center><a href="#Italia">Italia</a> - <a href="#Affari">Affari</a> - <a href="#Mondo">Mondo</a> - <a href="#Tecnologia">Tecnologia</a> - <a href="#Salute">Salute</a> - <a href="#WallStreet">Wall Street Italia</a> - <a href="https://lab24.ilsole24ore.com/coronavirus/" target="_blank">Covid-19</a></center>   


<center><h1><a name="Italia"><font color="Black">Italia</font></a></h1></center>
<div id="divRssItalia"></div>
<script>
    $('#divRssItalia').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait3DIT%2526ceid%253DIT%25253Ait',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<center><h1><a name="Affari"><font color="Black">Affari</font></a></h1></center>
<div id="divRssAffari"></div>
<script>
    $('#divRssAffari').FeedEk({
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

<center><h1><a name="WallStreet"><font color="Black">Wall Street Italia</font></a></h1></center>
<div id="divRssWS"></div>
<script>
    $('#divRssWS').FeedEk({
    FeedUrl : 'https://www.wallstreetitalia.com/news/rss',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

