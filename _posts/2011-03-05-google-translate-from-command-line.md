---
id: 105
title: Google translate from command line
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/google-translate-from-command-line
permalink: /google-translate-from-command-line/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 7882929811163347562
  - 7882929811163347562
  - 7882929811163347562
dsq_thread_id:
  - 2642893200
categories:
  - Linux
tags:
  - google
---
Save this in ~/bin/translate

<code style="white-space:nowrap;">&lt;code>&lt;span style="color:#000000;">&lt;span style="color:#ff8000;">#!/usr/bin/env python&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">from urllib2 import urlopen&lt;br />
from urllib import urlencode&lt;br />
import sys&lt;/span>&lt;/span></code></code>

<code style="white-space:nowrap;">&lt;code>&lt;span style="color:#ff8000;"># The google translate API can be found here:&lt;br />
# http://code.google.com/apis/ajaxlanguage/documentation/#Examples&lt;/span>&lt;/p>
&lt;p></code></code>

<code style="white-space:nowrap;">&lt;code>&lt;span style="color:#0000bb;">lang1&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">sys&lt;/span>&lt;span style="color:#007700;">.&lt;/span>&lt;span style="color:#0000bb;">argv&lt;/span>&lt;span style="color:#007700;">[&lt;/span>&lt;span style="color:#0000bb;">1&lt;/span>&lt;span style="color:#007700;">]
&lt;/span>&lt;span style="color:#0000bb;">lang2&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">sys&lt;/span>&lt;span style="color:#007700;">.&lt;/span>&lt;span style="color:#0000bb;">argv&lt;/span>&lt;span style="color:#007700;">[&lt;/span>&lt;span style="color:#0000bb;">2&lt;/span>&lt;span style="color:#007700;">]
&lt;/span>&lt;span style="color:#0000bb;">langpair&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#dd0000;">'%s|%s'&lt;/span>&lt;span style="color:#007700;">%(&lt;/span>&lt;span style="color:#0000bb;">lang1&lt;/span>&lt;span style="color:#007700;">,&lt;/span>&lt;span style="color:#0000bb;">lang2&lt;/span>&lt;span style="color:#007700;">)&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">text&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#dd0000;">' '&lt;/span>&lt;span style="color:#007700;">.&lt;/span>&lt;span style="color:#0000bb;">join&lt;/span>&lt;span style="color:#007700;">(&lt;/span>&lt;span style="color:#0000bb;">sys&lt;/span>&lt;span style="color:#007700;">.&lt;/span>&lt;span style="color:#0000bb;">argv&lt;/span>&lt;span style="color:#007700;">[&lt;/span>&lt;span style="color:#0000bb;">3&lt;/span>&lt;span style="color:#007700;">:])&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">base_url&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#dd0000;">'http://ajax.googleapis.com/ajax/services/language/translate?'&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">params&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">urlencode&lt;/span>&lt;span style="color:#007700;">( ((&lt;/span>&lt;span style="color:#dd0000;">'v'&lt;/span>&lt;span style="color:#007700;">,&lt;/span>&lt;span style="color:#0000bb;">1.0&lt;/span>&lt;span style="color:#007700;">),&lt;br />
(&lt;/span>&lt;span style="color:#dd0000;">'q'&lt;/span>&lt;span style="color:#007700;">,&lt;/span>&lt;span style="color:#0000bb;">text&lt;/span>&lt;span style="color:#007700;">),&lt;br />
(&lt;/span>&lt;span style="color:#dd0000;">'langpair'&lt;/span>&lt;span style="color:#007700;">,&lt;/span>&lt;span style="color:#0000bb;">langpair&lt;/span>&lt;span style="color:#007700;">),) )&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">url&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">base_url&lt;/span>&lt;span style="color:#007700;">+&lt;/span>&lt;span style="color:#0000bb;">params&lt;br />
content&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">urlopen&lt;/span>&lt;span style="color:#007700;">(&lt;/span>&lt;span style="color:#0000bb;">url&lt;/span>&lt;span style="color:#007700;">).&lt;/span>&lt;span style="color:#0000bb;">read&lt;/span>&lt;span style="color:#007700;">()&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">start_idx&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">content&lt;/span>&lt;span style="color:#007700;">.&lt;/span>&lt;span style="color:#0000bb;">find&lt;/span>&lt;span style="color:#007700;">(&lt;/span>&lt;span style="color:#dd0000;">'"translatedText":"'&lt;/span>&lt;span style="color:#007700;">)+&lt;/span>&lt;span style="color:#0000bb;">18&lt;br />
translation&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">content&lt;/span>&lt;span style="color:#007700;">[&lt;/span>&lt;span style="color:#0000bb;">start_idx&lt;/span>&lt;span style="color:#007700;">:]
&lt;/span>&lt;span style="color:#0000bb;">end_idx&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">translation&lt;/span>&lt;span style="color:#007700;">.&lt;/span>&lt;span style="color:#0000bb;">find&lt;/span>&lt;span style="color:#007700;">(&lt;/span>&lt;span style="color:#dd0000;">'"}, "'&lt;/span>&lt;span style="color:#007700;">)&lt;br />
&lt;/span>&lt;span style="color:#0000bb;">translation&lt;/span>&lt;span style="color:#007700;">=&lt;/span>&lt;span style="color:#0000bb;">translation&lt;/span>&lt;span style="color:#007700;">[:&lt;/span>&lt;span style="color:#0000bb;">end_idx&lt;/span>&lt;span style="color:#007700;">]
print &lt;/span>&lt;span style="color:#0000bb;">translation &lt;/span></code></code>