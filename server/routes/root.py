from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router_root = APIRouter()

@router_root.get("/", tags=["Root"])
async def root():
    content = {"message": "Welcome to Root"}
    response = JSONResponse(content=content, 
                            status_code=status.HTTP_200_OK)
    return response
