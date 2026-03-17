from fastapi import FastAPI, Depends
from typing import Annotated
app = FastAPI()

class Logger:
    def log(_self,message:str):
        print(f"logging message : {message}")
    
 
def get_logger():
    return Logger()        

logger_deps = Annotated[Logger, Depends(get_logger)]
        
@app.get('/log/{message}')
def log_message(message:str, logger:logger_deps):
    
    logger.log(message)
    
    return message


class EmailService:
    def send_email(receipent:str,email:str):
        print(f"sending email : {email} to {receipent}")
        
        
# a fn to get the EmailService instance

def get_email_service():
    return EmailService()

# a dependecy of email service 

email_service_deps = Annotated[EmailService, Depends(get_email_service)]

def send_email(receipent:str,email:str,email_service:email_service_deps):
    
    email_service.send_email(receipent,email)