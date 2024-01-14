from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/pagos/", response_model=schemas.Pago)
def create_pago(pago: schemas.PagoCreate, db: Session = Depends(database.get_db)):
    db_pago = models.Pago(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

@router.get("/pagos/", response_model=list[schemas.Pago])
def read_pagos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    pagos = db.query(models.Pago).offset(skip).limit(limit).all()
    return pagos
