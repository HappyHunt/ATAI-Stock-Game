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
    return KucoinClient.client.kucoin_client_market.get_contracts_list()


@router.get("/aaa")
async def contract_list():
    return KucoinClient.client.kucoin_client_market.get_kline_data(".KXBTUSDT", 1)

