import configparser
from kucoin_futures.client import Trade
import pymongo


class Init:
    def __init__(self, config_filepath : str) -> None:
        # Config file read
        self._config = configparser.ConfigParser()
        self._config.read(config_filepath)

        # Config variables read
        #   Database
        self._server = self._config.get('DATABASE', 'server')
        self._database = self._config.get('DATABASE', 'database')

        #   Kucoin API
        self._api_key = self._config.get('KUCOIN', 'api_key')
        self._api_secret = self._config.get('KUCOIN', 'api_secret')
        self._api_passphrase = self._config.get('KUCOIN', 'api_passphrase')

        # Connections init
        self._client = pymongo.MongoClient(self._server)
        self._kucoin_client = Trade(self._api_key, self._api_secret, self._api_passphrase)
        self._db = self._client[self._database]

    def get_db(self):
        return self._db

    def get_kucoin_client(self):
        return self._kucoin_client
