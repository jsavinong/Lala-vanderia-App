from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.post("/estado_pedidos/", response_model=schemas.EstadoPedido)
def create_estado_pedido(estado_pedido: schemas.EstadoPedidoCreate, db: Session = Depends(database.get_db)):
    db_estado_pedido = models.EstadoPedidos(**estado_pedido.dict())
    db.add(db_estado_pedido)
    db.commit()
    db.refresh(db_estado_pedido)
    return db_estado_pedido

@router.get("/estado_pedidos/", response_model=list[schemas.EstadoPedido])
def read_estados_pedidos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    estados_pedidos = db.query(models.EstadoPedidos).offset(skip).limit(limit).all()
    return estados_pedidos