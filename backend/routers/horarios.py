from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/horarios/", response_model=schemas.Horario)
def create_horario(horario: schemas.HorarioCreate, db: Session = Depends(database.get_db)):
    db_horario = models.Horario(**horario.dict())
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario

@router.get("/horarios/", response_model=list[schemas.Horario])
def read_horarios(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    horarios = db.query(models.Horario).offset(skip).limit(limit).all()
    return horarios
