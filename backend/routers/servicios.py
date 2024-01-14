from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/servicios/", response_model=schemas.Servicio)
def create_servicio(servicio: schemas.ServicioCreate, db: Session = Depends(database.get_db)):
    db_servicio = models.Servicio(**servicio.dict())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

@router.get("/servicios/", response_model=list[schemas.Servicio])
def read_servicios(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    servicios = db.query(models.Servicio).offset(skip).limit(limit).all()
    return servicios
