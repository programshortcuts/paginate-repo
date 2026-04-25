# routes/sidebar.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/sidebar")
def get_sidebar():
    return [
        {"id": 1, "title": "Home", "slug": "home"},
        {"id": 2, "title": "Lessons", "slug": "lessons"},
        {"id": 3, "title": "Settings", "slug": "settings"},
    ]