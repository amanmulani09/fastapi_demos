from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jose import JWTError, jwt 
from datetime import datetime, timedelta

SECRET_KEY = 'random_secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 8  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# fn to create the access token 
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token:str = Depends(oauth2_scheme)):
    
    credential_exception = HTTPException(
        status_code=401,
        detail="could not validate token",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    try: 
        payload = jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        username:str = payload.get('sub')
        if username is None:
            raise credential_exception
        return username
    except JWTError:
        raise credential_exception