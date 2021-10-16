# import tkinter as tk
import time
from pprint import pprint
import requests

# API from openweatherapp.com
api_key = 'e8a6318f847fcff8956b223b10519dff'


def get_data():
    city = 'Valencia'
    endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(endpoint)
    if r.status_code in range(200, 300):
        return r.json()


def design(condition):
    """
    This function defines the page design according to the weather condition.
    :param condition:
    :return:
    """
    if condition == 'clear sky':
        pass
    elif condition == 'few clouds':
        pass
    elif condition == 'scattered clouds':
        pass
    elif condition == 'broken clouds':
        pass
    elif condition == 'shower rain':
        pass
    elif condition == 'rain':
        pass
    elif condition == 'thunderstorm':
        pass
    elif condition == 'snow':
        pass
    elif condition == 'mist':
        pass


def get_weather_data():
    data = get_data()
    condition = data['weather'][0]['main'].lower()
    temp = round(data['main']['temp'] - 273.15)  # En qué unidades? -> Kelvin -> Celsius
    min_temp = round(data['main']['temp_min'] - 273.15)
    max_temp = round(data['main']['temp_max'] - 273.15)
    humidiy = round(data['main']['humidity'], 2)  # %
    wind_speed = data['wind']['speed']  # m/s
    sunrise = time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunrise']))
    timezone = data['timezone'] / 3600
    sunset = time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunset']))

    pprint(sunset)


if __name__ == '__main__':
    get_weather_data()
