import requests
import os
from dotenv import load_dotenv

load_dotenv()

try:
    lat = float(input("Enter a Latitude: "))
    lon = float(input("Enter a Longitude: "))
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

    if not OPENWEATHER_API_KEY:
        raise ValueError("OpenWeather API key not found in environment variables.")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()
        temp = res["main"]["temp"]
        temp_min = res["main"]["temp_min"]
        temp_max = res["main"]["temp_max"]

        print(f"Temperature at {lat} and {lon} is {temp}")
        print(f"Minimum Temperature at {lat} and {lon} is {temp_min}")
        print(f"Maximum Temperature at {lat} and {lon} is {temp_max}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("Exception occurred:", e)
