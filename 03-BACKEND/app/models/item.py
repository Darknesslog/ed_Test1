from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    """Модель элемента"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Ноутбук",
                "description": "Портативный компьютер",
                "price": 50000.0
            }
        }