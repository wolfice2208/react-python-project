from fastapi import APIRouter
from models.item import Item

router = APIRouter(prefix="/items", tags=["items"])

items_db = []

@router.get("/")
def get_items():
    return items_db

@router.post("/")
def create_item(item: Item):
    items_db.append(item)
    return item