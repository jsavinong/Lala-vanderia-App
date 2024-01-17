from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/metodos_de_pago/", response_model=schemas.MetodoDePago)
def create_metodo_pago(metodo: schemas.MetodoDePagoCreate, db: Session = Depends(database.get_db)):
    db_metodo = models.MetodosDePago(**metodo.dict())
    db.add(db_metodo)
    db.commit()
    db.refresh(db_metodo)
    return db_metodo

@router.get("/metodos_de_pago/", response_model=list[schemas.MetodoDePago])
def read_metodos_pago(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    metodos = db.query(models.MetodosDePago).offset(skip).limit(limit).all()
    return metodos
