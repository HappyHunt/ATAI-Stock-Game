import motor.motor_asyncio
import configparser as cfg

from server.utils import get_timestamp

CONFIG_FILEPATH = './config.ini'

# Config handle
#   * Open
config = cfg.ConfigParser()
config.read(CONFIG_FILEPATH)

#   * Read
DB_SRV_ADDR = config.get('DATABASE', 'server_addr')
DB_SRV_PORT = config.get('DATABASE', 'server_port')
DB_NAME = config.get('DATABASE', 'db_name')

# Mongo DB

MONGO_DETAILS = f"mongodb://{DB_SRV_ADDR}:{DB_SRV_PORT}"

#   * Connect
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

#   * Database
database = client[DB_NAME]


# *** Collections ***
def get_collection(currency: str, timeframe: str):
    return database.get_collection(f'{currency}.{timeframe}')


# *** Helpers ***
def candle_helper(candle) -> dict:
    # Convert candle document obj to dict
    return {
        "id": str(candle["_id"]),
        "timestamp": candle["timestamp"],
        "entry_price": candle["entry_price"],
        "highest_price": candle["highest_price"],
        "lowest_price": candle["lowest_price"],
        "close_price": candle["close_price"],
        "volume": candle["volume"],
    }


# *** Add ***
async def add_candle(candle_data: dict, currency: str, timeframe: str) -> dict | None:
    # Get appropriate collection
    collection = get_collection(currency, timeframe)

    # Check if there is already existed candlestick data for provided timestamp
    n = await collection.find_one({'timestamp': candle_data['timestamp']})
    if n is not None:
        return None

    # Add to database
    candle = await collection.insert_one(candle_data)

    # Get already inserted document and return it
    new_candle = await collection.find_one({"_id": candle.inserted_id})
    return candle_helper(new_candle)


async def add_many_candles(candles_data: list, currency: str, timeframe: str) -> None:
    # Get appropriate collection
    collection = get_collection(currency, timeframe)

    await collection.insert_many(candles_data)


async def find_many_candles(symbol, interval: str, start_time: int = get_timestamp() - 1209600000,
                            end_time: int = get_timestamp()):
    result = []
    params = {
        'timestamp': {
            '$gt': start_time,
            '$lte': end_time
        }
    }
    sort = list({
                    'timestamp': 1
                }.items())
    project = {
        '_id': 0
    }
    col = get_collection(symbol, interval)

    async for i in col.find(filter=params, sort=sort, projection=project):
        result.append(i)
    return result


async def find_one_candle(symbol, interval: str, timestamp: int):
    params = {
        'timestamp': {
            '$eq': timestamp
        }
    }
    project = {
        '_id': 0
    }
    col = get_collection(symbol, interval)
    r = await col.find_one(filter=params, projection=project)
    return r


async def find_last_candle(symbol, interval: str):
    project = {
        '_id': 0
    }
    col = get_collection(symbol, interval)
    r = await col.find_one(sort=[('timestamp', -1)], projection=project)
    return r
