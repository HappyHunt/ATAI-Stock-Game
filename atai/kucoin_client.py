from kucoin_futures.client import Trade
from kucoin_futures.client import Market
from atai.collectors.collector import Collector

KucoinDictionary: dict = {}


class KucoinClient:
    client = None

    def __init__(self, trade: Trade, market: Market, db=None):
        self.kucoin_client_trade = trade
        self.kucoin_client_market = market
        self.db = db

        self.btc_collector = Collector('BTC', '1min')

        self.db_collect()
        self.indicators_calculate()


    def db_collect(self):
        pass


    def indicators_calculate(self):
        pass


def bg_thread_work(kucoin_client: KucoinClient) -> None:
    return
