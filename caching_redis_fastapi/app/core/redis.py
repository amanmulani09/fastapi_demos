from redis.asyncio import Redis
from app.core.config import settings

_redis: Redis | None = None


async def init_redis() -> None:
    global _redis
    if _redis is None:
        _redis = Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True,
        )


async def close_redis() -> None:
    if _redis is not None:
        await _redis.close()


def get_redis() -> Redis:
    if _redis is None:
        raise RuntimeError("Redis not initialized. Did lifespan run?")
    return _redis
