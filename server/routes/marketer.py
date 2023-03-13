from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router_market = APIRouter()

@router_market.get("/market/", tags=["Market"])
async def root():
    content = {"message": "Welcome to Market Root"}
    response = JSONResponse(content=content, 
                            status_code=status.HTTP_200_OK)
    return response
