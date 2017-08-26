---
id: 1875
title: Popolazione mondiale
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1875
permalink: /popolazione-mondiale/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:1;}}'
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2822610496
categories:
  - Linux
  - Varie
tags:
  - mondiale
  - popolazione
---
`curl -s http://www.census.gov/popclock/data/population/world | awk -F'[:,]' '{print $7}'`