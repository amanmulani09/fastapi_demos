from fastapi import FastAPI
from pydantic import BaseModel, Field
from logger import setup_logger
import httpx

logger = setup_logger()

class Blog(BaseModel):
    id: str
    title: str = Field(max_length=50)
    content:str
    author: str


blogs = []

app = FastAPI()

@app.post('/blog')
async def create_post(blog:Blog):
    blogs.append(blog)
    logger.info(f"current all blogs : {blogs}")
    
    return {"blog created successfully1"}
    
    
@app.get('/external-posts')
async def get_external_posts():
    
    async with httpx.AsyncClient() as client:
        res = await client.get('https://jsonplaceholder.typicode.com/posts')
       
    external_posts : list = res.json()
    return external_posts[5:10] 