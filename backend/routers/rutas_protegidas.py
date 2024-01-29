from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend import models
from backend.database import get_db
from backend.auth import verificar_token_acceso

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/some-protected-route")
def protected_route(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    correo_electronico = verificar_token_acceso(token)
    if not correo_electronico:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
    # Aquí puedes obtener información adicional del usuario desde la base de datos si es necesario
    # usuario = db.query(models.Usuario).filter(models.Usuario.correo_electronico == correo_electronico).first() # TODO: Pendiente por definir
    
    return {"mensaje": f"Ruta protegida. Accedido por el usuario {correo_electronico}"}
