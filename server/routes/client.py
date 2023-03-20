from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse

from server.models.crypto import (IntervalBinance, symbols_dict_binance)
from server.database.db import (
    find_many_candles,
    find_one_candle,
    find_last_candle,
)
from server.routes.utils import CandleNotFoundException
from server.utils import get_timestamp

router_client = APIRouter()


@router_client.get("/client/", tags=["Client"])
async def root():
    content = {"message": "Welcome to Client Root"}
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response


@router_client.get("/client/candles/{symbol}/{interval}", tags=["Client"],
                   response_description="Candles data for time range",
                   status_code=status.HTTP_200_OK)
async def get_candles_for_time_range(symbol: str, interval: IntervalBinance, time_start: int, time_end: int = get_timestamp()):
    try:
        content = await find_many_candles(symbol, interval.name, time_start, time_end)
        if len(content) is 0:
            raise CandleNotFoundException(symbol, interval.name)
    except CandleNotFoundException as e:
        content = {"message": str(e)}
        return JSONResponse(content=content,
                            status_code=status.HTTP_404_NOT_FOUND)
    except ConnectionError as e:
        content = {"message": str(e)}
        return JSONResponse(content=content,
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        content = {"message": str(e)}
        return JSONResponse(content=content,
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(content=content,
                        status_code=status.HTTP_200_OK)


@router_client.get("/client/candle/{symbol}/{interval}", tags=["Client"],
                   response_description="One candle data for timestamp",
                   status_code=status.HTTP_200_OK)
async def get_candle_for_timestamp(symbol: str, interval: IntervalBinance, timestamp: int):
    try:
        content = await find_one_candle(symbol, interval.name, timestamp)
        if len(content) is 0:
            raise CandleNotFoundException(symbol, interval.name)
    except CandleNotFoundException as e:
        content = {"message": str(e)}
        return JSONResponse(content=content,
                            status_code=status.HTTP_404_NOT_FOUND)
    except ConnectionError as e:
        content = {"message": str(e)}
        return JSONResponse(content=content,
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        content = {"message": str(e)}
        return JSONResponse(content=content,
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(content=content,
                        status_code=status.HTTP_200_OK)

@router_client.get("/client/candle/last/{symbol}/{interval}", tags=["Client"],
                   response_description="Last candle data from database",
                   status_code=status.HTTP_200_OK)
async def get_last_candle_from_db(symbol: str, interval: IntervalBinance):
    content = await find_last_candle(symbol, interval.name)
    response = JSONResponse(content=content,
                            status_code=status.HTTP_200_OK)
    return response

