from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

fake_items_db = [
    {"id": 1, "name": "Ноутбук", "description": "Портативный компьютер", "price": 50000.0},
    {"id": 2, "name": "Мышь", "description": "Компьютерная мышь", "price": 1000.0},
    {"id": 3, "name": "Клавиатура", "description": "Механическая клавиатура", "price": 5000.0},
]

@router.get("/", response_model=List[Item])
async def get_items():
    """Получить все элементы"""
    return fake_items_db

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Получить элемент по ID"""
    for item in fake_items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Элемент не найден")

@router.post("/", response_model=Item)
async def create_item(item: Item):
    """Создать новый элемент"""
    # Генерируем ID
    if fake_items_db:
        new_id = max(item["id"] for item in fake_items_db) + 1
    else:
        new_id = 1
    
    new_item = {
        "id": new_id,
        "name": item.name,
        "description": item.description,
        "price": item.price
    }
    fake_items_db.append(new_item)
    return new_item

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """Обновить элемент по ID"""
    for i, existing_item in enumerate(fake_items_db):
        if existing_item["id"] == item_id:
            updated_item = {
                "id": item_id,
                "name": item.name,
                "description": item.description,
                "price": item.price
            }
            fake_items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Элемент не найден")

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    """Удалить элемент по ID"""
    for i, item in enumerate(fake_items_db):
        if item["id"] == item_id:
            deleted_item = fake_items_db.pop(i)
            return {"message": "Элемент удалён", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Элемент не найден")