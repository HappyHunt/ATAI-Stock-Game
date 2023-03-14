import uvicorn
from fastapi import FastAPI

import server.database.db
import server.routes.root as root
import server.routes.trader as trader
import server.routes.marketer as marketer


# API Init
app = FastAPI()
#   * Routers
app.include_router(root.router_root)
app.include_router(trader.router_trade)
app.include_router(marketer.router_market)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()