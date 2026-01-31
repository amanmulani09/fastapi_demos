from pydantic import BaseModel, ConfigDict

class ChoiceBase(BaseModel):
    choice_text:str
    is_correct:bool
    
class ChoiceCreate(ChoiceBase):
    pass

class ChoiceResponse(ChoiceBase):
    id:int
    question_id:int
    
    model_config = ConfigDict(from_attributes=True)
