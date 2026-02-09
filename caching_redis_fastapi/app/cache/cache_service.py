import json 
from typing import Any, Optional
from app.core.redis import redis


class CacheService:
    @staticmethod
    async def get(key:str) -> Optional[Any]:
        value = await redis.get(key)
        
        if value is None:
            return None
        return json.loads(value)
    
    @staticmethod
    async def set(key:str,value:Any,ttl:int) -> None:
        await redis.set(
            key,
            json.dumps(value),
            ex=ttl
        )
        
    @staticmethod
    async def delte(key:str) -> None:
        await redis.delete(key)