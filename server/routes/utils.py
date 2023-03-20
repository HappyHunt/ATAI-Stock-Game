class CandleNotFoundException(Exception):
    def __init__(self, symbol: str, interval: str):
        self.message = f"Candle for symbol '{symbol}' and interval '{interval}' not found."
        super().__init__(self.message)
