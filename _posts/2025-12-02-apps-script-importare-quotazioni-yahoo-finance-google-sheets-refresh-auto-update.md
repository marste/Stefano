---
title: "Apps Script per importare le quotazioni da Yahoo Finance in Google Sheets con aggiornamento automatico"
date: 2025-12-02 13:23:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/money.png'
share-img: 'https://marzorati.co/img/money.png'
layout: post
categories: [Financial]
tags: [sheets, importare, apps, script, quotazioni, yahoo, finance, google, sheets, reddit, aggiornamento, automatico]
---
- Se avete bisogno di importare le quotazioni dei vostri titoli azionari o ETF in Google Sheets in modo che si aggiornino automaticamente, potete usare l'apps script qua sotto.   
- Per farlo funzionare occorre semplicemente aprire un foglio di lavoro su <a href="https://docs.google.com/spreadsheets/" target="_blank">https://docs.google.com/spreadsheets/</a> e andare su **Estensioni** e **Apps Script**.   
- Cliccare sul **+** a fianco di **File** e selezionare **Script**.   
- Dare un titolo a piacere al file (non implica nulla sul funzionamento).   
- Elimina il contenuto già presente e incolla lo script che trovi qua di seguito.   
- Salva cliccando sull'icona del floppydisk o premi ctrl+s.  
- Ora torna nel tuo foglio di spreadsheets e utilizzando le varie funzioni di esempio, avrai il risultato voluto.   

```
/**
 * AUTO-REFRESH 2025
 * Funzioni Sheets:
 *  =ULTIMO("SWDA.MI")
 *  =VARGIORN("SWDA.MI")
 *  =YTD("SWDA.MI")
 *  =MAXVAL("SWDA.MI"; "2025-01-01")
 *  =MAXDATE("SWDA.MI"; "2025-01-01")
 *  =MAXINFO("SWDA.MI")
 *
 * Aggiornamento automatico:
 *  - il trigger chiama FORZA_REFRESH
 *  - Refresh!A1 cambia → forza il ricalcolo di tutte le funzioni
 */

////////////////////////////////////////////////////////////////////////////////
// -------------- MODULO AUTO REFRESH ----------------------------------------//
////////////////////////////////////////////////////////////////////////////////

/**
 * Crea o aggiorna il foglio Refresh, che forza il ricalcolo.
 * Da collegare a un trigger (es. ogni 5 minuti).
 */
function FORZA_REFRESH() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName("Refresh");
  if (!sh) sh = ss.insertSheet("Refresh");

  sh.getRange("A1").setValue(new Date()); // timestamp → ricalcolo globale
}

/**
 * Restituisce l'ultimo timestamp di refresh,
 * usato come parametro nascosto nelle funzioni.
 */
function _REF() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName("Refresh");
  if (!sh) return new Date();  // fallback
  return sh.getRange("A1").getValue();
}

////////////////////////////////////////////////////////////////////////////////
// -------------- FUNZIONI PRINCIPALI (con refresh invisibile) --------------//
////////////////////////////////////////////////////////////////////////////////

function ULTIMO(ticker, refresh = _REF()) {
  if (!ticker) return "Ticker?";
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}`;
  try {
    const json = JSON.parse(UrlFetchApp.fetch(url, {muteHttpExceptions: true}).getContentText());
    if (json.chart?.error) return "Errore";
    return Number(json.chart.result[0].meta.regularMarketPrice.toFixed(4));
  } catch (e) { return "—"; }
}

function VARGIORN(ticker, refresh = _REF()) {
  if (!ticker) return "Ticker?";
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}`;
  try {
    const json = JSON.parse(UrlFetchApp.fetch(url, {muteHttpExceptions: true}).getContentText());
    if (json.chart?.error) return "Errore";
    const meta = json.chart.result[0].meta;
    const cambio = meta.regularMarketPrice - meta.previousClose;
    const perc = (cambio / meta.previousClose) * 100;
    return Number(perc.toFixed(2));
  } catch (e) { return "—"; }
}

function YTD(ticker, refresh = _REF()) {
  if (!ticker) return "Ticker?";
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=ytd&interval=1d`;
  try {
    const json = JSON.parse(UrlFetchApp.fetch(url, {muteHttpExceptions: true}).getContentText());
    if (json.chart?.error) return "Errore";
    const result = json.chart.result[0];
    if (!result) return "No dati";

    let prices = result.indicators?.adjclose?.[0]?.adjclose || result.indicators?.quote?.[0]?.close || [];
    if (!prices || prices.length === 0) return "No prezzi";

    let primo = null, ultimo = null;
    for (let p of prices) {
      if (p !== null && p !== undefined) {
        if (primo === null) primo = p;
        ultimo = p;
      }
    }
    if (!primo || !ultimo) return "Dati incompleti";

    return Number((((ultimo - primo) / primo) * 100).toFixed(2));
  } catch (e) { return "Errore YTD: " + e.toString(); }
}

