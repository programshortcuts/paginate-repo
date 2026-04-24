from fastapi import APIRouter
from app.data import SIDEBAR_DATA

router = APIRouter()

@router.get("/sidebar")
def get_sidebar():
    return {"sidebar": SIDEBAR_DATA}