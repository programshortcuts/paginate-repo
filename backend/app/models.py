# models.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class SidebarItem(Base):
    __tablename__ = "sidebar_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)