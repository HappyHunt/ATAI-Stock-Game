from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from server.models.crypto import IntervalBinance
from server.database.db import (
    find_many_candles
)

router_charter = APIRouter()


@router_charter.get("/chart/", tags=["Chart"])
async def root():
    content = {"message": "Welcome to Chart Root"}
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response


@router_charter.get("/chart/candles/{symbol}/{interval}", tags=["Chart"],
                    response_description="Candles data download from database",
                    status_code=status.HTTP_200_OK)
async def get_candles_from_db(symbol: str, interval: IntervalBinance, time_start: int, time_end: int):
    content = await find_many_candles(symbol, interval.name, time_start, time_end)
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response

