from kucoin_futures.client import Trade
from kucoin_futures.client import Market
from atai.collectors.collector import Collector


class KucoinClient:
    client = None  # Temporary referention for development

    # Kucoin API symbols to understandable dev-symbols
    symbolsDict = {
        "BTC": "XBTUSDTM",
        "ETH": "ETHUSDTM",
        "BCH": "BCHUSDTM",
        "BSV": "BSVUSDTM",
        "LINK": "LINKUSDTM",
        "UNI": "UNIUSDTM",
        "YFI": "YFIUSDTM",
        "EOS": "EOSUSDTM",
        "DOT": "DOTUSDTM",
        "FIL": "FILUSDTM",
        "ADA": "ADAUSDTM",
        "XRP": "XRPUSDTM",
        "LTC": "LTCUSDTM",
        "TRX": "TRXUSDTM",
        "GRT": "GRTUSDTM",
        "SUSHI": "SUSHIUSDTM",
        "XLM": "XLMUSDTM",
        "1INCH": "1INCHUSDTM",
        "ZEC": "ZECUSDTM",
        "DASH": "DASHUSDTM",
        "AAVE": "AAVEUSDTM",
        "KSM": "KSMUSDTM",
        "DOGE": "DOGEUSDTM",
        "VET": "VETUSDTM",
        "BNB": "BNBUSDTM",
        "SXP": "SXPUSDTM",
        "SOL": "SOLUSDTM",
        "IOST": "IOSTUSDTM",
        "CRV": "CRVUSDTM",
        "ALGO": "ALGOUSDTM",
        "AVAX": "AVAXUSDTM",
        "FTM": "FTMUSDTM",
        "MATIC": "MATICUSDTM",
        "THETA": "THETAUSDTM",
        "ATOM": "ATOMUSDTM",
        "CHZ": "CHZUSDTM",
        "ENJ": "ENJUSDTM",
        "MANA": "MANAUSDTM",
        "DENT": "DENTUSDTM",
        "OCEAN": "OCEANUSDTM",
        "BAT": "BATUSDTM",
        "XEM": "XEMUSDTM",
        "QTUM": "QTUMUSDTM",
        "XTZ": "XTZUSDTM",
        "SNX": "SNXUSDTM",
        "NEO": "NEOUSDTM",
        "ONT": "ONTUSDTM",
        "XMR": "XMRUSDTM",
        "COMP": "COMPUSDTM",
        "ETC": "ETCUSDTM",
        "WAVES": "WAVESUSDTM",
        "BAND": "BANDUSDTM",
        "MKR": "MKRUSDTM",
        "RVN": "RVNUSDTM",
        "DGB": "DGBUSDTM",
        "SHIB": "SHIBUSDTM",
        "ICP": "ICPUSDTM",
        "DYDX": "DYDXUSDTM",
        "AXS": "AXSUSDTM",
        "HBAR": "HBARUSDTM",
        "EGLD": "EGLDUSDTM",
        "ALICE": "ALICEUSDTM",
        "YGG": "YGGUSDTM",
        "NEAR": "NEARUSDTM",
        "SAND": "SANDUSDTM",
        "C98": "C98USDTM",
        "ONE": "ONEUSDTM",
        "VRA": "VRAUSDTM",
        "GALA": "GALAUSDTM",
        "TLM": "TLMUSDTM",
        "CHR": "CHRUSDTM",
        "LRC": "LRCUSDTM",
        "FLOW": "FLOWUSDTM",
        "RNDR": "RNDRUSDTM",
        "IOTX": "IOTXUSDTM",
        "CRO": "CROUSDTM",
        "WAXP": "WAXPUSDTM",
        "PEOPLE": "PEOPLEUSDTM",
        "OMG": "OMGUSDTM",
        "LINA": "LINAUSDTM",
        "IMX": "IMXUSDTM",
        "NFT": "NFTUSDTM",
        "CELR": "CELRUSDTM",
        "ENS": "ENSUSDTM",
        "CELO": "CELOUSDTM",
        "CTSI": "CTSIUSDTM",
        "SLP": "SLPUSDTM",
        "ARPA": "ARPAUSDTM",
        "KNC": "KNCUSDTM",
        "API3": "API3USDTM",
        "ROSE": "ROSEUSDTM",
        "AGLD": "AGLDUSDTM",
        "APE": "APEUSDTM",
        "JASMY": "JASMYUSDTM",
        "ZIL": "ZILUSDTM",
        "GMT": "GMTUSDTM",
        "RUNE": "RUNEUSDTM",
        "LOOKS": "LOOKSUSDTM",
        "AUDIO": "AUDIOUSDTM",
        "KDA": "KDAUSDTM",
        "KAVA": "KAVAUSDTM",
        "BAL": "BALUSDTM",
        "GAL": "GALUSDTM",
        "LUNA": "LUNAUSDTM",
        "LUNC": "LUNCUSDTM",
        "OP": "OPUSDTM",
        "XCN": "XCNUSDTM",
        "UNFI": "UNFIUSDTM",
        "LIT": "LITUSDTM",
        "DUSK": "DUSKUSDTM",
        "STORJ": "STORJUSDTM",
        "RSR": "RSRUSDTM",
        "JST": "JSTUSDTM",
        "OGN": "OGNUSDTM",
        "TRB": "TRBUSDTM",
        "PERP": "PERPUSDTM",
        "KLAY": "KLAYUSDTM",
        "ANKR": "ANKRUSDTM",
        "LDO": "LDOUSDTM",
        "WOO": "WOOUSDTM",
        "REN": "RENUSDTM",
        "CVC": "CVCUSDTM",
        "INJ": "INJUSDTM",
        "APT": "APTUSDTM",
        "MASK": "MASKUSDTM",
        "REEF": "REEFUSDTM",
        "TON": "TONUSDTM",
        "MAGIC": "MAGICUSDTM",
        "CFX": "CFXUSDTM",
        "AGIX": "AGIXUSDTM",
        "FXS": "FXSUSDTM",
        "FET": "FETUSDTM",
        "AR": "ARUSDTM",
        "GMX": "GMXUSDTM",
        "BLUR": "BLURUSDTM",
        "ASTR": "ASTRUSDTM",
        "HIGH": "HIGHUSDTM",
        "ACH": "ACHUSDTM",
        "STX": "STXUSDTM",
        "COCOS": "COCOSUSDTM",
        "SSV": "SSVUSDTM",
        "FLOKI": "FLOKIUSDTM",
        "CKB": "CKBUSDTM",
        "TRU": "TRUUSDTM",
        "QNT": "QNTUSDTM"
    }

    def __init__(self, trade: Trade, market: Market, db=None):
        # Kucoin Handlers
        self.kucoin_client_trade = trade
        self.kucoin_client_market = market

        # Database
        self.db = db

        # Collectors
        self.btc_collector = Collector('BTC', KucoinClient.symbolsDict["BTC"], self.kucoin_client_market, self.db)
        self.eth_collector = Collector('ETH', KucoinClient.symbolsDict["ETH"], self.kucoin_client_market, self.db)
        self.dici_collector = Collector(market=self.kucoin_client_market)
        self.collectors = [self.btc_collector, self.eth_collector]

        # DB Init
        #    Data collect
        self.db_collect()
        #    Calculations
        self.indicators_calculate()
        #   Set Dictionary
        self.save_dictionary_in_database()

    def db_collect(self):
        # for collector in self.collectors:
        data = self.btc_collector.collect_all()
        collection = self.db['BTC.1min']
        for item in data[1::]:
            collection.insert_one(item)

    def save_dictionary_in_database(self):
        collist = self.db.list_collection_names()
        if "dictionary" in collist:
            print("The collection exists.")
            return
        dici = self.dici_collector.set_dictionary()
        collection = self.db["dictionary"]
        collection.insert_many(dici)

    def indicators_calculate(self):
        pass


# Background Thread main function
#    BG Thread is suppose to collect certain data and store it into MongoDB
def bg_thread_work(kucoin_client: KucoinClient) -> None:
    return
