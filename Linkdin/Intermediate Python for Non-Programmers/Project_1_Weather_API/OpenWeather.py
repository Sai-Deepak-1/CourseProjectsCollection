import requests
import os
from dotenv import load_dotenv

load_dotenv()


class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

            if not OPENWEATHER_API_KEY:
                raise ValueError(
                    "OpenWeather API key not found in environment variables."
                )

            url = f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={OPENWEATHER_API_KEY}"
            response = requests.get(url)

            if response.status_code == 200:
                self.res = response.json()
                self.temp = self.res["main"]["temp"]
                self.temp_min = self.res["main"]["temp_min"]
                self.temp_max = self.res["main"]["temp_max"]
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")

        except ValueError as ve:
            print("ValueError:", ve)
        except Exception as e:
            print("Exception occurred:", e)

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In {self.name} it is currently {self.temp}° {units_symbol}")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")


# lat = float(input("Enter a Latitude: "))
# lon = float(input("Enter a Longitude: "))

my_city = City("Tokyo", 35.6762, 139.6503)
my_city.temp_print()

vacation_city = City("Portland", 45.5152, -122.6784, units="imperial")
vacation_city.temp_print()
