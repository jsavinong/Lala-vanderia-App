# Importaciones necesarias
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from backend import models, schemas, database
from backend.auth import crear_token_acceso

router = APIRouter()

# Endpoint de inicio de sesión
@router.post("/login", response_model=schemas.Token)
def login(usuario: schemas.UsuarioLogin, db: Session = Depends(database.get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.correo_electronico == usuario.correo_electronico).first()
    if not db_usuario or not db_usuario.verificar_contraseña(usuario.contraseña):
        raise HTTPException(status_code=401, detail="Correo electrónico o contraseña incorrectos")
    access_token = crear_token_acceso(data={"sub": usuario.correo_electronico, "user_id": db_usuario.id})
    return {"access_token": access_token, "token_type": "bearer"}
