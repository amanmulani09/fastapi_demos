from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, Field
app = FastAPI()


class Template(BaseModel):
    template: str = Field(max_length=500)


def write_notification(email:str,template=""):
    
    with open("log.txt",mode="w") as email_file :
        content = f"notification for {email}: {template}"
        email_file.write(content)
        

@app.post('/send_notification/{email}')
async def send_notification(email:str, template:Template, background_task:BackgroundTasks):
    background_task.add_task(write_notification, email, template)
    return {"message":"email notification is being processed"}