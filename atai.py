import sys
import uvicorn
import threading
from atai.kucoin_client import (KucoinClient, bg_thread_work)
from configparser import NoOptionError
from fastapi import FastAPI
from atai.views import sample_view
from atai.initializer import Init


# App Config globals
CONFIG_FILE = './config.ini'
HOST = '127.0.0.1'
PORT = 8000


# DB, Kucoin API client inits
def init() -> bool:
    global db, trade, market

    try:
        initializer = Init(CONFIG_FILE)
        db = initializer.get_db()
        trade = initializer.get_kucoin_client_trade()
        market = initializer.get_kucoin_client_market()

    #   Config file does not exists
    except FileNotFoundError as e:
        print('--- INIT EXCEPTION ---')
        print(' -- ConfigFile Existance --')
        print(f'\t{e}')
        return False

    #   Invalid config syntax
    except NoOptionError as e:
        print('--- INIT EXCEPTION ---')
        print(' -- ConfigFile Syntax --')
        print(f'\t{e}')
        return False

    #   Database Connection refused
    except ConnectionError as e:
        print('--- INIT EXCEPTION ---')
        print(' -- MongoDB Connection --')
        print(f'\t{e}')
        return False

    #   Other exceptions
    except Exception as e:
        print('--- INIT EXCEPTION ---')
        print(' -- Unexpected Exception --')
        print(f'\t{type(e)}')
        print(f'\t{e}')
        return False
    
    return True


# Main Drive
def main():
    global app

    # Fast API init
    app = FastAPI()
    app.include_router(sample_view.router)

    # DB, Kucoin API client inits
    if not init():
        sys.exit(1)

    # Background collector thread
    kucoin_client = KucoinClient(trade=trade, market=market, db=db)
    KucoinClient.client = kucoin_client

    t = threading.Thread(target=bg_thread_work, args=(kucoin_client,), daemon=True)
    t.start()

    # App Run
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == '__main__':
    main()
    