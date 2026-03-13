from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import re

app = FastAPI()

class UserBase(BaseModel):
    username : str = Field(min_length=3, max_length=20)
    email : EmailStr
    password : str = Field(min_length=8)
    age : int = Field(gt=18)
    bio : Optional[str] = None
    
    @field_validator("password")
    @classmethod
    def validate_password(cls,value):
        
        regrex = r'^(?=.*[A-Z])(?=.*\d).+$'
        result = bool(re.match(regrex,value))
        
        if not result:
            raise ValueError("Please use a valid password")
    

class UserRegisterRequest(UserBase):
    pass
    
class UserRegisterResponse(BaseModel):
    message : str
    user : UserBase 

@app.post('/user',response_model=UserRegisterResponse)
async def register_user(user:UserRegisterRequest):
    return {
        "message":"user created successfully",
        "user":user
    }
