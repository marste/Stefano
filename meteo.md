---
layout: page
title: Meteo Rescaldina
permalink: /meteo/
image: 'https://marzorati.co/img/meteo.png'
share-img: 'https://marzorati.co/img/meteo.png'
---
<center>
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
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        .weather-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .weather-card {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            transition: transform 0.3s;
        }
        
        .weather-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.3);
        }
        
        .day {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .date {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-bottom: 15px;
        }
        
        .weather-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
        }
        
        .temp {
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .description {
            font-size: 0.9rem;
            opacity: 0.9;
            margin-bottom: 10px;
            text-transform: capitalize;
        }
        
        .details {
            font-size: 0.8rem;
            opacity: 0.8;
            margin-top: 10px;
        }
        
        .loading {
            text-align: center;
            font-size: 1.2rem;
            margin-top: 50px;
        }
        
        @media (max-width: 768px) {
            .weather-cards {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 480px) {
            .weather-cards {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Previsioni Meteo Rescaldina</h1>
            <p class="subtitle">Prossimi 6 giorni</p>
        </header>
        
        <div class="weather-cards" id="weather-cards">
            <div class="loading">
                <i class="fas fa-spinner fa-spin"></i> Caricamento dati meteo...
            </div>
        </div>
    </div>

    <script>
        // API Config
        const API_KEY = "ApnIbUcAvKoThDuZIgrogmWjOnZRSVHu";
        const LOCATION = "Rescaldina,IT";
        const DAYS = 6;
        
        // Fetch Weather Data
        async function fetchWeather() {
            try {
                const response = await fetch(
                    `https://api.tomorrow.io/v4/weather/forecast?location=${encodeURIComponent(LOCATION)}&apikey=${API_KEY}&timesteps=1d&units=metric`
                );
                
                if (!response.ok) throw new Error("Errore nel caricamento dei dati");
                
                const data = await response.json();
                displayWeather(data.timelines.daily);
            } catch (error) {
                document.getElementById("weather-cards").innerHTML = `
                    <div class="error">
                        <i class="fas fa-exclamation-triangle"></i> ${error.message}
                    </div>
                `;
            }
        }
        
        // Display Weather Data
        function displayWeather(dailyData) {
            const weatherContainer = document.getElementById("weather-cards");
            weatherContainer.innerHTML = "";
            
            // Get next 6 days (skip today if needed)
            const forecastDays = dailyData.slice(1, DAYS + 1);
            
            forecastDays.forEach(day => {
                const date = new Date(day.time);
                const dayName = date.toLocaleDateString("it-IT", { weekday: "long" });
                const formattedDate = date.toLocaleDateString("it-IT", { day: "numeric", month: "short" });
                
                const weatherCode = day.values.weatherCode;
                const tempMax = Math.round(day.values.temperatureMax);
                const tempMin = Math.round(day.values.temperatureMin);
                const humidity = day.values.humidityAvg;
                const windSpeed = Math.round(day.values.windSpeedAvg);
                
                // Get weather icon based on weatherCode
                const weatherIcon = getWeatherIcon(weatherCode);
                
                weatherContainer.innerHTML += `
                    <div class="weather-card">
                        <div class="day">${dayName}</div>
                        <div class="date">${formattedDate}</div>
                        <div class="weather-icon">${weatherIcon}</div>
                        <div class="temp">${tempMax}° <span style="opacity:0.7;">${tempMin}°</span></div>
                        <div class="description">${getWeatherDescription(weatherCode)}</div>
                        <div class="details">
                            <div><i class="fas fa-tint"></i> ${humidity}%</div>
                            <div><i class="fas fa-wind"></i> ${windSpeed} km/h</div>
                        </div>
                    </div>
                `;
            });
        }
        
        // Weather Icons Mapping
        function getWeatherIcon(weatherCode) {
            const icons = {
                1000: "☀️", // Clear
                1100: "🌤", // Mostly Clear
                1101: "⛅", // Partly Cloudy
                1102: "🌥", // Mostly Cloudy
                1001: "☁️", // Cloudy
                2000: "🌫", // Fog
                2100: "🌫", // Light Fog
                4000: "🌧", // Drizzle
                4001: "🌧", // Rain
                4200: "🌦", // Light Rain
                4201: "🌧", // Heavy Rain
                5000: "❄️", // Snow
                5001: "🌨", // Flurries
                5100: "❄️", // Light Snow
                5101: "🌨", // Heavy Snow
                6000: "🌧", // Freezing Drizzle
                6001: "🌧", // Freezing Rain
                6200: "🌧", // Light Freezing Rain
                6201: "🌧", // Heavy Freezing Rain
                7000: "🌨", // Ice Pellets
                7101: "🌨", // Heavy Ice Pellets
                7102: "🌨", // Light Ice Pellets
                8000: "⛈"  // Thunderstorm
            };
            return icons[weatherCode] || "🌤";
        }
        
        // Weather Descriptions
        function getWeatherDescription(weatherCode) {
            const descriptions = {
                1000: "Sereno",
                1100: "Prevalentemente sereno",
                1101: "Parzialmente nuvoloso",
                1102: "Molto nuvoloso",
                1001: "Nuvoloso",
                2000: "Nebbia",
                2100: "Nebbia leggera",
                4000: "Pioviggine",
                4001: "Pioggia",
                4200: "Pioggia leggera",
                4201: "Pioggia intensa",
                5000: "Neve",
                5001: "Nevischio",
                5100: "Neve leggera",
                5101: "Neve intensa",
                6000: "Pioggia gelata",
                6001: "Pioggia congelante",
                6200: "Pioggia gelata leggera",
                6201: "Pioggia gelata intensa",
                7000: "Grandine",
                7101: "Grandine intensa",
                7102: "Grandine leggera",
                8000: "Temporale"
            };
            return descriptions[weatherCode] || "Condizioni variabili";
        }
        
        // Initialize
        document.addEventListener("DOMContentLoaded", fetchWeather);
    </script>
</body>



</center>