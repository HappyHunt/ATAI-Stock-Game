from kucoin_futures.client import Market

class Collector:
    TIMEFRAMES = [1, 5, 15, 60] # in minutes

    # Constuctor
    def __init__(self, name: str, symbol: str, market: Market, db) -> None:
        self.name = name
        self.market = market
        self.db = db
        self.symbol = symbol


    def collect_all(self):
        for timeframe in Collector.TIMEFRAMES:
            self._collect(timeframe)

    def _collect(self, timeframe : int = 1):
        # Collect JSON data
        data = self.market.get_kline_data(self.symbol, timeframe)

        # Parse JSON data
        # print(40 * '=' + '\n')
        # print(data)
        # print('\n' + 40 * '*' + '\n')

        # Store in database
