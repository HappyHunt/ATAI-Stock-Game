import configparser
import pymongo
from kucoin_futures.client import Trade
from pathlib import Path


class Init:
    def __init__(self, config_filepath : str) -> None:
        # Config file read
        #   Config file existance check
        path = Path(config_filepath)
        if not path.exists():
            raise FileNotFoundError(f'{path.absolute()} : File does not exists')

        #   Config content read
        self._config = configparser.ConfigParser()
        self._config.read(config_filepath)

        # Config variables read
        #   Database
        srv_addr = self._config.get('DATABASE', 'server_addr')
        srv_port = int(self._config.get('DATABASE', 'server_port'))
        self._server = (srv_addr, srv_port)
        self._database = self._config.get('DATABASE', 'database')
        
        #   Kucoin API
        self._api_key = self._config.get('KUCOIN', 'api_key')
        self._api_secret = self._config.get('KUCOIN', 'api_secret')
        self._api_passphrase = self._config.get('KUCOIN', 'api_passphrase')

        # Connections init
        #   Database
        self._client = pymongo.MongoClient(self._server[0], self._server[1], serverSelectionTimeoutMS=3000)
        self._db = self._client[self._database]

        #   Database connection check
        try:
            self._client.admin.command('ismaster')
        except pymongo.errors.ServerSelectionTimeoutError:
            raise ConnectionError(f"MongoDB : server is not available at mongodb://{self._server[0]}:{self._server[1]}/")
        
        #   Kucoin API
        self._kucoin_client = Trade(self._api_key, self._api_secret, self._api_passphrase)



    def get_db(self):
        return self._db


    def get_kucoin_client(self) -> Trade:
        return self._kucoin_client