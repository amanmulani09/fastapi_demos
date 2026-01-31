import logging
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from app.service.choice import read_choices_from_db
from app.db.session import get_db
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/choices/{question_id}')
async def read_choices(question_id:int,db:db_dependency):
   
    result = await read_choices_from_db(question_id,db)
    
    if not result:
        logger.exception("Question not found")
        raise HTTPException(status_code=404,detail='Question not found')
    return result