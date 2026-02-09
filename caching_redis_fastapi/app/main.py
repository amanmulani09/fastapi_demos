from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.users import router as user_router
from app.core.redis import init_redis, close_redis
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis()
    yield
    await close_redis()


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan,
)

app.include_router(user_router)
