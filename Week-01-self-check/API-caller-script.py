import logging
import requests
import json


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

URL =  "https://api.open-meteo.com/v1/forecast"
def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2)
    logger.info(f"saved to {filename}")   

def fetch_weather(latitude, longitude):
    try:
        response = requests.get(
            URL,
            params={"latitude": latitude, "longitude": longitude, "current_weather": True},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        logger.error("The request timed out.")
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
    return None

def print_summary(data):
    weather = data["current_weather"]
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Wind speed: {weather['windspeed']} km/h")
    print(f"Time: {weather['time']}")

data = fetch_weather(24.850615, 66.992485)
if data is None:
    print("No data.")
else:
    print(data["current_weather"]["temperature"])

def main():
    data = fetch_weather(24.850615, 66.992485)
    if data is None: 
        return
    save_to_json(data, "weather.json")
    print_summary(data)

if __name__ == "__main__":
    main()