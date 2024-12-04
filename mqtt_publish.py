import paho.mqtt.client as mqtt
import requests
import json
import time

# Constants
MQTT_BROKER = "localhost"  
MQTT_TOPIC = "weather/data"
API_KEY = "7cab5c00e32d3b4d4fb8b3b80a2c35cb"  
CITY = "Mumbai" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def fetch_weather_data():
    try:
        params = {"q": CITY, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for HTTP failures
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

# MQTT setup
client = mqtt.Client()
client.connect(MQTT_BROKER)

# Publish weather data to MQTT broker
while True:
    weather_data = fetch_weather_data()
    if weather_data:
        client.publish(MQTT_TOPIC, json.dumps(weather_data))
        print("Data published:", weather_data)
    else:
        print("Skipping this cycle due to fetch error.")
    time.sleep(3600)  # Publish data every hour
