from fastapi import FastAPI, Depends, HTTPException
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
    
class Authservice:
    def validate_token(_self,token:str):
        
        if(token == "valid-token"):
            return True
        else: 
            raise HTTPException(status_code=401, detail="unauthorized user")
        
# create a fn to create auth service instance

def get_auth_service():
    return Authservice()

# create a auth service dependecy 

auth_service_deps = Annotated[Authservice, Depends(get_auth_service)]

@app.post('/generate-report')
def generate_report(token:str,auth_service:auth_service_deps):
    
    is_authenticated_user = auth_service.validate_token(token)
    
    if is_authenticated_user:
        return {"billo bagge billiya da ki karegi..."}