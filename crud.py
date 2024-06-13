from sqlalchemy.orm import Session
from . import models, schemas

def create_configuration(db: Session, config: schemas.ConfigurationCreate):
    db_config = models.Configuration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()

def update_configuration(db: Session, country_code: str, config: schemas.ConfigurationUpdate):
    db_config = get_configuration(db, country_code)
    if db_config:
        db_config.requirements = config.requirements
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_configuration(db: Session, country_code: str):
    db_config = get_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
