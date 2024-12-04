import requests

API_KEY = "7cab5c00e32d3b4d4fb8b3b80a2c35cb"
CITY = "Mumbai"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data():
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json()

weather_data = fetch_weather_data()
print(weather_data)
