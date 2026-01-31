import app.models.models as models

async def read_choices_from_db(question_id:int,db):
    
        result = db.query(models.Choice).filter(models.Choice.question_id == question_id).all()
        return result