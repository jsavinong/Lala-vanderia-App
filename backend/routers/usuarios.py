# Importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()


# Crear nuevos usuarios
@router.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(
    usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)
):
    db_usuario = models.Usuario.registrar_usuario(db=db, usuario_data=usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# Obtener usuarios
@router.get("/usuarios/", response_model=list[schemas.Usuario])
def read_usuarios(
    skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)
):
    usuarios = db.query(models.Usuario).offset(skip).limit(limit).all()
    return usuarios
