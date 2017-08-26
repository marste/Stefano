---
id: 78
title: Vedere i vari logs su Linux
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/vedere-i-vari-logs
permalink: /vedere-i-vari-logs-linux/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 4580668920804155133
  - 4580668920804155133
  - 4580668920804155133
dsq_thread_id:
  - 2188043187
categories:
  - Linux
tags:
  - log
---
=> **/var/log/messages** : General log messages

=> **/var/log/boot** : System boot log

=> **/var/log/debug** : Debugging log messages

=> **/var/log/auth.log** : User login and authentication logs

=> **/var/log/daemon.log** : Running services such as squid, ntpd and others log message to this file

=> **/var/log/dmesg** : Linux kernel ring buffer log

=> **/var/log/dpkg.log** : All binary package log includes package installation and other information

=> **/var/log/faillog** : User failed login log file

=> **/var/log/kern.log** : Kernel log file

=> **/var/log/lpr.log** : Printer log file

=> **/var/log/mail.*** : All mail server message log files

=> **/var/log/mysql.*** : MySQL server log file

=> **/var/log/user.log** : All userlevel logs

=> **/var/log/xorg.0.log** : X.org log file

=> **/var/log/apache2/*** : Apache web server log files directory

=> **/var/log/lighttpd/*** : Lighttpd web server log files directory

=> **/var/log/fsck/*** : fsck command log

=> **/var/log/apport.log** : Application crash report / log file

###Comandi da terminal:   

	tail -f /var/log/apport.log   
	more /var/log/xorg.0.log   
	cat /var/log/mysql.err   
	less /var/log/messages   
	grep -i fail /var/log/boot