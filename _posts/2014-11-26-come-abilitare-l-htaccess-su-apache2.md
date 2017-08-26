---
id: 3174
title: 'Come abilitare l&#8217;.htaccess su Apache2'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3174
permalink: /come-abilitare-l-htaccess-su-apache2/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3265015266
categories:
  - Linux
tags:
  - apache
  - apache2
  - htaccess
  - ubuntu
---
Configurazione di esempio di Apache per abilitare l&#8217;htaccess

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%"><span style="color: #bb0066; font-weight: bold">&lt;Directory</span> <span style="color: #bb0066; font-weight: bold">/&gt;</span>
    Options FollowSymLinks
    AllowOverride None
<span style="color: #bb0066; font-weight: bold">&lt;/Directory&gt;</span>


<span style="color: #bb0066; font-weight: bold">&lt;Directory</span> <span style="color: #a61717; background-color: #e3d2d2">"/var/www/html"</span><span style="color: #bb0066; font-weight: bold">&gt;</span>


    Options FollowSymLinks
    AllowOverride All
    Order allow,deny
    Allow from all

<span style="color: #bb0066; font-weight: bold">&lt;/Directory&gt;</span>
</pre>
</div>