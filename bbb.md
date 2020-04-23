---
layout: page
title: Ultime Notizie
permalink: /bbb/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
<script src='FeedEk.min.js'></script>

<div id="divRss"></div>
    
<script>
    $('#divRss').FeedEk({
    FeedUrl : 'https://jquery-plugins.net/rss',
    MaxCount : 5,
    ShowDesc : true,
    ShowPubDate:true,
    DescCharacterLimit:100,
    TitleLinkTarget:'_blank',
    DateFormat : 'MM/dd/yyyy',
    DateFormatLang : 'en'
  });
</script>