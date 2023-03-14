from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router_trade = APIRouter()

@router_trade.get("/trader/", tags=["Trade"])
async def root():
    content = {"message": "Welcome to Trade Root"}
    response = JSONResponse(content=content, 
                            status_code=status.HTTP_200_OK)
    return response

@router_trade.get("/trader/candle/{currency}/{timeframe}", tags=["Trade"])
async def get_candle_data(currency: str, timeframe: int, amount: int = 1):
    return {"message": "Candlestick data will be stored here"}