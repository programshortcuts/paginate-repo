# routes/sidebar.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ GET all items
@router.get("/sidebar")
def get_sidebar_items(db: Session = Depends(get_db)):
    return db.query(models.SidebarItem).all()

# ✅ POST new item
@router.post("/sidebar")
def add_sidebar_item(item: dict, db: Session = Depends(get_db)):
    new_item = models.SidebarItem(title=item["title"])
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item