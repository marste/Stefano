---
layout: page
title: Ultime Notizie
permalink: /prova/
image: 'https://marzorati.co/img/news.png'
share-img: 'https://marzorati.co/img/news.png'
---
<script type="text/javascript" src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="FeedEk.min.js"></script>

<script type="text/javascript">
		$(function () {
			$('#divRss').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2
			});

			$('#divRss2').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 3, ShowDesc: true, ShowPubDate: false, DescCharacterLimit: 100
			});
			$('#divRss3').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 4, ShowDesc: false
			});

			$('#divRss4').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2, DateFormat: 'd', DateFormatLang: 'en'
			});

			$('#divRss5').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2, DateFormat: 'D', DateFormatLang: 'fr-FR'
			});
			$('#divRss6').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2, DateFormat: 'f', DateFormatLang: 'en'
			});

			$('#divRss10').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2, DateFormat: 'MM-dd-yyyy HH:mm', DateFormatLang: 'en'
			});
			$('#divRss11').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2, DateFormat: 'dd MMMM yyyy', DateFormatLang: 'en'
			});
			$('#divRss12').FeedEk({
				FeedUrl: 'https://jquery-plugins.net/rss', MaxCount: 2, DateFormat: 'MM/dd/yyyy'
			});


			prettyPrint();
			$.ajax({ type: "POST", url: '/Home/PluginVisitAdd', data: { pluginId: 1 } });
		});

	</script>


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