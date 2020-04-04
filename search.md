---
layout: page
title: Google
permalink: /search/
image: 'https://marzorati.co/img/search.png'
---
<!--test -->
<center>
<div id="search-container">
<div class="md-form mt-0">
<input type="text" id="search-input" class="form-control" placeholder="Search" aria-label="Search">
</div>
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
  json: '/search.json'
  
})
</script>