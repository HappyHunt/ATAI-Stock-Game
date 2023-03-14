from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from server.models.candle import CandlestickSchema, CandlestickSchemaList
from server.models.crypto import IntervalKucoin
from server.models.responses import ResponseModel, ErrorResponseModel
from server.database.db import (
        add_candle,
        add_many_candles
    )

router_market = APIRouter()


@router_market.get("/market/", tags=["Market"])
async def root():
    content = {"message": "Welcome to Market Root"}
    response = JSONResponse(content=content, 
                            status_code=status.HTTP_200_OK)
    return response


@router_market.post("/market/candle/{currency}/{timeframe}", tags=["Market"],
                    response_description="Candlestick data added to database collection named ${currency}.{timeframe.name}",
                    status_code=status.HTTP_201_CREATED)
async def add_single_candlestick_data(currency: str, timeframe: IntervalKucoin, candle: CandlestickSchema = Body(...)):
    candle = jsonable_encoder(candle)
    new_candle = await add_candle(candle, currency, timeframe.name)

    if new_candle is None:
        return JSONResponse(ErrorResponseModel(error="",
                                               message="Provided candlestick data already exists.",
                                               code=status.HTTP_406_NOT_ACCEPTABLE),
                            status_code=status.HTTP_406_NOT_ACCEPTABLE
                            )

    return JSONResponse(ResponseModel(data=new_candle, 
                                      message=f"Candlestick added successfully to collection {currency}.{timeframe.name}",
                                      code=status.HTTP_201_CREATED),
                        status_code=status.HTTP_201_CREATED
                        )


@router_market.post("/market/candles/{currency}/{timeframe}", tags=["Market"],
                    response_description="Candlesticks data added to database collection named ${currency}.{timeframe.name}",
                    status_code=status.HTTP_201_CREATED)
async def add_many_candlestick_data(currency: str, timeframe: IntervalKucoin, candles: CandlestickSchemaList = Body(...)):
    candles_list = []
    for candle in candles.candles:
        candles_list.append(candle.dict())
    candles_list = jsonable_encoder(candles_list)

    await add_many_candles(candles_list, currency, timeframe.name)
    return JSONResponse(ResponseModel(data="",
                                      message=f"{len(candles_list)} candlesticks added successfully to collection {currency}.{timeframe.name}",
                                      code=status.HTTP_201_CREATED),
                        status_code=status.HTTP_201_CREATED
                        )
