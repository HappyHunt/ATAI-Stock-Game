from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from server.models.crypto import (IntervalBinance, symbols_dict_binance)
from server.database.db import (
    find_many_candles,
    find_one_candle,
    find_last_candle
)

router_client = APIRouter()


@router_client.get("/client/", tags=["Client"])
async def root():
    content = {"message": "Welcome to Client Root"}
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response


@router_client.get("/client/candles/{symbol}/{interval}", tags=["Client"],
                   response_description="Candles data download from database",
                   status_code=status.HTTP_200_OK)
async def get_candles_from_db(symbol: str, interval: IntervalBinance, time_start: int, time_end: int):
    content = await find_many_candles(symbol, interval.name, time_start, time_end)
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response


@router_client.get("/client/candle/{symbol}/{interval}", tags=["Client"],
                   response_description="Candle data download from database",
                   status_code=status.HTTP_200_OK)
async def get_candle_from_db(symbol: str, interval: IntervalBinance, timestamp: int):
    content = await find_one_candle(symbol, interval.name, timestamp)
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response


@router_client.get("/client/candle/last/{symbol}/{interval}", tags=["Client"],
                   response_description="Candle data download from database",
                   status_code=status.HTTP_200_OK)
async def get_last_candle_from_db(symbol: str, interval: IntervalBinance):
    content = await find_last_candle(symbol, interval.name)
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response
