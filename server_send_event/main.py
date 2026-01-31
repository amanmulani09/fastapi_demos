from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time 

app = FastAPI()

def event_generator():
    for i in range(1,6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)
        
@app.get('/events')
def sse_events():
    return StreamingResponse ( # to stream the constant response 
        event_generator(), 
        media_type="text/event-stream"
    )