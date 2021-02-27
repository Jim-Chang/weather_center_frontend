from typing import Optional
from abc import ABC, abstractmethod
from domain.models.weather import Weather

class IWeatherCenterService(ABC):

    @abstractmethod
    def get_latest(self) -> Optional[Weather]:
        pass