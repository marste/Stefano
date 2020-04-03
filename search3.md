---
layout: page
title: Google
permalink: /search3/
image: 'https://marzorati.co/img/search.png'
---
<!--test -->
<center>
<div id="search-container">
<input type="text" id="search-input" class="form-control" placeholder="Search">
<br>
<b id="results-container"></b>
</div>
</center>
<!--test -->

<!-- Script pointing to search-script.js -->
<script src="/search-script.js" type="text/javascript"></script>

<!-- Configuration -->
<script>
SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  json: '/search.json',
  searchResultTemplate: '<div><a href="{url}"><h1>{title}</h1></a><span>{date}</span></div>'
})
</script>