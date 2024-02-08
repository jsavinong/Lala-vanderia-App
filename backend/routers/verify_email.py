from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models import Usuario
from backend.database import get_db

router = APIRouter()

@router.get("/users/verify_email/{correo_electronico}")
def verificar_correo(correo_electronico: str, db: Session = Depends(get_db)):
    usuario = Usuario.buscar_por_correo(db, correo_electronico)
    if usuario:
        return {"is_registered": True}
    return {"is_registered": False}
