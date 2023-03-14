from binance.futures import Futures
from collector.collector import Collector

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

WANTED_CURRENCIES = [
    'BTC',
    'ETH'
]

def main():
    client = Futures()
    collectors: list[Collector] = []
    for symbol in WANTED_CURRENCIES:
        collectors.append(Collector(symbol=symbol, 
                                    client=client, 
                                    server_host=SERVER_HOST, 
                                    server_port=SERVER_PORT))

    for collector in collectors:
        collector.collect_all()


if __name__ == '__main__':
    main()
