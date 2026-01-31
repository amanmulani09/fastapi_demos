from app.db.core import SessionLocal, engine
import app.models.models as models


def db_connection():
    models.Base.metadata.create_all(bind=engine) # this will create all the tables and & columns in the database 

def get_db():
    db  = SessionLocal()
    try:
        yield db
    finally:
        db.close()
