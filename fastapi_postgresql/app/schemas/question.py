from pydantic import BaseModel, ConfigDict
from app.schemas.choice import ChoiceCreate, ChoiceResponse
from typing import List

class QuestionBase(BaseModel):
    question_text:str
    
class QuestionCreate(BaseModel):
    choices:List[ChoiceCreate]
    
class QuestionResponse(QuestionBase):
    id:int
    choices: List[ChoiceResponse] = []
    
    model_config = ConfigDict(from_attributes=True)
    