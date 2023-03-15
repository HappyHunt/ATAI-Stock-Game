import uvicorn
from fastapi import FastAPI

import server.routes.root as root
import server.routes.trader as trader
import server.routes.marketer as marketer
import server.routes.charter as charter


# API Init
app = FastAPI()
#   * Routers
app.include_router(root.router_root)
app.include_router(trader.router_trade)
app.include_router(marketer.router_market)
app.include_router(charter.router_charter)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()
