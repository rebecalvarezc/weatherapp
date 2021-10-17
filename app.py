import datetime
import time
import requests

# API from openweatherapp.com
api_key = ''


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
        'country': data['sys']['country'],
        'condition': data['weather'][0]['main'],
        'temp': round(data['main']['temp'] - 273.15),
        'min_temp': round(data['main']['temp_min'] - 273.15),
        'max_temp': round(data['main']['temp_max'] - 273.15),
        'humidity': round(data['main']['humidity'], 2),  # %
        'wind_speed': data['wind']['speed'],
        'sunrise': time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunrise'] + data['timezone'])),
        'sunset': time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunset'] + data['timezone']))
    }
    return conditions


def share_data():
    date = datetime.date.today().strftime('%A %d of %B')
    while True:
        city = input('Please write the name of the city in where you want to know the weather.\n--> ').lower().title()
        json_data = get_data(city)
        if json_data:
            conditions = get_weather_data(city)
            print(
                f"""\nToday, {date}, in {conditions['city']} ({conditions['country']}) the temperature will be {conditions['temp']}ºC.
    The percentage of humidity will be: {conditions['humidity']}%
    The max temperature today will be: {conditions['max_temp']}ºC 
    The min temperatura will be: {conditions['min_temp']} ºC.
    The sun will rise at {conditions['sunrise']} and set at: {conditions['sunset']}\n""")
        else:
            print(f'Sorry, no data was found for {city}')
            break


if __name__ == '__main__':
    share_data()
