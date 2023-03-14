import requests
import time
from tqdm import tqdm

from binance.futures import Futures
from models.candle import CandlestickSchema, CandlestickSchemaList
from models.crypto import (IntervalBinance,
                                  IntervalKucoin,
                                  Stock,
                                  interval_dict_binance,
                                  symbols_dict_binance,
                                  symbols_dict_kucoin)


class Collector:
    def __init__(self, symbol: str, client: Futures, server_host: str, server_port: int, stock: Stock = Stock.BINANCE) -> None:
        self.symbol = symbol
        self.client = client
        self.stock = stock
        self._server_addr = (server_host, server_port)
        self.base_url = f'http://{server_host}:{server_port}/market'


    def collect_all(self, limit: int = 200) -> None:
        for interval in IntervalBinance:
            self.collect_candles(interval=interval, limit=limit)


    def collect_candles(self, interval: IntervalKucoin | IntervalBinance, limit: int = 200):

        print(f'[Collector] : {self.symbol} : {self.stock.name} : {self.symbol}.{interval.name} : Collecting...')

        match self.stock:
            case Stock.BINANCE:
                api_symbol = symbols_dict_binance.get(self.symbol)

                curr_time = self._get_current_timestamp()
                data = self.client.klines(symbol=api_symbol,
                                          interval=interval.value,
                                          limit=1,
                                          startTime=1300000000000)
                
                start_time = data[0][0]
                step = self._get_step(int(interval_dict_binance[interval.value]))

                for t in tqdm(range(start_time, curr_time, step)):
                    data = self.client.klines(symbol=api_symbol,
                                              interval=interval.value,
                                              limit=limit,
                                              startTime=t)

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
                    url = f'{self.base_url}/candles/{self.symbol}/{timeframe}'

                    r = requests.post(url, json=candles_list)


    def _get_current_timestamp(self):
        return int(time.time()) * 1000


    def _get_step(self, interval: int):
        return interval * 60 * 200 * 1000