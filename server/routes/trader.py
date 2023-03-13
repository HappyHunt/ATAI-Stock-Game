from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router_trade = APIRouter()

@router_trade.get("/trader/", tags=["Trade"])
async def root():
    content = {"message": "Welcome to Trade Root"}
    response = JSONResponse(content=content, 
                            status_code=status.HTTP_200_OK)
    return response
