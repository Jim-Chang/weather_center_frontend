from typing import List
from datetime import datetime
import arrow

class Weather:

    delta_days_map = {
        0: '今天',
        1: '明天',
        2: '後天',
    }

    def __init__(
        self,
        datetime: datetime,
        temprature: float,
        humidity: float,
        descriptions: List[str] = [],
    ):
        self.datetime = datetime
        self.temprature = temprature
        self.humidity = humidity
        self.descriptions = descriptions

    def __str__(self):
        return self.format_to_message()

    def __eq__(self, other):
        return self.datetime == other.datetime and \
            self.temprature == other.temprature and \
            self.humidity == other.humidity and \
            self.descriptions == other.descriptions

    def format_to_message(self) -> str:
        '''
        今天 9 點，小雨
        氣溫：20 度
        濕度：86 %
        '''
        return '{day} {hour} 點，{description}\n氣溫：{temp} 度\n濕度：{humidity} %'.format(
            day=self._get_day_str(),
            hour=self._get_hour(),
            description=self._get_description(),
            temp=round(self.temprature, 1),
            humidity=self.humidity
        )

    def format_to_weather_center_message(self) -> str:
        '''
        最後數據
        氣溫：20 度
        濕度：86 %
        記錄時間：2021-01-01 18:00:00
        '''
        return '最後數據\n氣溫：{temp} 度\n濕度：{humidity} %\n記錄時間：{recorded_at}'.format(
            temp=round(self.temprature, 1),
            humidity=round(self.humidity, 1),
            recorded_at=arrow.get(self.datetime).format('YYYY-MM-DD hh:mm:ss'),
        )

    def _get_day_str(self) -> str:
        now_date = arrow.now().shift(hours=8).date()
        data_date = arrow.get(self.datetime).shift(hours=8).date()  # api 時區 +0
        delta_days = (data_date - now_date).days
        return self.delta_days_map.get(delta_days)

    def _get_hour(self) -> int:
        return arrow.get(self.datetime).shift(hours=8).hour

    def _get_description(self) -> str:
        return ' '.join(self.descriptions)