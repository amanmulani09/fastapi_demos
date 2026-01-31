from sqlalchemy.orm import Session
import app.models.models as models
from app.schemas.question import QuestionCreate

async def create_questions_in_db(question:QuestionCreate,db:Session):
    
        db_question = models.Question(question_text = question.question_text)
        db.add(db_question)
        db.commit()
        db.flush()
        
        for choice in question.choices:
            db_choice = models.Choice(choice_text=choice.choice_text,is_correct=choice.is_correct,question_id = db_question.id)
            db.add(db_choice)
            
        db.commit()  
        db.refresh(db_question) 
        return db_question
    
async def read_question_in_db(question_id:int,db:Session):
    result = db.query(models.Question).filter(models.Question.id == question_id).first() # to query the db 
    return result