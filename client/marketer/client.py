from binance import Futures
from collector import Collector
from server.models.crypto import (IntervalBinance,
                                  IntervalKucoin,
                                  Stock,
                                  interval_dict_binance,
                                  symbols_dict_binance,
                                  symbols_dict_kucoin)


def main():
    client = Futures()
    collector = Collector("BTC", client)

    interval = IntervalBinance.MIN1
    stock = Stock.BINANCE

    collector.collect_all()


if __name__ == '__main__':
    main()
