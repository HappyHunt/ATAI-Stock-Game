from kucoin_futures.client import Trade
from kucoin_futures.client import Market
from atai.collectors.collector import Collector


class KucoinClient:
    client = None   # Temporary referention for development

    # Kucoin API symbols to understandable dev-symbols
    symbolsDict = {
        'btc' : 'XBTUSDTM',
        'eth' : 'ETHUSDTM'
    }

    def __init__(self, trade: Trade, market: Market, db=None):
        # Kucoin Handlers
        self.kucoin_client_trade = trade
        self.kucoin_client_market = market
        
        # Database
        self.db = db

        # Collectors
        self.btc_collector = Collector('btc', KucoinClient.symbolsDict['btc'], self.kucoin_client_market, self.db)
        self.eth_collector = Collector('eth', KucoinClient.symbolsDict['eth'], self.kucoin_client_market, self.db)
        self.collectors = [self.btc_collector, self.eth_collector]

        # DB Init
        #    Data collect
        self.db_collect()
        #    Calculations
        self.indicators_calculate()


    def db_collect(self):
        for collector in self.collectors:
            collector.collect_all()


    def indicators_calculate(self):
        pass


# Background Thread main function
#    BG Thread is suppose to collect certain data and store it into MongoDB
def bg_thread_work(kucoin_client: KucoinClient) -> None:
    return
