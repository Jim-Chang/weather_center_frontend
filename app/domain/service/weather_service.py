from typing import List
from abc import ABC, abstractmethod
from domain.models import Weather

class IWeatherService(ABC):

    @abstractmethod
    def get_forecast(self, place_name: str = None, lat: float = None, lon: float = None, forcast_data_count: int = 5) -> List[Weather]:
        pass