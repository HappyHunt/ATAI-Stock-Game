import uvicorn
from fastapi import FastAPI
from atai.views import sample_view
from atai.initializer import Init

# App Config globals
CONFIG_FILE = './config.ini'
HOST = 'localhost'
PORT = 8000


def main():
    global app, db, kucoin

    # Fast API init
    app = FastAPI()
    app.include_router(sample_view.router)

    # DB, Kucoin API client inits
    init = Init(CONFIG_FILE)
    db = init.get_db()
    kucoin = init.get_kucoin_client()

    # App Run
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == '__main__':
    main()
    