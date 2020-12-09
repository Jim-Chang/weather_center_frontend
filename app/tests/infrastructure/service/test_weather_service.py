import pytest
import responses
import json
import arrow

from domain.models import Weather
from infrastructure.service.weather_service import OpenWeatherService

@pytest.mark.http
@responses.activate
def test_open_weather_service__get_forecast():
    with open('tests/files/open_weather__forecast.json') as f:
        weather_service_json = json.loads(f.read())

    responses.add(
        responses.GET,
        'https://api.openweathermap.org/data/2.5/forecast',
        json=weather_service_json,
        status=200
    )

    svc = OpenWeatherService()
    assert svc.get_forecast(place_name='taipei') == [
        Weather(
            datetime=arrow.get(1607331600).datetime,
            temprature=20.24,
            humidity=86,
            descriptions=['小雨']
        ),
        Weather(
            datetime=arrow.get(1607342400).datetime,
            temprature=19.53,
            humidity=84,
            descriptions=['小雨']
        ),
        Weather(
            datetime=arrow.get(1607353200).datetime,
            temprature=19.02,
            humidity=85,
            descriptions=['小雨']
        ),
        Weather(
            datetime=arrow.get(1607364000).datetime,
            temprature=18.48,
            humidity=84,
            descriptions=['小雨']
        ),
        Weather(
            datetime=arrow.get(1607374800).datetime,
            temprature=18.29,
            humidity=84,
            descriptions=['小雨']
        ),
    ]
