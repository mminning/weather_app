from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import requests as rq


def get_coordinates(city, state):
    # Initialize Nominatim API with a descriptive user_agent
    # A user_agent is required by Nominatim's usage policy
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


# Usage
city = "Wichita"
state = "KS"
coords = get_coordinates(city, state)

if coords:
    latitude = coords[0]
    longitude = coords[1]
    print(f"Coordinates for {city}, {state}:")
    print(f"Latitude: {coords[0]}")
    print(f"Longitude: {coords[1]}")
else:
    print("Location not found.")

getforecast = rq.get(f"https://api.weather.gov/points/{latitude},{longitude}")
getforecast_content = getforecast.json()

print(getforecast)