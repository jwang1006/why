import requests

weather_api_key = "c6de26cacdce198bd27a13ddf18a59d3"
currentWeatherURL = "https://api.openweathermap.org/data/2.5/weather"
forecastURL = "https://api.openweathermap.org/data/2.5/forecast"

my_city = "South Pasadena"

parameters = {
    "q": my_city,
    "appid": weather_api_key,
    "units": "imperial"
}

def checkForRain():
    response = requests.get(forecastURL, params=parameters)

    response.raise_for_status()
    data = response.json()["list"]
    for i in range(18, 24):
        if data[i]["weather"][0]["main"]=="Rain":
            return True

def sendRainText():
    pass

while True:
    if checkForRain():
        sendRainText()