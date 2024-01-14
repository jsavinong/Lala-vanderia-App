from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/planes/", response_model=schemas.PlanSuscripcion)
def create_plan(plan: schemas.PlanSuscripcionCreate, db: Session = Depends(database.get_db)):
    db_plan = models.PlanSuscripcion(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

@router.get("/planes/", response_model=list[schemas.PlanSuscripcion])
def read_planes(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    planes = db.query(models.PlanSuscripcion).offset(skip).limit(limit).all()
    return planes
