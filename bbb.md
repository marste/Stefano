---
layout: page
title: Ultime Notizie
permalink: /bbb/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<style>
    .itemTitle a{font-weight:bold; font-size:18px; color:#4EBAFF !important; text-decoration:none }
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:11px;color:#AAAAAA;}
	.feedEkList 
</style>

<div id="divRss"></div>
    
<script>
    $('#divRss').FeedEk({
    FeedUrl : 'https://www.wallstreetitalia.com/news/rss',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    DescCharacterLimit:300,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>