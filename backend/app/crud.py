from sqlalchemy.orm import Session
from . import models, schemas

def create_fan(db: Session, fan: schemas.FanCreate, documento_path: str):
    db_fan = models.Fan(**fan.dict(), documento=documento_path)
    db.add(db_fan)
    db.commit()
    db.refresh(db_fan)
    return db_fan
