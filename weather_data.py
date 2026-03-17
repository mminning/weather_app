from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import requests as rq

# GET COORDINATES FROM CITY, STATE
def get_coordinates(city, state):
    """ gets coordinates for a city and a state.
    Args: city (string), state (string, 2 letter ALL CAPS abbreviation)
    returns: latitude, longitude"""
    geolocator = Nominatim(user_agent="basshog")

    try:
        # Combine city and state for the query
        query = f"{city}, {state}"
        location = geolocator.geocode(query)

        if location:
            return (location.latitude, location.longitude)
        else:
            return None

    except GeocoderTimedOut:
        # Handle cases where the geocoding service times out
        return get_coordinates(city, state)

def get_temperatures(city, state, days):
    coordinates = get_coordinates(city, state)
    if coordinates:
        latitude = coordinates[0]
        longitude = coordinates[1]
        get_city = rq.get(f"https://api.weather.gov/points/{latitude},{longitude}")
        get_city_data = get_city.json()
        forecast_hourly_url = get_city_data["properties"]["forecastHourly"]

        #get temperature data for specific time range
        forecast_hourly_data = rq.get(forecast_hourly_url)
        forecast_hourly_data = forecast_hourly_data.json()
        temps = [temp["temperature"] for temp in forecast_hourly_data["properties"]["periods"]]
        temps = temps[:24*days:4]

        dates = [date["startTime"] for date in forecast_hourly_data["properties"]["periods"]]
        dates = dates[:24*days:4]

        temp_date_pairs = dict(zip(dates, temps))
        return temp_date_pairs
    else:
        error_message = "City not found."
        return error_message

# Get Data (test)
if __name__ == "__main__":
    url = get_temperatures("Wichita", "KS", 2)
    coordinates = get_coordinates("Wichita", "KS")
    print(coordinates)
    print(url)
    print(len(url))

