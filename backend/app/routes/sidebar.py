# routes/sidebar.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# temporary in-memory database
sidebar_items = [
    {"id": 1, "title": "Home"},
    {"id": 2, "title": "Lessons"},
]

class SidebarItem(BaseModel):
    title: str


@router.get("/sidebar")
def get_sidebar():
    return sidebar_items


@router.post("/sidebar")
def add_sidebar_item(item: SidebarItem):
    new_item = {
        "id": len(sidebar_items) + 1,
        "title": item.title
    }
    sidebar_items.append(new_item)
    return new_item