from .utils import check_required_parameters


def klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data**
    | *Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.*
    :API endpoint: ``GET /fapi/v1/klines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data
    :parameter symbol: string; the trading symbol.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/klines", params)


# TODO
"""
ADD QUERY HERE AND IMPORT IT IN FUTURES
"""
