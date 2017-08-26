---
title: How to change MySQL root password on Windows
date: 2016-02-01 14:00:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /change-mysql-root-password-windows/
categories:
  - Windows
tags:
  - mysql
  - root
  - password
  - windows
  - user
  - commandline
---
Change directory to where you installed mysql to:   

	C:\> cd C:\mysql\bin

Switch to mysql command line:   

	C:\mysql\bin> mysql -u root mysql

Then set a default password:

    mysql> SET PASSWORD FOR root@localhost=PASSWORD('newpass');
  
where "newpass" is the password you want to use.

Then then add your new user:   

	mysql> CREATE USER 'stefano'@'localhost' IDENTIFIED BY 'mypass';
