import requests
import os

A_Key = 'Enter your API key here'
zip_code = input("What is the zip code of your area? ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},US&units=imperial&APPID={A_Key}"
)
#TODO: Variables
data = weather_data.json()
name = data['name']
weather = weather_data.json()['weather'][0]['main']
desc = weather_data.json()['weather'][0]['description']
temp = round(weather_data.json()['main']['temp'])

# 1. Check if the file exists
file_exists = os.path.isfile('weather out.csv')

with open('weather out.csv', 'a') as f:
    # 2. This only runs if the file is brand new
    if not file_exists:
        f.write("City, Weather, Desc., Temp\n")
    f.write(f"{name}, {weather}, {desc}, {temp}\n")


print(f"Recorded data for {name}!")
