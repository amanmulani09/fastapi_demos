from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class ProductBase(BaseModel):
    name : str = Field(min_length=3)
    price : float = Field(gt=0, lt=100000)
    stock : int = Field(ge=0)
    category: Optional[str] = None
    
class ProductCreate(ProductBase):
    pass
    
class ProductResponse(BaseModel):
    message: str
    product:ProductBase


@app.post('/products',response_model=ProductResponse)
async def create_products(product:ProductCreate):
    return {
        "message":"product created",
        "product":product
    }