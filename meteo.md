---
layout: page
title: Meteo Rescaldina
permalink: /meteo/
image: 'https://marzorati.co/img/meteo.png'
share-img: 'https://marzorati.co/img/meteo.png'
---
<center>

<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Previsioni Meteo Rescaldina</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: #ffffff;
            padding: 10px;
        }
        
        .weather-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .weather-card {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            border: 1px solid #e9ecef;
        }
        
        .day {
            font-size: 1rem;
            font-weight: 600;
            color: #495057;
            margin-bottom: 5px;
        }
        
        .date {
            font-size: 0.8rem;
            color: #868e96;
            margin-bottom: 10px;
        }
        
        .weather-icon {
            font-size: 1.8rem;
            margin-bottom: 10px;
            color: #4a6bdf;
        }
        
        .temp {
            font-size: 1.4rem;
            font-weight: bold;
            color: #212529;
            margin-bottom: 5px;
        }
        
        .temp span {
            opacity: 0.7;
            font-weight: normal;
        }
        
        .description {
            font-size: 0.8rem;
            color: #495057;
            margin-bottom: 8px;
            text-transform: capitalize;
        }
        
        .details {
            font-size: 0.75rem;
            color: #868e96;
            display: flex;
            justify-content: space-around;
        }
        
        .details i {
            margin-right: 3px;
            color: #4a6bdf;
        }
        
        @media (max-width: 768px) {
            .weather-cards {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        @media (max-width: 480px) {
            .weather-cards {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="weather-cards" id="weather-cards">
        <div style="text-align: center; grid-column: 1/-1; padding: 20px;">
            <i class="fas fa-spinner fa-spin"></i> Caricamento...
        </div>
    </div>

    <script>
        // API Config
        const API_KEY = "ApnIbUcAvKoThDuZIgrogmWjOnZRSVHu";
        const LOCATION = "45.6206,8.9526";  // Coordinate di Rescaldina
        const DAYS = 6;
        
        // Fetch Weather Data
        async function fetchWeather() {
            const weatherContainer = document.getElementById("weather-cards");
            
            try {
                const response = await fetch(
                    `https://api.tomorrow.io/v4/weather/forecast?location=${LOCATION}&apikey=${API_KEY}&timesteps=daily&units=metric`
                );
                
                if (!response.ok) throw new Error("Errore nel caricamento dati");
                
                const data = await response.json();
                if (!data.timelines?.daily) throw new Error("Dati non disponibili");
                
                displayWeather(data.timelines.daily);
            } catch (error) {
                weatherContainer.innerHTML = `
                    <div style="grid-column: 1/-1; color: #dc3545; text-align: center; padding: 20px;">
                        <i class="fas fa-exclamation-triangle"></i> ${error.message}
                    </div>
                `;
            }
        }
        
        // Display Weather Data
        function displayWeather(dailyData) {
            const weatherContainer = document.getElementById("weather-cards");
            weatherContainer.innerHTML = "";
            
            dailyData.slice(0, DAYS).forEach(day => {
                const date = new Date(day.time);
                const dayName = date.toLocaleDateString("it-IT", { weekday: "short" });
                const formattedDate = date.toLocaleDateString("it-IT", { day: "numeric", month: "short" });
                
                weatherContainer.innerHTML += `
                    <div class="weather-card">
                        <div class="day">${dayName}</div>
                        <div class="date">${formattedDate}</div>
                        <div class="weather-icon">${getWeatherIcon(day.values.weatherCode)}</div>
                        <div class="temp">${Math.round(day.values.temperatureMax)}° <span>${Math.round(day.values.temperatureMin)}°</span></div>
                        <div class="description">${getWeatherDescription(day.values.weatherCode)}</div>
                        <div class="details">
                            <div><i class="fas fa-tint"></i> ${Math.round(day.values.humidityAvg)}%</div>
                            <div><i class="fas fa-wind"></i> ${Math.round(day.values.windSpeedAvg)} km/h</div>
                        </div>
                    </div>
                `;
            });
        }
        
        // Helper functions
        function getWeatherIcon(weatherCode) {
            const icons = {
                1000: "☀️", 1100: "🌤", 1101: "⛅", 1102: "🌥",
                1001: "☁️", 2000: "🌫", 2100: "🌫", 4000: "🌧",
                4001: "🌧", 4200: "🌦", 4201: "🌧", 5000: "❄️",
                5001: "🌨", 5100: "❄️", 5101: "🌨", 6000: "🌧",
                6001: "🌧", 6200: "🌧", 6201: "🌧", 7000: "🌨",
                7101: "🌨", 7102: "🌨", 8000: "⛈"
            };
            return icons[weatherCode] || "🌤";
        }
        
        function getWeatherDescription(weatherCode) {
            const descriptions = {
                1000: "Sereno", 1100: "Sereno", 1101: "Nuv.sparse",
                1102: "Nuvoloso", 1001: "Coperto", 2000: "Nebbia",
                2100: "Foschia", 4000: "Pioviggine", 4001: "Pioggia",
                4200: "Pioggia", 4201: "Pioggia", 5000: "Neve",
                5001: "Neve", 5100: "Neve", 5101: "Neve",
                6000: "Gelata", 6001: "Gelata", 6200: "Gelata",
                6201: "Gelata", 7000: "Grandine", 7101: "Grandine",
                7102: "Grandine", 8000: "Temporale"
            };
            return descriptions[weatherCode] || "Variabile";
        }
        
        // Initialize
        document.addEventListener("DOMContentLoaded", fetchWeather);
    </script>
</body>
</html>


</center>