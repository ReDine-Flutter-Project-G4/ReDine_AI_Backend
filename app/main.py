import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address

from .routers import ai_router

load_dotenv()
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

origins = os.getenv("BACKEND_ORIGINS", "")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.state.limiter = limiter

app.include_router(ai_router)
@app.get("/api/test")
def root():
    return {"message": "Hello FastAPI"}