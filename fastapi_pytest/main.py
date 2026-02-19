from fastapi import FastAPI, HTTPException
from models import Task
from typing import List

app = FastAPI()

# in memory DB
tasks = []
    
@app.post('/task',response_model=Task)
async def create_task(task:Task):
    tasks.append(task)
    return task

@app.get('/tasks',response_model=List[Task])
async def get_tasks():
    return tasks

@app.get('/task/{id}')
async def get_task(id:int):
    for task in tasks:
        if(task.id == id):
            return task
    raise HTTPException(status_code=404, detail="Task Not Found")