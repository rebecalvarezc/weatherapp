# import tkinter as tk
import time
from pprint import pprint
import requests
import streamlit as st

# API from openweatherapp.com
api_key = 'e8a6318f847fcff8956b223b10519dff'


# Functions
def get_data(city: str) -> dict:
    """
    This function access the API of the chosen city
    :param city:
    :return:
    """
    city = city
    endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(endpoint)
    if r.status_code in range(200, 300):
        return r.json()


def get_weather_data(city: str) -> dict:
    """
    This function returns the data for the selected city.
    :param city: city where the friend lives
    :return: dictionary with weather parameters.
    """
    data = get_data(city)
    conditions = {
        'city': city,
        'condition': data['weather'][0]['main'],
        'temp': round(data['main']['temp'] - 273.15),
        'min_temp': round(data['main']['temp_min'] - 273.15),
        'max_temp': round(data['main']['temp_max'] - 273.15),
        'humidity': round(data['main']['humidity'], 2),  # %
        'wind_speed': data['wind']['speed'],
        'sunrise': time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunrise'])),
        'timezone': data['timezone'] / 3600,
        'sunset': time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunset']))
    }
    return conditions


