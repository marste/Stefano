---
title: Inserire del codice in un post Jekyll
subtitle: Utilizzare code snippet highlight
date: 2019-09-04 15:45:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/html.png'
share-img: 'https://marzorati.co/img/html.png'
layout: post
categories:
  - html
tags:
  - esempio
  - codice
  - html
  - embed
  - code
  - snippet
---
Accertarsi che nel file <code>_config.yml</code> sia presente la riga <code>highlighter: rouge</code>

Quando crei un nuovo post, basterà inserire il codice tra <code>&#123;&#37; highlight html &#37;&#125;</code> e <code>&#123;&#37; endhighlight &#37;&#125;</code> mettendo al posto di HTML il linguaggio inserito.   

I linguaggi previsti sono più di 185 e trovi la lista <a href="https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers" target="_blank">QUA</a>
