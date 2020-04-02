---
layout: page
title: Google
permalink: /cerca/
image: 'https://marzorati.co/img/search.png'
---

<!-- Html Elements for Search -->
<center>
<div id="search-container">
<input type="text" id="search-input" placeholder="search...">
<br>
<br>
<ul id="results-container"></ul>
</div>
</center>

<div id="search-container" class="form-control">
      <input type="text" id="search-input" class="btn btn-default" placeholder="Search" aria-label="Search">
	  <ul id="results-container"></ul>
</div>

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