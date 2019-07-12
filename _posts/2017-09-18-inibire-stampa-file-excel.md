---
layout: post
title: Impedire la stampa di un file Excel
date: '2017-09-18 14:00:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/excel.png'
share-img: 'https://marzorati.co/img/excel.png'
categories:
  - Excel
tags:
  - stampa
  - print
  - vba
  - excel
  - impedire
published: true
---
Se non volete che il vostro lavoro in Excel venga stampato da utenti.

Premere ALT+F11 per aprire l’editor di codice.
Facciamo doppio clic su *"ThisWorkbook"* o *"Questa_cartella_di_lavoro"* per aprire la finestra dei comandi.

Dalla casella a cascata di sinistra selezioniamo *"Workbook"* e da quella a destra scegliamo il comando *"BeforePrint"*.

Fra la stringa

	Private Sub Workbook_BeforePrint(Cancel As Boolean)

e la stringa

	End Sub

incolliamo il seguente codice:

	Cancel = True
	MsgBox "Non puoi stampare questo file", vbInformation

Salviamo il codice e torniamo in Excel. Se proviamo a lanciare una stampa, una finestra di pop-up reciterà: *"Non puoi stampare questo file".*