# import tkinter as tk
import time
from pprint import pprint
import requests

# API from openweatherapp.com
api_key = 'e8a6318f847fcff8956b223b10519dff'


def get_data():
    city = 'Puerto Rico'
    endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    r = requests.get(endpoint)
    if r.status_code in range(200, 300):
        return r.json()


# canvas = tk.Tk()
# canvas.geometry('600x500')
# canvas.title('Weather App')
#
# f = ('poppins', 15, 'bold')
# t = ('poppins', 35, 'bold')
#
# textfield = tk.Entry(canvas, font=t)
# textfield.pack(pady=20)
# textfield.focus()
#
# label1 = tk.label(canvas, font=t)
# label1.pack()
# label2 = tk.label(canvas, font=f)
# label2.pack()
#
# canvas.mainloop()
def get_weather_data():
    data = get_data()
    condition = data['weather'][0]['main']
    temp = round(data['main']['temp'] - 273.15)  # En qué unidades? -> Kelvin -> Celsius
    min_temp = round(data['main']['temp_min'] - 273.15)
    max_temp = round(data['main']['temp_max'] - 273.15)
    humidiy = round(data['main']['humidity'], 2)  # %
    wind_speed = data['wind']['speed']  # m/s
    sunrise = time.strftime('%A %I:%M%p', time.gmtime(data['sys']['sunrise'])) # GMT+1 London & Spain = GMT+2
    timezone = data['timezone']/3600
    sunset = data['sys']['sunset'] # UTC

    pprint(data)


if __name__ == '__main__':
    get_weather_data()
