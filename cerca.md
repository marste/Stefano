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

<!--test -->
 <form>
 <div id="search-container">
  <div class="input-group">
    <input type="text" id="search-input" class="form-control" placeholder="Search">
    <div class="input-group-btn">
      <button class="btn btn-default" type="submit">
        <i class="glyphicon glyphicon-search"></i>
      </button>
    </div>
  </div>
</form>
<ul id="results-container"></ul>
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