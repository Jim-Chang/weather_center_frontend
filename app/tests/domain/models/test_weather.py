import pytest
import arrow
from domain.models import Weather


@pytest.mark.unitest
def test_weather():
    now = arrow.now().datetime
    w = Weather(
        datetime=now,
        temprature=20.3,
        humidity=88,
        descriptions=['test1', 'test2']
    )

    assert w.datetime == now
    assert w.temprature == 20.3
    assert w.humidity == 88
    assert w.descriptions == ['test1', 'test2']

    assert w._get_day_str() == '今天'
    assert w._get_hour() == now.hour + 8
    assert w._get_description() == 'test1 test2'

@pytest.mark.unitest
def test_weather__get_day_str():
    w = Weather(
        datetime=arrow.now().datetime,
        temprature=20.3,
        humidity=88,
        descriptions=['test1', 'test2']
    )
    assert w._get_day_str() == '今天'

    w.datetime = arrow.now().shift(days=1).datetime
    assert w._get_day_str() == '明天'

    w.datetime = arrow.now().shift(days=2).datetime
    assert w._get_day_str() == '後天'