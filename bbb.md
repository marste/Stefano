---
layout: page
title: Ultime Notizie
permalink: /bbb/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<style>
    .feedEkList{width:450px; list-style:none outside none;background-color:#FFFFFF; border:1px solid #D3CAD7; padding:4px 6px; color:#3E3E3E;}
    .feedEkList li{border-bottom:1px solid #D3CAD7; padding:5px;}
    .feedEkList li:last-child{border-bottom:none;}
    .itemTitle a{font-weight:bold; color:#4EBAFF !important; text-decoration:none }
    .itemTitle a:hover{ text-decoration:underline }
    .itemDate{font-size:11px;color:#AAAAAA;}
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