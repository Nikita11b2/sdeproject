from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import get_db

router = APIRouter()

@router.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db=db, config=config)

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.update_configuration(db=db, country_code=config.country_code, config=config)

@router.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.delete_configuration(db=db, country_code=country_code)
