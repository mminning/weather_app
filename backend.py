import os
from dotenv import load_dotenv
from weather_data import get_temperatures




load_dotenv()
APIkey = os.getenv("OPENWEATHERKEY")


def get_data(city, days, datatype)
   url = f"https://api.openweathermap.org/data/2.5/forecast?id={cityID}&appid={APIkey}"