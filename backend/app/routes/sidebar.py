# routes/sidebar.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ GET (read sidebar items)
@router.get("/sidebar")
def get_sidebar(db: Session = Depends(get_db)):
    return db.query(models.SidebarItem).all()

# ✅ POST (add sidebar item)
@router.post("/sidebar")
def add_sidebar_item(item: dict, db: Session = Depends(get_db)):
    new_item = models.SidebarItem(title=item["title"])
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item