import requests
from tkinter import *
import math

city_name = input("City Name: ")
api_key = ""  # User your own API key


def get_weather(api_key, city_name):
    # f is used to make a format string
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}'

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor(temp - 273.15)  # Convert kelvin to Fahrenite

    feels_like = response['main']['feels_like']
    feels_like = math.floor(feels_like - 273.15)

    humidity = response['main']['humidity']

    # print(humidity)

    return {
        "temp": temp,
        "feels_like": feels_like,
        "humidity": humidity
    }


weather = get_weather(api_key, city_name)

print(weather['temp'])
print(weather['feels_like'])
print(weather['humidity'])

# formatted_data = json_data['weather'][0]['description']
# print(formatted_data)


root = Tk()

root.geometry("400x250")
root.title(f'{city_name} Weather')


def display_city_name(city):
    city_label = Label(root, text=f"City: {city_name}")
    city_label.config(font=("Consolas", 28))
    city_label.pack(side="top")


def display_stats(weather):
    temp = Label(root, text=f"Temperature : {weather['temp']} C")
    feels_like = Label(root, text=f"Feels Like : {weather['feels_like']} C")

    humidity = Label(root, text=f"Humidity :{weather['humidity']} %")

    temp.config(font=("Consolas", 22))
    feels_like.config(font=("Consolas", 16))
    humidity.config(font=("Consolas", 16))

    temp.pack(side="top")
    feels_like.pack(side="top")
    humidity.pack(side="top")


display_city_name(city_name)
display_stats(weather)

mainloop()  # Keeps the window onscreen instead of closing it
