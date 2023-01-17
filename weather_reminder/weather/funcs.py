import requests
from typing import Union


def add_weather_info(
        data: Union[dict, list, str],
        url: str = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4990360ecbb3086ea3865e1c7b4988c4'
) -> dict:
    try:
        if isinstance(data, dict) and len(data) > 1:
            for city in data:
                city_weather = requests.get(url.format(city['name'])).json()
                city['temperature'] = int((city_weather['main']['temp'] - 32) / 1.8)
                city['feels_like'] = int((city_weather['main']['feels_like'] - 32) / 1.8)
                city['country_code'] = city_weather['sys']['country']
                city['description'] = city_weather['weather'][0]['description']
                city['wind_speed'] = city_weather['wind']['speed']
                city['pressure'] = city_weather['main']['pressure']
                city['humidity'] = city_weather['main']['humidity']
                city['visibility'] = city_weather['visibility']
        elif isinstance(data, list):
                data = data[0]

        elif isinstance(data, str):
            data = {'name': data}

        city_weather = requests.get(url.format(data['name'])).json()
        data['temperature'] = int((city_weather['main']['temp'] - 32) / 1.8)
        data['feels_like'] = int((city_weather['main']['feels_like'] - 32) / 1.8)
        data['country_code'] = city_weather['sys']['country']
        data['description'] = city_weather['weather'][0]['description']
        data['wind_speed'] = city_weather['wind']['speed']
        data['pressure'] = city_weather['main']['pressure']
        data['humidity'] = city_weather['main']['humidity']
        data['visibility'] = city_weather['visibility']

    except IndexError:
        data = data

    return data

