from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from server.models.candle import CandlestickSchema, CandlestickSchemaList
from server.models.crypto import Timeframe
from server.models.responses import ResponseModel, ErrorResponseModel
from server.database.db import (
        add_candle,
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
async def add_single_candlestick_data(currency: str, timeframe: Timeframe, candle: CandlestickSchema = Body(...)):
    candle = jsonable_encoder(candle)
    new_candle = await add_candle(candle, currency, timeframe.name)

    if new_candle is None:
        return JSONResponse(ErrorResponseModel(error="",
                                               message="Provided candlestick data already exists.",
                                               code=status.HTTP_406_NOT_ACCEPTABLE),
                            status_code=status.HTTP_406_NOT_ACCEPTABLE
                            )

    return JSONResponse(ResponseModel(data=new_candle, 
                                      message=f"Candlestick added succsessfully to collection {currency}.{timeframe.name}",
                                      code=status.HTTP_201_CREATED),
                        status_code=status.HTTP_201_CREATED
                        )


@router_market.post("/market/candles/{currency}/{timeframe}", tags=["Market"],
                    response_description="Candlesticks data added to database collection named ${currency}.{timeframe.name}",
                    status_code=status.HTTP_201_CREATED)
async def add_multi_cadlestick_data(currency: str, timeframe: Timeframe, candles: CandlestickSchemaList = Body(...)):
    new_candles = []
    
    for i in range(len(candles.candles)):
        new_candle = await add_candle(jsonable_encoder(candles.candles[i]), currency, timeframe.name)
        
        if new_candle is not None:
            new_candles.append(new_candle)

    if len(new_candles) == 0:
        return JSONResponse(ErrorResponseModel(error="",
                                               message="All provided candlesticks data already exists.",
                                               code=status.HTTP_406_NOT_ACCEPTABLE),
                            status_code=status.HTTP_406_NOT_ACCEPTABLE
                            )

    return JSONResponse(ResponseModel(data=new_candles, 
                                      message=f"{len(new_candles)} of {len(candles.candles)} candlesticks added succsessfully to collection {currency}.{timeframe.name}",
                                      code=status.HTTP_201_CREATED),
                        status_code=status.HTTP_201_CREATED
                        )
