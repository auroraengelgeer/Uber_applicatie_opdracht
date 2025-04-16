import requests


def get_weather_data(city_name, api_key):
    # API-endpoint
    url = (f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")
