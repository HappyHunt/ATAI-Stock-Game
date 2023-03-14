from enum import Enum


class IntervalKucoin(Enum):
    MIN1 = "1"
    MIN5 = "5"
    MIN15 = "15"
    H1 = "60"
    H2 = "120"
    H4 = "240"
    H8 = "480"
    H12 = "720"
    D1 = "1440"
    W1 = "10080"


class IntervalBinance(Enum):
    MIN1 = "1m"
    MIN5 = "5m"
    MIN15 = "15m"
    H1 = "1h"
    H2 = "2h"
    H4 = "4h"
    H8 = "8h"
    H12 = "12h"
    D1 = "1d"
    W1 = "1w"


class Stock(Enum):
    BINANCE = 'Binance'
    KUCOIN = 'Kucoin'


interval_dict_binance = {
    "1m": 1,
    "5m": 5,
    "15m": 15,
    "1h": 60,
    "2h": 120,
    "4h": 240,
    "8h": 480,
    "12h": 720,
    "1d": 1440,
    "1w": 10080
}

# Kucoin API symbols to understandable dev-symbols
symbols_dict_kucoin = {
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

# Binance API symbols to understandable dev-symbols
symbols_dict_binance = {
    "BTC": "BTCUSDT",
    "ETH": "ETHUSDT",
}
