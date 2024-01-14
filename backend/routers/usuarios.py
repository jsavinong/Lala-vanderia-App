# Importaciones necesarias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

# Obtener todos los usuarios
@router.get("/usuarios/", response_model=list[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    usuarios = db.query(models.Usuario).offset(skip).limit(limit).all()
    return usuarios

# Agregar aquí otros endpoints relacionados con usuarios
