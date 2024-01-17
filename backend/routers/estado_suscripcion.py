from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/estado_suscripcion/", response_model=schemas.EstadoSuscripcion)
def create_estado_suscripcion(estado_suscripcion: schemas.EstadoSuscripcionCreate, db: Session = Depends(database.get_db)):
    db_estado_suscripcion = models.EstadoSuscripcion(**estado_suscripcion.dict())
    db.add(db_estado_suscripcion)
    db.commit()
    db.refresh(db_estado_suscripcion)
    return db_estado_suscripcion

@router.get("/estado_suscripcion/", response_model=list[schemas.EstadoSuscripcion])
def read_estado_suscripcion(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    estados_suscripcion = db.query(models.EstadoSuscripcion).offset(skip).limit(limit).all()
    return estados_suscripcion