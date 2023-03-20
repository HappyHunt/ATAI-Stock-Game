import requests

from server.models.crypto import IntervalBinance
from server.models.candle import CandlestickSchema
from server.environment import BASE_URL


def get_data_for_interval(symbol: str, interval: IntervalBinance, time_start: int, time_end: int):
    url = f'{BASE_URL}/client/candles/{symbol}/{interval.value}'
    r = requests.get(url, params={"time_start": time_start, "time_end": time_end})
    return r.json()


def get_indicator(symbol: str, interval: IntervalBinance, time_start: int, time_end: int):
    url = f'{BASE_URL}/client/candles/indicators/{symbol}/{interval}'
    r = requests.get(url, params={"time_start": time_start, "time_end": time_end})
    return r.json()

