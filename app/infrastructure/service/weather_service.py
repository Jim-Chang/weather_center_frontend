from typing import List
import requests
import arrow
import settings
from utils.log import logging

from domain.service.weather_service import IWeatherService
from domain.models import Weather


class OpenWeatherService(IWeatherService):

    API_BASE = 'https://api.openweathermap.org/data/2.5/{}'

    def get_forcast(self, place_name: str = None, lat: float = None, lon: float = None, forcast_data_count: int = 5) -> List[Weather]:
        if place_name is None and (lat is None or lon is None):
            raise ValueError('Must provide place name or lat and lon')

        payload = {
            'lang': 'zh_tw',
            'units': 'metric',
            'cnt': forcast_data_count,
            'appid': settings.OPEN_WEATHER_APPID,
        }

        if place_name:
            payload['q'] = place_name
        else:
            payload['lat'] = lat
            payload['lon'] = lon

        result = requests.get(self.API_BASE.format('forcast'), params=payload)

        if (status_code := result.status_code) != 200:
            logging.error('OpenWeatherService get_forcast status code is {}'.format(status_code))
            return []

        raw_json = result.json()

        if (cod_code := raw_json['cod']) != '200':
            logging.error('OpenWeatherService get_forcast is not success, cod is {}'.format(cod_code))
            return []

        return [self._create_weather(data) for data in raw_json['list']]

    def _create_weather(self, data: dict) -> Weather:
        return Weather(
            datetime=arrow.get(data['dt']),
            temprature=data['main']['temp'],
            humidity=data['main']['humidity'],
            descriptions=[w['description'] for w in data['weather']]
        )