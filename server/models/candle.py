from typing import List
from pydantic import BaseModel, Field


class CandlestickSchema(BaseModel):
    timestamp: int = Field(..., gt=0)
    entry_price: float = Field(..., gt=0)
    highest_price: float = Field(..., gt=0)
    lowest_price: float = Field(..., gt=0)
    close_price: float = Field(..., gt=0)
    volume: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "timestamp": 1678734120000,
                "entry_price": 24346.0,
                "highest_price": 24366.0,
                "lowest_price": 24337.0,
                "close_price": 24364.0,
                "volume": 70653.0
            }
        }


class CandlestickSchemaList(BaseModel):
    candles: List[CandlestickSchema] = Field(...)
