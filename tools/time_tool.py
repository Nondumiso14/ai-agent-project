import zoneinfo
from datetime import datetime 
from agents import  function_tool
from geopy.geocoders import Nominatim 
from timezonefinder import TimezoneFinder

geolocator = Nominatim(user_agent = "smart_assistant")
tf = TimezoneFinder()

@function_tool
def get_time(city: str) -> str:
    """"
    Returning the currrent time for any city dynamically.
    """
    try:
        #Converting city name into coordinates using geolocator(geocode)
        location = geolocator.geocode(city)
        if not location: 
            return f"Sorry, I couldn't find the city {city}."
        latitude = location.latitude
        longitude = location.longitude

        #converting co-ordinates into a timezone
        timezone_name = tf.timezone_at(
            lat = latitude,
            lng = longitude
        )

        if not timezone_name:
            return (f"Sorry I couldn't extract the timezone for {city}")
        
        current_time = datetime.now(zoneinfo.ZoneInfo(timezone_name))

        formatted_time = current_time.strftime( "%Y-%m-%d %H:%M:%S")

        return (f"The current time in {city} is {formatted_time}")
    except Exception as e:
        return f"Error getting time: {str(e)}"
