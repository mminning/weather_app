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

def get_cityforecast(city, state):
    coordinates = get_coordinates(city, state)
    if coordinates:
        latitude = coordinates[0]
        longitude = coordinates[1]
        getforecast = rq.get(f"https://api.weather.gov/points/{latitude},{longitude}")
        getforecast_content = getforecast.json()
        forecast_url = getforecast_content["properties"]["forecast"]
        return forecast_url
    else:
        error_message = "City not found."
        return error_message

# Get Coordinates
url = get_cityforecast("Wiklj", "KS")
coordinates = get_coordinates("Wichita", "KS")
print(coordinates)
print(url)

