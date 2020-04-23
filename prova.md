---
layout: page
title: Ultime Notizie
permalink: /prova/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<script type="text/javascript" src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="FeedEk.min.js"></script>



				<div id="divRss5"></div>
				<strong>Code</strong>
<pre class="prettyprint">
$('#divRss5').FeedEk({
  FeedUrl:'https://jquery-plugins.net/rss',
  MaxCount: 2,
  DateFormat: 'D',
  DateFormatLang:'fr-FR'
});
</pre>