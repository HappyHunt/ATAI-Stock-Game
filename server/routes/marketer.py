from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models.candle import CandlestickSchema
from models.responses import ResponseModel, ErrorResponseModel
from database.db import (
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
                    response_description="Candlestick data added into the database")
async def add_candlestick_data(currency: str, timeframe: int, candle: CandlestickSchema = Body(...)):
    candle = jsonable_encoder(candle)
    new_candle = await add_candle(candle, currency, timeframe)
    return ResponseModel(new_candle, "Candlestick added succsessfully.")