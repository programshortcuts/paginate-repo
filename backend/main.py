# main.py 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.sidebar import router as sidebar_router


app = FastAPI()

from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(sidebar_router, prefix="/api")
@app.get("/")
def root():
    return {"status":"ok"}