from jose import jwt
from datetime import datetime, timedelta
import uuid
from passlib.context import CryptContext
from store.auth_store import refresh_sessions

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)

def create_access_token(user_id:str):
    
    payload = {
        "sub":user_id,
        "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def create_refresh_token(user_id:str):
    
    token_id = str(uuid.uuid4())
    
    refresh_sessions[token_id] = {
        "user_id":user_id,
        "expires":datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    }
    
    return token_id