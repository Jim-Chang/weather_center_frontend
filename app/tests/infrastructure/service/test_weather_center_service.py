import pytest
import settings
import responses
import arrow

from domain.models.weather import Weather
from infrastructure.service.weather_center_service import WeatherCenterService

@pytest.mark.in_memory
@responses.activate
def test_weather_center_service__get_latest__case_1():
    responses.add(
        responses.GET,
        'http://{}/api/v1/weather/latest'.format(settings.WEATHER_CENTER_IP),
        json={
            'status': 'ok',
            'data': {
                'temperature': 20.1,
                'humidity': 60.2,
                'datetime': '2020-02-27T11:57:33+08:00',
            },
        },
        status=200
    )

    svc = WeatherCenterService()
    assert svc.get_latest() == Weather(
        datetime=arrow.get('2020-02-27T11:57:33+08:00'),
        temprature=20.1,
        humidity=60.2
    )

@pytest.mark.in_memory
@responses.activate
def test_weather_center_service__get_latest__case_2():
    responses.add(
        responses.GET,
        'http://{}/api/v1/weather/latest'.format(settings.WEATHER_CENTER_IP),
        json={
            'status': 'no_data',
        },
        status=200
    )

    svc = WeatherCenterService()
    assert svc.get_latest() is None

@pytest.mark.in_memory
@responses.activate
def test_weather_center_service__get_latest__case_3():
    responses.add(
        responses.GET,
        'http://{}/api/v1/weather/latest'.format(settings.WEATHER_CENTER_IP),
        json={},
        status=500
    )

    svc = WeatherCenterService()
    assert svc.get_latest() is None