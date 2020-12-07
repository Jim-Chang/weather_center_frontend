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
        humidity: int,
        descriptions: List[str],
    ):
        self.datetime = datetime
        self.temprature = temprature
        self.humidity = humidity
        self.descriptions = descriptions

    def __str__(self):
        return self.format_to_message()

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
            temp=self.temprature,
            humidity=self.humidity
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