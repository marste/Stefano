---
title: "Apps Script per importare le quotazioni da Yahoo Finance in Google Sheets"
date: 2025-11-29 13:23:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/money.png'
share-img: 'https://marzorati.co/img/money.png'
layout: post
categories: [Financial]
tags: [spreadsheets, importare, apps, script, quotazioni, yahoo, finance, google, sheets, reddit]
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
 * SCRIPT DEFINITIVO – Tutto in uno (2025)
 * Funzioni disponibili in Google Sheets:
 *   =ULTIMO("SWDA.MI")           → prezzo attuale
 *   =VARGIORN("SWDA.MI")         → +1.24%  (variazione odierna)
 *   =YTD("SWDA.MI")              → +7.18
 *   =MAXVAL("SWDA.MI"; "2025-01-01")   → massimo da data
 *   =MAXDATE("SWDA.MI"; "2025-01-01")  → data massimo
 *   =MAXINFO("SWDA.MI")          → tabella completa
 */

function ULTIMO(ticker) {
  if (!ticker) return "Ticker?";
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}`;
  try {
    const json = JSON.parse(UrlFetchApp.fetch(url, {muteHttpExceptions: true}).getContentText());
    if (json.chart?.error) return "Errore";
    return Number(json.chart.result[0].meta.regularMarketPrice.toFixed(4));
  } catch (e) { return "—"; }
}

function VARGIORN(ticker) {
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

function YTD(ticker) {
  if (!ticker) return "Ticker?";
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?range=ytd&interval=1d`;
  try {
    const json = JSON.parse(UrlFetchApp.fetch(url, {muteHttpExceptions: true}).getContentText());
    if (json.chart?.error) return "Errore";
    const result = json.chart.result[0];
    if (!result) return "No dati";

    // Prova prima adjclose (aggiustati), fallback su quote.close
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

function MAXVAL(ticker, dataInizio = "") { return _getMaxInfo(ticker, dataInizio, "value"); }
function MAXDATE(ticker, dataInizio = "") { return _getMaxInfo(ticker, dataInizio, "date"); }
function MAXINFO(ticker, dataInizio = "") { return _getMaxInfo(ticker, dataInizio, "full"); }

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
      case "value": return Number(maxP.toFixed(4));
      case "date": return new Date(maxT * 1000);
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
