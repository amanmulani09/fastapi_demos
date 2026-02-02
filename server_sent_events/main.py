from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

import asyncio
import uuid 

app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

job_progres = {}

async def long_running_job(job_id:str):
    for percent in range(0,101,10):
        job_progres[job_id] = percent
        await asyncio.sleep(1)
        
    job_progres[job_id] = "done"
    
# normal rest api start the job 

@app.post("/start-job")
async def start_job(background_tasks:BackgroundTasks):
    job_id = str(uuid.uuid4())
    job_progres[job_id] = 0
    
    background_tasks.add_task(long_running_job,job_id)
    
    return {"job_id":job_id}
#SSE endpoint

@app.get('/progress/{job_id}')
async def progress_stream(job_id:str):
    async def event_generator():
        while True:
            progress = job_progres.get(job_id)
            
            if progress == "done":
                yield "data: Done\n\n"
                break
            yield f"data:{progress}\n\n"
            await asyncio.sleep(1)
            
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )