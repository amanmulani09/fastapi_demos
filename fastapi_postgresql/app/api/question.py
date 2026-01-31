import logging
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.schemas.question import QuestionCreate, QuestionResponse
from app.service.question import create_questions_in_db, read_question_in_db
from app.db.session import get_db

logger = logging.getLogger(__name__)

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/questions', response_model=QuestionResponse)
async def create_questions(question:QuestionCreate, db:db_dependency):
        try:
            await create_questions_in_db(question,db)
            return {"message":"Question created successfull"}
        except Exception as e:
            logger.exception("Failed to create question")
            raise HTTPException(status_code=500,detail=str(e))
            
@router.get('/questions/{question_id}')
async def read_question(question_id:int, db:db_dependency):
    result = await read_question_in_db(question_id,db)
    
    if not result:
        logger.exception("Question not found")
        raise HTTPException(status_code=404,detail='Question not found')
    return result