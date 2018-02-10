---
layout: post
title: SSH for host has been enabled
date: '2018-02-10 16:00:00 +0200'
author: Stefano Marzorati
published: true
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/3c0416b4-96d5-11e6-a559-00163ed833e7/2256818653/vmware-workstation-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/3c0416b4-96d5-11e6-a559-00163ed833e7/2256818653/vmware-workstation-logo.png'
categories:
  - Windows
tags:
  - vmware
  - ssh
  - host
  - warning
  - enabled
  - disabled
  - vcenter
---
To disable SSH and warning using vSphere Web Client:

From the vSphere Web Client, select vCenter from the Home menu.
Select Hosts and Clusters under the Inventory Trees.
Expand the tree in the left pane of the vSphere Web Client.
**Click the ESXi host with the yellow exclamation** and click the **Configuration** tab.
Click on **Security Profile** nella sezione Software.
In **Services** click **Properties**.
Trova il servizio **SSH** e stoppalo.