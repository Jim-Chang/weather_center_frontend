from typing import Optional
import yfinance as yf
from utils.log import logging

from domain.models import Stock
from domain.service.stock_service import IStockService

class YfStockService(IStockService):

    def get_stock(self, name: str) -> Optional[Stock]:
        ticker = yf.Ticker(name)

        try:
            return Stock(
                name=name,
                bid=ticker.info['bid'],
                pre_close=ticker.info['regularMarketPreviousClose'],
                day_high=ticker.info['regularMarketDayHigh'],
                day_low=ticker.info['regularMarketDayLow'],
                year_high=ticker.info['fiftyTwoWeekHigh'],
                year_low=ticker.info['fiftyTwoWeekLow']
            )

        except Exception:
            logging.error('Get stock info from yfinance error. Stock name: {}'.format(name), exc_info=True)