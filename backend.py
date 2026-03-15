import os
from dotenv import load_dotenv
from weather_data import get_coordinates

get_coordinates(city, state)


load_dotenv()
APIkey = os.getenv("OPENWEATHERKEY")


def get_data(city, days, datatype)
   url = f"https://api.openweathermap.org/data/2.5/forecast?id={cityID}&appid={APIkey}"