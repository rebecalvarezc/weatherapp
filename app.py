# import tkinter as tk
import time
from pprint import pprint
import requests
import streamlit as st

# API from openweatherapp.com
api_key = 'e8a6318f847fcff8956b223b10519dff'

# HTML
html_template = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
    <div style = "background-color: {}; padding: 10px; border-radius: 10px">
    <h1 style = "color: {}; text-align:center;font-family:'Roboto', serif;"> My friends weather channel </h1>
    </div>"""
html_intro = """
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
    <div style = "background-color: {}; padding: 5px; border-radius: 10px">
    <h2 style = "color: {}; text-align:center; font-size: 32px; font-family:'Roboto', serif;"> {} </h2>
    <h4 style = "color: {}; text-align:center; font-size: 16px; font-family:'Roboto', sans serif;"> {} </h4>
    <br>
    <p style = "font-family:'Roboto', serif; padding: 8px"> {} </p>
    </div>"""
html_boxes = """
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
    <div style = "background-color: {}; padding: 5px; border-radius: 10px">
    <img src="" width= "70px" height= "50px" align="{}"/>
    <h4 style = "color: {}; text-align:left; font-size: 16px; font-family:'Roboto', sans serif;"> {} </h4>
    <p style = "font-family:'Roboto', serif; padding: 8px"> {} </p>
    </div>"""

# Constants

HISTORY = '''My name is Rebeca Alvarez and I am originally from Venezuela. I moved 4 years ago to Valencia, Spain.
As i have a lor of friends around the world, I decided to create this app to check the weather wherever they are. 
Down below I will introduce you to myy friends, I hope you like them as much as I do :)'''

VALERIA = {
    'name': 'Valeria',
    'home': '''Valeria is my childhood best friend! She is married to Carlos and they both live happily in Dublin, Ireland.
    I have visited her twice already and I really love how beautiful Ireland is and how lovely the people in there are. 
    But Ireland is really rainy, so I constantly worry that she might get sick.'''}


# Functions
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

    pprint(data)


if __name__ == '__main__':
    get_weather_data()
    st.markdown(html_template.format('#955251', 'white'), unsafe_allow_html=True)
    st.markdown(html_intro.format('white', '#955251', 'Welcome!', 'black', 'This is my personal app that I made for my friends :)', HISTORY), unsafe_allow_html=True)
    st.markdown(html_boxes.format('white','left', '#955251', VALERIA['name'], VALERIA['home']), unsafe_allow_html=True)
