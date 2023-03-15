from binance import Futures
from collector import Collector
import threading


def main():
    client = Futures()
    collector = Collector("BTC", client)
    collector1 = Collector("ETH", client)

    collector.collect_all()
    collector1.collect_all()


if __name__ == '__main__':
    main()
