from fastapi import APIRouter
from atai.kucoin_client import KucoinClient
from atai.indicators.ta import sma

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/indicators/sma")
async def indicator_sma():
    src = [1, 5, 6, 7, 9, 1, 3, 4, 5, 5, 6, 7, 8, 2, 15, 64, 38, 95, 15, 48]
    return sma(src, 2)

@router.get("/contract-list")
async def contract_list():
    return KucoinClient.client.kucoin_client_market.get_contracts_list()


@router.get("/aaa")
async def contract_list():
    return KucoinClient.client.kucoin_client_market.get_kline_data(".KXBTUSDT", 1)

