---
title: Disabilitare il Portachiavi su Ubuntu
subtitle: 'Basta con i noiosi popup di richiesta password'
date: 2019-08-12 14:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
bigimg:
  - "https://www.wordsmart.it/wp-content/uploads/2019/03/come-installare-Ubuntu.jpg" : "Ubuntu"
categories:
  - Linux
tags:
  - disable
  - keyring
  - portachiavi
  - ubuntu
  - seahorse
---
Lancia il comando **<code>seahorse</code>**, se non è presente il programma installalo con il comando:   

	sudo apt-get install seahorse

1) Fare clic con il tasto destro su **Login** e selezionare **Cambia password**.
Right-click on **Login** and select **Change Password**.

2) Inserisci la vecchia password quando vedi il pop-up. Quindi lascia vuoto il campo della nuova password e fai clic su **Continua**   
Enter the old password when you see the pop-up. Then leave the new password field blank. Don’t enter even space. Click **Continue**   

3) Apparirà un ovvio messaggio pop-up che le password non saranno crittografate. Fai clic su **Continua**   
You should see an obvious warning pop-up that passwords will be unencrypted. Click **Continue**   

4) Questo è tutto! Riavvia il computer per rendere effettive le impostazioni. La prossima volta che avvii il browser Chrome o Chromium, o altri programmi non dovresti visualizzare la richiesta di portachiavi.   
That’s it! Restart your computer for the setting to take effect. Next time you launch Chrome or Chromium browser, you should not see keyring request.