function MAXVAL(ticker, dataInizio = "", refresh = _REF()) { 
  return _getMaxInfo(ticker, dataInizio, "value");
}
function MAXDATE(ticker, dataInizio = "", refresh = _REF()) { 
  return _getMaxInfo(ticker, dataInizio, "date");
}
function MAXINFO(ticker, dataInizio = "", refresh = _REF()) { 
  return _getMaxInfo(ticker, dataInizio, "full");
}

////////////////////////////////////////////////////////////////////////////////
// -------------- FUNZIONE INTERNA MAX --------------------------------------//
////////////////////////////////////////////////////////////////////////////////

function _getMaxInfo(ticker, dataInizio, mode) {
  if (!ticker) return "Ticker?";
  const range = dataInizio ? "5y" : "max";
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=${range}&interval=1d`;

  try {
    const json = JSON.parse(UrlFetchApp.fetch(url, {muteHttpExceptions: true}).getContentText());
    if (json.chart?.error) return "Errore";

    const r = json.chart.result[0];
    const prices = r.indicators?.adjclose?.[0]?.adjclose || r.indicators?.quote?.[0]?.close;
    const ts = r.timestamp;

    const live = r.meta.regularMarketPrice;
    const prevClose = r.meta.previousClose;
    const cambioGiorno = live - prevClose;
    const percGiorno = ((cambioGiorno / prevClose) * 100).toFixed(2);

    let start = 0;
    if (dataInizio) {
      const d = (dataInizio instanceof Date) ? dataInizio : new Date(dataInizio);
      if (isNaN(d.getTime())) return "Data errata";
      start = Math.floor(d.getTime() / 1000);
    }

    let maxP = -Infinity, maxT = null;
    for (let i = 0; i < prices.length; i++) {
      if (prices[i] === null || ts[i] < start) continue;
      if (prices[i] > maxP) { maxP = prices[i]; maxT = ts[i]; }
    }
    if (maxT === null) return "No dati";

    const drawdown = ((live - maxP) / maxP * 100).toFixed(2);

    switch (mode) {
      case "value": 
        return Number(maxP.toFixed(4));
      case "date": 
        return new Date(maxT * 1000);
      case "full":
        return [
          ["Ticker", ticker],
          ["Prezzo attuale", live.toFixed(4)],
          ["Var. oggi", (cambioGiorno > 0 ? "+" : "") + cambioGiorno.toFixed(4) + " (" + percGiorno + "%)"],
          ["Massimo", maxP.toFixed(4)],
          ["Data massimo", Utilities.formatDate(new Date(maxT * 1000), Session.getScriptTimeZone(), "dd/MM/yyyy")],
          ["Drawdown", drawdown + "%"],
          ["YTD 2025", YTD(ticker) + "%"],
          ["Periodo", dataInizio ? "dal " + Utilities.formatDate(new Date(start * 1000), Session.getScriptTimeZone(), "dd/MM/yyyy") : "storico"]
        ];
    }
  } catch (e) { return "Errore"; }
}
```

Ora, sempre da **Apps Script** andate sull'icona ad orologio **Attivatori**.   
- Scegliere la funzione da eseguire, selezionando: **FORZA_REFRESH**
- Selezionare l'origine dell'evento, selezionando: **Evento vincolato a specifiche temporali**
- Selezionare il tipo di attivatore basato sull'orario, selezionando: **Timer in minuti**
- Selezionare intervallo in minuti, selezionando: **Ogni 5 minuti**

Nel foglio, verrà creato in automatico un nuovo sheet che si chiamerà **Refresh** e nella cella A1 comparirà la data attuale che verrà refreshata ogni 5 minuti.   

Sarà poi sufficiente modificare la formula così:

```
=ULTIMO(SWDA.MI; Refresh!A1)
=VARGIORN(SWDA.MI; Refresh!A1)
```

Trovate la mia pubblicazione anche su <a href="https://www.reddit.com/r/ItaliaPersonalFinance/comments/1p98nup/comment/nrd7yzm/" target="_blank">Reddit</a>