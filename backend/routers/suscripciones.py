from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()


@router.post("/suscripciones/", response_model=schemas.SuscripcionUsuario)
def create_suscripcion(
    suscripcion: schemas.SuscripcionUsuarioCreate,
    db: Session = Depends(database.get_db),
):
    db_suscripcion = models.SuscripcionUsuario(**suscripcion.dict())
    db.add(db_suscripcion)
    db.commit()
    db.refresh(db_suscripcion)
    return db_suscripcion


@router.get("/suscripciones/", response_model=list[schemas.SuscripcionUsuario])
def read_suscripciones(
    skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)
):
    suscripciones = db.query(models.SuscripcionUsuario).offset(skip).limit(limit).all()
    return suscripciones
