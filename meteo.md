---
layout: page
title: Meteo Rescaldina
permalink: /meteo/
image: 'https://marzorati.co/img/meteo.png'
share-img: 'https://marzorati.co/img/meteo.png'
---
<center>



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
        const LOCATION = "45.6206,8.9526";  // Coordinate di Rescaldina
        const DAYS = 6;
        
        // Fetch Weather Data
        async function fetchWeather() {
            const weatherContainer = document.getElementById("weather-cards");
            
            try {
                const response = await fetch(
                    `https://api.tomorrow.io/v4/weather/forecast?location=${LOCATION}&apikey=${API_KEY}&timesteps=daily&units=metric`
                );
                
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.message || `Errore HTTP! Status: ${response.status}`);
                }
                
                const data = await response.json();
                
                if (!data.timelines?.daily) {
                    throw new Error("Formato dati non valido");
                }
                
                displayWeather(data.timelines.daily);
            } catch (error) {
                weatherContainer.innerHTML = `
                    <div class="error">
                        <i class="fas fa-exclamation-triangle"></i> Errore nel recupero dei dati:<br>
                        ${error.message}<br><br>
                        <small>Verifica la console per dettagli.</small>
                    </div>
                `;
                console.error("Dettaglio errore:", error);
            }
        }
        
        // Display Weather Data
        function displayWeather(dailyData) {
            const weatherContainer = document.getElementById("weather-cards");
            weatherContainer.innerHTML = "";
            
            // Get next 6 days (skip today if needed)
            const forecastDays = dailyData.slice(0, DAYS);
            
            forecastDays.forEach(day => {
                const date = new Date(day.time);
                const dayName = date.toLocaleDateString("it-IT", { weekday: "long" });
                const formattedDate = date.toLocaleDateString("it-IT", { day: "numeric", month: "short" });
                
                const weatherCode = day.values.weatherCode;
                const tempMax = Math.round(day.values.temperatureMax);
                const tempMin = Math.round(day.values.temperatureMin);
                const humidity = Math.round(day.values.humidityAvg);
                const windSpeed = Math.round(day.values.windSpeedAvg);
                
                weatherContainer.innerHTML += `
                    <div class="weather-card">
                        <div class="day">${capitalizeFirstLetter(dayName)}</div>
                        <div class="date">${formattedDate}</div>
                        <div class="weather-icon">${getWeatherIcon(weatherCode)}</div>
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
        
        // Helper functions
        function capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        }
        
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
                1000: "Sereno", 1100: "Preval. sereno", 1101: "Parz. nuvoloso",
                1102: "Molto nuvoloso", 1001: "Nuvoloso", 2000: "Nebbia",
                2100: "Nebbia leggera", 4000: "Pioviggine", 4001: "Pioggia",
                4200: "Pioggia leggera", 4201: "Pioggia intensa", 5000: "Neve",
                5001: "Nevischio", 5100: "Neve leggera", 5101: "Neve intensa",
                6000: "Pioggia gelata", 6001: "Pioggia congelante",
                6200: "Pioggia gelata leggera", 6201: "Pioggia gelata intensa",
                7000: "Grandine", 7101: "Grandine intensa", 7102: "Grandine leggera",
                8000: "Temporale"
            };
            return descriptions[weatherCode] || "Condizioni variabili";
        }
        
        // Initialize
        document.addEventListener("DOMContentLoaded", fetchWeather);
    </script>
</body>


</center>