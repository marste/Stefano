---
title: "Apps Script per importare le quotazioni da Yahoo Finance in Google Sheets con aggiornamento automatico"
date: 2026-01-12 08:23:00 +0200
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
/*************************************************
 * FUNZIONI FINANZA – VERSIONE 12/01/2026
 *
 * =ULTIMO("SWDA.MI")
 * =VARGIORN("SWDA.MI")
 * =YTD("SWDA.MI")
 * =VARPER("SWDA.MI"; 30)
 * =MAXDATE("SWDA.MI"; "1y")
 * =MAXVAL("SWDA.MI"; "5y")
 * =MAXINFO("SWDA.MI"; "7y")
 * =FORZA_REFRESH()
 *************************************************/

function _fetchChart(ticker, range, interval) {
  const url =
    "https://query1.finance.yahoo.com/v8/finance/chart/" +
    encodeURIComponent(ticker) +
    "?range=" + range +
    "&interval=" + interval +
    "&includePrePost=false";

  const res = UrlFetchApp.fetch(url, {
    muteHttpExceptions: true,
    headers: { "User-Agent": "Mozilla/5.0" }
  });

  const json = JSON.parse(res.getContentText());
  return json?.chart?.result?.[0] || null;
}

/***********************
 * ULTIMO PREZZO
 ***********************/
function ULTIMO(ticker) {
  if (!ticker) return "Ticker?";
  const r = _fetchChart(ticker, "5d", "1d");
  const prices = r?.indicators?.quote?.[0]?.close;
  if (!prices) return "Dati non disponibili";

  for (let i = prices.length - 1; i >= 0; i--) {
    if (prices[i] != null) return Number(prices[i].toFixed(4));
  }
  return "No prezzi";
}

/***********************
 * VARIAZIONE GIORNALIERA %
 ***********************/
function VARGIORN(ticker) {
  if (!ticker) return "Ticker?";
  const r = _fetchChart(ticker, "5d", "1d");
  const p = r?.indicators?.quote?.[0]?.close;
  if (!p || p.length < 2) return "Dati incompleti";

  let last = null, prev = null;
  for (let i = p.length - 1; i >= 0; i--) {
    if (p[i] != null) {
      if (last === null) last = p[i];
      else { prev = p[i]; break; }
    }
  }
  if (last === null || prev === null) return "Dati incompleti";
  return Number((((last - prev) / prev) * 100).toFixed(2));
}

/***********************
 * VARIAZIONE YTD %
 ***********************/
function YTD(ticker) {
  if (!ticker) return "Ticker?";
  const r = _fetchChart(ticker, "ytd", "1d");
  const p = r?.indicators?.quote?.[0]?.close;
  if (!p) return "Dati incompleti";

  let first = null, last = null;
  for (let v of p) {
    if (v != null) {
      if (first === null) first = v;
      last = v;
    }
  }
  if (first === null || last === null) return "Dati incompleti";
  return Number((((last - first) / first) * 100).toFixed(2));
}

/***********************
 * VARIAZIONE % SU N GIORNI
 ***********************/
function VARPER(ticker, giorni) {
  if (!ticker) return "Ticker?";
  if (!giorni || giorni < 1) return "Periodo?";

  const range = Math.max(giorni + 5, 30) + "d";
  const r = _fetchChart(ticker, range, "1d");
  const p = r?.indicators?.quote?.[0]?.close;
  if (!p) return "Dati incompleti";

  const clean = p.filter(v => v != null);
  if (clean.length <= giorni) return "Dati incompleti";

  const last = clean[clean.length - 1];
  const past = clean[clean.length - 1 - giorni];
  return Number((((last - past) / past) * 100).toFixed(2));
}

/***********************
 * MAX VALORE DA DATA
 * Parametri: ticker, range obbligatorio, dataInizio opzionale
 ***********************/
function MAXVAL(ticker, range, dataInizio) {
  return _maxCore(ticker, dataInizio, "value", range);
}

/***********************
 * DATA DEL MASSIMO
 ***********************/
function MAXDATE(ticker, range, dataInizio) {
  return _maxCore(ticker, dataInizio, "date", range);
}

/***********************
 * MAX INFO
 ***********************/
function MAXINFO(ticker, range, dataInizio) {
  return _maxCore(ticker, dataInizio, "full", range);
}

/***********************
 * CORE MASSIMO
 ***********************/
function _maxCore(ticker, dataInizio, mode, range="1y") {
  if (!ticker || !range) return "Ticker o range mancante";
  const r = _fetchChart(ticker, range, "1d");
  if (!r) return "Errore Yahoo";

  const prices = r.indicators?.quote?.[0]?.close;
  const ts = r.timestamp;
  if (!prices || !ts) return "Dati incompleti";

  let startTs = 0;
  if (dataInizio) {
    const d = new Date(dataInizio);
    if (!isNaN(d.getTime())) startTs = Math.floor(d.getTime() / 1000);
  }

  let maxP = -Infinity, maxT = null;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] == null || ts[i] < startTs) continue;
    if (prices[i] > maxP) {
      maxP = prices[i];
      maxT = ts[i];
    }
  }
  if (maxT === null) return "No dati";

  const ultimo = ULTIMO(ticker);
  const drawdown = typeof ultimo === "number" ? Number((((ultimo - maxP) / maxP) * 100).toFixed(2)) : "—";

  const dataMax = Utilities.formatDate(new Date(maxT*1000), Session.getScriptTimeZone(), "dd/MM/yyyy");

  if (mode === "value") return Number(maxP.toFixed(4));
  if (mode === "date") return dataMax;

  return [
    ["Ticker", ticker],
    ["Prezzo attuale", ultimo],
    ["Var. oggi %", VARGIORN(ticker)],
    ["Massimo", Number(maxP.toFixed(4))],
    ["Data massimo", dataMax],
    ["Drawdown %", drawdown],
    ["YTD %", YTD(ticker)]
  ];
}

/***********************
 * FORZA REFRESH
 ***********************/
function FORZA_REFRESH() {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName("Refresh");
  if (!sh) {
    sh = ss.insertSheet("Refresh");
    sh.hideSheet();
  }
  sh.getRange("A1").setValue(new Date());
}

```

Ora, sempre da **Apps Script** andate sull'icona ad orologio **Attivatori**.   
- Scegliere la funzione da eseguire, selezionando: **FORZA_REFRESH**
- Selezionare l'origine dell'evento, selezionando: **Evento vincolato a specifiche temporali**
- Selezionare il tipo di attivatore basato sull'orario, selezionando: **Timer in minuti**
- Selezionare intervallo in minuti, selezionando: **Ogni 30 minuti**

Nel foglio, verrà creato in automatico un nuovo sheet che si chiamerà **Refresh** e nella cella A1 comparirà la data attuale che verrà refreshata ogni 30 minuti.   

Sarà poi sufficiente modificare la formula così:

```
=ULTIMO(SWDA.MI; Refresh!A1)
=VARGIORN(SWDA.MI; Refresh!A1)
```
