from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.router import api_router
from app.db.session import db_connection

@asynccontextmanager
async def lifespan(app:FastAPI): # lifespan consider this as a useEffect & component lifecycles 
    # startup
    db_connection()
    
app = FastAPI(lifespan=lifespan) # execute the life span before the app startup and after the app ends 
app.include_router(api_router,prefix='/api')