import requests
import os
from agents import function_tool
from dotenv import load_dotenv

load_dotenv()

@function_tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    api_key = os.getenv("WEATHER_API_KEY")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        return f"Sorry, I couldn't find weather data for {city}."
    
    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    
    return f"The weather in {city} is {temp}°C, {condition}, with {humidity}% humidity."