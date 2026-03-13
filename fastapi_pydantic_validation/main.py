from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()

class CreateUser(BaseModel):
    name : str = Field(...,min_length=3,max_length=50)
    age : int = Field(..., gt=18,lt=60)
    email: EmailStr
    
    # custom validation 
    
   
class CreateProduct(BaseModel):
    name : str = Field(min_length=3)
    price: float = Field(gt=0, lt=100000)   
    stock: int = Field(gt=0,)
    category:Optional[str] = None

@app.post('/user')
def create_user(user:CreateUser): #CreateUser is the schema of the request body
    return {
        "msg":"user created successfully",
        "data":user
    }

