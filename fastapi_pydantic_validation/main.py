from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()

class UserBase(BaseModel):
    name : str = Field(...,min_length=3,max_length=50)
    age : int = Field(..., gt=18,lt=60)
    email: EmailStr
class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    msg: str
    data:UserBase    

@app.post('/user',response_model=UserResponse)
def create_user(user:UserCreate): #CreateUser is the schema of the request body
    return {
        "msg":"user created successfully",
        "data":user
    }

async def get_user(user_id:str):
    
