from typing import Optional
import requests
import settings
from utils.log import logging
import arrow

from domain.service.weather_center_service import IWeatherCenterService
from domain.models.weather import Weather

class WeatherCenterService(IWeatherCenterService):

    def get_latest(self) -> Optional[Weather]:
        result = requests.get('http://{}/api/v1/weather/latest'.format(settings.WEATHER_CENTER_IP))

        if (status_code := result.status_code) != 200:
            logging.error('WeatherCenterService get_latest status code is {}'.format(status_code))
            return None

        raw_json = result.json()
        if raw_json['status'] != 'ok':
            logging.error('WeatherCenterService get_latest status is not ok')
            return None

        data = raw_json['data']
        return Weather(
            datetime=arrow.get(data['datetime']).datetime,
            temprature=data['temperature'],
            humidity=data['humidity'],
        )