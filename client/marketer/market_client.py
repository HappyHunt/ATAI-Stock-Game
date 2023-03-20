from binance import Futures
from collector import Collector


def main():
    client = Futures()
    collector = Collector("ETH", client)

    collector.collect_all()


if __name__ == '__main__':
    main()
