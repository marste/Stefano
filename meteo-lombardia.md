---
layout: page
title: Meteo Lombardia
permalink: /meteo-lombardia/
image: 'https://marzorati.co/img/meteo.png'
share-img: 'https://marzorati.co/img/meteo.png'
---
<center>
<iframe src="https://astrogeo.va.it/meteo/widget/widget.php?colore=blu&temperatura=true" style="width:360px;height:495px; border:none"></iframe>
<br>


<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Previsioni Meteo Lombardia</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background-color: #0066cc;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
        .weather-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .weather-card {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .weather-card h3 {
            color: #0066cc;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .current-weather {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .current-weather .temp {
            font-size: 2.5em;
            font-weight: bold;
            margin-right: 20px;
        }
        .forecast-day {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px dashed #eee;
        }
        .forecast-day:last-child {
            border-bottom: none;
        }
        .alert {
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 4px;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 0.9em;
        }
        .weather-icon {
            width: 50px;
            height: 50px;
            vertical-align: middle;
        }
        .loading {
            text-align: center;
            padding: 20px;
            font-style: italic;
            color: #666;
        }
        .city-selector {
            margin: 15px 0;
            text-align: center;
        }
        select {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        @media (max-width: 768px) {
            .weather-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Previsioni Meteo Lombardia</h1>
        <p id="data-aggiornamento">Caricamento in corso...</p>
    </div>

    <div class="city-selector">
        <label for="city">Seleziona città: </label>
        <select id="city" onchange="caricaMeteo()">
            <option value="Milano">Milano</option>
            <option value="Brescia">Brescia</option>
            <option value="Bergamo">Bergamo</option>
            <option value="Como">Como</option>
            <option value="Cremona">Cremona</option>
            <option value="Lecco">Lecco</option>
            <option value="Lodi">Lodi</option>
            <option value="Mantova">Mantova</option>
            <option value="Monza">Monza</option>
            <option value="Pavia">Pavia</option>
            <option value="Sondrio">Sondrio</option>
            <option value="Varese">Varese</option>
        </select>
    </div>

    <div id="alert-meteo" class="alert" style="display: none;">
        <h3>Avviso Meteo</h3>
        <p id="testo-allerta">...</p>
    </div>

    <div class="weather-container">
        <div class="weather-card">
            <h3>Oggi</h3>
            <div id="meteo-oggi" class="loading">
                Caricamento dati meteo...
            </div>
        </div>

        <div class="weather-card">
            <h3>Domani</h3>
            <div id="meteo-domani" class="loading">
                Caricamento dati meteo...
            </div>
        </div>

        <div class="weather-card">
            <h3>Dopodomani</h3>
            <div id="meteo-dopodomani" class="loading">
                Caricamento dati meteo...
            </div>
        </div>
    </div>

    <div class="weather-card">
        <h3>Previsioni 7 giorni</h3>
        <div id="previsioni-settimana">
            <div class="loading">Caricamento previsioni settimanali...</div>
        </div>
    </div>

    <div class="footer">
        <p>Dati forniti da <a href="https://www.weatherapi.com/" target="_blank">WeatherAPI.com</a></p>
        <p id="ultimo-aggiornamento">Ultimo aggiornamento: --</p>
    </div>

    <script>
        // Configurazione API - Utilizza la tua API Key
        const API_KEY = '65513a3eb3ea4269946134346250204';
        
        // Funzione principale per caricare i dati meteo
        async function caricaMeteo() {
            const cittaSelezionata = document.getElementById('city').value;
            
            try {
                // Mostra lo stato di caricamento
                document.querySelectorAll('.loading').forEach(el => {
                    el.textContent = `Caricamento dati per ${cittaSelezionata}...`;
                });
                
                // Carica meteo corrente e previsioni
                const response = await fetch(`https://api.weatherapi.com/v1/forecast.json?key=${API_KEY}&q=${cittaSelezionata}&days=7&lang=it`);
                const data = await response.json();
                
                // Aggiorna la pagina con i dati
                aggiornaPagina(data);
                
            } catch (errore) {
                console.error("Errore nel caricamento meteo:", errore);
                document.querySelector('.loading').textContent = "Impossibile caricare i dati meteo. Riprova più tardi.";
            }
        }

        // Funzione per aggiornare la pagina con i dati meteo
        function aggiornaPagina(data) {
            const now = new Date();
            const location = data.location;
            const current = data.current;
            const forecast = data.forecast.forecastday;
            
            // Aggiorna intestazione
            document.getElementById('data-aggiornamento').textContent = 
                `Aggiornato: ${now.toLocaleDateString('it-IT', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}`;
            document.getElementById('ultimo-aggiornamento').textContent = 
                `Ultimo aggiornamento: ${now.toLocaleTimeString('it-IT')} - ${location.name}, ${location.region}`;
            
            // Aggiorna meteo corrente (oggi)
            document.getElementById('meteo-oggi').innerHTML = `
                <div class="current-weather">
                    <div class="temp">${Math.round(current.temp_c)}°C</div>
                    <div>
                        <img src="${current.condition.icon.replace('64x64', '128x128')}" class="weather-icon">
                        <p>${current.condition.text}</p>
                        <p>Umidità: ${current.humidity}%</p>
                        <p>Vento: ${current.wind_kph} km/h (${current.wind_dir})</p>
                        <p>Pressione: ${current.pressure_mb} hPa</p>
                    </div>
                </div>
                <p><strong>Temperature odierne:</strong> Min ${Math.round(forecast[0].day.mintemp_c)}°C - Max ${Math.round(forecast[0].day.maxtemp_c)}°C</p>
                <p><strong>Precipitazioni:</strong> ${forecast[0].day.totalprecip_mm} mm</p>
                <p><strong>Alba/Tramonto:</strong> ${forecast[0].astro.sunrise} / ${forecast[0].astro.sunset}</p>
            `;
            
            // Aggiorna meteo domani e dopodomani
            for (let i = 1; i <= 2; i++) {
                if (forecast[i]) {
                    const giorno = forecast[i];
                    const dataGiorno = new Date(giorno.date);
                    
                    document.getElementById(`meteo-domani${i === 1 ? '' : 'dopo'}`).innerHTML = `
                        <div class="current-weather">
                            <div class="temp">${Math.round(giorno.day.avgtemp_c)}°C</div>
                            <div>
                                <img src="${giorno.day.condition.icon.replace('64x64', '128x128')}" class="weather-icon">
                                <p>${giorno.day.condition.text}</p>
                            </div>
                        </div>
                        <p><strong>Data:</strong> ${dataGiorno.toLocaleDateString('it-IT', { weekday: 'long', day: 'numeric', month: 'long' })}</p>
                        <p><strong>Temperature:</strong> Min ${Math.round(giorno.day.mintemp_c)}°C - Max ${Math.round(giorno.day.maxtemp_c)}°C</p>
                        <p><strong>Precipitazioni:</strong> ${giorno.day.totalprecip_mm} mm</p>
                        <p><strong>Umidità:</strong> ${giorno.day.avghumidity}%</p>
                    `;
                }
            }
            
            // Aggiorna previsioni 7 giorni
            let previsioniHTML = '';
            forecast.forEach((giorno, index) => {
                const dataGiorno = new Date(giorno.date);
                
                previsioniHTML += `
                    <div class="forecast-day">
                        <div>
                            <strong>${index === 0 ? 'Oggi' : dataGiorno.toLocaleDateString('it-IT', { weekday: 'long' })}</strong>
                            <span>${dataGiorno.toLocaleDateString('it-IT', { day: 'numeric', month: 'short' })}</span>
                        </div>
                        <div style="display: flex; align-items: center;">
                            <img src="${giorno.day.condition.icon}" style="width: 30px; margin-right: 10px;">
                            <span>${Math.round(giorno.day.avgtemp_c)}°C</span>
                            <span style="margin: 0 10px; color: #888;">|</span>
                            <span>${Math.round(giorno.day.mintemp_c)}°C / ${Math.round(giorno.day.maxtemp_c)}°C</span>
                            <span style="margin-left: 10px; color: #0066cc; font-size: 0.9em;">${giorno.day.daily_chance_of_rain}% pioggia</span>
                        </div>
                    </div>
                `;
            });
            
            document.getElementById('previsioni-settimana').innerHTML = previsioniHTML;
            
            // Controlla se ci sono allerte meteo
            if (data.alerts && data.alerts.alert.length > 0) {
                document.getElementById('alert-meteo').style.display = 'block';
                document.getElementById('testo-allerta').innerHTML = 
                    `<strong>${data.alerts.alert[0].headline}</strong><br>${data.alerts.alert[0].desc}`;
            } else if (forecast.some(g => g.day.daily_will_it_rain === 1 || g.day.daily_will_it_snow === 1)) {
                document.getElementById('alert-meteo').style.display = 'block';
                const giorniPioggia = forecast.filter(g => g.day.daily_will_it_rain === 1).length;
                document.getElementById('testo-allerta').textContent = 
                    `Attenzione: sono previste precipitazioni in ${giorniPioggia} dei prossimi 7 giorni.`;
            } else {
                document.getElementById('alert-meteo').style.display = 'none';
            }
        }

        // Carica i dati meteo al caricamento della pagina
        document.addEventListener('DOMContentLoaded', caricaMeteo);
        
        // Aggiorna i dati ogni ora (3600000 ms)
        setInterval(caricaMeteo, 3600000);
    </script>
</body>


</center>