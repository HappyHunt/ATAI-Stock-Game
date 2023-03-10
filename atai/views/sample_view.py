from fastapi import APIRouter
from atai.kucoin_client import KucoinClient

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/contract-list")
async def contract_list():
    data = KucoinClient.client.kucoin_client_market.get_contracts_list()
    return data


@router.get("/crypto/{name}/{timeframe}")
async def crypto(name: str, timeframe: int):
    if timeframe in [1, 5, 15, 60]:
        if name.lower() == 'btc':
            return KucoinClient.client.kucoin_client_market.get_kline_data("XBTUSDTM", timeframe)
        elif name.lower() == 'eth':
            return KucoinClient.client.kucoin_client_market.get_kline_data("ETHUSDTM", timeframe)
    
    return {"code" : "400001",
            "msg" : "Invalid Input"}        
