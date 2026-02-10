import json
from typing import Any, Optional
from pydantic import BaseModel
from app.core.redis import get_redis


class CacheService:
    @staticmethod
    async def get(key: str) -> Optional[Any]:
        redis = get_redis()
        value = await redis.get(key)
        return json.loads(value) if value else None

    @staticmethod
    async def set(key: str, value: Any, ttl: int) -> None:
        redis = get_redis()
        # Convert Pydantic models to dict before JSON serialization
        if isinstance(value, BaseModel):
            value = value.model_dump()
        await redis.set(key, json.dumps(value), ex=ttl)

    @staticmethod
    async def delete(key: str) -> None:
        redis = get_redis()
        await redis.delete(key)
