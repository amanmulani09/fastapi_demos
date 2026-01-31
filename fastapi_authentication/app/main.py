from app.data.users import user_db
from app.auth.authentication import create_access_token, get_current_user

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.get('/')
def root():
    return {"welcome to the app"}

@app.post('/token')
async def login_for_access_token(form_data:OAuth2PasswordRequestForm= Depends()):
    user = user_db.get(form_data.username)
    print(user,'user--')
    print(form_data.password,'form_data')
    if user is None or user.password != form_data.password:
        raise HTTPException(status_code=400, detail='incorrect username or password')
    access_token = create_access_token(data={"sub":user.username})
    return {"access_token": access_token, "token_type":"bearer"}


@app.get('/protected')
async def protected_route(username:str = Depends(get_current_user)):
    return {"message": f"Hello, {username}! This is a protected resource."}
