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