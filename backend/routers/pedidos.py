from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/pedidos/", response_model=schemas.Pedido)
def create_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db)):
    db_pedido = models.Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

@router.get("/pedidos/", response_model=list[schemas.Pedido])
def read_pedidos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    pedidos = db.query(models.Pedido).offset(skip).limit(limit).all()
    return pedidos
