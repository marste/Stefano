---
title: "Apps Script per importare le quotazioni da Yahoo Finance in Google Sheets con aggiornamento automatico"
date: 2026-04-02 08:23:00 +0200
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

Ho aggiunto che 

```
/*************************************************
 * FUNZIONI FINANZA – VERSIONE CORRETTA - Cluade 02/04/2026
 *
 * Correzioni rispetto alla versione 13/03/2026:
 * - VARGIORN: usa meta.chartPreviousClose (o previousClose) direttamente
 *   dai meta della chiamata live, evitando l'euristica sulle daily bars
 *   che causava il calcolo errato del prevClose.
 * - _getPrevCloseFromDailyBars: riscritta per preferire chartPreviousClose
 *   dai meta invece della logica con tolleranza 0.3% (troppo stretta).
 *
 * =ULTIMO("SWDA.MI")
 * =VARGIORN("SWDA.MI")
 * =YTD("SWDA.MI")
 * =VARPER("SWDA.MI"; 30)
 * =MAXDATE("SWDA.MI"; "1y")
 * =MAXVAL("SWDA.MI"; "5y")
 * =MAXINFO("SWDA.MI"; "7y")
 * =MINVAL("SWDA.MI"; "6mo")
 * =MINDATE("SWDA.MI"; "1y")
 * =MININFO("SWDA.MI"; "3y")
 * =CAMBIO("EURUSD")
 * =CAMBIO_PCT("EURUSD")
 * =DEBUG_TICKER("SWDA.MI")
 * =FORZA_REFRESH()
 *************************************************/

function _normTicker(t) {
  return String(t || "").trim();
}

function _roundByHint(x, hint) {
  if (x == null || isNaN(x)) return null;
  const d = (hint != null && !isNaN(hint)) ? Math.max(0, Math.min(8, Number(hint))) : 4;
  return Number(Number(x).toFixed(d));
}

function _fetchChart(ticker, range, interval) {
  const t = _normTicker(ticker);
  const cb = Date.now();
  const url =
    "https://query1.finance.yahoo.com/v8/finance/chart/" +
    encodeURIComponent(t) +
    "?range=" + encodeURIComponent(range) +
    "&interval=" + encodeURIComponent(interval) +
    "&includePrePost=false" +
    "&_cb=" + cb;

  const res = UrlFetchApp.fetch(url, {
    muteHttpExceptions: true,
    headers: { "User-Agent": "Mozilla/5.0", "Accept": "application/json" }
  });

  let json;
  try { json = JSON.parse(res.getContentText()); } catch (e) { return null; }
  return json?.chart?.result?.[0] || null;
}

function _lastNonNull(arr) {
  if (!arr || !arr.length) return null;
  for (let i = arr.length - 1; i >= 0; i--) {
    const v = arr[i];
    if (v != null && !isNaN(v)) return v;
  }
  return null;
}

function _lastTwoNonNull(arr) {
  if (!arr || !arr.length) return { last: null, prev: null };
  let last = null, prev = null;
  for (let i = arr.length - 1; i >= 0; i--) {
    const v = arr[i];
    if (v == null || isNaN(v)) continue;
    if (last === null) last = v;
    else { prev = v; break; }
  }
  return { last, prev };
}

/***********************
 * LIVE LAST: usa meta.regularMarketPrice da 1d/5m (fallback 1d/1m, poi 5d/1d)
 ***********************/
function _getLiveLast(ticker) {
  const t = _normTicker(ticker);
  const tries = [
    { range: "1d", interval: "5m",  label: "1d/5m" },
    { range: "1d", interval: "1m",  label: "1d/1m" },
    { range: "5d", interval: "1d",  label: "5d/1d" }
  ];

  for (const tr of tries) {
    const r = _fetchChart(t, tr.range, tr.interval);
    if (!r) continue;

    const m = r.meta || {};
    const hint = m.priceHint;

    // Last preferito: meta.regularMarketPrice
    let last = (m.regularMarketPrice != null && !isNaN(m.regularMarketPrice))
      ? Number(m.regularMarketPrice)
      : null;

    // Fallback: ultimo close della serie
    if (last == null) {
      const lastClose = _lastNonNull(r?.indicators?.quote?.[0]?.close);
      if (lastClose != null) last = Number(lastClose);
    }

    if (last != null) {
      return {
        last,
        priceHint: hint,
        intervalUsed: tr.label,
        meta: m
      };
    }
  }

  return { last: null, priceHint: null, intervalUsed: null, meta: null };
}

/***********************
 * PREV CLOSE ROBUSTO
 *
 * CORREZIONE: la vecchia logica usava una tolleranza dello 0,3% per capire
 * se dailyLast fosse il close di oggi o di ieri — troppo stretta in mercati
 * mossi, causando il pick del ramo sbagliato e quindi una variazione errata.
 *
 * Nuova logica:
 * 1. Usa meta.chartPreviousClose (o meta.previousClose) dalla chiamata 5d/1d:
 *    Yahoo lo popola con il close ufficiale di ieri, senza ambiguità.
 * 2. Fallback: penultimo close dalle barre giornaliere.
 ***********************/
function _getPrevCloseFromDailyBars(ticker, liveLast) {
  const t = _normTicker(ticker);

  const r = _fetchChart(t, "5d", "1d");
  if (!r) return { prevClose: null, dailyLast: null, dailyPrev: null };

  const m = r.meta || {};

  // --- PRIMA SCELTA: chartPreviousClose / previousClose dai meta ---
  // Questi campi contengono direttamente il close ufficiale del giorno precedente.
  const metaPrev =
    (m.chartPreviousClose != null && !isNaN(m.chartPreviousClose)) ? Number(m.chartPreviousClose) :
    (m.previousClose     != null && !isNaN(m.previousClose))      ? Number(m.previousClose)      :
    null;

  if (metaPrev != null) {
    const closes = r?.indicators?.quote?.[0]?.close;
    const two = _lastTwoNonNull(closes);
    return {
      prevClose: metaPrev,
      dailyLast: two.last != null ? Number(two.last) : null,
      dailyPrev: two.prev != null ? Number(two.prev) : null
    };
  }

  // --- FALLBACK: penultimo close dalle barre giornaliere ---
  const closes = r?.indicators?.quote?.[0]?.close;
  const two = _lastTwoNonNull(closes);
  return {
    prevClose: two.prev != null ? Number(two.prev) : null,
    dailyLast: two.last != null ? Number(two.last) : null,
    dailyPrev: two.prev != null ? Number(two.prev) : null
  };
}

/***********************
 * ULTIMO PREZZO
 ***********************/
function ULTIMO(ticker) {
  const t = _normTicker(ticker);
  if (!t) return "Ticker?";

  const live = _getLiveLast(t);
  if (live.last == null) return "Dati non disponibili";

  return _roundByHint(live.last, live.priceHint);
}

/***********************
 * VARIAZIONE GIORNALIERA %
 *
 * CORREZIONE: usa direttamente meta.chartPreviousClose (o previousClose)
 * già presente nella risposta di _getLiveLast, senza passare per
 * _getPrevCloseFromDailyBars e la sua logica di tolleranza difettosa.
 * _getPrevCloseFromDailyBars viene usata solo come fallback se i meta
 * non contengono il prevClose.
 ***********************/
function VARGIORN(ticker) {
  const t = _normTicker(ticker);
  if (!t) return "Ticker?";

  const live = _getLiveLast(t);
  if (live.last == null) return "Dati incompleti";

  const m = live.meta || {};

  // Prova prima a leggere il prevClose direttamente dai meta della chiamata live
  let prev =
    (m.chartPreviousClose != null && !isNaN(m.chartPreviousClose)) ? Number(m.chartPreviousClose) :
    (m.previousClose      != null && !isNaN(m.previousClose))      ? Number(m.previousClose)      :
    null;

  // Se i meta non lo hanno (raro), fallback a daily bars
  if (prev == null) {
    const prevObj = _getPrevCloseFromDailyBars(t, live.last);
    prev = prevObj.prevClose;
  }

  if (prev == null || isNaN(prev) || Number(prev) === 0) return "Dati incompleti";

  return Number((((Number(live.last) - prev) / prev) * 100).toFixed(2));
}

/***********************
 * YTD % (storico close giornaliero)
 ***********************/
function YTD(ticker) {
  const t = _normTicker(ticker);
  if (!t) return "Ticker?";

  const r = _fetchChart(t, "ytd", "1d");
  if (!r) return "Errore Yahoo";

  const p = r?.indicators?.quote?.[0]?.close;
  if (!p) return "Dati incompleti";

  let first = null, last = null;
  for (let v of p) {
    if (v != null && !isNaN(v)) {
      if (first === null) first = v;
      last = v;
    }
  }

  if (first === null || last === null || Number(first) === 0) return "Dati incompleti";
  return Number((((Number(last) - Number(first)) / Number(first)) * 100).toFixed(2));
}

/***********************
 * VARPER % su N giorni (storico close)
 ***********************/
function VARPER(ticker, giorni) {
  const t = _normTicker(ticker);
  if (!t) return "Ticker?";
  if (!giorni || giorni < 1) return "Periodo?";

  const range = Math.max(giorni + 5, 30) + "d";
  const r = _fetchChart(t, range, "1d");
  if (!r) return "Errore Yahoo";

  const p = r?.indicators?.quote?.[0]?.close;
  if (!p) return "Dati incompleti";

  const clean = p.filter(v => v != null && !isNaN(v));
  if (clean.length <= giorni) return "Dati incompleti";

  const last = clean[clean.length - 1];
  const past = clean[clean.length - 1 - giorni];
  if (Number(past) === 0) return "Dati incompleti";

  return Number((((Number(last) - Number(past)) / Number(past)) * 100).toFixed(2));
}

/***********************
 * MAX helpers (storico)
 ***********************/
function MAXVAL(ticker, range, dataInizio)  { return _maxCore(ticker, dataInizio, "value", range); }
function MAXDATE(ticker, range, dataInizio) { return _maxCore(ticker, dataInizio, "date",  range); }
function MAXINFO(ticker, range, dataInizio) { return _maxCore(ticker, dataInizio, "full",  range); }

function _maxCore(ticker, dataInizio, mode, range = "1y") {
  const t = _normTicker(ticker);
  if (!t || !range) return "Ticker o range mancante";

  const r = _fetchChart(t, range, "1d");
  if (!r) return "Errore Yahoo";

  const prices = r?.indicators?.quote?.[0]?.close;
  const ts = r?.timestamp;
  if (!prices || !ts) return "Dati incompleti";

  let startTs = 0;
  if (dataInizio) {
    const d = new Date(dataInizio);
    if (!isNaN(d.getTime())) startTs = Math.floor(d.getTime() / 1000);
  }

  let maxP = -Infinity, maxT = null;
  for (let i = 0; i < prices.length; i++) {
    const v = prices[i];
    if (v == null || isNaN(v)) continue;
    if (ts[i] < startTs) continue;
    if (v > maxP) { maxP = v; maxT = ts[i]; }
  }

  if (maxT === null || maxP === -Infinity) return "No dati";

  const ultimo = ULTIMO(t);
  const drawdown =
    (typeof ultimo === "number" && Number(maxP) !== 0)
      ? Number((((Number(ultimo) - Number(maxP)) / Number(maxP)) * 100).toFixed(2))
      : "—";

  const dataMax = Utilities.formatDate(new Date(maxT * 1000), Session.getScriptTimeZone(), "dd/MM/yyyy");

  if (mode === "value") return _roundByHint(maxP, 4);
  if (mode === "date")  return dataMax;

  return [
    ["Ticker",         t],
    ["Prezzo attuale", ultimo],
    ["Var. oggi %",    VARGIORN(t)],
    ["Massimo",        _roundByHint(maxP, 4)],
    ["Data massimo",   dataMax],
    ["Drawdown %",     drawdown],
    ["YTD %",          YTD(t)]
  ];
}

/***********************
 * MIN helpers (storico)
 ***********************/
function MINVAL(ticker, range)  { return _minCore(ticker, range, "value"); }
function MINDATE(ticker, range) { return _minCore(ticker, range, "date");  }
function MININFO(ticker, range) { return _minCore(ticker, range, "full");  }

function _minCore(ticker, range, mode) {
  if (!ticker) return "Ticker?";
  if (!range)  range = "1y";

  const r = _fetchChart(ticker, range, "1d");
  if (!r) return "Errore Yahoo";

  const prices = r?.indicators?.quote?.[0]?.close;
  const ts     = r?.timestamp;
  if (!prices || !ts) return "Dati incompleti";

  let minP = Infinity, minT = null;
  for (let i = 0; i < prices.length; i++) {
    const px = prices[i];
    if (px == null || isNaN(px)) continue;
    if (px < minP) { minP = px; minT = ts[i]; }
  }

  if (minT === null) return "No dati";

  const ultimo = ULTIMO(ticker);
  const rebound = (typeof ultimo === "number")
    ? Number((((ultimo - minP) / minP) * 100).toFixed(2))
    : "—";

  const dataMin = Utilities.formatDate(
    new Date(minT * 1000),
    Session.getScriptTimeZone(),
    "dd/MM/yyyy"
  );

  if (mode === "value") return Number(minP.toFixed(4));
  if (mode === "date")  return dataMin;

  return [
    ["Ticker",              ticker],
    ["Prezzo attuale",      ultimo],
    ["Var. oggi %",         VARGIORN(ticker)],
    ["Minimo (" + range + ")", Number(minP.toFixed(4))],
    ["Data minimo",         dataMin],
    ["Rimbalzo %",          rebound],
    ["YTD %",               YTD(ticker)]
  ];
}

/***********************
 * CAMBIO VALUTA (via CHART - stabile)
 *
 * =CAMBIO("EURUSD")
 * =CAMBIO("USDEUR")
 * =CAMBIO("EURUSD"; 6)
 ***********************/
function CAMBIO(pair, decimals) {
  if (!pair) return "Pair?";

  const ticker = pair.toUpperCase() + "=X";
  const r = _fetchChart(ticker, "1d", "5m");
  if (!r) return "Errore Yahoo";

  const price = r?.meta?.regularMarketPrice;
  if (price == null) return "No dati";

  const dec = (decimals != null && !isNaN(decimals)) ? Number(decimals) : 4;
  return Number(Number(price).toFixed(dec));
}

/***********************
 * VARIAZIONE % CAMBIO
 *
 * =CAMBIO_PCT("EURUSD")
 ***********************/
function CAMBIO_PCT(pair, decimals) {
  if (!pair) return "Pair?";

  const ticker = pair.toUpperCase() + "=X";
  const r = _fetchChart(ticker, "1d", "5m");
  if (!r) return "Errore Yahoo";

  const last = r?.meta?.regularMarketPrice;
  const prev = r?.meta?.previousClose ?? r?.meta?.chartPreviousClose ?? null;

  if (last == null || prev == null || prev === 0) return "Dati incompleti";

  const pct = ((last - prev) / prev) * 100;
  const dec = (decimals != null && !isNaN(decimals)) ? Number(decimals) : 2;
  return Number(pct.toFixed(dec));
}

/***********************
 * DEBUG_TICKER
 * Mostra tutti i valori chiave per diagnosticare discrepanze
 ***********************/
function DEBUG_TICKER(ticker) {
  const t = _normTicker(ticker);
  if (!t) return "Ticker?";

  const live    = _getLiveLast(t);
  const prevObj = _getPrevCloseFromDailyBars(t, live.last);
  const m       = live.meta || {};

  const metaPrev =
    (m.chartPreviousClose != null && !isNaN(m.chartPreviousClose)) ? Number(m.chartPreviousClose) :
    (m.previousClose      != null && !isNaN(m.previousClose))      ? Number(m.previousClose)      :
    null;

  // Il prevClose effettivamente usato da VARGIORN (meta > daily fallback)
  const prevUsedByVargiorn = metaPrev ?? prevObj.prevClose;

  return [
    ["Ticker",                          t],
    ["LIVE intervalUsed",               live.intervalUsed],
    ["LIVE regularMarketPrice",         m.regularMarketPrice],
    ["META chartPreviousClose",         m.chartPreviousClose],
    ["META previousClose",              m.previousClose],
    ["META prev usato (VARGIORN)",      prevUsedByVargiorn],
    ["DAILY lastClose",                 prevObj.dailyLast],
    ["DAILY prevClose (fallback)",      prevObj.dailyPrev],
    ["VARGIORN calcolato",              VARGIORN(t)],
    ["PRICEHINT",                       live.priceHint]
  ];
}

/***********************
 * TRIGGER CONTROLLATO
 * (Ogni ora precisa, 09:00 - 18:00, LUN-VEN)
 ***********************/
function TRIGGER_PROGRAMMATO() {
  const dataAttuale    = new Date();
  const oraAttuale     = dataAttuale.getHours();
  const giornoSettimana = dataAttuale.getDay(); // 0=Dom, 1=Lun, ..., 6=Sab

  if (giornoSettimana >= 1 && giornoSettimana <= 5 && oraAttuale >= 9 && oraAttuale <= 18) {
    FORZA_REFRESH();
    console.log("Refresh eseguito alle ore: " + oraAttuale + ":00");
  } else {
    console.log("Fascia oraria o giorno non attivi. Ora attuale: " + oraAttuale);
  }
}

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

 Ora, sempre da Apps Script andate sull'icona ad orologio Attivatori.

- Scegliere la funzione da eseguire, selezionando: **TRIGGER_PROGRAMMATO**
- Selezionare l'origine dell'evento, selezionando: Evento vincolato a specifiche temporali
- Selezionare il tipo di attivatore basato sull'orario, selezionando: Timer in minuti
- Selezionare intervallo in minuti, selezionando: Ogni 30 minuti

Nel foglio, verrà creato in automatico un nuovo sheet che si chiamerà Refresh e nella cella A1 comparirà la data attuale che verrà refreshata ogni 30 minuti dalle ore 09:00 alle ore 18:00 dal lunedì al venerdì.   