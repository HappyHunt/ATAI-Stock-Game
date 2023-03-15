from server.models.crypto import (IntervalBinance, Stock)


class Collector(object):
    def __init__(self, symbol: str, client):
        self.symbol = symbol
        self.client = client
        return

    # IMPORTS
    from .collector import collect_candles

    # METHODS
    def collect_all(self):
        for i in IntervalBinance:
            self.collect_candles(i, Stock.BINANCE)
