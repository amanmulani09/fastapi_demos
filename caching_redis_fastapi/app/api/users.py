from fastapi import APIRouter, HTTPException
from app.cache.cache_service import CacheService
from app.models.user import User

router = APIRouter()

#simulate a slow db call

async def fetch_user_from_db(user_id:str) -> User:
    print('doing actual api call....')
    return User(
        id=user_id,
        name="Johnrao deokar",
        email="cooljohn@gmail.com"
    )
    
@router.get("/users/{user_id}",response_model=User)
async def get_user(user_id:str):
    cache_key = f"user:{user_id}:profile:v1"
    ttl = 300 # in seconds (5 min)
    
    # try cache 
    cached_user = await CacheService.get(cache_key)
    
    if cached_user:
        print('returning from cache....')
        return cached_user
    
    #cache miss 
    
    user = await fetch_user_from_db(user_id)
    
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    
    # store in cache 
    
    await CacheService.set(
        key=cache_key,
        value=user,
        ttl=ttl
    )
    
    return user