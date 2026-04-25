# main.py 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sidebar

app = FastAPI()


from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sidebar.router)
@app.get("/")
def root():
    return {"status":"ok"}


