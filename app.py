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
html_friends = """
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
    <div style = "background-color: {}; padding: 5px; border-radius: 10px">
    <h4 style = "color: {}; text-align:left; font-size: 16px; font-family:'Roboto', sans serif;"> {} </h4>
    <p style = "font-family:'Roboto', serif; padding: 8px"> {} </p>
    </div>"""
html_boxes = """
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
    <img <img src="{}" width= "60px" height= "50px"/>
    <h4 style = "color: {}; text-align:left; font-size: 18px; font-family:'Roboto', sans serif;"> {} </h4>
    <p> Here\'s the weather info for the city of {} where {} lives: </p>"""
html_list = """<li>{}</li>"""
# Constants

HISTORY = '''My name is Rebeca Alvarez and I am originally from Venezuela. I moved 4 years ago to Valencia, Spain.
As i have a lor of friends around the world, I decided to create this app to check the weather wherever they are. 
Down below I will introduce you to myy friends, I hope you like them as much as I do :)'''

VALERIA = {
    'name': '👩🏻 Valeria',
    'home': '''Valeria is my childhood best friend! She is married to Carlos and they both live happily in Dublin, Ireland.
    I have visited her twice already and I really love how beautiful Ireland is and how lovely the people in there are. 
    But Ireland is really rainy, so I constantly worry that she might get sick.'''}

RODNEY = {
    'name': '👨🏿‍🦲 Ronny',
    'home': '''Ronny is my friend & my programming teacher and he is incredibly intelligent! He used to live in 
    Venezuela, but right now he lives in Tyumen, Rusia. He is studying there his Master degree and I hope he can make ç
    new friends there :).  I worry it would be too cold for him, as Venezuela is a tropical country and he is not used to
    the winter season.'''
}

MARKO = {
    'name': '👱🏻‍♂ Marko',
    'home': '''Marko is the guy I like and he lives in Novo Mesto, Slovenia. I love his country because the landscapes 
    are really beautiful. He told me that sometimes there's snow there which is very exciting! I want to be more familiar 
    with the weather in his country, so I decided to add him to this app.'''
}


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


def design(condition: str, city: str, person: str):
    """
    This function defines the page design according to the weather condition.
    :param condition:
    :return:
    """

    if condition == 'clear':
        st.markdown(html_boxes.format('https://cdn-icons-png.flaticon.com/512/3917/3917805.png', '#98B4D4',
                                      'Oh how lucky, the sky is clear!😁', city, person))
    elif condition == 'clouds':
        st.markdown(html_boxes.format('https://cdn1.iconfinder.com/data/icons/user-interface-colorful/48/cloud-512.png',
                                      '#98B4D4', 'It\'s a bit cloudy today😊', city, person),
                    unsafe_allow_html=True)
    elif condition == 'scattered clouds':
        st.markdown(html_boxes.format('#98B4D4', 'images/sunny.png', 'white', 'Seems like a good day to me😋'))
    elif condition == 'broken clouds':
        st.markdown(html_boxes.format('#98B4D4', 'images/sunny.png', 'white', 'Hum, a bit gloomy👻'))
    elif condition == 'shower rain':
        st.markdown(html_boxes.format('#98B4D4', 'images/sunny.png', 'white', 'It\'s raining men, Alleluia!🎶'))
    elif condition == 'rain':
        st.markdown(html_boxes.format('#98B4D4', 'images/sunny.png', 'white', 'Rainy day\'s make me blue😔'))
    elif condition == 'thunderstorm':
        st.markdown(html_boxes.format('#98B4D4', 'images/sunny.png', 'white', 'Ohhh scary..😣'))
    elif condition == 'snow':
        st.markdown(html_boxes.format('#98B4D4', 'images/sunny.png', 'white', 'Do you want to build a snowman? 🥶'))
    elif condition == 'mist':
        st.markdown(html_boxes.format('#98B4D4',
                                      'https://cdn.imgbin.com/0/23/22/imgbin-computer-icons-mist-weather-fog-mist-Z4Ft71QgvDRDwXRFattvFYuwK.jpg',
                                      'white', 'Oh seems like there\'s a lot of humidity'))


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


if __name__ == '__main__':
    menu = ['Home', 'Rebeca', 'Valeria', 'Ronny', 'Marko']
    selection = st.sidebar.selectbox('Menu', menu)
    if selection == 'Home':
        st.markdown(html_template.format('#955251', 'white'), unsafe_allow_html=True)
        st.markdown(html_intro.format('white', '#955251', 'Welcome!', 'black',
                                      'This is my personal app that I made for my friends :)', HISTORY),
                    unsafe_allow_html=True)
        st.markdown(html_friends.format('white', '#955251', VALERIA['name'], VALERIA['home']), unsafe_allow_html=True)
        st.markdown(html_friends.format('white', '#955251', RODNEY['name'], RODNEY['home']), unsafe_allow_html=True)
        st.markdown(html_friends.format('white', '#955251', MARKO['name'], MARKO['home']), unsafe_allow_html=True)
    elif selection == 'Rebeca':
        st.markdown(html_template.format('#98B4D4', 'white'), unsafe_allow_html=True) # Este  también puede cambiar con el clima en cada persona !!!
        info = get_weather_data('Valencia')
        design(info['condition'].lower(), 'Valencia', 'Rebeca')
        st.write(info)
    elif selection == 'Valeria':
        pass
    elif selection == 'Ronny':
        pass
    else:
        pass
