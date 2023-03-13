import uvicorn
from fastapi import FastAPI

import database.db
import routes.root as root
import routes.trader as trader
import routes.marketer as marketer


def main():
    # API Init
    app = FastAPI()
    #   * Routers
    app.include_router(root.router_root)
    app.include_router(trader.router_trade)
    app.include_router(marketer.router_market)

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()