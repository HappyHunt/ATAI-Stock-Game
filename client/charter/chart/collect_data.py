from client.charter.chart import my_requests
from server.models.crypto import IntervalBinance


class Charter(object):
    def __init__(self, symbol: str, interval: IntervalBinance):
        self.symbol = symbol
        self.interval = interval

    def get_data(self):
        data = my_requests.get_data_for_interval(self.symbol, self.interval, 1268743500000, 1678970700000)
        return data
