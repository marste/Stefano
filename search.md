---
layout: page
title: Cosa stai cercando?
permalink: /search/
image: 'https://marzorati.co/img/google.png'
---
<!-- Search Form -->
<center>
<div id="search-container">
<input type="text" id="search-input" class="form-control" placeholder="Search">
<br>
<b id="results-container"></b>
</div>
</center>
<!-- Search Form -->

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