import motor.motor_asyncio
import configparser as cfg

from models.candle import TIMEFRAMES, CRYPTO_CURRENCIES


class DatabaseMongo:
    def __init__(self, config_filepath: str) -> None:

        # Config handle
        #   * Open
        self._config = cfg.ConfigParser()
        self._config.read(config_filepath)

        #   * Read
        self._db_srv_addr = self._config.get('DATABASE', 'server_addr')
        self._db_srv_port = self._config.get('DATABASE', 'server_port')
        self._db_name = self._config.get('DATABASE', 'db_name')

        # Mongo DB
        mongo_details = f"mongodb://{self._db_srv_addr}:{self._db_srv_port}"

        #   * Connect
        self._client = motor.motor_asyncio.AsyncIOMotorClient(mongo_details)

        #   * Database
        self._db = self._client[self._db_name]


    def get_collection(self, currency: str, timeframe: int):
        return self._db.get_collection(f'{currency}.{timeframe}')