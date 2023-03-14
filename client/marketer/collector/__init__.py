import requests
from .collector import get_step, get_timestamp
from .candle import CandlestickSchema, CandlestickSchemaList
from server.models.crypto import (IntervalBinance,
                                  IntervalKucoin,
                                  Stock,
                                  interval_dict_binance,
                                  symbols_dict_binance,
                                  symbols_dict_kucoin)


class Collector(object):
    BASE_URL = 'http://127.0.0.1:8000/market/'

    def __init__(self, symbol: str, client):
        self.symbol = symbol
        self.client = client
        return

    # METHODS
    def collect_all(self):
        for i in IntervalBinance:
            self.collect_candles(i, Stock.BINANCE)

    def collect_candles(self, interval: IntervalKucoin | IntervalBinance, stock: Stock = Stock.BINANCE,
                        limit: int = 200):
        collected_data = []

        print(f'{self.__class__} : {stock.name} : {self.symbol}.{interval.name} : Collecting...')

        match stock:
            case Stock.BINANCE:
                api_symbol = symbols_dict_binance.get(self.symbol)

                curr_time = get_timestamp()
                data = self.client.klines(symbol=api_symbol,
                                          interval=interval.value,
                                          limit=1,
                                          startTime=1300000000000)
                start_time = data[0][0]

                while start_time < curr_time:
                    data = self.client.klines(symbol=api_symbol,
                                              interval=interval.value,
                                              limit=limit,
                                              startTime=start_time)
                    start_time = start_time + get_step(int(interval_dict_binance[interval.value]))
                    c_list: list[CandlestickSchema] = []
                    for item in data:
                        obj = CandlestickSchema(timestamp=item[0],
                                                entry_price=item[1],
                                                highest_price=item[2],
                                                lowest_price=item[3],
                                                close_price=item[4],
                                                volume=item[5])
                        c_list.append(obj)

                    candles_list = CandlestickSchemaList(candles=c_list).dict()

                    timeframe = IntervalKucoin[interval.name].value
                    url = f'{Collector.BASE_URL}candles/{self.symbol}/{timeframe}'

                    r = requests.post(url, json=candles_list)

            case Stock.KUCOIN:
                api_symbol = symbols_dict_kucoin.get(self.symbol)

                for i in range(1000, -1, -1):
                    start_time = get_timestamp() - 1000 * get_step(int(interval.value))
                    data = self.client.klines(symbol=api_symbol,
                                              interval=interval.value,
                                              limit=limit,
                                              start_time=start_time)
                    collected_data.append(data)

        print(collected_data)
