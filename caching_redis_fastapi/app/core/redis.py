from redis.asyncio import Redis
from app.core.config import Settings

redis: Redis | None = None

async def init_redis()-> None:
    global redis
    redis = Redis(
        host=Settings.REDIS_HOST,
        port = Settings.REDIS_PORT,
        db=Settings.REDIS_DB,
        decode_responses=True # str insead of byte
    )
    
async def close_redis() -> None:
    if redis:
        redis.close()