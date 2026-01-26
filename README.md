# Python-Weather-Logger
This tool gathers weather data from the users input of a zip code (for more accuracy), and gets the weather data from the website "openweathermap.org". It puts the data into a spreadsheet known as a ".csv" file.

🌦️ Python Weather Data Logger
A lightweight Python automation tool that fetches real-time weather data based on a US ZIP Code and logs the results into a structured CSV spreadsheet.

This project utilizes the OpenWeatherMap API to ensure accuracy by mapping ZIP codes to their official city names before storage.

✨ Features
Precise Location Tracking: Uses ZIP codes to avoid "duplicate city" naming errors.

Automatic CSV Management: Smart logic detects if weather_out.csv exists. It creates the file with headers if missing, or appends new data if the file is already present.

Real-time Data: Fetches the high-level weather state (Clouds, Rain, Clear, etc.) and current temperature in Fahrenheit.

Data Persistence: Saves data locally for historical tracking and analysis.

🛠️ Tech Stack
Language: Python 3.x

Libraries: requests, os

API: OpenWeatherMap API

🚀 How It Works
The user provides a 5-digit US ZIP code.

The script calls the OpenWeatherMap API using a secure API Key.

The API returns a JSON response containing the official city name and current weather conditions.

The script parses the JSON and writes the following columns to weather_out.csv:

City (The official name mapped from the ZIP)

Weather (Current condition)

Temp (Temperature in Imperial units)

📦 Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/weather-data-logger.git
Install dependencies:

Bash

pip install requests
Add your API Key: Replace the A_Key variable in the script with your personal API key from OpenWeatherMap.

Run the script:

Bash

python main.py
