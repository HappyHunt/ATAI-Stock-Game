import motor.motor_asyncio
import configparser as cfg


CONFIG_FILEPATH = './server/config.ini'

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
    # Get apropriate collection
    collection = get_collection(currency, timeframe)

    # Check if there is already existed candlestick data for provided timestamp
    n = await collection.find_one({'timestamp' : candle_data['timestamp']})
    if n is not None:
        return None

    # Add to database
    candle = await collection.insert_one(candle_data)
    
    # Get already inserted document and return it
    new_candle = await collection.find_one({"_id": candle.inserted_id})
    return candle_helper(new_candle)
