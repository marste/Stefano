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
<<<<<<< HEAD
=======
  noResultsText ('Non ho trovato nulla'),
>>>>>>> bb9fd1fa3f99c4522fb3d04865c6dd4c5f0ef3ce
  json: '/search.json'
})
</script>
