---
id: 86
title: Uninstall programmi installati da sorgenti
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/uninstall-programmi-installati-da-sorgenti
permalink: /uninstall-programmi-installati-da-sorgenti/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8318000017530741048
  - 8318000017530741048
  - 8318000017530741048
dsq_thread_id:
  - 2201162930
categories:
  - Linux
tags:
  - remove
---
&#8230;Ma in questo caso avendo installato con **make-install**, senza quindi nemmeno **checkinstall**, addio tracce di tutti i file installati. Quindi questa guida serve soprattutto a me, giusto per ricordarmi che quando faccio qualche test è sempre meglio avere una lista di quello che faccio. Per tenere traccia dei file ci sono due metodi:

<p style="text-align:justify;">
  <strong>Primo metodo:</strong>
</p>

> <p style="text-align:justify;">
>   <code># &lt;span style="color:#0000ff;">make uninstall&lt;/span></code>
> </p>

<p style="text-align:justify;">
  ma trovare un tarball che include questo è quasi come vincere al superenalotto
</p>

<p style="text-align:justify;">
  <strong>Secondo metodo:</strong>
</p>

<p style="text-align:justify;">
  prendere nota di tutti i file installati:
</p>

> <p style="text-align:justify;">
>   <code># &lt;span style="color:#0000ff;">find /* &gt; pacchetti.prima&lt;/span></code>
> </p>

<p style="text-align:justify;">
  a questo punto eseguire il <strong>make-install</strong>
</p>

<p style="text-align:justify;">
  quindi prendere nota di tutti i file dopo l&#8217;installazione:
</p>

> <p style="text-align:justify;">
>   <code># &lt;span style="color:#0000ff;">find /* &gt; pacchetti.dopo&lt;/span></code>
> </p>

<p style="text-align:justify;">
  ottenere le differenze tra i due file usando <strong>diff</strong>:
</p>

> <p style="text-align:justify;">
>   <code># &lt;span style="color:#0000ff;">diff pacchetti.prima pacchetti.dopo &gt; uninstall&lt;/span></code>
> </p>

<p style="text-align:justify;">
  iniziare la rimozione:
</p>

> <p style="text-align:justify;">
>   <code># &lt;span style="color:#0000ff;">for i in $(grep "&gt;" uninstall | awk '{ print $2 }')&lt;/span></code>
> </p>
> 
> <p style="text-align:justify;">
>   <span style="color:#0000ff;"><code>do</code></span>
> </p>
> 
> <p style="text-align:justify;">
>   <span style="color:#0000ff;"><code>/bin/rm -fi $i;</code></span>
> </p>
> 
> <p style="text-align:justify;">
>   <span style="color:#0000ff;"><code>done</code></span>
> </p>

<p style="text-align:justify;">
  a questo punto compariranno a video i file da disinstallare, e basta scrivere <strong>yes</strong>.
</p>

<p style="text-align:justify;">
  &nbsp;
</p>

<p style="text-align:justify;">
  <a href="http://www.edmondweblog.com/index.php/2010/11/11/uninstall-programmi-installati-da-sorgenti/">via</a>
</p>