import time
from enum import Enum
from kucoin_futures.client import Market
from pydantic import BaseModel


class TIMEFRAME(Enum):
    MIN1 = 1
    MIN5 = 5
    MIN15 = 15
    H1 = 60
    H2 = 120
    H4 = 240
    H8 = 480
    H12 = 720
    D1 = 1440
    W1 = 10080


class CandleData(BaseModel):
    time: int
    entry_price: float
    highest_price: float
    lowest_price: float
    close_price: float
    trading_volume: float


class Collector:
    # Constuctor
    def __init__(self, name: str = "", symbol: str = "", market: Market = Market, db = any) -> None:
        self.name = name
        self.market = market
        self.db = db
        self.symbol = symbol

    def collect_all(self):
        # Begin time collection 2021/1/1 T 00:00:00
        # begin = 1609455600
        begin = 1678716000  # 2023/3/13 T 15:00:00
        # for timeframe in list(TIMEFRAME):
        data = self._collect(TIMEFRAME.MIN1.value, begin)
        return data


    @staticmethod
    def collect_step(timeframe: int):
        return timeframe*60*200*1000

    def _collect(self, timeframe: int = 1, begin: int | None = None, end: int | None = None):
        # Collect JSON data
        current_time = begin*1000
        begin_time = begin*1000
        data = [CandleData]
        while True:
            current_time += self.collect_step(timeframe)
            if current_time > int(time.time()*1000):
                temp = self.market.get_kline_data(symbol=self.symbol, granularity=timeframe, begin_t=begin_time)
                for item in temp:
                    data.append({
                        'time': item[0],
                        'entry_price': item[1],
                        'highest_price': item[2],
                        'lowest_price': item[3],
                        'close_price': item[4],
                        'trading_volume': item[5]
                    })
                return data
            temp = self.market.get_kline_data(symbol=self.symbol, granularity=timeframe, begin_t=begin_time)
            for item in temp:
                data.append({
                    'time': item[0],
                    'entry_price': item[1],
                    'highest_price': item[2],
                    'lowest_price': item[3],
                    'close_price': item[4],
                    'trading_volume': item[5]
                })
            begin_time = data[-1]['time']

        # Parse JSON data
        # print(40 * '=' + '\n')
        # print(data)
        # print('\n' + 40 * '*' + '\n')

        # Store in database
    def set_dictionary(self):
        data = self.market.get_contracts_list()
        result_dict = []
        for currency in data:
            if currency['quoteCurrency'] == "USDT":
                temp_dic = {currency['baseCurrency']: currency['symbol']}
                result_dict.append(temp_dic)
        return result_dict

