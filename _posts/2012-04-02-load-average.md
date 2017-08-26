---
id: 1151
title: Load Average
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1151
permalink: /load-average/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"186825781127806977";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"186825781127806977";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2061011451
categories:
  - Linux
tags:
  - average
  - load
  - loadaverage
---
Un **load average** maggiore di 1 indica che c&#8217;è almeno un processo che sta attendendo il proprio turno di esecuzione senza avere spazio per essere eseguito subito.

Le tre cifre indicano la media dell&#8217;ultimo minuto, negli ultimi 5 minuti e negli ultimi 15 minuti, dando così anche un&#8217;idea del trend che si sta avendo.

In generale la **&#8220;situazione ideale&#8221;** e&#8217; quella in cui il *** load average* rimane sempre al di sotto di 1*numero di cpu**, anche se in realtà non è per nulla difficile trovare situazioni in cui il *load average* è ben più alto.

Picchi sporadici anche di *load* alto non sono mai un problema, un *load* costantemente alto ( la definizione di alto dipende da molteplici fattori, a seconda delle situazioni può essere alto un *load* di 2, in altre puoi considerare alto un *load* di 15&#8230; ) invece determina un problema di carico sulla cpu eccessivo.

Un *load* eccessivo determina un calo notevole delle prestazioni della macchina, fino a renderla anche non responsiva ai comandi in shell o determinarne dei semi blocchi.

/me che in vita sua ha visto macchine con un load di > 700 reggere ( su sparc64 ) e macchine morire a < di 30 ( su x86 )

<a href="http://goo.gl/v0762" target="_blank">via</a>