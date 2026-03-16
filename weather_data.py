from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import requests as rq

# GET COORDINATES FROM CITY, STATE
def get_coordinates(city, state):
    """ gets coordinates for a city and a state.
    Args: city (string), state (string, 2 letter ALL CAPS abbreviation)"""
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

#usage
coords = get_coordinates(city="Wichita", state="KS")

if coords:
    latitude = coords[0]
    longitude = coords[1]
    #print(f"Coordinates for {city}, {state}:")
    #print(f"Latitude: {coords[0]}")
    #print(f"Longitude: {coords[1]}")
else:
    print("Location not found.")

# GET WEATHERDATA FROM COORDS
def get_cityforecast(latitude, longitude):
    getforecast = rq.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    getforecast_content = getforecast.json()
    forecast_url = getforecast_content["properties"]["forecast"]
    return forecast_url

url = get_cityforecast(latitude, longitude)
print(url)