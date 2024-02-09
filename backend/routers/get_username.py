from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.get("/users/{correo_electronico}/name", response_model=schemas.UsuarioBase)
def get_username(correo_electronico: str, db: Session = Depends(database.get_db)):
    db_user = models.Usuario.buscar_por_correo(db, correo_electronico)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return schemas.UsuarioBase(nombre=db_user.nombre, correo_electronico=db_user.correo_electronico)