from fastapi import APIRouter
from app.api import choice, question

api_router = APIRouter() # APIRouter is used to create or combine multiple routers 

api_router.include_router(choice.router)
api_router.include_router(question.router)