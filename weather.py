# import required modules
import requests
import os
from dotenv import load_dotenv


# load environment variables from .env file
load_dotenv()
# why use os module?
# WE use the os module so that we can safely read values 
# (like secrets or API keys) stored in our environment.
# It also allows us to access variables defined 
# in the .env file securely.
API_key = os.getenv("WEATHER_API_KEY") # API_KEY = 1232435


def get_weather(city):
    # prepare the url with city and API Key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"


    response = requests.get(url) # sends a GET request to the API

    # Check if the request failed or not
    if response.status_code != 200:
        print("Error:", response.status_code)
        return None
    
    # Parse JSON reponse into python dictionary
    data = response.json()

    # lets extract relevant fields and return as dictnary
    return {
        "name": data["name"],
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
    
# this is the json response that we get from the api and we parsed it in line data = response.json().
    #  {
    #  "coord": {
    #    "lon": -0.13,
    #    "lat": 51.51
    #  },
    #  "weather": [
    #    {
    #      "id": 300,
    #      "main": "Drizzle",
    #      "description": "light intensity drizzle",
    #      "icon": "09d"
    #    }
    #  ],
    #  "base": "stations",
    #  "main": {
    #    "temp": 280.32,
    #    "pressure": 1012,
    #    "humidity": 81,
    #    "temp_min": 279.15,
    #    "temp_max": 281.15
    #  },
    #  "visibility": 10000,
    #  "wind": {
    #    "speed": 4.1,
    #    "deg": 80
    #  },
    #  "clouds": {
    #    "all": 90
    #  },
    #  "dt": 1485789600,
    #  "sys": {
    #    "type": 1,
    #    "id": 5091,
    #    "message": 0.0103,
    #    "country": "GB",
    #    "sunrise": 1485762037,
    #    "sunset": 1485794875
    #  },
    #  "id": 2643743,
    #  "name": "London",
    #  "cod": 200
    #  }
      







