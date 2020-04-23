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
	.feedEkList 
</style>

<div id="divRss"></div>
    
<script>
    $('#divRss').FeedEk({
    FeedUrl : 'https://www.wallstreetitalia.com/news/rss',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>

<div id="divRss1"></div>
<script>
    $('#divRss1').FeedEk({
    FeedUrl : 'https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YW1vU0FtbDBLQUFQAQ?hl%3Dit%26gl%3DIT%26ceid%3DIT%253Ait3DIT%2526ceid%253DIT%25253Ait',
    MaxCount : 10,
    ShowDesc : true,
    ShowPubDate:true,
    TitleLinkTarget:'_blank',
    DateFormat : 'dd/MM/yyyy',
    DateFormatLang : 'it'
  });
</script>