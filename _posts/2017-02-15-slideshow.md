---
title: Slideshow
date: 2017-02-15 11:42:00 +0200
author: Stefano Marzorati
layout: slide
theme: black
transition: slide
published: false
permalink: /slideshow/
categories:
  - Fun
tags:
  - sempre
  - qualcuno
  - prezzo
  - basso
---
<section data-markdown>
# How to use reveal.js in Jekyll

by [Luu Gia Thuy](http://luugiathuy.com) / [@luugiathuy](http://twitter.com/luugiathuy)

April 6, 2015
</section>

<section data-markdown>
## Overview

[reveal.js](https://github.com/hakimel/reveal.js/) enables you to create
beautiful interactive slide decks using HTML. This presentation will show you
how to integrate it with [Jekyll](http://jekyllrb.com/)
</section>

<section data-markdown>
## reveal.js

Clone reveal.js to your site's root folder:

```
git clone https://github.com/hakimel/reveal.js.git
```

Or, add it as your site's submodule:

```
git submodule add https://github.com/hakimel/reveal.js.git
```
</section>

<section data-markdown>
## Slide Layout

Create a layout file, call `slide.html` in `_layouts` folder. And use this gist
for the content of the file https://gist.github.com/luugiathuy/c07ac5608addadb642e5.

</section>

<section data-markdown>
## Slide

Now, in your page/post YAML front matter, use `slide` for the layout. You can
define *title*, *author*, *description* as well as the slide's *theme* and
*transition*:

```yaml
---
layout: slide
title: Jekyll&#58; Make presentation page with reveal.js
description: A presentation slide for how to use reveal.js in Jekyll
theme: black
transition: slide
---
```
</section>

<section data-markdown>
## Slide

Each slide is enclosed in a `&lt;section&gt;` tag:

```html
&lt;section data-markdown&gt;
## Overview

[reveal.js](https://github.com/hakimel/reveal.js/) enables you to create
beautiful interactive slide decks using HTML. This presentation will show you
how to integrate it with [Jekyll](http://jekyllrb.com/)
&lt;/section&gt;
```

</section>

<section data-markdown>

<<<<<<< HEAD
## THE END
=======
# THE END
>>>>>>> 0eebdfaad9117c4c3836beaa06705a2496f37480

</section>