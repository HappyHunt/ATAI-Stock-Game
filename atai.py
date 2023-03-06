import sys
import uvicorn
from configparser import NoOptionError
from fastapi import FastAPI
from atai.views import sample_view
from atai.initializer import Init


# App Config globals
CONFIG_FILE = './config_legit.ini'
HOST = '127.0.0.1'
PORT = 8000


# DB, Kucoin API client inits
def init() -> bool:
    global db, kucoin

    try:
        init = Init(CONFIG_FILE)
        db = init.get_db()
        kucoin = init.get_kucoin_client()

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
    if not init(): sys.exit(1)

    # App Run
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == '__main__':
    main()
    