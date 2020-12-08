from typing import Optional
from abc import ABC, abstractmethod
from domain.models import Stock

class IStockService(ABC):
    
    @abstractmethod
    def get_stock(self, name: str) -> Optional[Stock]:
        pass